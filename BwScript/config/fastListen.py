# coding=utf-8
import mod.server.extraServerApi as sapi
import mod.client.extraClientApi as capi
from types import FunctionType

fast_listen_list = []
system = {'class_type': None, 'class_obj': None}
CLIENT_ENGINE = 'client'
SERVER_ENGINE = 'server'

def Listen(namespace='engine', systemName='engine'):
    global system
    func = None
    if isinstance(namespace, FunctionType):
        func = namespace
        namespace = sapi.GetEngineNamespace() if system.get('class_type') == 'server' else capi.GetEngineNamespace()
    if systemName == 'engine': systemName = sapi.GetEngineSystemName() if system.get('class_type') == 'server' else capi.GetEngineSystemName()
    global fast_listen_list
    
    def wrapper(func):
        fast_listen_list.append((namespace, systemName, func.__name__, func))
        return func
    return wrapper if func is None else wrapper(func)

def initFastListen(self):
    global fast_listen_list
    global system
    system = {'class_type':'server' if issubclass(self.__class__, sapi.GetServerSystemCls()) else 'client', 'class': self}
    for namespace, systemName, eventName, callbackFunc in fast_listen_list:
        self.ListenForEvent(namespace, systemName, eventName, self, callbackFunc)