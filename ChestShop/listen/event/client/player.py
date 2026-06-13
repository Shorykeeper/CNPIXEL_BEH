# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class ApproachEntityClientEvent(BaseEvent):
    """玩家接近实体时触发"""
    playerId = None
    entityId = None


class LeaveEntityClientEvent(BaseEvent):
    """玩家离开实体时触发"""
    playerId = None
    entityId = None


class DimensionChangeClientEvent(BaseEvent):
    """玩家维度变化时客户端抛出

    当通过传送门从末地回到主世界时，toY值为32767，其他情况下一般会比设置值高1.62
    """
    playerId = None
    fromDimensionId = None
    toDimensionId = None
    fromX = None
    fromY = None
    fromZ = None
    toX = None
    toY = None
    toZ = None


class DimensionChangeFinishClientEvent(BaseEvent):
    """玩家维度变化完成后客户端抛出
    当通过传送门从末地回到主世界时，toPos的y值为32767，其他情况下一般会比设置值高1.62
    """
    playerId = None
    fromDimensionId = None
    toDimensionId = None
    toPos = None


class ExtinguishFireClientEvent(BaseEvent):
    """
    玩家熄灭火焰时触发。下雨、泼水等方式的火焰不会触发。
    """
    pos = None
    playerId = None
    cancel = None


class GameTypeChangedClientEvent(BaseEvent):
    """个人游戏模式发生变更时客户端触发。
    游戏模式：GetMinecraftEnum().GameType.*:Survival，Creative，Adventure分别对应0~2 默认游戏模式发生变更时最后会映射在个人游戏模式之上。
    """
    playerId = None
    oldGameType = None
    newGameType = None


class OnPlayerHitBlockClientEvent(BaseEvent):
    """
    触发机制：通过OpenPlayerHitBlockDetection打开方块破坏检测后，当玩家破坏到方块时触发此事件。玩家着地时会触发OnGroundClientEvent，而不是此事件。客户端和服务端分别做破坏检测，可能会两个事件返回的结果略有差异。
    """
    playerId = None
    posX = None
    posY = None
    posZ = None
    blockId = None
    auxValue = None


class OnPlayerHitMobClientEvent(BaseEvent):
    """
    触发机制：通过OpenPlayerHitMobDetection打开实体破坏检测后，当有实体与玩家破坏时触发此事件。注意：客户端和服务端分别做破坏检测，可能会两个事件返回的结果略有差异。
    """
    playerList = None


class PerspChangeClientEvent(BaseEvent):
    """
    视角切换时会触发的事件
    视角数字代表含义 0: 第一人称 1: 第三人称背面 2: 第三人称正面
    """
    _from = None
    to = None

