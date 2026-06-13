# -*- coding: utf-8 -*-
"""
Created on 2024/9/29

"""
from .utils import *
from BaseClientSystem import BaseClientSystem


class Main(BaseClientSystem):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)

    @Listen.on(client.LoadClientAddonScriptsAfter)
    def server_load_addon_scripts_after(self, args):
        self.register_controller()

    def register_controller(self):
        pass

    @Listen.on(client.UiInitFinished)
    def UiInitFinished(self, args):
        self.NotifyToServer('UiInitFinished', {'playerId': playerId})
        clientApi.RegisterUI(modName, "shop_ui",
                             "ChestShop.client.ui.chest_shop.Main", "chest_shop.main")
        clientApi.RegisterUI(modName, "player_list",
                             "ChestShop.client.ui.player_list.Main", "player_list.main")
        clientApi.CreateUI(modName, "player_list", {"client": self, "isHud": 1})

    @Listen.on("open_shop_ui", Listen.server)
    def open_shop_ui(self, args):
        clientApi.PushScreen(modName, "shop_ui", {"client": self, "data": args})

    @Listen.on("close_ui", Listen.server)
    def close_ui(self, args):
        clientApi.PopScreen()
