# -*- encoding: utf-8 -*-
import random, mod.server.extraServerApi as serverApi, mod.common.minecraftEnum as Enum, time
from mod_log import logger as logger
from ..config.modConfig import *
from ..listen.listen import Listen, server, client, EventPriority
from .BaseListener import *
ServerSystem = serverApi.GetServerSystemCls()
EngineComponent = serverApi.GetEngineCompFactory()
SF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()

#setCommand = lambda cmdStr, playerId=None, showOutput=False: cf.CreateCommand(levelId).SetCommand(cmdStr, playerId, showOutput)
setCommand = lambda cmdStr, playerId=None, showOutput=False: SF.CreateCommand(levelId).SetCommand(cmdStr, playerId, showOutput)
game = SF.CreateGame(levelId)
commandComp = SF.CreateCommand(levelId)
BlockComp = SF.CreateBlockInfo(levelId)
ChestBlockComp = SF.CreateChestBlock(levelId)
posComp = SF.CreatePos
rotComp = SF.CreateRot
itemComp = SF.CreateItem
nameComp = SF.CreateName
dataComp = SF.CreateExtraData
msgComp = SF.CreateMsg
lvComp = SF.CreateLv
hasTag = lambda tag, entityId: SF.CreateTag(entityId).EntityHasTag(tag)
showMsg = lambda msg, playerId=None: setCommand('/tellraw @%s {"rawtext":[{"text":"%s"}]}' % (('s', 'a')[playerId == None], msg.replace('"', '\\"')), playerId)
addTag = lambda tag, entityId: SF.CreateTag(entityId).AddEntityTag(tag)

success = game.SetCanActorSetOnFireByLightning
function = lambda mcfunc, Id: setCommand('/execute as @s at @s run function %s' % mcfunc, Id)
setExData = lambda key, value, Id: SF.CreateExtraData(Id).SetExtraData(key, value)
getExData = lambda key, Id: SF.CreateExtraData(Id).GetExtraData(key)
cleanExData = lambda key, Id: SF.CreateExtraData(Id).CleanExtraData(key)

pickaxe_name_level = { 0: 'air',1: 'wooden_pickaxe',2: 'stone_pickaxe',3: 'iron_pickaxe',4: 'diamond_pickaxe'}
axe_name_level = { 0: 'air',1: 'wooden_axe',2: 'stone_axe',3: 'iron_axe',4: 'diamond_axe'}

