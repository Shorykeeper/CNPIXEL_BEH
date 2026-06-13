# -*- coding: utf-8 -*-

from mod.common.mod import Mod
from .config.modConfig import *
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name=modName, version=version)
class ZhiYunXiGua(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def serverInit(self):
        path = "{}.server.main.Main".format(modName)
        serverApi.RegisterSystem(modName, systemName, path)
        print ("======Init{}Server======".format(modName))

    @Mod.DestroyServer()
    def serverDestroy(self):
        pass

    @Mod.InitClient()
    def clientInit(self):
        path = "{}.client.main.Main".format(modName)
        clientApi.RegisterSystem(modName, systemName, path)
        print ("======Init{}Client======".format(modName))

    @Mod.DestroyClient()
    def clientDestroy(self):
        pass
