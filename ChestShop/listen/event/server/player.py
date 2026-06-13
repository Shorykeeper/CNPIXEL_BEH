# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class MobDieEvent(BaseEvent):
    """实体被玩家杀死时触发

    - id : str 实体id
    - attacker : str 伤害来源id

    注意：不能在该事件回调中对此玩家手持物品进行修改，如SpawnItemToPlayerCarried、ChangePlayerItemTipsAndExtraId等接口
    """
    pass


class AddExpEvent(BaseEvent):
    """触发时机：当玩家增加经验时触发

    - id : str 玩家id
    - addExp : int 增加的经验值

    """
    pass


class AddLevelEvent(BaseEvent):
    """触发时机：当玩家升级时触发

    - id : str 玩家id
    - addLevel : int 增加的等级值
    - newLevel : int 新的等级

    """
    pass


class ChangeLevelUpCostServerEvent(BaseEvent):
    """触发时机：获取玩家下一个等级升级经验时，用于重新加载玩家的升级经验，每个等级在重置之前只会触发一次

    - level : int 玩家当前等级
    - levelUpCostExp : int 当前等级升级到下一个等级需要的经验值，当设置升级经验小于1时会被强制调整到1
    - changed : bool 设置为True，重新加载玩家升级经验才会生效

    """
    pass


class DimensionChangeFinishServerEvent(BaseEvent):
    """玩家维度变换完成后服务器端抛出

    - playerId : str 玩家实体id
    - fromDimensionId : int 维度变换前的维度
    - toDimensionId : int 维度变换后的维度
    - toPos : tuple(float,float,float) 变换后的坐标x,y,z,其中y值为脚底角度的身体高度值

    当通过传送门从末地回到主世界时，toPos的y值为32767，其他情况一般会比设置值高1.62
    """
    pass


class DimensionChangeServerEvent(BaseEvent):
    """玩家维度变换时服务器端抛出

    - playerId : str 玩家实体id
    - fromDimensionId : int 维度变换前的维度
    - toDimensionId : int 维度变换后的维度
    - fromX : float 变换前的坐标x
    - fromY : float 变换前的坐标y
    - fromZ : float 变换前的坐标z
    - toX : float 变换后的坐标x
    - toY : float 变换后的坐标y
    - toZ : float 变换后的坐标z

    当通过传送门从末地回到主世界时，toY值为32767，其他情况一般会比设置值高1.62
    """
    pass


class ExtinguishFireServerEvent(BaseEvent):
    """玩家灭火时触发。下雨，泼水等方式的灭火不会触发

    - pos : tuple(float,float,float) 灭火方块的坐标
    - playerId : str 玩家id
    - cancel : bool 修改为True时，可阻止玩家灭火。需要与ExtinguishFireClientEvent一起修改

    """
    pass


class GameTypeChangedServerEvent(BaseEvent):
    """触发时机：当个人游戏模式发生改变时服务器端触发

    - playerId : str 玩家Id，SetDefaultGameType接口改变游戏模式时该参数为空字符串
    - oldGameType : int 切换前的游戏模式
    - newGameType : int 切换后游戏模式

    游戏模式：GetMinecraftEnum().GameType.*:生存,创造,冒险分别对应0~2，默认游戏模式发生改变后最终反映在游戏中
    """
    pass


class OnPlayerHitBlockServerEvent(BaseEvent):
    """触发时机：通过OpenPlayerHitBlockDetection打开方块破坏检测后，当玩家破坏方块时触发该事件。监听玩家着地请使用客户端的OnGroundClientEvent。客户端和服务器端分别做破坏检测，可能会两个事件返回的结果有差异

    - playerId : str 破坏方块的玩家Id
    - posX : int 破坏方块x坐标
    - posY : int 破坏方块y坐标
    - posZ : int 破坏方块z坐标
    - blockId : str 破坏方块的identifier
    - auxValue : int 破坏方块的附加值
    - dimensionId : int 维度id

    """
    pass


class OnPlayerHitMobServerEvent(BaseEvent):
    """触发时机：通过OpenPlayerHitMobDetection打开实体破坏检测后，当有实体与玩家破坏时触发该事件。注意：客户端和服务器端分别做破坏检测，可能会两个事件返回的结果有差异

    - playerList : list[str] 实体破坏到的玩家id的list

    """
    pass


class PlayerAttackEntityEvent(BaseEvent):
    """触发时机：当玩家攻击时触发

    - playerId : str 玩家id
    - victimId : str 受伤者id
    - damage : int 伤害值：牵引通过过来的值是0 允许脚本层修改为其他数
    - isValid : int 脚本是否设置伤害值：1表示是；0表示否
    - cancel : bool 是否取消此次攻击，默认不取消
    - isKnockBack : bool 是否支持击退效果，默认支持，当不支持时将屏蔽虚弱击退效果

    """
    pass


