from .utils import *


class BaseScreenNodeSystem(ScreenNode):
    base_path = "/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel"
    ListenDict = {Listen.minecraft: ("Minecraft", "Engine"), Listen.client: ("Minecraft", "Engine"), Listen.server: (modName, "main")}

    def __init__(self, namespace, name, param):
        super(BaseScreenNodeSystem, self).__init__(namespace, name, param)
        self.system = weakref.proxy(clientApi.GetSystem(modName, "main"))
        self.levelId = clientApi.GetLevelId()
        self.playerId = clientApi.GetLocalPlayerId()
        self.onRegister()

    def onRegister(self):
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
        self.system.ListenForEvent(name, system, event, self, func, priority=priority)

    def unlisten(self, event, func, _type=Listen.minecraft, priority=EventPriority.NORMAL):
        if _type not in self.ListenDict:
            return
        name, system = self.ListenDict[_type]
        self.system.UnListenForEvent(name, system, event, self, func, priority=priority)