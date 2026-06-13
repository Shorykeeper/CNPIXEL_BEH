# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class BlockLiquidStateChangeAfterServerEvent(BaseEvent):
    """
    触发时机：方块转变为含水或离开含水（流体）后触发

    - blockName : str 方块的identifier，包含命名空间及名称
    - auxValue : int 方块附加值
    - dimension : int 方块维度
    - x : int 方块x坐标
    - y : int 方块y坐标
    - z : int 方块z坐标
    - turnLiquid : bool 是否转变为含水，true则转变为含水，false则离开含水
    """
    blockName = None
    auxValue = None
    dimension = None
    x = None
    y = None
    z = None
    turnLiquid = None


class BlockLiquidStateChangeServerEvent(BaseEvent):
    """
    触发时机：方块转变为含水或离开含水（流体）前触发

    - blockName : str 方块的identifier，包含命名空间及名称
    - auxValue : int 方块附加值
    - dimension : int 方块维度
    - x : int 方块x坐标
    - y : int 方块y坐标
    - z : int 方块z坐标
    - turnLiquid : bool 是否转变为含水，true则转变为含水，false则离开含水
    """
    blockName = None
    auxValue = None
    dimension = None
    x = None
    y = None
    z = None
    turnLiquid = None


class BlockNeighborChangedServerEvent(BaseEvent):
    """
    触发时机：自定义方块周围的方块发生变更时，需要配置etease:neighborchanged_sendto_script，具体情况请查阅《自定义作物》文档
    """
    dimensionId = None
    posX = None
    posY = None
    posZ = None
    blockName = None
    auxValue = None
    neighborPosX = None
    neighborPosY = None
    neighborPosZ = None
    fromBlockName = None
    fromBlockAuxValue = None
    toBlockName = None
    toAuxValue = None


class BlockRandomTickServerEvent(BaseEvent):
    """
    触发时机：自定义方块配置etease:random_tick 随tick时触发
    """
    posX = None
    posY = None
    posZ = None
    blockName = None
    fullName = None
    auxValue = None
    dimensionId = None


class BlockRemoveServerEvent(BaseEvent):
    """
    触发时机：监听该事件的方块在销毁时触发，可以通过ListenOnBlockRemoveEvent方法进行监听，或者通过json组件 netease:listen_block_remove 进行配置
    """
    x = None
    y = None
    z = None
    fullName = None
    auxValue = None
    dimension = None


class BlockSnowStateChangeAfterServerEvent(BaseEvent):
    """
    触发时机：方块转变为含雪或离开含雪后触发
    """
    dimension = None
    x = None
    y = None
    z = None
    turnSnow = None
    setBlockType = None


class BlockSnowStateChangeServerEvent(BaseEvent):
    """
    触发时机：方块转变为含雪或离开含雪前触发
    """
    dimension = None
    x = None
    y = None
    z = None
    turnSnow = None
    setBlockType = None


class BlockStrengthChangedServerEvent(BaseEvent):
    """
    触发时机：自定义机械元件方块红石信号强度发生变更时触发
    """
    posX = None
    posY = None
    posZ = None
    blockName = None
    auxValue = None
    newStrength = None
    dimensionId = None


class ChestBlockTryPairWithServerEvent(BaseEvent):
    """
    触发时机：两个并排的小箱子子方块准备组合成一个大箱子子方块时
    """
    cancel = None
    blockX = None
    blockY = None
    blockZ = None
    otherBlockX = None
    otherBlockY = None
    otherBlockZ = None
    dimensionId = None


class CommandBlockContainerOpenEvent(BaseEvent):
    """
    触发时机：玩家点击命令方块，尝试打开命令方块的设置界面
    """
    playerId = None
    isBlock = None
    blockX = None
    blockY = None
    blockZ = None
    victimId = None
    cancel = None


class CommandBlockUpdateEvent(BaseEvent):
    """
    触发时机：玩家尝试修改命令方块的内部命令时

    当修改的目标为命令方块矿车时（此时isBlock为False），设置cancel为True，依旧可以阻止修改命令方块矿车的内部指令，但是从客户端能看到命令方块矿车的内部指令变更了，不过这只是虚晃一枪，重新登录或其它客户端打开命令方块矿车的设置界面，就会发现其实际内部指令并没有变更
    """
    playerId = None
    playerUid = None
    command = None
    isBlock = None
    blockX = None
    blockY = None
    blockZ = None
    victimId = None
    cancel = None


