# -*- coding: utf-8 -*-
from utils import *


class Main(BaseCustomScreenProxy):
    def __init__(self, screenName, screenNode):
        super(Main, self).__init__(screenName, screenNode)
        self.ui_create = False
        self.CPS_left_click_set = []
        self.CPS_right_click_set = []

    def OnCreate(self):
        self.ui_create = True
        if self.screen is None:
            return

        panel = self.screen.GetBaseUIControl(base_path)
        self.child = self.screen.CreateChildControl("xg_hud.root_panel_watermelon", "root_panel_watermelon", panel)

    @Listen("LeftClickBeforeClientEvent")
    def OnLeftClickBeforeClientEvent(self, args):
        self.CPS_left_click_set.append(time.time())

    @Listen("TapBeforeClientEvent")
    def OnTapBeforeClientEvent(self, args):
        self.CPS_left_click_set.append(time.time())

    @Listen("RightClickBeforeClientEvent")
    def OnRightClickBeforeClientEvent(self, args):
        self.CPS_right_click_set.append(time.time())

    @ViewBinder.binding(ViewBinder.BF_BindBool, "#input_mode.keyboard_and_mouse")
    def return_input_mode_keyboard_and_mouse(self):
        if CF.CreatePlayerView(PlayerId).GetToggleOption("INPUT_MODE") == 0:
            return True
        return False

    @ViewBinder.binding(ViewBinder.BF_BindBool, "#input_mode.touch")
    def return_input_mode_touch(self):
        if CF.CreatePlayerView(PlayerId).GetToggleOption("INPUT_MODE") == 1:
            return True
        return False

    @ViewBinder.binding(ViewBinder.BF_BindBool, "#input_mode.controller")
    def return_input_mode_controller(self):
        if CF.CreatePlayerView(PlayerId).GetToggleOption("INPUT_MODE") == 2:
            return True
        return False

    @ViewBinder.binding(ViewBinder.BF_BindString, "#FPS_value")
    def return_FPS_value(self):
        return "FPS:{}".format(int(Game.GetFps()))

    @ViewBinder.binding(ViewBinder.BF_BindString, "#CPS_value")
    def return_CPS_value(self):
        now = time.time()
        for left in self.CPS_left_click_set:
            if now - left > 1:
                self.CPS_left_click_set.remove(left)
                continue
        for right in self.CPS_right_click_set:
            if now - right > 1:
                self.CPS_right_click_set.remove(right)
                continue
        left_cps = len(self.CPS_left_click_set)
        right_cps = len(self.CPS_right_click_set)

        if (left_cps >= 24) or (right_cps >= 50):
            self.system.NotifyToServer("CPS_high", {"L": left_cps, "R": right_cps})

        if left_cps == 0 and right_cps == 0:
            return ""
        elif left_cps == 0:
            return " | CPS:0|{}".format(right_cps)
        elif right_cps == 0:
            return " | CPS:{}".format(left_cps)
            
        else:
            return " | CPS:{}|{}".format(left_cps, right_cps)

    def OnDestroy(self):
        """
        @description UI销毁时调用
        """
        self.screen.RemoveChildControl(self.child)
        self.ui_create = False

