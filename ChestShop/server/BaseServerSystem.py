from utils import *
class BaseServerSystem(ServerSystem):
    ListenDict = {Listen.minecraft: ("Minecraft", "Engine"), Listen.client: (modName, "main"), Listen.server: ("Minecraft", "Engine")}

    def __init__(self, namespace, name):
        super(BaseServerSystem, self).__init__(namespace, name)
        self.Register()

    def Register(self):
        for key in dir(self):
            obj = getattr(self, key)
            if callable(obj) and hasattr(obj, 'listen_event'):
                event = getattr(obj, 'listen_event')
                _type = getattr(obj, 'listen_type')
                priority = getattr(obj, 'listen_priority')
                self.listen(event, obj, _type=_type, priority=priority)

    def Update(self):
        pass

    def Destroy(self):
        pass

    def listen(self, event, func, _type=Listen.minecraft, priority=EventPriority.NORMAL):
        if _type not in self.ListenDict:
            return
        name, system = self.ListenDict[_type]
        self.ListenForEvent(name, system, event, self, func, priority=priority)

    def unlisten(self, event, func, _type=Listen.minecraft, priority=EventPriority.NORMAL):
        if _type not in self.ListenDict:
            return
        name, system = self.ListenDict[_type]
        self.UnListenForEvent(name, system, event, self, func, priority=priority)