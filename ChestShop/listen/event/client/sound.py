# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class OnMusicStopClientEvent(BaseEvent):
    """
    音乐停止时，当玩家调用StopCustomMusic来停止自定义背景音乐时，会触发此事件
    """
    musicName = None


class PlayMusicClientEvent(BaseEvent):
    """
    播放背景音乐时触发
    """
    name = None
    cancel = None


class PlaySoundClientEvent(BaseEvent):
    """
    播放环境音效或UI音效时触发
    """
    name = None
    pos = None
    volume = None
    pitch = None
    cancel = None