class DestroyBlockEvent(BaseEvent):
    """
    触发时机：当方块已经被玩家破坏时触发。

    在生存模式或创造模式下都会触发
    """
    x = None
    y = None
    z = None
    face = None
    fullName = None
    auxData = None
    playerId = None
    dimensionId = None


class EntityPlaceBlockAfterServerEvent(BaseEvent):
    """
    触发时机：当实体成功放置方块后触发

    部分放置后会生成实体、可操作的方块、带有特殊逻辑的方块，不会触发该事件，包含但不限于台阶、门、告示牌、花簇、红石中继器、矿车、宝箱、熔炉等。
    """
    x = None
    y = None
    z = None
    fullName = None
    auxData = None
    entityId = None
    dimensionId = None
    face = None


class FallingBlockBreakServerEvent(BaseEvent):
    """
    触发时机：当下落的方块实体被破坏时，服务端触发该事件

    - fallingBlockId : str 下落的方块实体id
    - fallingBlockX : float 下落的方块实体位置x
    - fallingBlockY : float 下落的方块实体位置y
    - fallingBlockZ : float 下落的方块实体位置z
    - blockName : str 被重置方块的identifier，包含命名空间及名称
    - fallTickAmount : int 下落的方块实体持续落下了多少tick
    - dimensionId : int 下落的方块实体维度id
    - cancelDrop : bool 是否取消方块物品掉落，可以在脚本层中设置

    不是所有的下落的方块都会触发该事件，需要在json中先配置触发开关（具体情况参考： 自定义重置方块 ）
    """
    pass


class FallingBlockCauseDamageBeforeServerEvent(BaseEvent):
    """触发时机：当下落的方块开始计算撞击到实体的伤害时，服务端触发该事件

    - fallingBlockId : str 下落的方块实体id
    - fallingBlockX : float 下落的方块实体位置x
    - fallingBlockY : float 下落的方块实体位置y
    - fallingBlockZ : float 下落的方块实体位置z
    - blockName : str 被重置方块的identifier，包含命名空间及名称
    - dimensionId : int 下落的方块实体维度id
    - collidingEntitys : list(str) 当前碰撞到的实体列表id，如果没有的话则是None
    - fallTickAmount : int 下落的方块实体持续落下了多少tick
    - fallDistance : float 下落的方块实体持续落下了多少距离
    - isHarmful : bool 是否计算对实体的伤害，传递过来的值由json配置和伤害是否大于0决定，可以在脚本层修改传递
    - fallDamage : int 对实体的伤害，传递过来的值距离和json配置决定，可以在脚本层修改传递

    不是所有的下落的方块都会触发该事件，需要在json中先配置触发开关（具体情况参考： 自定义重置方块 ）

    服务端常常触发在客户端之后，而且有时会相差一个tick，这就意味着可能出现以下现象：服务端强制fallTickAmount比配置强力破坏时间多1tick，下落的距离、下落的伤害计算出来比客户端时间多1tick的误差。
    """
    pass


class FallingBlockReturnHeavyBlockServerEvent(BaseEvent):
    """触发时机：当下落的方块实体返回普通重置方块时，服务端触发该事件

    - fallingBlockId : int 下落的方块实体id
    - blockX : int 方块x坐标
    - blockY : int 方块y坐标
    - blockZ : int 方块z坐标
    - heavyBlockName : str 重置方块的identifier，包含命名空间及名称
    - prevHereBlockName : str 变回重置方块时，原来方块位置的identifier，包含命名空间及名称
    - dimensionId : int 下落的方块实体维度id
    - fallTickAmount : int 下落的方块实体持续落下了多少tick

    不是所有的下落的方块都会触发该事件，需要在json中先配置触发开关（具体情况参考： 自定义重置方块 ）
    """
    pass


class HeavyBlockStartFallingServerEvent(BaseEvent):
    """触发时机：当重置方块变成下落的方块实体后，服务端触发该事件

    - fallingBlockId : str 下落的方块实体id
    - blockX : int 方块x坐标
    - blockY : int 方块y坐标
    - blockZ : int 方块z坐标
    - blockName : str 重置方块的identifier，包含命名空间及名称
    - dimensionId : int 下落的方块实体维度id

    不是所有的下落的方块都会触发该事件，需要在json中先配置触发开关（具体情况参考： 自定义重置方块 ）
    """
    pass


