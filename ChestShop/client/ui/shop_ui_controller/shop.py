# coding=utf-8
from ..utils import *


class ShopController:
    target_slots = []
    for row_start in [19, 28, 37]:
        target_slots.extend(range(row_start, row_start + 7))
    def __init__(
            self,
            screen_node,
            client_system,
            chest_grid,
            shop_id
            ):
        self.screen_node = screen_node
        self.system = client_system
        self.chest_grid = chest_grid
        self.goods_dict = SHOP_DATA.get(shop_id, dict()).get("goods", dict()).copy()
        self.chest_grid_dict = {index: {"description": ""} for index in range(54)}  # type: dict[int, dict]
        self.tab_type = 0
        self.upgrade_data = screen_node.data.get("upgrade_data", {}).copy()
        self.enchant_data = screen_node.data.get("enchant_data", {}).copy()
        self.set_goods_dict()

    def set_goods_dict(self):
        self.chest_grid_dict = {index: {"description": ""} for index in range(54)}
        goods_data = self.goods_dict.copy()
        for i in range(len(goods_data)):
            tab_info = {k: v for k, v in goods_data[i].items() if k != "goods"}
            self.chest_grid_dict[i] = tab_info.copy()
        goods_data = goods_data.get(self.tab_type, {}).get("goods", {}).copy()
        for i, (good_key, good_value) in enumerate(goods_data.items()):
            if i < len(self.target_slots):
                slot = self.target_slots[i]
                item_type = good_value.get("type", "default")
                if item_type in self.upgrade_data:
                    max_level = len(good_value["itemList"]) - 1
                    good_value = good_value["itemList"][self.upgrade_data[item_type]].copy()
                    good_value["level"] = self.upgrade_data[item_type]
                    good_value["max_level"] = max_level
                    good_value["type"] = item_type
                elif item_type == "enchant_item":
                    enchant_type = good_value.get("enchantType", "none")
                    max_level = len(good_value["itemList"]) - 2
                    good_value = good_value["itemList"][self.enchant_data[enchant_type]].copy() #error
                    good_value["level"] = self.enchant_data[enchant_type]
                    good_value["max_level"] = max_level
                    good_value["type"] = item_type
                    good_value["enchantType"] = enchant_type
                self.chest_grid_dict[slot] = good_value
            else:
                break
        glass_pane = {
            "description": "§7⇧类别\n⇩物品",
            "itemDict": {
                "newItemName": "stained_glass_pane",
                "newAuxValue": 8,
                "count": 1
            }
        }
        glass_pane_1 = {
            "description": "§a⇧类别\n⇩物品",
            "itemDict": {
                "newItemName": "stained_glass_pane",
                "newAuxValue": 5,
                "count": 1
            }
        }
        for i in range(9, 18):
            self.chest_grid_dict[i] = glass_pane.copy()
        self.chest_grid_dict[self.tab_type + 9] = glass_pane_1.copy()

    def chest_items_label(self, index):
        item = self.chest_grid_dict[index]
        description = item.get('description', '')
        item_dict = item.get('itemDict')
        if item_dict is not None:
            if index in self.target_slots:
                item_info = itemComp.GetItemBasicInfo(item_dict.get("newItemName", ""), item_dict.get("newAuxValue", 0))  # type: dict
                enchant_full = "§c(已满级)§f" if self.enchant_data.get(item.get("enchantType", "")) > item.get("max_level", 0) else ""
                description = """§a{}§r{}
§7花费: {} x {}

§7{}

§b滑动以查看物品信息!\n§e点击购买!
§8{}\n§8NBT: 1 tag(s)""".format(item_info["itemName"], enchant_full, CURRENCY_ENUM.get(item.get("currency", "experience"), "§f[限免] 选队币"), item.get("price", 0), description, item_dict.get("newItemName"))
            return description
        return ""

    def chest_items_stack_count_label(self, index):
        path = "/grid_item_for_chest{}/item_cell/item/item_renderer".format(index + 1)
        item_cell = self.chest_grid.GetChildByPath(path)
        renderer = item_cell.asItemRenderer()
        if self.chest_grid_dict[index].get("description", "") == "":
            renderer.SetVisible(False)
            return ""
        else:
            renderer.SetVisible(True)
            item = self.chest_grid_dict[index]
            if item.get("type", "default") in self.upgrade_data:
                if item.get("itemDict") is None:
                    item = self.upgrade_data["itemList"][self.upgrade_data[item.get("type", "default")]].copy()
            item_dict = item.get("itemDict", dict())
            renderer.SetUiItem(
                item_dict.get("newItemName", ""),
                item_dict.get("newAuxValue", 0),
                True if (index == self.tab_type) or (item.get("type", "default") == "enchant_item") else False
            )
            count = item_dict.get("count", 1)
            return "" if count == 1 else str(count)

    def test_can_buy(self, currency, price):
        inventory_price = 0
        if currency == "experience":
            return True
        for item in self.screen_node.PlayerInventoryItemDict:
            if item:
                if item["newItemName"].split(":")[-1] == currency.split(":")[-1]:
                    inventory_price += item["count"]
        if inventory_price < price:
            return price - inventory_price
        return True

    def buy_goods(self, args):
        index = args["#collection_index"]
        button_type = args["#collection_name"]
        if button_type == "chest_grid_item":
            if index <= len(self.goods_dict) - 1:
                if self.chest_grid_dict[index]:
                    self.screen_node.player_sound(("random.click", 1, 1))
                    self.tab_type = index
                    self.set_goods_dict()
                    self.screen_node.UpdateScreen()
            elif index in self.target_slots:
                item = self.chest_grid_dict[index]
                if item != {'description': ''}:
                    item_type = item.get("type", "default")
                    currency = item.get("currency", "")
                    def test_can_buy(event_name):
                        can_buy = self.test_can_buy(currency, item.get("price", 0))
                        if can_buy is True:
                            self.system.NotifyToServer(event_name, item)
                        else:
                            item_name = itemComp.GetItemBasicInfo(item["itemDict"]["newItemName"], item["itemDict"]["newAuxValue"]).get("itemName", "")
                            message = BUY_FAIL_TEXT.replace("{item_name}", item_name).replace("{price}", str(item.get("price", 0))).replace("{currency}", CURRENCY_ENUM.get(currency, "§f[限免] 选队币")).replace("{need_currency}", str(can_buy))
                            CF.CreateTextNotifyClient(levelId).SetLeftCornerNotify(str(message))
                            self.screen_node.player_sound(BUY_FAIL_SOUNDS)
                    if item_type == "default":
                        test_can_buy("PlayerBuyGoodsEvent")
                    elif item_type == "wool":
                        test_can_buy("PlayerBuyWoolEvent")
                    elif item_type == "clay":
                        test_can_buy("PlayerBuyClayEvent")
                    elif item_type == "glass":
                        test_can_buy("PlayerBuyGlassEvent")
                    elif item_type == "ct":
                        test_can_buy("PlayerCtEvent")
                    elif item_type in self.upgrade_data:
                        test_can_buy("PlayerBuyGoodsCustomizeEvent")
                        
                    elif item_type == "enchant_item":
                        if self.enchant_data.get(item.get("enchantType", ""), -1) <= item.get("max_level", 0):
                            test_can_buy("PlayerBuyGoodsCustomizeEvent")
                        else:
                            self.screen_node.player_sound(BUY_FAIL_SOUNDS)
                            item_name = itemComp.GetItemBasicInfo(item["itemDict"]["newItemName"], item["itemDict"]["newAuxValue"]).get("itemName", "")
                            CF.CreateTextNotifyClient(levelId).SetLeftCornerNotify(BUY_FAIL_TEXT.replace("{item_name}", item_name).replace("{price}", str(item.get("price", 0))).replace("{currency}", CURRENCY_ENUM.get(currency, "§f[限免] 选队币")))
                            
                    elif item_type == "armour":
                        if item.get("level", 0) <= self.screen_node.data.get("I3P77O", 0):# 装备
                            self.screen_node.player_sound(BUY_FAIL_SOUNDS)
                            item_name = itemComp.GetItemBasicInfo(item["itemDict"]["newItemName"], item["itemDict"]["newAuxValue"]).get("itemName", "")
                            CF.CreateTextNotifyClient(levelId).SetLeftCornerNotify(BUY_FAIL_TEXT_FOR_ARMOUR.replace("{item_name}", item_name).replace("{price}", str(item.get("price", 0))).replace("{currency}", CURRENCY_ENUM.get(currency, "§f[限免] 选队币")))
                        else:
                            self.screen_node.data["I3P77O"] = item.get("level", 0) #装备
                            test_can_buy("PlayerBuyGoodsCustomizeEvent")
                    else:
                        test_can_buy("PlayerBuyGoodsCustomizeEvent")
