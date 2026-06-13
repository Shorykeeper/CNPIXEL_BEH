# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class ClientJumpButtonPressDownEvent(BaseEvent):
    """
    跳跃按钮按下事件，返回值设置参数只对本次按下事件起作用
    """
    continueJump = None


class ClientJumpButtonReleaseEvent(BaseEvent):
    """跳跃按钮按下释放事件"""
    pass


class GetEntityByCoordEvent(BaseEvent):
    """
    玩家点击屏幕时触发，多个手指在屏幕上时，只有第一个会触发。
    """
    pass


class GetEntityByCoordReleaseClientEvent(BaseEvent):
    """玩家点击屏幕后释放时触发，多个手指在屏幕上时，只有最后一个手指释放时触发。"""
    pass


class HoldBeforeClientEvent(BaseEvent):
    """玩家长按屏幕，即将响应到游戏内时触发。仅在移动设备或PC的F11模式下触发。PC的非F11模式可以使用RightClickBeforeClientEvent事件监听鼠标右键

    玩家长按屏幕的处理顺序为：
        - 玩家点击屏幕，在长按判定时间内（默认为400毫秒，可以通过SetHoldTimeThreshold接口修改）一直没有进行移动或释放
        - 触发该事件
        - 如果事件没有cancel，则根据主手上物品，处理的对象类型以及与玩家的距离，进行挖掘/使用物品/与实体交互等操作 即该事件只会到达长按判定时间的间隙触发一次，之后一直按住不会继续触发，可以使用TapOrHoldReleaseClientEvent监听长按后释放

    与TapBeforeClientEvent事件类似，被ui层获取，没有穿透到世界的点击不会触发该事件
    """
    cancel = None


class LeftClickBeforeClientEvent(BaseEvent):
    """
    玩家按下鼠标左键时触发。仅在PC的普通控制模式（即非F11模式）下触发。
    """
    cancel = None


class LeftClickReleaseClientEvent(BaseEvent):
    """玩家释放鼠标左键时触发。仅在PC的普通控制模式（即非F11模式）下触发。"""
    pass


class OnBackButtonReleaseClientEvent(BaseEvent):
    """返回按钮（当前特指Android系统导航中的返回按钮）释放时触发"""
    pass


class OnClientPlayerStartMove(BaseEvent):
    """移动按钮按下事件，按下一个方向键的同时，去按另外一个方向键，不会触发第二次"""
    pass


class OnClientPlayerStopMove(BaseEvent):
    """移动按钮按下释放事件，同时按下多个方向键，需要释放所有的方向键才会触发事件"""
    pass


class OnKeyPressInGame(BaseEvent):
    """
    按键按下或按键释放时触发
    """
    screenName = None
    key = None
    isDown = None


class RightClickBeforeClientEvent(BaseEvent):
    """
    玩家按下鼠标右键时触发。仅在PC下触发（即普通控制模式及F11模式都会触发）。
    """
    cancel = None


class OnGamepadKeyPressClientEvent(BaseEvent):
    """
    游戏手柄按键事件
    """
    screenName = None
    key = None
    isDown = None


class OnGamepadStickClientEvent(BaseEvent):
    """
    游戏手柄摇杆事件
    """
    key = None
    x = None
    y = None

class OnGamepadTriggerClientEvent(BaseEvent):
    """
    游戏手柄板机事件
    """
    key = None
    magnitude = None


class RightClickReleaseClientEvent(BaseEvent):
    """玩家释放鼠标右键时触发。仅在PC的普通控制模式（即非F11模式）下触发。在F11下右键，按下会触发RightClickBeforeClientEvent，释放会触发TapOrHoldReleaseClientEvent"""
    pass


class TapBeforeClientEvent(BaseEvent):
    """玩家点击屏幕并释放时触发，即将响应到游戏内时触发。仅在移动设备或PC的F11模式下触发。PC的非F11模式可以使用LeftClickBeforeClientEvent事件监听鼠标左键

    玩家点击屏幕的处理顺序为：
        - 玩家点击屏幕，没有进行移动，并且在短按判定时间（250毫秒）内释放
        - 触发该事件
        - 如果事件没有cancel，则根据处理的对象类型以及与玩家的距离，进行攻击/使用物品/与实体交互等操作

    与GetEntityByCoordEvent事件不同的是，被ui层获取，没有穿透到世界的点击不会触发该事件，例如：
        - 点击原始的移动/跳跃等按键，
        - 通过SetIsHud(0)屏蔽了游戏操作
        - 对按键使用AddTouchEventHandler接口时isSwallow参数设置为True
    """
    cancel = None


class TapOrHoldReleaseClientEvent(BaseEvent):
    """玩家点击屏幕后释放时触发。仅在移动设备或PC的F11模式下触发。PC的非F11模式可以使用LeftClickReleaseClientEvent与RightClickReleaseClientEvent事件监听鼠标释放"""
    pass