class PlayerCheatSpinAttackServerEvent(BaseEvent):
    """
    * 仅Apollo可用
    触发时机：玩家开始/结束快速旋转攻击并且不符合发送快速旋转攻击条件时触发（装备三叉星附魔的物品、在水中或雨中，并且未骑乘）

    - playerId : str 玩家的entityId
    - isStart : bool True时表示开始快速旋转攻击；False时表示结束快速旋转攻击

    例如如果没有定义类似三叉星/激流附魔的物品，那么触发此事件说明此玩家使用了【夺光环】外挂
    """
    pass


class PlayerDieEvent(BaseEvent):
    """触发时机：当玩家死亡时触发

    - id : str 玩家id
    - attacker : str 伤害来源id

    """
    pass


class PlayerDoInteractServerEvent(BaseEvent):
    """
    玩家与具有minecraft:interact组件的实体交互时触发该事件，例如玩家手持空桶对牛浇水、玩家手持打火石点燃火把
    """
    playerId = None
    itemDict = None
    interactEntityId = None


class PlayerEatFoodServerEvent(BaseEvent):
    """触发时机：当玩家吃下食物时触发

    - playerId : str 玩家Id
    - itemDict : dict 食物物品的信息字典
    - hunger : int 食物增加的饱食值，可修改
    - nutrition : float 食物的营养价值，恢复饱食度 = 食物增加的饱食值 * 食物的营养价值 * 2，饱食度最大不超过当前饱食值，可修改

    吃草籽以及治疗蘑菇不触发该事件
    """
    pass


class PlayerHurtEvent(BaseEvent):
    """触发时机：当玩家受伤时触发

    - id : str 受伤玩家id
    - attacker : str 伤害来源实体id，如果没有实体攻击，例如高空坠落，id为-1

    """
    pass


class PlayerInteractServerEvent(BaseEvent):
    """触发时机：玩家即将与某个实体交互

    - cancel : bool 是否取消触发，默认为False，如果设置为True，可阻止触发后的实体交互事件
    - playerId : str 主动与实体交互的玩家的唯一ID
    - itemDict : dict 当前玩家手持物品的信息字典
    - victimId : str 被交互的实体的唯一ID

    """
    pass


class PlayerRespawnEvent(BaseEvent):
    """触发时机：当玩家重生时触发

    - id : str 玩家id

    该事件为玩家点击重生按键时触发，但是触发时玩家可能尚未完成重生，此时请尽量对玩家进行切维度或设置生存值等操作 一般情况下推荐使用PlayerRespawnFinishServerEvent
    """
    pass


class PlayerRespawnFinishServerEvent(BaseEvent):
    """触发时机：当玩家重生完成后触发

    - id : str 玩家id

    该事件触发时玩家已经重生完成，可以安全地使用切维度等操作
    """
    pass


class PlayerSleepServerEvent(BaseEvent):
    """玩家使用床睡觉时成功

    - playerId : str 玩家id

    """
    pass


class PlayerSpinAttackServerEvent(BaseEvent):
    """* 仅Apollo可用
    触发时机：玩家开始/结束快速旋转攻击时触发

    - playerId : str 玩家的entityId
    - isInWaterOrRain : bool 是否在水中或雨中
    - isRiding : bool 是否骑乘状态
    - isStart : bool True时表示开始快速旋转攻击；False时表示结束快速旋转攻击

    """
    pass


class PlayerStopSleepServerEvent(BaseEvent):
    """玩家停止睡觉

    - playerId : str 玩家id
    """
    pass


class PlayerTeleportEvent(BaseEvent):
    """触发时机：当玩家传送到其他位置时触发，例如玩家使用末影珍珠或tp指令时

    - id : str 玩家id

    """
    pass


class PlayerTrySleepServerEvent(BaseEvent):
    """玩家尝试使用床睡觉

    - playerId : str 玩家id
    - cancel : bool 是否取消（开发者传入）

    """
    pass


class ServerPlayerGetExperienceOrbEvent(BaseEvent):
    """触发时机：当玩家获取经验球时触发的事件

    - playerId : str 玩家id
    - experienceValue : int 经验球的经验值
    - cancel : bool 是否取消（开发者传入）

    cancel值设置为True时，拾起的经验球不会增加经验值，但是经验球一样会消失
    """
    pass


class StoreBuySuccServerEvent(BaseEvent):
    """触发时机：玩家在游戏中购买物品时服务器端抛出的事件

    - playerId : str 购买物品的玩家实体id

    """
    pass


class LobbyGoodBuySucServerEvent(BaseEvent):
    """触发时机：玩家联机大厅登录或联机大厅内购买物品时服务器端抛出的事件

    - playerId : str 购买物品的玩家实体id
    - uid : str 购买物品的玩家uid
    - resid : int 当前游戏id

    """
    pass



