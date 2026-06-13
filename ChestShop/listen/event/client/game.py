# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class AddEntityClientEvent(BaseEvent):
    """客户端创建新实体时触发
    """
    id = None
    posX = None
    posY = None
    posZ = None
    dimensionId = None
    isBaby = None
    engineTypeStr = None
    itemName = None
    auxValue = None


class AddPlayerAOIClientEvent(BaseEvent):
    """
    玩家加入游戏或其它玩家进入当前玩家所在的区块时触发的AOI事件，替代AddPlayerEvent
    """
    playerId = None


class ChunkAcquireDiscardedClientEvent(BaseEvent):
    """
    触发时机:客户端区块即将被卸载时
    """
    dimension = None
    chunkPosX = None
    chunkPosZ = None


class ChunkLoadedClientEvent(BaseEvent):
    """
    触发时机:客户端区块加载完成时
    """
    dimension = None
    chunkPosX = None
    chunkPosZ = None


class ClientChatEvent(BaseEvent):
    """
    客户端聊天事件
    """
    username = None
    playerId = None
    message = None
    cancel = None


class LoadClientAddonScriptsAfter(BaseEvent):
    """客户端加载mod完成事件"""
    pass


class OnCommandOutputClientEvent(BaseEvent):
    """
    当command命令有成功输出信息时触发
    """
    command = None
    message = None


class OnLocalPlayerStopLoading(BaseEvent):
    """
    触发时机:玩家进入存档，生成点地形加载完成时触发。此事件触发时可以进行切换维度的操作
    """
    playerId = None


class OnScriptTickClient(BaseEvent):
    """客户端tick事件,1秒30次"""
    pass


class RemoveEntityClientEvent(BaseEvent):
    """客户端实体被移除时触发"""
    id = None


class RemovePlayerAOIClientEvent(BaseEvent):
    """
    玩家离开当前玩家所在的区块时触发AOI事件
    """
    playerId = None


class UnLoadClientAddonScriptsBefore(BaseEvent):
    """客户端卸载mod之前触发"""
    pass
