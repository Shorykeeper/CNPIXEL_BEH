# -*- coding: utf-8 -*
"""
Created on 2025/6/4
"""
from ..utils import *

class PlayerListController(BaseModule):

    def __init__(self):
        super(PlayerListController, self).__init__()
        self.ping_timer = 0
        self.player_list = {}

    @Listen.on(server.OnScriptTickServer)
    def on_script_tick_server(self):
        if self.ping_timer == 30:
            self.ping_timer = 0
            players = serverApi.GetPlayerList()
            self.system.NotifyToMultiClients(players, "get_player_name_list", self.player_list)
            for player in self.player_list:
                if player not in players:
                    self.player_list.pop(player)
        else:
            self.ping_timer += 1

    @Listen.on("get_player_name_list", Listen.client)
    def get_player_name_list(self, args):
        pid = args["__id__"]
        scoreboard = game.GetAllPlayerScoreboardObjects()  # type:list[dict]
        value = 0
        refix = ""
        for score in scoreboard:
            if pid == score["playerId"]:
                scoreList = score["scoreList"]
                for score in scoreList:
                    if score["name"] == "A1T12P":
                        value = score["value"]
                    elif score["name"] == "S8Q83P":
                        refix = REFIX_ENUM.get(score["value"], "")
        name = nameComp(pid).GetName()
        ping = time.time() - args["ping"]
        color = TEAM_ENUM.get(value, {"color": "§f", "chinese": ""})
        self.player_list[pid] = {"name": "{}§l{}{} §r{}{}".format(refix, color["color"], color["chinese"], color["color"], name), "ping": ping}