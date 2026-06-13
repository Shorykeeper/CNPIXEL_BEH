# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class ActorAcquiredItemClientEvent(BaseEvent):
    """
    触发时机：玩家获得物品时客户端抛出的事件（有些获得物品的方式只会触发客户端事件，有些只会触发服务端事件，在使用时注意一点。）
    """
    actor = None
    secondaryActor = None
    itemDict = None
    acquireMethod = None


class ActorUseItemClientEvent(BaseEvent):
    """
    触发时机：玩家使用物品时客户端抛出的事件（比较特殊情况不走该事件的例子：1）回血包；2）药物对有水的烛蜡使用；3）装备工具）
    """
    playerId = None
    itemDict = None
    useMethod = None


class AnvilCreateResultItemAfterClientEvent(BaseEvent):
    """
    玩家点击铁砧合成得到的物品时抛出的事件
    """
    playerId = None
    itemShowName = None
    itemDict = None
    oldItemDict = None
    materialItemDict = None


class ClientItemTryUseEvent(BaseEvent):
    """
    玩家点击右键尝试使用物品时客户端抛出的事件，可以通过设置cancel为True取消使用物品。
    注意：如果需要取消物品的使用需要同时在ClientItemTryUseEvent和ServerItemTryUseEvent中将cancel设置为True才能正确取消

    ServerItemTryUseEvent/ClientItemTryUseEvent 不能取消对方模块使用物品的行为，如使用生物样本，使用钓出/收集，使用点火石等；如果想要取消这种行为，请使用ClientItemUseOnEvent和ServerItemUseOnEvent
    """
    playerId = None
    itemDict = None
    cancel = None


class ClientItemUseOnEvent(BaseEvent):
    """
    玩家在对方模块使用物品时客户端抛出的事件。注意：如果需要取消物品的使用需要同时在ClientItemUseOnEvent和ServerItemUseOnEvent中将ret设置为True才能正确取消
    """
    entityId = None
    itemDict = None
    x = None
    y = None
    z = None
    blockName = None
    blockAuxValue = None
    face = None
    clickX = None
    clickY = None
    clickZ = None
    ret = None


class ClientShapedRecipeTriggeredEvent(BaseEvent):
    """
    玩家合成物品时触发
    """
    recipeId = None


class GrindStoneRemovedEnchantClientEvent(BaseEvent):
    """
    玩家点击磨石合成得到的物品时抛出的事件
    """
    playerId = None
    oldItemDict = None
    additionalItemDict = None
    newItemDict = None
    exp = None


class InventoryItemChangedClientEvent(BaseEvent):
    """
    玩家背包物品变化时客户端抛出的事件。

    如果槽位变空，变化后的槽位中物品为空气

    触发时槽位物品仍然为变化前物品

    背包内物品移动，合成，分解的操作会多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序
    """
    playerId = None
    slot = None
    oldItemDict = None
    newItemDict = None


class ItemReleaseUsingClientEvent(BaseEvent):
    """
    触发时机：玩家释放正在使用的物品
    """
    playerId = None
    durationLeft = None
    itemDict = None
    maxUseDuration = None
    cancel = None


class OnCarriedNewItemChangedClientEvent(BaseEvent):
    """
    手持物品发生变更时，触发该事件；数量变更不会通知
    """
    itemDict = None


class PlayerTryDropItemClientEvent(BaseEvent):
    """
    触发时机：玩家丢弃物品时触发
    """
    playerId = None
    itemDict = None
    cancel = None


class StartUsingItemClientEvent(BaseEvent):
    """
    玩家使用物品时抛出（目前仅支持Bucket、Trident、RangedWeapon、Medicine、Food、Potion、Crossbow、ChemistryStick）
    """
    playerId = None
    itemDict = None


class StopUsingItemClientEvent(BaseEvent):
    """
    玩家停止使用物品时抛出（目前仅支持Bucket、Trident、RangedWeapon、Medicine、Food、Potion、Crossbow、ChemistryStick）
    """
    playerId = None
    itemDict = None
