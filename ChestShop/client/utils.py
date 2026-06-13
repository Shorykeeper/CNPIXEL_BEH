# -*- encoding: utf-8 -*-
import time, math, mod.client.extraClientApi as clientApi, mod.common.minecraftEnum as enum, random
from mod_log import logger as logger
from ..config.modConfig import *
from ..listen.listen import Listen, server, client, EventPriority
from .BaseListener import *

ClientSystem = clientApi.GetClientSystemCls()
CF = clientApi.GetEngineCompFactory()
levelId = clientApi.GetLevelId()
game = CF.CreateGame(levelId)
playerId = clientApi.GetLocalPlayerId()
textBoardComp = CF.CreateTextBoard(playerId)
posComp = CF.CreatePos(playerId)
rotComp = CF.CreateRot(playerId)
music = CF.CreateCustomAudio(levelId)
NameComp = lambda playerID: CF.CreateName(playerID)  # type: playerID:(str or int)
Name = NameComp(playerId).GetName()
itemComp = CF.CreateItem(playerId)
