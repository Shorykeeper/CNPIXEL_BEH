# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
import time

ClientSystem = clientApi.GetClientSystemCls()


class PingRenderClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.mPlayerId = clientApi.GetLocalPlayerId()
        self.mLevelId = clientApi.GetLevelId()
        self.ping = 0
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.UiInitFinished)
        self.ListenForEvent('PingRenderMod', 'PingRenderServerSystem', 'Pong', self, self.HandlePong)
        clientApi.GetEngineCompFactory().CreateGame(self.mLevelId).AddRepeatedTimer(1, self.RepeatPing)
        
    def RepeatPing(self):
        self.NotifyToServer('Ping', {
            'ping_time': time.time()
        })

    def HandlePong(self, args):
        pong_time = time.time()
        self.ping = pong_time - args['ping_time']
        
    
    def UiInitFinished(self, args):
        clientApi.RegisterUI('PingRenderMod', 'PingRender', "PingRenderScript.PingRenderUi.PingRenderScreen", "PingRender.main")
        clientApi.CreateUI('PingRenderMod', 'PingRender', {"isHud": 1, 'data':{},'client':self})
        
    def Destroy(self):
        pass
