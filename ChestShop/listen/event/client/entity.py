# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class ApproachEntityClientEvent(BaseEvent):
    """
    玩家接近实体时触发
    """
    playerId = None
    entityId = None


class EntityModelChangedClientEvent(BaseEvent):
    """
    事件机制：实体模型改变时触发
    """
    entityId = None
    newModel = None
    oldModel = None


class EntityStopRidingEvent(BaseEvent):
    """
    事件机制：当实体停止骑乘时触发
    以下情况不允许取消
        - ride组件StopEntityRiding接口
        - 玩家传送时
        - 坐骑死亡时
        - 玩家看不见时
        - 玩家死亡时
        - 未服务的马
        - 海洋生物进入水中
        - 切换维度
    """
    id = None
    rideId = None
    exitFromRider = None
    entityIsBeingDestroyed = None
    switchingRides = None
    cancel = None


class HealthChangeClientEvent(BaseEvent):
    """
    实体生命值发生变化时触发
    """
    entityId = None
    _from = None
    to = None

    def __getattribute__(self, name):
        if name == '_from':
            return self.__dict__['from']
        return super(HealthChangeClientEvent, self).__getattribute__(name)

    def __setattr__(self, name, value):
        if name == '_from':
            self.__dict__['from'] = value
        else:
            super(HealthChangeClientEvent, self).__setattr__(name, value)


class LeaveEntityClientEvent(BaseEvent):
    """玩家离开实体时触发"""
    playerId = None
    entityId = None


class OnGroundClientEvent(BaseEvent):
    """
    实体着地事件。玩家，粒子，矿车，掉落的物品，火焰的TNT掉落地面时触发，其他实体着地时不触发。

    - id : str 实体id

    """
    pass


class StartRidingClientEvent(BaseEvent):
    """
    事件机制：一个实体即将骑乘另一个实体
    """
    cancel = None
    actorId = None
    victimId = None
