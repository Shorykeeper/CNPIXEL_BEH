# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class ClientChestCloseEvent(BaseEvent):
    """
    关闭箱子界面时触发，包含小箱子子，合并后大箱子子和末影箱子子
    """
    pass


class ClientChestOpenEvent(BaseEvent):
    """
    打开箱子界面时触发，包含小箱子子，合并后大箱子子和末影箱子子
    """
    playerId = None
    x = None
    y = None
    z = None


class ClientPlayerInventoryCloseEvent(BaseEvent):
    """关闭物品背包界面时触发"""
    pass


class ClientPlayerInventoryOpenEvent(BaseEvent):
    """打开物品背包界面时触发"""
    isCreative = None
    cancel = None


class GridComponentSizeChangedClientEvent(BaseEvent):
    """触发时机:UI grid组件里格子数目发生变化时触发"""
    pass


class OnItemSlotButtonClickedEvent(BaseEvent):
    """
    点击快捷栏和背包栏的物品槽时触发
    """
    slotIndex = None


class PlayerChatButtonClickClientEvent(BaseEvent):
    """玩家点击聊天按钮或回车键触发弹出聊天窗口时客户端抛出的事件"""
    pass


class PopScreenEvent(BaseEvent):
    """
    screen移除触发
    """
    screenName = None


class PushScreenEvent(BaseEvent):
    """
    screen创建触发
    """
    screenName = None


class UiInitFinished(BaseEvent):
    """UI初始化框架完成,此时可以创建UI"""
    pass
