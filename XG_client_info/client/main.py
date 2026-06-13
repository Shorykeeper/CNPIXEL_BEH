# -*- coding: utf-8 -*-
from utils import *


NativeScreenManager = clientApi.GetNativeScreenManagerCls()

class Main(BaseSystem):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)
        NativeScreenManager.instance().RegisterScreenProxy("hud.hud_screen", "XG_client_info.client.ui.hud_proxys.Main")
