# -*- coding: utf-8 -*-
from .BaseScreenNodeSystem import BaseScreenNodeSystem

from utils import *

class Main(BaseScreenNodeSystem):
    def __init__(self, namespace, name, param):
        super(Main, self).__init__(namespace, name, param)
        self.system = param.get('client', None)
        self.list_control = set()
        self.player_list = {}

    def Create(self):
        pass

    def show_player_list(self):
        panel = self.GetBaseUIControl("/stack_panel/panel/list")
        panel_size = 0
        ping_size = 0
        first_text = self.CreateChildControl("player_list.text", "first_text", self.GetBaseUIControl("/stack_panel/panel"))
        first_text.asLabel().SetText(FIRST_TEXT, True)
        self.list_control.add(first_text)
        for player_id, player_data in self.player_list.items():
            control = self.CreateChildControl("player_list.player_name", player_id, panel)
            self.list_control.add(control)
            headshot = HEADSHOT_LIST[random.randint(0, len(HEADSHOT_LIST)-1)]
            self.GetBaseUIControl("/stack_panel/panel/list/{}".format(player_id)).asLabel().SetText(headshot + player_data["name"], True)
            x = self.GetBaseUIControl("/stack_panel/panel/list/{}".format(player_id)).GetSize()[0]
            if x > panel_size:
                panel_size = x
            ping = int(player_data.get("ping", 0) * 1000)
            if ping > PING[3]:
                ping = PING[3]
            image = "" if ping < PING[0] else "" if ping < PING[1] else "" if ping < PING[2] else ""
            self.GetBaseUIControl("/stack_panel/panel/list/{}/ping".format(player_id)).asLabel().SetText("§e" + str(ping) + image, True)
            p_x = self.GetBaseUIControl("/stack_panel/panel/list/{}/ping".format(player_id)).GetSize()[0]
            if p_x > ping_size:
                ping_size = p_x
        last_text = self.CreateChildControl("player_list.text", "last_text", self.GetBaseUIControl("/stack_panel/panel"))
        last_text.asLabel().SetText(LAST_TEXT, True)
        self.list_control.add(last_text)
        position = list(last_text.GetPosition())
        position[1] += 11 * len(self.player_list) + 10
        last_text.SetPosition(tuple(position))
        background = self.GetBaseUIControl("/stack_panel/panel/background")
        background_size = list(background.GetSize())
        for control in self.list_control:
            if control.GetChildByPath("/ping") is not None:
                control.SetSize((panel_size, 11), True)
                control.GetChildByPath("/ping").SetSize((ping_size, 11), True)
                x = control.GetSize()[0] + control.GetChildByPath("/ping").GetSize()[0] + 5
                if x > background_size[0]:
                    background_size[0] = x
            else:
                x = control.GetSize()[0]
                if x > background_size[0]:
                    background_size[0] = x
        background_size[1] = 11 * len(self.player_list) + 20
        background.SetSize(tuple(background_size), True)

    def hide_player_list(self):
        for control in self.list_control:
            self.RemoveChildControl(control)
        self.list_control.clear()
        background = self.GetBaseUIControl("/stack_panel/panel/background")
        background.SetSize((0, 0), True)

    @Listen.on("get_player_name_list", Listen.server)
    def get_player_name_list(self, player_list):
        self.player_list = player_list
        self.system.NotifyToServer("get_player_name_list", {"ping": time.time()})

    @ViewBinder.binding(ViewBinder.BF_ButtonClickDown, "#pe_button_pressed")
    def button_click_down(self, args):
        self.show_player_list()

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp, "#pe_button_pressed")
    def button_click_up(self, args):
        self.hide_player_list()

    @Listen.on(client.OnKeyPressInGame)
    def onKeyPressInGame(self, args):
        if args["screenName"] == "hud_screen":
            if args["key"] == str(enum.KeyBoardType.KEY_TAB):
                if args["isDown"] == "1":
                    self.show_player_list()
                else:
                    self.hide_player_list()

    @Listen.on(client.OnGamepadKeyPressClientEvent)
    def onGamepadKeyPressClientEvent(self, args):
        if args["screenName"] == "hud_screen":
            if args["key"] == enum.GamepadKeyType.KEY_VIEW:
                if args["isDown"] == "1":
                    self.show_player_list()
                else:
                    self.hide_player_list()


    def Destroy(self):
        """
        @description UI销毁时调用
        """
        pass
