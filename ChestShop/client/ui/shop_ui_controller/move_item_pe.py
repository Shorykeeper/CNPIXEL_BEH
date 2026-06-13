# coding=utf-8
import copy

from ..utils import *
class ButtonType:
    hotbar = "grid_item_for_hotbar"
    inventory = "grid_item_for_inventory"
    chest = "chest_grid_item"


offset_animation = {
    "namespace": "chest_shop",
    "flying_item_renderer_animation": {
        "anim_type": "offset",
        "duration": 0.1,
        "from": [
            0,
            0
        ],
        "next": "",
        "to": [
            0,
            0
        ]
    },
}


class MoveItemController:

    def __init__(
            self,
            screen_node,
            client_system,
            inventory_grid,
            hotbar_grid,
            ):
        self.screen_node, self.system, self.inventory_grid, self.hotbar_grid= screen_node, client_system, inventory_grid, hotbar_grid
        self.PlayerInventoryItemDict = self.screen_node.PlayerInventoryItemDict
        self.pick_up_item = None
        self.pick_up_item_renderer = self.screen_node.GetBaseUIControl(
            self.screen_node.base_path + "/root_panel/inventory_selected_icon_button/item_renderer").asItemRenderer()
        self.pick_up_item_stack_count_label = self.screen_node.GetBaseUIControl(
            self.screen_node.base_path + "/root_panel/inventory_selected_icon_button/item_renderer/stack_count_label").asLabel()
        self.selected_cell = ("", 0)  # type: tuple[str, int]
        self.old_selected_cell = ("", 0)  # type: tuple[str, int]
        self.item_message_timer = None
        self.item_message_id = None

    def container_take_all_place_all(self, args):  # 容器全部拿取_全部放置
        """
        容器全部拿取_全部放置
        """
        index = self.reset_index(args)
        if index is None:
            return
        button_type = args["#collection_name"]
        itenDict = self.PlayerInventoryItemDict[index]
        if itenDict is not None:
            if button_type == ButtonType.hotbar:
                self.hotbar_grid.GetChildByPath("/grid_item_for_hotbar{}/item_selected_image_panel/item_selected_image".format(index + 1)).asImage().SetVisible(True)
            elif button_type == ButtonType.inventory:
                self.inventory_grid.GetChildByPath("/grid_item_for_inventory{}/item_selected_image_panel/item_selected_image".format(index - 8)).asImage().SetVisible(True)
        self.old_selected_cell = copy.deepcopy(self.selected_cell)
        self.selected_cell = (button_type, index)
        if self.pick_up_item is None:
            pick_up_item = self.PlayerInventoryItemDict[index]
            self.pick_up_item = pick_up_item
            if pick_up_item is None:
                self.selected_cell = ("", 0)
            else:
                self.create_item_message(pick_up_item)
        else:
            pick_up_item = self.PlayerInventoryItemDict[index]
            self.create_item_message(pick_up_item)
            if self.selected_cell == self.old_selected_cell:
                self.pick_up_item = None
                self.selected_cell = ("", 0)
                self.set_item_selected_image()
                return
            maxStackSize = itemComp.GetItemBasicInfo(self.pick_up_item["newItemName"], self.pick_up_item["newAuxValue"]).get("maxStackSize", 0)
            if pick_up_item is None:
                self.exchange_pick_up_item(index)
                self.set_item_selected_image()
            elif pick_up_item.get("newItemName") == self.pick_up_item.get("newItemName"):
                if pick_up_item.get("newAuxValue", 0) == self.pick_up_item.get("newAuxValue", 0):
                    if pick_up_item.get("count") + self.pick_up_item.get("count") <= maxStackSize:
                        self.pick_up_item["count"] += pick_up_item.get("count")
                        self.PlayerInventoryItemDict[index] = None
                        self.exchange_pick_up_item(index)
                        self.set_item_selected_image()
                    elif pick_up_item.get("count") == maxStackSize:
                        self.set_item_selected_image()
                    else:
                        self.PlayerInventoryItemDict[index]["count"] -= maxStackSize - self.pick_up_item["count"]
                        self.pick_up_item["count"] = maxStackSize
                        self.exchange_pick_up_item(index)
                        self.set_item_selected_image()
                else:
                    self.exchange_pick_up_item(index)
                    self.set_item_selected_image()
            else:
                self.exchange_pick_up_item(index)
                self.set_item_selected_image()
            self.pick_up_item = None
            self.old_selected_cell = copy.deepcopy(self.selected_cell)
            self.set_item_selected_image()

    def set_item_selected_image(self):
        old_button_type = self.old_selected_cell[0]
        old_index = self.old_selected_cell[1]
        if old_button_type == ButtonType.hotbar:
            self.hotbar_grid.GetChildByPath("/grid_item_for_hotbar{}/item_selected_image_panel/item_selected_image".format(old_index + 1)).asImage().SetVisible(False)
        elif old_button_type == ButtonType.inventory:
            self.inventory_grid.GetChildByPath("/grid_item_for_inventory{}/item_selected_image_panel/item_selected_image".format(old_index - 8)).asImage().SetVisible(False)
        self.old_selected_cell = ("", 0)

    def exchange_pick_up_item(self, index):
        """
        交换鼠标拿起的物品
        """
        old_index = self.old_selected_cell[1]
        self.PlayerInventoryItemDict[index], self.PlayerInventoryItemDict[old_index] = self.PlayerInventoryItemDict[old_index], self.PlayerInventoryItemDict[index]
        item_dict = self.PlayerInventoryItemDict[index]
        pos = {
            "start_x": 0,
            "start_y": 0,
            "end_x": 0,
            "end_y": 0,
            "index": 0,
            "index_": 0
        }
        if self.old_selected_cell[0] == ButtonType.hotbar:
            start_x, start_y = self.hotbar_grid.GetChildByPath("/grid_item_for_hotbar{}".format(self.old_selected_cell[1] + 1)).GetGlobalPosition()
            pos["start_x"] = start_x + 1
            pos["start_y"] = start_y + 1
        elif self.old_selected_cell[0] == ButtonType.inventory:
            start_x, start_y = self.inventory_grid.GetChildByPath("/grid_item_for_inventory{}".format(self.old_selected_cell[1] - 8)).GetGlobalPosition()
            pos["start_x"] = start_x + 1
            pos["start_y"] = start_y + 1
        if self.selected_cell[0] == ButtonType.hotbar:
            end_x, end_y = self.hotbar_grid.GetChildByPath("/grid_item_for_hotbar{}".format(self.selected_cell[1] + 1)).GetGlobalPosition()
            pos["end_x"] = end_x + 1
            pos["end_y"] = end_y + 1
        elif self.selected_cell[0] == ButtonType.inventory:
            end_x, end_y = self.inventory_grid.GetChildByPath("/grid_item_for_inventory{}".format(self.selected_cell[1] - 8)).GetGlobalPosition()
            pos["end_x"] = end_x + 1
            pos["end_y"] = end_y + 1

        offset_animation["flying_item_renderer_animation"]["from"] = [pos["start_x"], pos["start_y"]]
        offset_animation["flying_item_renderer_animation"]["to"] = [pos["end_x"], pos["end_y"]]
        clientApi.RegisterUIAnimations(offset_animation)
        flying_item_renderer_id = "flying_item_renderer{}".format(str(int(time.time() * 1000)))
        panel = self.screen_node.GetBaseUIControl(self.screen_node.base_path)
        self.screen_node.CreateChildControl("chest_shop.flying_item_renderer", flying_item_renderer_id, panel)
        flying_item_renderer = self.screen_node.GetBaseUIControl(
            self.screen_node.base_path + "/" + flying_item_renderer_id).asItemRenderer()
        flying_item_renderer.SetUiItem(
            item_dict.get("newItemName", ""),
            item_dict.get("newAuxValue", 0),
            True if item_dict.get('enchantData') else False
        )
        def set_new_item(flying_item_renderer_id):
            self.screen_node.RemoveChildControl(flying_item_renderer_id)
            if self.old_selected_cell[0] == ButtonType.hotbar:
                self.PlayerInventoryItemDict[self.old_selected_cell[1]] = item_dict
            elif self.old_selected_cell[0] == ButtonType.inventory:
                self.PlayerInventoryItemDict[self.old_selected_cell[1]] = item_dict
            self.screen_node.UpdateScreen()

        game.AddTimer(0.4, set_new_item, flying_item_renderer)
        self.screen_node.set_player_inventory()

    def create_item_message(self, item_dict):
        """
        创建物品消息
        """
        if item_dict:
            if self.item_message_timer:
                self.screen_node.RemoveChildControl(self.item_message_id)
                game.CancelTimer(self.item_message_timer)
            item_name = itemComp.GetItemBasicInfo(item_dict.get("newItemName", ""), item_dict.get("newAuxValue", 0))["itemName"]
            panel = self.screen_node.GetBaseUIControl("/")
            item_message_id = "item_message{}".format(str(int(time.time() * 1000)))
            self.item_message_id = self.screen_node.CreateChildControl("chest_shop.item_message", item_message_id, panel)
            self.screen_node.GetBaseUIControl("/{}/label".format(item_message_id)).asLabel().SetText(item_name)
            self.item_message_timer = game.AddTimer(3.1, lambda: self.screen_node.RemoveChildControl(item_message_id))

    def container_take_half_place_one(self, args):  # 容器半拿取_放置一半
        """
        容器半拿取_放置一半
        """
        pass

    def container_auto_place(self, args):  # 容器自动放置
        """
        容器自动放置
        """
        pass


    def drop_one(self, args):  # 丢弃一个
        """
        丢弃一个
        """
        pass

    def drop_all(self, args):  # 丢弃全部
        """
        丢弃全部
        """
        pass

    def drop_all_item(self, args):  # 丢弃全部物品
        """
        丢弃全部物品
        """
        if self.pick_up_item is not None:
            self.PlayerInventoryItemDict[self.selected_cell[1]] = None
            rotComp = CF.CreateRot(playerId)
            self.system.NotifyToServer("spawn_item", {"itemDict": self.pick_up_item,
                                                      "pos": posComp.GetPos(),
                                                      "dimension": game.GetCurrentDimension(),
                                                      "dir": clientApi.GetDirFromRot(rotComp.GetRot())})
            self.pick_up_item = None
            self.old_selected_cell = copy.deepcopy(self.selected_cell)
            self.selected_cell = ("", 0)
            self.set_item_selected_image()
            self.screen_node.UpdateScreen()
            self.screen_node.set_player_inventory()

    def shape_drawing(self, args):  # 形状绘制
        """
        形状绘制
        """
        pass

    def container_slot_hovered(self, args):  # 容器格子悬停
        """
        容器格子悬停
        """
        pass

    def double_pressed(self, args):  # 双击
        """
        双击
        """
        pass

    def reset_index(self, args):  # 重置索引
        """
        重置索引
        """
        index = args["#collection_index"]
        button_type = args["#collection_name"]
        if button_type == ButtonType.hotbar:
            return index
        elif button_type == ButtonType.inventory:
            return index + 9
        else:
            return None
