# -*- coding: utf-8 -*
"""
Created on 2024/9/29
"""
from utils import *
from BaseServerSystem import BaseServerSystem
from controller.shopUIController import ShopUIController
from controller.playerListController import PlayerListController

class Main(BaseServerSystem):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)
        self.shopUIController = None
        self.playerListController = None

    @Listen.on(server.LoadServerAddonScriptsAfter)
    def server_load_addon_scripts_after(self, args):
        self.register_controller()

    def register_controller(self):
        self.shopUIController = ShopUIController()
        self.playerListController = PlayerListController()


    @Listen.on(server.PlayerDoInteractServerEvent)
    def Player_Do_Interact_Server_Event(self, args):
        pid = args["playerId"]
        target_id = args["interactEntityId"]
        EngineTypeStr = SF.CreateEngineType(target_id).GetEngineTypeStr()
        x, y, z = SF.CreatePos(target_id).GetPos()
        x1, y1, z1 = SF.CreatePos(pid).GetPos()
        Interact_distance = ((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2) ** 0.5

        if EngineTypeStr == "template:npc":
            if Interact_distance > 6.4:
                addTag("interact_ban", pid)
                addTag("封禁", pid)
                return
            if hasTag('owner', pid) and hasTag('canmap', pid):
                addTag("inChossingMode", target_id)
                commandComp.SetCommand("function entite/npc/interacted")
            elif hasTag("inf", pid):
                self.OpenShopUI(pid, target_id)


    def OpenShopUI(self, pid, target_id):
        scoreboard = game.GetAllPlayerScoreboardObjects() # type:list[dict]
        value = 0
        for score in scoreboard:
            if pid == score["playerId"]:
                scoreList = score["scoreList"]
                for score in scoreList:
                    if score["name"] == "O8P02W":
                        value = score["value"]

        if not hasTag("道具商店", target_id):
            value_enchanted = 7
            if value == 3 or value == 4:
                value_enchanted = 9
            self.NotifyToClient(pid, "open_shop_ui", {"shop_id": "shop_{}".format(value_enchanted),"upgrade_data": self.shopUIController.get_upgrade_data(pid),"enchant_data": self.shopUIController.get_ench_data(pid),"I3P77O": self.shopUIController.get_armor_level(pid)})
        else:
            if value == 1:
                function("mode/1_mode_bedfight", pid)
            else:
                self.NotifyToClient(pid, "open_shop_ui", {"shop_id": "shop_{}".format(value),"upgrade_data": self.shopUIController.get_upgrade_data(pid),"enchant_data": self.shopUIController.get_ench_data(pid),"I3P77O": self.shopUIController.get_armor_level(pid)})


    @Listen.on(server.ServerItemTryUseEvent)
    def Server_ItemTryUse_Event(self, args):
        pid = args["playerId"]
        if args.get("itemDict", {}).get("newItemName") == "minecraft:ender_eye":
            args['cancel'] = True
            if hasTag('rbw_chained', pid):
                self.NotifyToClient(pid, "open_shop_ui", {"shop_id": "rbw_chained"})
            elif hasTag('rbw_unt', pid):
                self.NotifyToClient(pid, "open_shop_ui", {"shop_id": "rbw_unt"})
            else:
                self.NotifyToClient(pid, "open_shop_ui", {"shop_id": "shop_8"})


    # @Listen.on(server.DamageEvent)
    # def Damage_Event(self, args):
        # pid = args['entityId']  # 受伤者
        # cause = args['cause']
        # EngineTypeStr = SF.CreateEngineType(pid).GetEngineTypeStr()
        # enum = serverApi.GetMinecraftEnum().ActorDamageCause
        # if EngineTypeStr == "minecraft:player" and cause == enum.EntityAttack or cause == enum.Projectile or cause == enum.BlockExplosion:
            # self.NotifyToClient(pid, "close_ui", {})


    @Listen.on(server.WillTeleportToServerEvent)
    def teleport_close(self, args):
        pid = args['entityId']
        self.NotifyToClient(pid, "close_ui", {})


