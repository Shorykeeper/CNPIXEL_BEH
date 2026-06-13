# -*- coding: utf-8 -*
"""
Created on 2025/6/4
"""
from ..utils import *

class ShopUIController(BaseModule):

    def __init__(self):
        super(ShopUIController, self).__init__()


    @Listen.on("PlayerBuyGoodsCustomizeEvent", Listen.client)
    def player_buy_goods_customize_event(self, args):
        """
        玩家购买自定义type的物品
        """
        pid = args["__id__"]  # 玩家id
        if self.del_currency(args):
            if args["type"] in SCOREBOARD_LIST: # I0S08X axe X2C07R paxe
                value = args.get("level", 0)
                if value < args.get("max_level", 0):
                    commandComp.SetCommand("scoreboard players add @s {} 1".format(args["type"]), pid)
                itemComp(pid).SpawnItemToPlayerInv(args["itemDict"], pid)

            elif args["type"] == "enchant_item": 
                value = args.get("level", 0)
                if value <= args.get("max_level", 0): #意义: 遍历所有人中和购买者队伍分数相同的人 给自身加级
                    if args["enchantType"] in ENCH_SCOREBOARD_LIST:
                        commandComp.SetCommand("execute as @a if score @s A1T12P = {} A1T12P run function global/team/upgrade/{}".format(nameComp(pid).GetName(), args["enchantType"]), pid)
                        if args["enchantType"] in ENCH_SCOREBOARD_TRAP_LIST:
                            addTag("trap_{}".format(args["enchantType"]), pid)
                            function("global/trap/purchasingTrapCarryOn", pid)
                            type_map = {"X5T99R": "疯狂矿工","C1T28Q": "保护增益","A1B23C": "锋利增益","Z3K56L": "龙增益","Q7M04P": "治愈池","Y9V88N": "铁锻炉"}
                            item_name = type_map.get(args["enchantType"], '团队增益')
                            commandComp.SetCommand('execute as @a if score @s A1T12P = %s A1T12P run tellraw @s {"rawtext":[{"text":"§7%s§a购买了%s"}]}' % (nameComp(pid).GetName(), nameComp(pid).GetName(), item_name), pid)
                self.system.BroadcastEvent("PlayerBuyEnchantEvent", args)
                self.system.NotifyToClient(pid, "buy_goods_result", {"success": True, "upgrade_data": self.get_upgrade_data(pid),
                                                          "enchant_data": self.get_ench_data(pid),
                                                          "I3P77O": self.get_armor_level(pid), "goods_data": args})
                return
                
            elif args["type"] == "armour":
                itemList = args["itemList"]  # type:dict
                itemComp(pid).SetPlayerAllItems(itemList) # scoreboard: 
                commandComp.SetCommand("scoreboard players set @s I3P77O {}".format(args.get("level", 0)), pid)
                commandComp.SetCommand("tag @s add 附魔", pid) #刷新一次附魔等级

            elif args["type"] == "wool":
                self.system.BroadcastEvent("PlayerBuyWoolEvent", args)
            elif args["type"] == "clay":
                self.system.BroadcastEvent("PlayerBuyClayEvent", args)
            elif args["type"] == "glass":
                self.system.BroadcastEvent("PlayerBuyGlassEvent", args)

                
            else:
                self.system.BroadcastEvent("PlayerBuyGoodsCustomizeEvent", args)
            self.system.NotifyToClient(pid, "buy_goods_result", {"success": True, "upgrade_data": self.get_upgrade_data(pid),
                                                          "enchant_data": self.get_ench_data(pid),
                                                          "I3P77O": self.get_armor_level(pid), "goods_data": args})

    def buy_goods_result(self, pid, success, goods_data):
        self.system.NotifyToClient(pid, "buy_goods_result", {"success": success, "upgrade_data": self.get_upgrade_data(pid),
                                                      "enchant_data": self.get_ench_data(pid),
                                                      "I3P77O": self.get_armor_level(pid), "goods_data": goods_data})

    def open_shop_ui(self, pid, shop_id):
        if shop_id in SHOP_DATA:
            self.system.NotifyToClient(pid, "open_shop_ui", {"shop_id": shop_id, "upgrade_data": self.get_upgrade_data(pid),
                                                      "enchant_data": self.get_ench_data(pid),
                                                      "I3P77O": self.get_armor_level(pid)})
            return True
        return False

    @Listen.on("PlayerBuyGoodsEvent", Listen.client) #item_type == "default":
    def player_buy_goods_event(self, args):
        pid = args["__id__"]  # 玩家id
        if self.del_currency(args):
            itemDict = args["itemDict"]  # type:dict
            if itemComp(pid).SpawnItemToPlayerInv(itemDict, pid) is False:
                pos = posComp(pid).GetPos()
                dimension = SF.CreateDimension(pid).GetEntityDimensionId()
                itemComp(levelId).SpawnItemToLevel(itemDict, dimension, pos)  
            self.system.NotifyToClient(pid, "buy_goods_result", {"success": True, "upgrade_data": self.get_upgrade_data(pid),
                                                          "enchant_data": self.get_ench_data(pid),
                                                          "I3P77O": self.get_armor_level(pid), "goods_data": args})
        else:
            self.system.NotifyToClient(pid, "buy_goods_result", {"success": False, "upgrade_data": self.get_upgrade_data(pid),
                                                          "enchant_data": self.get_ench_data(pid),
                                                          "I3P77O": self.get_armor_level(pid), "goods_data": args})


    @Listen.on("PlayerBuyWoolEvent", Listen.client)
    def player_buy_wool_event(self, args):
        """
        玩家购买羊毛
        """
        pid = args["__id__"]  # 玩家id
        itemDict = args["itemDict"]  # type:dict
        self.system.NotifyToClient(pid, "buy_goods_result", {"success": True, "upgrade_data": self.get_upgrade_data(pid),
                                                          "enchant_data": self.get_ench_data(pid),
                                                          "I3P77O": self.get_armor_level(pid), "goods_data": args})
        commandComp.SetCommand("function global/team/wool", pid)
        self.del_currency(args)


    @Listen.on("PlayerBuyClayEvent", Listen.client)
    def player_buy_clay_event(self, args):
        """
        玩家购买陶瓦
        """
        pid = args["__id__"]  # 玩家id
        itemDict = args["itemDict"]  # type:dict
        self.system.NotifyToClient(pid, "buy_goods_result", {"success": True, "upgrade_data": self.get_upgrade_data(pid),
                                                          "enchant_data": self.get_ench_data(pid),
                                                          "I3P77O": self.get_armor_level(pid), "goods_data": args})
        commandComp.SetCommand("function global/team/clay", pid)
        self.del_currency(args)

    @Listen.on("PlayerBuyGlassEvent", Listen.client)
    def player_buy_glass_event(self, args):
        """
        玩家购买玻璃
        """
        pid = args["__id__"]  # 玩家id
        itemDict = args["itemDict"]  # type:dict
        self.system.NotifyToClient(pid, "buy_goods_result", {"success": True, "upgrade_data": self.get_upgrade_data(pid),
                                                          "enchant_data": self.get_ench_data(pid),
                                                          "I3P77O": self.get_armor_level(pid), "goods_data": args})
        commandComp.SetCommand("function global/team/glass", pid)
        self.del_currency(args)


    @Listen.on("PlayerCtEvent", Listen.client)
    def Player_Ct_Event(self, args):
        """
        玩家选择队伍
        """
        pid = args["__id__"]  # 玩家id
        Team = 0
        #if self.del_currency(args):
        commandComp.SetCommand("function global/team/ct/tongyong", pid)
        itemDict = args.get("itemDict", {})
        if itemDict.get("newItemName", {}) == "minecraft:bed":
            if itemDict.get("newAuxValue", {}) == 14:
                commandComp.SetCommand("function global/team/ct/r", pid)
            elif itemDict.get("newAuxValue", {}) == 3:
                commandComp.SetCommand("function global/team/ct/b", pid)
            elif itemDict.get("newAuxValue", {}) == 5:
                commandComp.SetCommand("function global/team/ct/g", pid)
            elif itemDict.get("newAuxValue", {}) == 4:
                commandComp.SetCommand("function global/team/ct/y", pid)
        self.system.NotifyToClient(pid, "close_ui", {})


    def get_upgrade_data(self, pid):
        scoreboard = game.GetAllPlayerScoreboardObjects()  # type:list[dict]
        scoreList = {name: 0 for name in SCOREBOARD_LIST}
        for obj in scoreboard:
            if obj["playerId"] == pid:
                scoreList_ = obj["scoreList"]  # type:list[dict]
                for i in scoreList_:
                    if i["name"] in SCOREBOARD_LIST:
                        scoreList[i["name"]] = i["value"]
                break
        return scoreList


    def get_ench_data(self, pid):
        scoreboard = game.GetAllPlayerScoreboardObjects()  # type:list[dict]
        scoreList = {name: 0 for name in ENCH_SCOREBOARD_LIST}
        for obj in scoreboard:
            if obj["playerId"] == pid:
                scoreList_ = obj["scoreList"]  # type:list[dict]
                for i in scoreList_:
                    if i["name"] in ENCH_SCOREBOARD_LIST:
                        scoreList[i["name"]] = i["value"]
                break
        return scoreList

    def get_armor_level(self, pid):
        scoreboard = game.GetAllPlayerScoreboardObjects()  # type:list[dict]
        for obj in scoreboard:
            if obj["playerId"] == pid:
                scoreList_ = obj["scoreList"]  # type:list[dict]
                for i in scoreList_:
                    if i["name"] == "I3P77O":#armor_level
                        return i["value"]
                break
        return 0

    def del_currency(self, args):
        pid = args["__id__"]  # 玩家id
        price = args["price"]  # type:int
        currency = args["currency"].split(":")[-1]
        if currency == "experience":
            lv = lvComp(pid).GetPlayerLevel()
            if price <= lv:
                lvComp(pid).AddPlayerLevel(-price)
                return True
            else:
                self.system.NotifyToClient(pid, "buy_goods_result", {"success": False, "goods_data": args, "lv": lv})
                return False
        return commandComp.SetCommand("clear @s {} 0 {}".format(currency, price), pid)

    @Listen.on("spawn_item", Listen.client)
    def spawn_item(self, args):
        pid = args["__id__"]
        itemDict = args["itemDict"]
        dimension = args["dimension"]
        pos = args["pos"]
        dx = args["dir"][0]
        dz = args["dir"][2]
        item_id = itemComp(levelId).SpawnItemToLevel(itemDict, dimension, pos)
        SF.CreateAction(item_id).SetMobKnockback(dx, dz, 1.0, -1.0, 1.0)

    @Listen.on(server.ServerPlayerTryTouchEvent)
    def server_player_try_touch_event(self, args):
        pid = args["playerId"]
        game.AddTimer(1, lambda: self.system.NotifyToClient(pid, "server_player_try_touch_event", {}))

    @Listen.on("set_player_inventory", Listen.client)
    def set_player_inventory(self, args):
        pid = args["__id__"]
        items = args["items"]
        itemComp(pid).SetPlayerAllItems(items)


