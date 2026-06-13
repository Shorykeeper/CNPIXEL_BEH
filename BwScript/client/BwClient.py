# -*- coding: utf-8 -*-
# 永远不要相信客户端
import __future__
from time import time
from ..config.config import *
import mod.client.extraClientApi as capi # type: ignore
cf = capi.GetEngineCompFactory()
levelId = capi.GetLevelId()
Id = capi.GetLocalPlayerId()
LocalPlayerId = capi.GetLocalPlayerId()
from ..config.fastListen import *


class BwClientSys(capi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(BwClientSys, self).__init__(namespace, name)
        initFastListen(self)
        cf.CreateGame(levelId).AddRepeatedTimer(1.0, self.Second)
        cf.CreateGame(levelId).AddRepeatedTimer(0.06, self.Tick)
        
        self.click_time_set = set()
        self.chat_count = 0
        self.chat_delay = 0
        self.honk = 0
        self.zb = 0
#        self.server_listen('show_cursor', self.show_cursor)  #
        
        self.ListenEngineEvent = lambda eventName, callbackFunc: self.ListenForEvent(capi.GetEngineNamespace(), capi.GetEngineSystemName(), eventName, self, callbackFunc)
        self.ListenEngineEvent('TapBeforeClientEvent', self.LeftClickBeforeClientEvent2)
        self.ListenEngineEvent('LeftClickBeforeClientEvent', self.LeftClickBeforeClientEvent2)

        
    def Destroy(self):
        self.UnListenAllEvents()


    @Listen
    def PushScreenEvent(self, args):
        if 'screenDef' in args:
            if 'pause.pause_screen' == args['screenDef']:
                self.NotifyToServer('Other', {'mode': 12})


    @Listen(NAMESPACE, SERVER_SYSTEM_NAME)
    def LoadScoreboardEvent(self, args):
        data = args['data']
        if data:
            comp = cf.CreateConfigClient(levelId)
            configDict = comp.GetConfigData(configscoreName, True)
            if configDict != None:
                NewData = self.Convert(configDict)
            else:
                NewData = None
            for bWVzc2Fn, bWVzc2Fnks in data.iteritems():
                if bWVzc2Fn in InterFlow_Scoreboard:
                    if NewData == None:
                        NewData = {ScoreboardDataKey.get(bWVzc2Fn, ''): bWVzc2Fnks}
                    else:
                        NewData[ScoreboardDataKey.get(bWVzc2Fn, '')] = bWVzc2Fnks
                    comp.SetConfigData(configscoreName, NewData, True)
            self.ReloadScoreboardEve()
                    
    @Listen(NAMESPACE, SERVER_SYSTEM_NAME)
    def ReloadScoreboardEvent(self, args): #加入游戏加载
        comp = cf.CreateConfigClient(levelId)
        configDict = comp.GetConfigData(configscoreName, True)
        data = self.Convert(configDict)
        self.NotifyToServer('Other', {'data': data, 'mode': 13})
        
    def ReloadScoreboardEve(self):
        comp = cf.CreateConfigClient(levelId)
        configDict = comp.GetConfigData(configscoreName, True)
        data = self.Convert(configDict)
        self.NotifyToServer('Other', {'data': data, 'mode': 13})
        
    def Convert(self, configDict): #转换
        if isinstance(configDict, dict):
            return {self.Convert(bWVzc2Fn): self.Convert(bWVzc2Fnks) for bWVzc2Fn, bWVzc2Fnks in configDict.iteritems()}
        elif isinstance(configDict, list):
            return [self.Convert(element) for element in configDict]
        elif isinstance(configDict, tuple):
            tmp = [self.Convert(element) for element in configDict]
            return tuple(tmp)
        elif isinstance(configDict, unicode): # type: ignore
            return configDict.encode('utf-8')
        else:
            return configDict
        
    def Second(self):
        self.NotifyToServer('SecondEventClient', {})
        self.click = 0
        self.chat_delay += 1
        if self.chat_delay >= chat_reset_delay:
            self.chat_count = 0

        if cf.CreatePlayer(LocalPlayerId).isMoving():
            self.honk = 0
        else:
            self.honk += 1
            if self.honk >= max_honk_time: #挂机时间
                self.honk = 0
                self.NotifyToServer('SHORYonHonkEvent', {}) #挂满就似
            elif self.honk == max_honk_time * 0.5:
                self.NotifyToServer('SHORYonHonkWarning', {}) #过半提示一下



    def Tick(self):
        if self.chat_count >= max_chat_count:
            self.NotifyToServer('Other', {'mode': 3})
            self.chat_count = 0
            self.chat_delay = 0
            


    @Listen(NAMESPACE, SERVER_SYSTEM_NAME)
    def Zb(self, args):
        mode = args['mode']
        state = args['state']
        if state == 1:
            if mode == 1:
                self.zb = 1
            elif mode == 2:
                self.zb = 2
            elif mode == 3:
                self.zb = 3
        elif state == 2:
            self.zb = 0
        
    @Listen(NAMESPACE, SERVER_SYSTEM_NAME)
    def Other(self, args):
        mode = args['mode']
        if mode == 0:
            comp = cf.CreateConfigClient(levelId)
            comp.SetConfigData(configkickName, {'kick': False, 'uid': cf.CreatePlayer(LocalPlayerId).getUid(), 'ip': capi.GetIp()}, True)
        if mode == -1:
            comp = cf.CreateConfigClient(levelId)
            comp.SetConfigData(configkickName, {'kick': True, 'uid': cf.CreatePlayer(LocalPlayerId).getUid(), 'ip': capi.GetIp()}, True)
        elif mode == 3:
            self.click -= 1
        elif mode == 4:
            self.chat_count += 1
            self.chat_delay = 0
        elif mode == 6:
            self.NotifyToServer('Other', {'mode': 3})
            self.chat_count = 0
            self.chat_delay = 0
        elif mode == 5:
            pass
        
    def LeftClickBeforeClientEvent2(self, args):
        self.click_time_set.add(time())


    @Listen   #            
    def OnLocalPlayerStopLoading(self, args):
        Id = args['playerId']
        self.NotifyToServer('Other', {'mode': 1})
        comp = cf.CreateConfigClient(levelId)
        data = comp.GetConfigData(configkickName, True)
        if data['kick']:
            self.NotifyToServer('Other', {'mode': -1})




    @Listen
    def UpdatePlayerSkinClientEvent(self, args):
        comp = cf.CreateGame(levelId)
        Id = args['playerId']
        if comp.IsOfficialSkin(Id):
            model_comp = cf.CreateModel(Id)
            # 尝试设置皮肤，注意路径格式
            # 这里的 "Shorykeeper.png" 是假设的文件名，请确保你的资源包里真的有这个文件
            is_success = model_comp.SetSkin("1.png")

            if is_success:
                print("update >>>> success")
            else:
                print("update >>>> failed: 路径错误或文件不存在")


    @Listen
    def PlayerTryDestroyBlockClientEvent(self, args):
        Id = args['playerId']
        block_name = args['blockName']
        x, y, z = args['x'], args['y'], args['z']
        xyz = (x, y, z)
        comp = cf.CreateGame(levelId)
        if block_name not in server_can_destroy_blocks:
            args['cancel'] = True