class HopperTryPullInServerEvent(BaseEvent):
    """触发时机：当漏斗上方连接容器后，容器向漏斗开始输入物品时触发，事件仅触发一次

    - x : int 漏斗x坐标
    - y : int 漏斗y坐标
    - z : int 漏斗z坐标
    - abovePosX : int 交互的容器x坐标
    - abovePosY : int 交互的容器y坐标
    - abovePosZ : int 交互的容器z坐标
    - dimensionId : int 维度id
    - canHopper : bool 是否允许漏斗向容器加东西（要关闭此交互，需要先监听此事件再放置容器）

    """
    pass


class HopperTryPullOutServerEvent(BaseEvent):
    """触发时机：当漏斗以附着的方式连接容器时，即从侧面连接容器时，漏斗向容器开始输出物品时触发，事件仅触发一次

    - x : int 漏斗x坐标
    - y : int 漏斗y坐标
    - z : int 漏斗z坐标
    - attachedPosX : int 交互的容器x坐标
    - attachedPosY : int 交互的容器y坐标
    - attachedPosZ : int 交互的容器z坐标
    - dimensionId : int 维度id
    - canHopper : bool 是否允许漏斗向容器加东西（要关闭此交互，需要先监听此事件再放置容器）

    """
    pass


class OnAfterFallOnBlockServerEvent(BaseEvent):
    """
    触发时机：当实体降落在方块上后服务端触发，主要用于加的计算

    - entityId : str 实体id
    - posX : float 实体位置x
    - posY : float 实体位置y
    - posZ : float 实体位置z
    - motionX : float 瞬间移动X方向的力
    - motionY : float 瞬间移动Y方向的力
    - motionZ : float 瞬间移动Z方向的力
    - blockName : str 方块的identifier，包含命名空间及名称
    - calculate : bool 是否按脚本层传递值计算力

    不是所有的方块都会触发该事件，需要在json中先配置触发开关（具体情况参考： 自定义方块JSON组件 ）

    如果需要在脚本层修改motion，传递的需要是浮点型，例如需要赋值0.0而非0

    如果需要修改实体的力，最好配合客户端事件同步修改，避免出现非预期现象

    因为传递最后一定按原方块规则计算力（普通方块置0，台阶、熔岩桶、草下、地下苔藓、树木、海草、海带等反弹），所以在脚本层如果想直接修改当前力需要将calculate设为true取消原计算，按传递值计算

    在降落在地面之后，OnAfterFallOnBlockServerEvent会直接触发，因此请在脚本层中做相应的逻辑判断

    """
    pass


class OnBeforeFallOnBlockServerEvent(BaseEvent):
    """触发时机：当实体即将降落在方块上时服务端触发，主要用于伤害计算

    - entityId : str 实体id
    - blockX : int 方块x坐标
    - blockY : int 方块y坐标
    - blockZ : int 方块z坐标
    - blockName : str 方块的identifier，包含命名空间及名称
    - fallDistance : float 实体下落距离，可以在脚本层传递
    - cancel : bool 修改为True时，可以阻止实体下落伤害的计算

    不是所有的方块都会触发该事件，需要在json中先配置触发开关（具体情况参考： 自定义方块JSON组件 ）

    如果需要在脚本层修改fallDistance，传递的一定是要浮点型，例如需要赋值0.0而非0

    可能会因为轻型反弹触发多次

    fallDistance参数在传递非0值后生效

    """
    pass


class OnEntityInsideBlockServerEvent(BaseEvent):
    """触发时机：当实体撞进区块所在区域内有方块时，服务端持续触发

    - cancel : bool 是否允许触发，默认为False，如果设置为True，可以阻止触发后的继续逻辑
    - blockX : int 方块x坐标
    - blockY : int 方块y坐标
    - blockZ : int 方块z坐标
    - slowdownMultiX : float 实体移动X方向的减速比列，可以在脚本层被修改
    - slowdownMultiY : float 实体移动Y方向的减速比列，可以在脚本层被修改
    - slowdownMultiZ : float 实体移动Z方向的减速比列，可以在脚本层被修改
    - blockName : str 方块的identifier，包含命名空间及名称
    - entityId : str 触发的entity的唯一ID

    不是所有的方块都会触发该事件，需要在json中先配置触发开关（具体情况参考： 自定义方块JSON组件 ），原方块需要先通过RegisterOnEntityInside接口注册才能触发

    如果需要修改slowdownMulti/cancel，强烈建议与客户端事件同步修改，避免出现客户端显示不一致等现象

    如果需要在脚本层修改slowdownMulti，传递的一定是要浮点型，例如需要赋值1.0而非1

    有任意slowdownMulti参数被传递非0值后生效

    slowdownMulti参数更像是一个Buff，例如不是最初计算，而是先存储在实体属性中后再计算、在已经有slowdownMulti属性的情况下会取最小的值、免掉下落伤害等，与原方块特性逻辑基本一致。

    """
    pass


