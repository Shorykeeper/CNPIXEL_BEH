# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class AttackAnimBeginClientEvent(BaseEvent):
    """攻击动画开始时触发

    使用SetModel更换模型后，此事件方才生效
    """
    id = None


class AttackAnimEndClientEvent(BaseEvent):
    """攻击动画结束时触发

    使用SetModel更换模型后，此事件方才生效
    """
    id = None


class WalkAnimBeginClientEvent(BaseEvent):
    """行走动画开始时触发

    使用SetModel更换模型后，此事件方才生效
    """
    id = None


class WalkAnimEndClientEvent(BaseEvent):
    """行走动画结束时触发

    使用SetModel更换模型后，此事件方才生效
    """
    id = None
