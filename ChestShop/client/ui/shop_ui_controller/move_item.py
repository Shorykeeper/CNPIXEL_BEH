# coding=utf-8
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
        self.selected_cell_set = set()  # type: set[tuple[str, int]]

    def compare_item_dict(self, item_dict_1, item_dict_2):
        pass

    def container_take_all_place_all(self, args):  # 容器全部拿取_全部放置
        """
        容器全部拿取_全部放置
        """
        index = self.reset_index(args)
        if index is None:
            return
        button_type = args["#collection_name"]
        if self.pick_up_item is None:
            if button_type == ButtonType.hotbar:
                path = "/grid_item_for_hotbar{}/item_cell/item/item_renderer".format(index + 1)
                self.hotbar_grid.GetChildByPath(path).asItemRenderer().SetVisible(False)
            elif button_type == ButtonType.inventory:
                path = "/grid_item_for_inventory{}/item_cell/item/item_renderer".format(index - 8)
                self.inventory_grid.GetChildByPath(path).asItemRenderer().SetVisible(False)
            pick_up_item = self.PlayerInventoryItemDict[index]
            if pick_up_item is not None:
                self.set_pick_up_item(pick_up_item)
                self.PlayerInventoryItemDict[index] = None
        else:
            maxStackSize = itemComp.GetItemBasicInfo(self.pick_up_item["newItemName"], self.pick_up_item["newAuxValue"]).get("maxStackSize", 0)
            self.selected_cell_set.add((button_type, index))
            pick_up_item = self.PlayerInventoryItemDict[index]
            if pick_up_item is None:
                self.exchange_pick_up_item(index)
            elif self.pick_up_item.get("newItemName", "") == pick_up_item.get("newItemName"):
                if self.pick_up_item.get("newAuxValue", 0) == pick_up_item.get("newAuxValue"):
                    if self.PlayerInventoryItemDict[index]["count"] + self.pick_up_item["count"] <= maxStackSize:
                        self.pick_up_item["count"] += self.PlayerInventoryItemDict[index]["count"]
                        self.clear_pick_up_item(index)
                    elif self.PlayerInventoryItemDict[index]["count"] == maxStackSize:
                        self.exchange_pick_up_item(index)
                    else:
                        self.pick_up_item["count"] -= maxStackSize - self.PlayerInventoryItemDict[index]["count"]
                        self.PlayerInventoryItemDict[index]["count"] = maxStackSize
                        self.set_pick_up_item(self.pick_up_item)
                else:
                    self.pick_up_item = pick_up_item
                    self.exchange_pick_up_item(index)
            else:
                self.exchange_pick_up_item(index)
        self.screen_node.UpdateScreen()
        self.screen_node.set_player_inventory()

    def container_take_half_place_one(self, args):  # 容器半拿取_放置一半
        """
        容器半拿取_放置一半
        """
        index = self.reset_index(args)
        if index is None:
            return
        pick_up_item = self.PlayerInventoryItemDict[index]
        if pick_up_item is None:
            if self.pick_up_item is not None:
                self.pick_up_item["count"] -= 1
                self.PlayerInventoryItemDict[index] = self.pick_up_item.copy()
                self.PlayerInventoryItemDict[index]["count"] = 1
                self.set_pick_up_item(self.pick_up_item)
        else:
            if self.pick_up_item is None:
                pick_up_item = pick_up_item.copy()
                half_count = pick_up_item["count"] // 2
                remainder = pick_up_item["count"] % 2
                if half_count > 0:
                    self.PlayerInventoryItemDict[index]["count"] = half_count
                else:
                    self.PlayerInventoryItemDict[index] = None
                pick_up_item["count"] = half_count + remainder
                self.set_pick_up_item(pick_up_item)
            else:
                if self.pick_up_item.get("newItemName", "") == pick_up_item.get("newItemName"):
                    if self.pick_up_item.get("newAuxValue", 0) == pick_up_item.get("newAuxValue"):
                        maxStackSize = itemComp.GetItemBasicInfo(self.pick_up_item["newItemName"], self.pick_up_item["newAuxValue"]).get("maxStackSize", 0)
                        if self.PlayerInventoryItemDict[index]["count"] + 1 <= maxStackSize:
                            self.PlayerInventoryItemDict[index]["count"] += 1
                            self.pick_up_item["count"] -= 1
                            self.set_pick_up_item(self.pick_up_item)
                        else:
                            self.exchange_pick_up_item(index)
        self.screen_node.UpdateScreen()
        self.screen_node.set_player_inventory()

    def container_auto_place(self, args):  # 容器自动放置
        """
        容器自动放置
        """
        index = self.reset_index(args)
        if index is None:
            return
        item_dict = self.PlayerInventoryItemDict[index]
        self.PlayerInventoryItemDict[index] = None
        if item_dict is None:
            return
        item_dict["FlyTo"] = True
        button_type = args["#collection_name"]
        pos = {
            "start_x": 0,
            "start_y": 0,
            "end_x": 0,
            "end_y": 0,
            "index": 0,
            "index_": 0,
            "item": False
        }
        maxStackSize = itemComp.GetItemBasicInfo(item_dict["newItemName"],
                                                 item_dict["newAuxValue"]).get("maxStackSize", 0)
        if button_type == ButtonType.hotbar:
            start_x, start_y = self.hotbar_grid.GetChildByPath("/grid_item_for_hotbar{}".format(index + 1)).GetGlobalPosition()
            pos["start_x"] = start_x + 1
            pos["start_y"] = start_y + 1
            for index_, item in enumerate(self.PlayerInventoryItemDict[9:]):
                if item is None:
                    self.PlayerInventoryItemDict[index_ + 9] = item_dict.copy()
                    end_x, end_y = self.inventory_grid.GetChildByPath(
                        "/grid_item_for_inventory{}".format(index_ + 1)).GetGlobalPosition()
                    pos["end_x"] = end_x + 1
                    pos["end_y"] = end_y + 1
                    pos["index_"] = index_
                    pos["item"] = True
                    break

        elif button_type == ButtonType.inventory:
            start_x, start_y = self.inventory_grid.GetChildByPath("/grid_item_for_inventory{}".format(index - 8)).GetGlobalPosition()
            pos["start_x"] = start_x + 1
            pos["start_y"] = start_y + 1
            for index_, item in enumerate(self.PlayerInventoryItemDict[:9]):
                if item is None:
                    self.PlayerInventoryItemDict[index_] = item_dict.copy()
                    end_x, end_y = self.hotbar_grid.GetChildByPath("/grid_item_for_hotbar{}".format(index_ + 1)).GetGlobalPosition()
                    pos["end_x"] = end_x + 1
                    pos["end_y"] = end_y + 1
                    pos["index"] = index_
                    pos["item"] = True
                    break

        if not pos["item"]:
            item_dict.pop("FlyTo")
            self.PlayerInventoryItemDict[index] = item_dict
            return

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
        if item_dict.get("FlyTo"):
            item_dict.pop("FlyTo")

        def set_new_item():
            self.screen_node.RemoveChildControl(flying_item_renderer)
            if button_type == ButtonType.hotbar:
                self.PlayerInventoryItemDict[index_ + 9] = item_dict
            elif button_type == ButtonType.inventory:
                self.PlayerInventoryItemDict[index_] = item_dict
            self.screen_node.UpdateScreen()

        game.AddTimer(0.4, set_new_item)
        self.screen_node.set_player_inventory()


    def drop_one(self, args):  # 丢弃一个
        """
        丢弃一个
        """
        index = self.reset_index(args)
        if index is None:
            return
        item_dict = self.PlayerInventoryItemDict[index]
        if item_dict is None:
            return
        self.PlayerInventoryItemDict[index] = item_dict.copy()
        self.PlayerInventoryItemDict[index]["count"] -= 1
        item_dict["count"] = 1
        rotComp = CF.CreateRot(playerId)
        self.system.NotifyToServer("spawn_item", {"itemDict": item_dict,
                                                  "pos": posComp.GetPos(),
                                                  "dimension": game.GetCurrentDimension(),
                                                  "dir": clientApi.GetDirFromRot(rotComp.GetRot())})
        self.screen_node.UpdateScreen()
        self.screen_node.set_player_inventory()

    def drop_all(self, args):  # 丢弃全部
        """
        丢弃全部
        """
        index = self.reset_index(args)
        if index is None:
            return
        item_dict = self.PlayerInventoryItemDict[index]
        if item_dict is None:
            return
        self.PlayerInventoryItemDict[index] = None
        rotComp = CF.CreateRot(playerId)
        self.system.NotifyToServer("spawn_item", {"itemDict": item_dict,
                                                  "pos": posComp.GetPos(),
                                                  "dimension": game.GetCurrentDimension(),
                                                  "dir": clientApi.GetDirFromRot(rotComp.GetRot())})
        self.screen_node.UpdateScreen()
        self.screen_node.set_player_inventory()

    def drop_all_item(self, args):  # 丢弃全部物品
        """
        丢弃全部物品
        """
        if self.pick_up_item is not None:
            rotComp = CF.CreateRot(playerId)
            self.system.NotifyToServer("spawn_item", {"itemDict": self.pick_up_item,
                                                      "pos": posComp.GetPos(),
                                                      "dimension": game.GetCurrentDimension(),
                                                      "dir": clientApi.GetDirFromRot(rotComp.GetRot())})
            self.pick_up_item = None
            self.pick_up_item_renderer.SetVisible(False)
            self.screen_node.UpdateScreen()
            self.screen_node.set_player_inventory()

    def shape_drawing(self, args):  # 形状绘制
        """
        形状绘制
        """
        index = self.reset_index(args)
        if index is None:
            return

    def container_slot_hovered(self, args):  # 容器格子悬停
        """
        容器格子悬停
        """
        index = self.reset_index(args)
        if index is None:
            return
        pass

    def double_pressed(self, args):  # 双击
        """
        双击
        """
        index = self.reset_index(args)
        if index is None:
            return
        print "double_pressed", index
        item_dict = self.PlayerInventoryItemDict[index]
        self.PlayerInventoryItemDict[index] = None
        if item_dict is None:
            return
        button_type = args["#collection_name"]
        if button_type == ButtonType.hotbar:
            for index_, item in enumerate(self.PlayerInventoryItemDict[9:]):
                if item is None:
                    self.PlayerInventoryItemDict[index_ + 9] = item_dict.copy()
                    break

        elif button_type == ButtonType.inventory:
            for index_, item in enumerate(self.PlayerInventoryItemDict[:9]):
                if item is None:
                    self.PlayerInventoryItemDict[index_] = item_dict.copy()
                    break
        self.screen_node.UpdateScreen()
        self.screen_node.set_player_inventory()


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

    def set_pick_up_item(self, item_dict):
        """
        设置鼠标拿起的物品
        """
        self.pick_up_item = item_dict
        self.pick_up_item_renderer.SetVisible(True)
        self.pick_up_item_renderer.SetUiItem(
            item_dict.get("newItemName", ""),
            item_dict.get("newAuxValue", 0),
            True if item_dict.get('enchantData') else False
        )
        count = self.pick_up_item["count"]
        self.pick_up_item_stack_count_label.SetText(str("" if count == 1 else count))

    def clear_pick_up_item(self, index):
        """
        清空鼠标拿起的物品
        """
        self.PlayerInventoryItemDict[index] = self.pick_up_item
        self.pick_up_item = None
        self.pick_up_item_renderer.SetVisible(False)

    def exchange_pick_up_item(self, index):
        """
        交换鼠标拿起的物品
        """
        self.PlayerInventoryItemDict[index], self.pick_up_item = self.pick_up_item, self.PlayerInventoryItemDict[index]
        if self.pick_up_item is not None:
            self.set_pick_up_item(self.pick_up_item)
        else:
            self.pick_up_item_renderer.SetVisible(False)

    def test_pick_up_item(self):
        """
        测试鼠标拿起的物品
        """
        if self.pick_up_item is not None:
            return self.pick_up_item
        else:
            return None
