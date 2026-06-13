import weakref, mod.server.extraServerApi as serverApi
from .event import BaseEvent
from ..config.modConfig import *
from .listen import Listen, EventPriority
from mod_log import logger

class BaseModule(object):
    system = None
    ListenDict = {Listen.minecraft: ("Minecraft", "Engine"), Listen.client: (modName, "main"), Listen.server: (modName, "main")}

    def __init__(self):
        self.levelId = serverApi.GetLevelId()
        self.system = weakref.proxy(serverApi.GetSystem(modName, "main"))
        self.onRegister()

    def onRegister(self):
        for key in dir(self):
            obj = getattr(self, key)
            if callable(obj) and hasattr(obj, 'listen_event'):
                event = getattr(obj, 'listen_event')
                _type = getattr(obj, 'listen_type')
                priority = getattr(obj, 'listen_priority')
                self.listen(event, obj, _type=_type, priority=priority)

    def ListenForEvent(self, name, system, event, instance, func, priority=EventPriority.NORMAL):
        self.system.ListenForEvent(name, system, event, instance, func, priority=priority)

    def UnListenForEvent(self, name, system, event, instance, func, priority=EventPriority.NORMAL):
        self.system.UnListenForEvent(name, system, event, instance, func, priority=priority)

    def listen(self, event, func, _type=Listen.minecraft, priority=EventPriority.NORMAL):
        if _type not in self.ListenDict:
            return
        name, system = self.ListenDict[_type]
        self.ListenForEvent(name, system, event, self, func, priority=priority)

    def unlisten(self, event, func, _type=Listen.minecraft, priority=EventPriority.NORMAL):
        if _type not in self.ListenDict:
            return
        if isinstance(event, basestring):
            event_name = event
        elif issubclass(event, BaseEvent):
            event_name = event.__name__
        else:
            logger.error('None event type: {}'.format(event))
            return
        name, system = self.ListenDict[_type]
        print event_name
        self.UnListenForEvent(name, system, event_name, self, func, priority=priority)


class BaseListener(BaseModule):

    def __init__(self):
        super(BaseListener, self).__init__()
        logger.info(('Register listener {}').format(self.__class__.__name__))