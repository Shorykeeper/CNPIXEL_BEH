# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class PlayerInventoryOpenScriptServerEvent(BaseEvent):
    """
    某个客户端打开物品背包界面时触发
    """
    playerId = None
    isCreative = None