class OnStandOnBlockServerEvent(BaseEvent):
    """触发时机：当实体站在方块上时，服务端持续触发

    - cancel : bool 是否允许触发，默认为False，如果设置为True，可以阻止触发后的继续逻辑
    - blockX : int 方块x坐标
    - blockY : int 方块y坐标
    - blockZ : int 方块z坐标
    - blockName : str 方块的identifier，包含命名空间及名称
    - entityId : str 触发的entity的唯一ID
    - cancel : bool 是否取消传递，可以在脚本层修改传递，避免出现客户端显示不一致等现象

    不是所有的方块都会触发该事件，需要在json中先配置触发开关（具体情况参考： 自定义方块JSON组件 ），原方块需要先通过RegisterOnStandOn接口注册才能触发

    如果需要修改motion/cancel，强烈建议与客户端事件同步修改，避免出现客户端显示不一致等现象

    如果需要在脚本层修改motion，传递的一定是要浮点型，例如需要赋值0.0而非0
    """
    pass
class PistonActionServerEvent(BaseEvent):
    """触发时机：活塞激活或收缩影响附近模块时

    - cancel : bool 是否允许触发，默认为False，如果设置为True，可阻止触发后的继续事件
    - action : str 推送时=expanding；收缩时=retracting
    - pistonFacing : int 活塞的朝向，参考Facing枚举
    - pistonMoveFacing : int 活塞的移动方向，参考Facing枚举
    - dimensionId : int 活塞方块所在的维度
    - pistonX : int 活塞方块的x坐标
    - pistonY : int 活塞方块的y坐标
    - pistonZ : int 活塞方块的z坐标
    - blockList : list[(x,y,z),...] 活动移动影响到大生被移动效果的方块坐标(x,y,z)，均为int类型
    - breakBlockList : list[(x,y,z),...] 活动移动影响到大生被破坏效果的方块坐标(x,y,z)，均为int类型
    - entityList : list[string,...] 活动移动影响到大生被移动或被破坏效果的实体的ID列表

    """
    pass


class ServerBlockEntityTickEvent(BaseEvent):
    """触发时机：自定义方块配置了netease:block_entity组件并设置tick为true，玩家进入该方块的tick范围时触发

    - blockName : str 该方块名称
    - dimension : int 该方块所在的维度
    - posX : int 该方块的x坐标
    - posY : int 该方块的y坐标
    - posZ : int 该方块的z坐标

    """
    pass


class ServerBlockUseEvent(BaseEvent):
    """触发时机：玩家右键点击新版自定义方块（或通过接口AddBlockItemListenForUseEvent添加监听的MC原生方块）时，服务端抛出该事件（该事件tick执行，需要注意效率问题）。

    - playerId : str 玩家Id
    - blockName : str 方块的identifier，包含命名空间及名称
    - aux : int 方块附加值
    - cancel : bool 设置为True可阻止与方块交互的逻辑
    - x : int 方块x坐标
    - y : int 方块y坐标
    - z : int 方块z坐标
    - dimensionId : int 维度id

    """
    pass


class ServerEntityTryPlaceBlockEvent(BaseEvent):
    """
    触发时机：当实体尝试放置方块时触发该事件。

    - x : int 方块x坐标
    - y : int 方块y坐标
    - z : int 方块z坐标
    - fullName : str 方块的identifier，包含命名空间及名称
    - auxData : int 方块附加值
    - entityId : str 尝试放置方块的实体ID
    - dimensionId : int 维度id
    - face : int 点击方块的面，参考Facing枚举
    - cancel : bool 默认为False，在脚本层设置为True就能取消方块的放置

    """
    pass


class ServerPlaceBlockEntityEvent(BaseEvent):
    """触发时机：手动放置或通过接口创建包含自定义方块实体的方块时触发，此时可向该方块实体中存放数据

    - blockName : str 该方块名称
    - dimension : int 该方块所在的维度
    - posX : int 该方块的x坐标
    - posY : int 该方块的y坐标
    - posZ : int 该方块的z坐标
    """
    pass


