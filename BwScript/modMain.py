# coding=utf-8
import __future__
from .config.config import *
from mod.common.mod import Mod
import mod.client.extraClientApi as capi
import mod.server.extraServerApi as sapi


@Mod.Binding(name=NAMESPACE, version="1.0")
class CommandFunctionExpansionMod(object):
    def __init__(self):
        pass

    @Mod.InitServer()
    def initMod(self):
        sapi.RegisterSystem(NAMESPACE, SERVER_SYSTEM_NAME, SERVER_SYSTEM_PATH)

    @Mod.InitClient()
    def init(self):
        capi.RegisterSystem(NAMESPACE, CLIENT_SYSTEM_NAME, CLIENT_SYSTEM_PATH)
