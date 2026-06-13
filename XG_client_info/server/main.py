# -*- coding: utf-8 -*-
"""
Created on 2025-11-03
服务端系统
"""
from utils import *
class eid:
    pass


class Main(BaseServer):
    def __init__(self, namespace, systemName):
        super(Main, self).__init__(namespace, systemName)

    @Listen(event_type=Listen.client)
    def CPS_high(self, args):
        pid = args["__id__"]
        L = args["L"]
        R = args["R"]
        if Game.GetPlayerGameType(pid) == 6: # Spectator
            return
        showMsg("§l§bAur§fora §8| §r§e{} §7failed §cCombat(A)§7(VL.{}-{})".format(NameComp(pid).GetName(), L, R))
        addTag("ac_ban", pid)
        CommandComp.SetCommand("tag @s add 封禁", pid)



