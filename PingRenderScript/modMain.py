# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="PingRenderMod", version="1.0.0")
class PingRenderClient(object):
    @Mod.InitClient()
    def PingRenderClientInit(self):
        clientApi.RegisterSystem("PingRenderMod", "PingRenderClientSystem", "PingRenderScript.PingRenderClientSystem.PingRenderClientSystem")
        print('=====> PingRender Init <=====')
        
    @Mod.DestroyClient()
    def PingRenderClientDestroy(self):
        print('=====> PingRender Destroy <=====')
        
    @Mod.InitServer()
    def PingRenderServerInit(self):
        serverApi.RegisterSystem('PingRenderMod', 'PingRenderServerSystem', 'PingRenderScript.PingRenderServerSystem.PingRenderServerSystem')
        print('=====> PingRender(Server Side) Init <=====')

    @Mod.DestroyServer()
    def PingRenderServerDestroy(self):
        print('=====> PingRender(Server Side) Destroy <=====')