class ServerPlayerTryDestroyBlockEvent(BaseEvent):
    """当玩家即将破坏方块时，服务端线程抛出该事件。

    - x : int 方块x坐标
    - y : int 方块y坐标
    - z : int 方块z坐标
    - face : int 方块被破坏的面朝向id，参考Facing枚举
    - fullName : str 方块的identifier，包含命名空间及名称
    - auxData : int 方块附加值
    - playerId : str 尝试破坏方块的玩家ID
    - dimensionId : int 维度id
    - cancel : bool 默认为False，在脚本层设置为True就能取消方块的破坏
    - spawnResources : bool 是否生成掉落物，默认为True，在脚本层设置为False就能取消生成掉落物

    如果需要阻止某些特殊方块的破坏，需要结合PlayerTryDestroyBlockClientEvent一起使用，例如：苔藓、岩浆、草、地下、树叶、海草、珊瑚等这些基于方块数据进行渲染的方块
    """
    pass


class ShearsDestoryBlockBeforeServerEvent(BaseEvent):
    """触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在服务端线程抛出该事件

    - blockX : int 方块位置x
    - blockY : int 方块位置y
    - blockZ : int 方块位置z
    - blockName : str 方块的identifier，包含命名空间及名称
    - auxData : int 方块附加值
    - dropName : str 触发剪刀效果的掉落物identifier，包含命名空间及名称
    - dropCount : int 触发剪刀效果的掉落物数量
    - playerId : str 触发剪刀效果的玩家id
    - dimensionId : int 玩家触发时的维度id
    - cancelShears : bool 是否取消剪刀效果

    该事件在ServerPlayerTryDestroyBlockEvent之后触发，如果在ServerPlayerTryDestroyBlockEvent事件中设置了取消Destroy或取消掉落物会导致该事件不触发

    取消剪刀效果后不会掉落任何的方块类型：苔藓、岩浆草、草下、下界岩、树苗、海草、珊瑚等这些非实体方块。取消剪刀效果需要结合ShearsDestoryBlockBeforeClientEvent同时使用，否则在表现上可能会出现剪不断的情况，但实际上剪不断的效果还是会生成线。

    如果需要修改cancel，强烈建议结合客户端事件一起修改，避免出现客户端表现不一致等非预期现象。
    """
    pass


class StartDestroyBlockServerEvent(BaseEvent):
    """玩家开始破坏方块时触发。创建模式下不触发。

    - pos : tuple(float,float,float) 方块的坐标
    - blockName : str 方块的identifier，包含命名空间及名称
    - auxValue : int 方块的附加值
    - playerId : str 玩家id
    - dimensionId : int 维度id
    - cancel : bool 修改为True时，可阻止玩家进入破坏方块的状态。需要与StartDestroyBlockClientEvent一起修改。

    如果是火焰破坏方块，即设置该事件cancel，火焰也会被熄灭。如果需要阻止火焰熄灭，需要结合ExtinguishFireServerEvent使用
    """
    pass


class StepOffBlockServerEvent(BaseEvent):
    """
    触发时机：实体移动离开一个实体方块时触发

    - blockX : int 方块x坐标
    - blockY : int 方块y坐标
    - blockZ : int 方块z坐标
    - entityId : str 触发的entity的唯一ID
    - blockName : str 方块的identifier，包含命名空间及名称
    - dimensionId : int 维度id

    不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考： 自定义方块JSON组件 ）， 原版方块需要先通过RegisterOnStepOff接口注册才能触发
    """
    pass


class StepOnBlockServerEvent(BaseEvent):
    """触发时机：实体刚好移动到一个新的实体方块时触发。

    - cancel : bool 是否允许触发，默认为False，如果设置为True，可阻止触发后的继续物理事件
    - blockX : int 方块x坐标
    - blockY : int 方块y坐标
    - blockZ : int 方块z坐标
    - entityId : str 触发的entity的唯一ID
    - blockName : str 方块的identifier，包含命名空间及名称
    - dimensionId : int 维度id

    在合并微更新之后，该事件触发时机和服务端线程“minecraft:on_step_on”微语言行为组件一致

    压力板与线程球在经过的版本中是可以通过的，但在更新后这种非实体方块并不会触发，如果有需要可以通过OnEntityInsideBlockServerEvent事件。

    不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考： 自定义方块JSON组件 ）， 原版方块需要先通过RegisterOnStepOn接口注册才能触发。原版的红石粉默认注册了，但是深层红石粉没有默认注册。

    如果需要修改cancel，强烈建议结合客户端事件一起修改，避免出现客户端表现不一致等非预期现象。
    """
    pass


class FarmBlockToDirtBlockServerEvent(BaseEvent):
    """
    耕地退化为泥土时触发
    - dimension : int 方块维度
    - x : int 方块x坐标
    - y : int 方块y坐标
    - z : int 方块z坐标
    - setBlockType : int 耕地退化为泥土的原因，参考SetBlockType
    """
    pass
