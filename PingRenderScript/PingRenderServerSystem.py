# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()


class PingRenderServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.mlevelId = serverApi.GetLevelId()
        self.ListenForEvent('PingRenderMod', 'PingRenderClientSystem', 'Ping', self, self.HandlePing)

    def HandlePing(self, args):
        self.NotifyToClient(args['__id__'], 'Pong', args)

    def Destroy(self):
        pass
