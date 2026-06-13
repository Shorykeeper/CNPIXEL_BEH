# coding=utf-8
from .event import BaseEvent
import event.client as client
import event.server as server

class UnknowEvent(Exception):
    pass


class EventPriority:
    """
    等级越高，越后处理
    """
    LOWEST = 10
    LOW = 8
    NORMAL = 6
    HIGH = 4
    HIGHEST = 2
    MONITOR = 0


class Listen:
    server = 'server'
    minecraft = 'minecraft'
    client = 'client'

    @staticmethod
    def on(event_name, event_type='minecraft', priority=EventPriority.NORMAL):
        if isinstance(event_name, basestring):
            event_name = event_name
        elif issubclass(event_name, BaseEvent):
            event_name = event_name.__name__
        else:
            raise UnknowEvent("未知的事件")

        def decorator(func):
            func.listen_type = event_type
            func.listen_event = event_name
            func.listen_priority = priority
            return func

        return decorator