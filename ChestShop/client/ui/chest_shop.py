# -*- coding: utf-8 -*-
import shop_ui_controller.inventory as inventory
import shop_ui_controller.move_item as move_item
import shop_ui_controller.move_item_pe as move_item_pe
import shop_ui_controller.shop as shop
from .BaseScreenNodeSystem import BaseScreenNodeSystem

from utils import *

class ui_path:
    base_path = "/large_chest_panel"
    root_screen = "/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel"
    inventory_grid = base_path + "/root_panel/chest_panel/inventory_panel_bottom_half_with_label/inventory_panel/inventory_grid"
    hotbar_grid = base_path + "/root_panel/chest_panel/hotbar_grid"
    chest_grid = base_path + "/root_panel/chest_panel/large_chest_panel_top_half/large_chest_grid"


class Main(BaseScreenNodeSystem):
    base_path = "/large_chest_panel"
    root_screen = "/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel"
    def __init__(self, namespace, name, param):
        super(Main, self).__init__(namespace, name, param)
        self.data = param.get('data', {})
        self.system = param.get('client', None)
        self.shop_id = self.data.get('shop_id', None)
        self.PlayerInventoryController = None
        self.MoveItemController = None
        self.ShopController = None
        self.PlayerInventoryItemDict = itemComp.GetPlayerAllItems(enum.ItemPosType.INVENTORY, True)  # type:list[dict]
        self.create_ui = False

    def Create(self):
        self.create_ui = True
        InputMode = CF.CreatePlayerView(levelId).GetToggleOption(enum.OptionId.INPUT_MODE)
        self.PlayerInventoryController = inventory.PlayerInventoryController(
            self,
            self.system,
            self.GetBaseUIControl(ui_path.inventory_grid).asGrid(),
            self.GetBaseUIControl(ui_path.hotbar_grid).asGrid()
        )
        self.MoveItemController = move_item_pe.MoveItemController(
            self,
            self.system,
            self.GetBaseUIControl(ui_path.inventory_grid).asGrid(),
            self.GetBaseUIControl(ui_path.hotbar_grid).asGrid()
        ) if InputMode == enum.InputMode.Touch else move_item.MoveItemController(
            self,
            self.system,
            self.GetBaseUIControl(ui_path.inventory_grid).asGrid(),
            self.GetBaseUIControl(ui_path.hotbar_grid).asGrid()
        )
        self.ShopController = shop.ShopController(
            self,
            self.system,
            self.GetBaseUIControl(ui_path.chest_grid).asGrid(),
            self.shop_id
        )

    @Listen.on("buy_goods_result", Listen.server)
    def on_buy_goods_result(self, event):
        if self.create_ui:
            if event.get("upgrade_data"):
                self.ShopController.upgrade_data = event["upgrade_data"].copy()
            if event.get("enchant_data"):
                self.ShopController.enchant_data = event["enchant_data"].copy()
            if event["success"]:
                self.player_sound(BUY_SUCCEED_SOUNDS)
                itemDict = event.get("goods_data", {})
                item_name = itemComp.GetItemBasicInfo(itemDict.get("itemDict", dict()).get("newItemName", ""),
                                                      itemDict.get("itemDict", dict()).get("newAuxValue", 0)).get("itemName", "")
                CF.CreateTextNotifyClient(levelId).SetLeftCornerNotify(
                    BUY_SUCCEED_TEXT.replace("{item_name}", item_name).replace(
                        "{price}", str(itemDict.get("price", 0))).replace(
                        "{currency}", CURRENCY_ENUM.get(itemDict.get("currency", ""), "§f[限免] 选队币")))
            else:
                itemDict = event.get("goods_data", {})
                if itemDict:
                    if itemDict.get("currency", "") == "experience":
                        if event.get("lv") is None:
                            return
                    item_name = itemComp.GetItemBasicInfo(itemDict.get("itemDict", dict()).get("newItemName", "air"),
                                                          itemDict.get("itemDict", dict()).get("newAuxValue", 0)).get("itemName", "")
                    CF.CreateTextNotifyClient(levelId).SetLeftCornerNotify(
                        BUY_FAIL_TEXT.replace("{item_name}", item_name).replace(
                            "{price}", str(itemDict.get("price", 0))).replace(
                            "{currency}", CURRENCY_ENUM.get(itemDict.get("currency", ""), "§f[限免] 选队币")).replace(
                                "{need_currency}", str(itemDict.get("price", 0) - event.get("lv", 0)))
                    )
                    self.player_sound(BUY_FAIL_SOUNDS)
            self.ShopController.set_goods_dict()
            self.update_player_inventory()

    @Listen.on("ActorAcquiredItemClientEvent")
    def on_actor_acquired_item_client_event(self, args):
        if args["acquireMethod"] == enum.ItemAcquisitionMethod.PickedUp:
            self.update_player_inventory()

    def update_player_inventory(self):
        """
        更新玩家背包
        """
        self.PlayerInventoryItemDict = itemComp.GetPlayerAllItems(enum.ItemPosType.INVENTORY, True)  # type:list[dict]
        self.PlayerInventoryController.PlayerInventoryItemDict = self.PlayerInventoryItemDict
        self.MoveItemController.PlayerInventoryItemDict = self.PlayerInventoryItemDict
        self.UpdateScreen()

    @ViewBinder.binding(ViewBinder.BF_BindString, "#shop_name")
    def shop_name(self):
        return SHOP_DATA.get(self.shop_id, dict()).get("name", "商店")

    @ViewBinder.binding(ViewBinder.BF_BindBool, "#pocket_slot_visible")
    def pocket_slot_visible(self):
        InputMode = CF.CreatePlayerView(levelId).GetToggleOption(enum.OptionId.INPUT_MODE)
        return True if InputMode == enum.InputMode.Touch else False

    @ViewBinder.binding_collection(ViewBinder.BF_BindString, "grid_item_for_hotbar", "#inventory_stack_label")
    def hotbar_items_stack_count_label(self, index):
        return self.PlayerInventoryController.hotbar_items_stack_count_label(index)
    @ViewBinder.binding_collection(ViewBinder.BF_BindString, "grid_item_for_hotbar", "#hover_text")
    def hotbar_items_label(self, index):
        return self.PlayerInventoryController.hotbar_items_label(index)
    @ViewBinder.binding_collection(ViewBinder.BF_BindString, "grid_item_for_inventory", "#inventory_stack_label")
    def inventory_items_stack_count_label(self, index):
        return self.PlayerInventoryController.inventory_items_stack_count_label(index)
    @ViewBinder.binding_collection(ViewBinder.BF_BindString, "grid_item_for_inventory", "#hover_text")
    def inventory_items_label(self, index):
        return self.PlayerInventoryController.inventory_items_label(index)
    @ViewBinder.binding_collection(ViewBinder.BF_BindString, "chest_grid_item", "#inventory_stack_label")
    def chest_items_stack_count_label(self, index):
        return self.ShopController.chest_items_stack_count_label(index)
    @ViewBinder.binding_collection(ViewBinder.BF_BindString, "chest_grid_item", "#hover_text")
    def chest_items_label(self, index):
        return self.ShopController.chest_items_label(index)

    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#container_take_all_place_all')  # 容器全部拿取_全部放置
    def container_take_all_place_all(self, args):
        self.MoveItemController.container_take_all_place_all(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#container_take_all_place_all')  # 容器全部拿取_全部放置
    def buy_goods(self, args):
        self.ShopController.buy_goods(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#container_take_half_place_one')  # 容器半拿取_放置一半
    def container_take_half_place_one(self, args):
        self.MoveItemController.container_take_half_place_one(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#container_auto_place')  # 容器自动放置
    def container_auto_place(self, args):
        self.MoveItemController.container_auto_place(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#drop_one')  # 丢弃一个
    def drop_one(self, args):
        self.MoveItemController.drop_one(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#drop_all')  # 丢弃全部
    def drop_all(self, args):
        self.MoveItemController.drop_all(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#drop_all_item')  # 丢弃全部
    def drop_all_item(self, args):
        self.MoveItemController.drop_all_item(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#shape_drawing')  # 形状绘制
    def shape_drawing(self, args):
        self.MoveItemController.shape_drawing(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, '#container_slot_hovered')  # 容器格子悬停
    def container_slot_hovered(self, args):
        self.MoveItemController.container_slot_hovered(args)
    @ViewBinder.binding(ViewBinder.BF_ButtonClick, '#double_pressed')  # 双击
    def double_pressed(self, args):
        self.MoveItemController.double_pressed(args)

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp, '#close_button_click')
    def close_button_click(self, args):
        clientApi.PopScreen()

    def set_player_inventory(self):
        """
        设置玩家背包
        """
        items = {(0, slotPos): item for slotPos, item in enumerate(self.PlayerInventoryItemDict)}
        self.system.NotifyToServer("set_player_inventory", {"items": items})

    def player_sound(self, (sound_name, volume, pitch)):
        """
        播放玩家音效
        """
        if self.create_ui:
            music.PlayCustomMusic(sound_name, (0, 0, 0), volume, pitch, False, playerId)

    def Destroy(self):
        """
        @description UI销毁时调用
        """
        self.create_ui = False
        InputMode = CF.CreatePlayerView(levelId).GetToggleOption(enum.OptionId.INPUT_MODE)
        if InputMode == enum.InputMode.Touch:
            return
        if self.MoveItemController.pick_up_item is not None:
            for pos, item in enumerate(self.PlayerInventoryItemDict):
                if item is None:
                    self.PlayerInventoryItemDict[pos] = self.MoveItemController.pick_up_item
                    break
        self.set_player_inventory()
