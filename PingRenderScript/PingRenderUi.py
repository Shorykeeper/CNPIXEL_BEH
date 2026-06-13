# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi

ScreenNode = clientApi.GetScreenNodeCls()
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()

class PingRenderScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.mPlayerId = clientApi.GetLocalPlayerId()
        self.mLevelId = clientApi.GetLevelId()
        self.data = param.get('data',{})
        self.client = param.get('client',None)
        clientApi.GetEngineCompFactory().CreateGame(self.mLevelId).AddRepeatedTimer(1.0, self.Ping)

    def callback(self, args):
        pass

    def Create(self):
        print('=====> PingRenderUi Created <=====')
        buttonUIControl = self.GetBaseUIControl("/button").asButton()
        buttonUIControl.AddTouchEventParams({"isSwallow":True})
        buttonUIControl.SetButtonTouchUpCallback(self.callback)
        buttonUIControl.SetTouchEnable(True)

    def Ping(self):
        self.GetBaseUIControl('/button/button_label').asLabel().SetText('Ping: ' + '{:.0f}ms'.format(self.client.ping * 500.0))

    def Destroy(self):
        print('=====> PingRenderUi Destroyed <=====')

    # @ViewBinder.binding(ViewBinder.BF_ButtonClickUp, '#buttonClick')
    # def buttonClick(self,args):
    #     path = args['ButtonPath']