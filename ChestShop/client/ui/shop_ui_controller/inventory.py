# coding=utf-8
from ..utils import *


class PlayerInventoryController:

    def __init__(
            self,
            screen_node,
            client_system,
            inventory_grid,
            hotbar_grid,
            ):
        self.screen_node = screen_node
        self.system = client_system
        self.inventory_grid = inventory_grid
        self.hotbar_grid = hotbar_grid
        self.PlayerInventoryItemDict = self.screen_node.PlayerInventoryItemDict

    def hotbar_items_label(self, index):
        item = self.PlayerInventoryItemDict[index]
        return self.return_item_label(item)

    def inventory_items_label(self, index):
        item = self.PlayerInventoryItemDict[index + 9]
        return self.return_item_label(item)

    def return_item_label(self, item):
        InputMode = CF.CreatePlayerView(levelId).GetToggleOption(enum.OptionId.INPUT_MODE)
        if InputMode == enum.InputMode.Touch:
            return ""
        if item is not None:
            itemBasicInfo = itemComp.GetItemBasicInfo(item["newItemName"], item["newAuxValue"])
            if item.get("userData", dict()) is None:
                item["userData"] = dict()
            if item.get("userData", dict()).get("ItemCustomTips"):
                text = "{}".format(
                    item.get("userData", dict()).get("ItemCustomTips").get("__value__")
                    .replace("%name%", itemBasicInfo["itemName"])
                    .replace("%category%", itemBasicInfo["itemCategory"].replace("construction", "§5建筑§f").replace("nature", "§5自然§f").replace("equipment", "§5装备§f").replace("items", "§5物品§f"))
                    .replace("%attack_damage%", str(itemBasicInfo["weaponDamage"])))
                return text

            text = "{}\n{}".format(
                item.get("userData", dict()).get("display", dict()).get("Name", dict()).get("__value__", itemBasicInfo["itemName"]),
                itemBasicInfo["itemCategory"].replace("construction", "§5建筑§f").replace("nature", "§5自然§f").replace("equipment", "§5装备§f").replace("items", "§5物品§f")
            )
            return text
        return ""

    def hotbar_items_stack_count_label(self, index):
        item_renderer = self.hotbar_grid.GetChildByPath("/grid_item_for_hotbar{}/item_cell/item/item_renderer".format(index + 1)).asItemRenderer()
        item = self.PlayerInventoryItemDict[index]
        if self.PlayerInventoryItemDict[index]:
            item_renderer.SetVisible(True)
            if item.get("FlyTo"):
                item_renderer.SetVisible(False)
            item_renderer.SetUiItem(
                item.get("newItemName", ""),
                item.get("newAuxValue", 0),
                True if item.get('enchantData') else False
            )
            count = item.get("count", "")
            return "" if count == 1 else str(count)
        else:
            item_renderer.SetVisible(False)
        return ""

    def inventory_items_stack_count_label(self, index):
        index += 9
        item_renderer = self.inventory_grid.GetChildByPath("/grid_item_for_inventory{}/item_cell/item/item_renderer".format(index - 8)).asItemRenderer()
        item = self.PlayerInventoryItemDict[index]
        if self.PlayerInventoryItemDict[index]:
            item_renderer.SetVisible(True)
            if item.get("FlyTo"):
                item_renderer.SetVisible(False)
            item_renderer.SetUiItem(
                item.get("newItemName", ""),
                item.get("newAuxValue", 0),
                True if item.get('enchantData') else False
            )
            count = self.PlayerInventoryItemDict[index].get("count", "")
            return "" if count == 1 else str(count)
        else:
            item_renderer.SetVisible(False)
        return ""
