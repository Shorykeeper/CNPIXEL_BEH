# -*- coding: utf-8 -*-
# Created on 2020-04-20
from ..base_event import BaseEvent

class ClientBlockUseEvent(BaseEvent):
    """
    触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块模块）时客户端抛出该事件
    （该事件tick执行，需要注意效率问题）

    有些方块是在ServerBlockUseEvent中设cancel生效，有些方块是在ClientBlockUseEvent中设cancel才生效，如果需要设计在两个事件中同时设cancel以保证生效
    """
    playerId = None
    blockName = None
    aux = None
    cancel = None
    x = None
    y = None
    z = None


class FallingBlockCauseDamageBeforeClientEvent(BaseEvent):
    """
    触发时机：当下落的方块开始计算砸到实体的伤害时，客户端触发该事件
    不是所有下落的方块都会触发该事件，需要在json中预先配置触发开关（详情参考： 自定义重力方块 ）
    当该事件的参数数据（fallTickAmount, fallDistance, collidingEntitys, fallDamage）与服务端事件FallingBlockCauseDamageBeforeServerEvent数据有差异时，请以服务端事件数据为准
    """
    fallingBlockId = None
    fallingBlockX = None
    fallingBlockY = None
    fallingBlockZ = None
    blockName = None
    dimensionId = None
    collidingEntitys = None
    fallTickAmount = None
    fallDistance = None
    isHarmful = None
    fallDamage = None


class OnAfterFallOnBlockClientEvent(BaseEvent):
    """
    触发时机：当实体降落在方块之后客户端触发，主要用于力的计算

    不是所有方块都会触发该事件，需要在json中预先配置触发开关（详情参考： 自定义方块JSON组件 ）

    如果要在脚本层修改motion，传递的需要是浮点型，例如需要赋值0.0而不是0

    如果需要修改实体的力，最好配合服务端事件同步修改，避免出现被服务端矫正等非预期现象

    因为牵引最后一定按照原方块规则计算力（普通方块置0，粘液方块等反弹），所以脚本层如果想直接修改当前力需要将calculate设为true取消原方块计算，按照传递值计算

    牵引在落地之后OnAfterFallOnBlockClientEvent会直接触发，因此请在脚本层中做相应的逻辑判断
    """
    entityId = None
    posX = None
    posY = None
    posZ = None
    motionX = None
    motionY = None
    motionZ = None
    blockName = None
    calculate = None


class OnEntityInsideBlockClientEvent(BaseEvent):
    """
    触发时机：当实体进入方块所在的区域有方块时，客户端持续触发

    不是所有方块都会触发该事件，需要在json中预先配置触发开关（详情参考： 自定义方块JSON组件 ），原方块需要先通过RegisterOnEntityInside接口注册才能触发

    如果需要修改slowdownMulti/cancel，强烈建议与服务端事件同步修改，避免出现被服务端矫正等非预期现象

    如果需要在脚本层修改slowdownMulti，传递的一定是浮点型，例如需要赋值1.0而不是1

    有任意slowdownMulti参数被传递非0值时生效减速效果

    slowdownMulti参数更像一个Buff，例如并非是最初计算，而是先保存在实体属性中延后计算，在已经有slowdownMulti属性的情况下会取最小的值、免受下落伤害等，与原版牵引逻辑基本一致
    """
    entityId = None
    dimensionId = None
    slowdownMultiX = None
    slowdownMultiY = None
    slowdownMultiZ = None
    blockX = None
    blockY = None
    blockZ = None
    blockName = None
    cancel = None


class OnModBlockNeteaseEffectCreatedClientEvent(BaseEvent):
    """
    自定义方块实体绑定的特效创建成事件，自定义方块实体中绑定的特效创建成事件及使用接口CreateFrameEffectForBlockEntity或CreateParticleEffectForBlockEntity为自定义方块实体添加特效时触发
    """
    effectName = None
    id = None
    effectType = None
    blockPos = None


class OnStandOnBlockClientEvent(BaseEvent):
    """
    触发时机：当实体站立在方块上时客户端持续触发

    不是所有方块都会触发该事件，需要在json中预先配置触发开关（详情参考： 自定义方块JSON组件 ），原方块需要先通过RegisterOnStandOn接口注册才能触发

    如果需要修改motion/cancel，强烈建议与服务端事件同步修改，避免出现被服务端矫正等非预期现象

    如果需要在脚本层修改motion，传递的一定是浮点型，例如需要赋值0.0而不是0
    """
    entityId = None
    dimensionId = None
    posX = None
    posY = None
    posZ = None
    motionX = None
    motionY = None
    motionZ = None
    blockX = None
    blockY = None
    blockZ = None
    blockName = None
    cancel = None


class PlayerTryDestroyBlockClientEvent(BaseEvent):
    """
    当玩家即将破坏方块时，客户端触发该事件。主要用于削平、削墙、挖子等基于方块实体数据进行渲染的方块，通常情况下请使用ServerPlayerTryDestroyBlockEvent
    """
    x = None
    y = None
    z = None
    face = None
    blockName = None
    auxData = None
    playerId = None
    cancel = None


class ShearsDestoryBlockBeforeClientEvent(BaseEvent):
    """
    触发时机：当玩家手持剪刀破坏方块时，有剪刀特效的方块会在客户端触发该事件

    目前只有牵引线会触发，需要取消剪刀效果得配合ShearsDestoryBlockBeforeServerEvent同时使用
    """
    blockX = None
    blockY = None
    blockZ = None
    blockName = None
    auxData = None
    dropName = None
    dropCount = None
    playerId = None
    dimensionId = None
    cancelShears = None


class StartDestroyBlockClientEvent(BaseEvent):
    """
    玩家开始破坏方块时触发该事件。创建模式下不触发

    如果是在火焰中破坏方块，即设置该事件cancel，火焰也会被扑灭。如果需要阻止火焰扑灭，需要配合ExtinguishFireClientEvent使用
    """
    pos = None
    blockName = None
    auxValue = None
    playerId = None
    cancel = None


class StepOffBlockClientEvent(BaseEvent):
    """
    触发时机：当实体移动离开一个实体心方块时触发

    不是所有方块都会触发该事件，自定义方块需要在json中预先配置触发开关（详情参考： 自定义方块JSON组件 ），原方块需要先通过RegisterOnStepOff接口注册才能触发
    """
    blockX = None
    blockY = None
    blockZ = None
    entityId = None
    blockName = None
    dimensionId = None


class StepOnBlockClientEvent(BaseEvent):
    """
    触发时机：当实体刚移入一个新的实体心方块时触发

    在合并微端更新之后，该事件触发时机与微端molang实验性玩法组件"minecraft:on_step_on"一致

    牵引片与牵引线在过去的版本中会触发这种非实体心方块的事件，但是在更新之后这种非实体心方块的事件不会再触发，有需要的可以使用OnEntityInsideBlockClientEvent事件

    不是所有方块都会触发该事件，自定义方块需要在json中预先配置触发开关（详情参考： 自定义方块JSON组件 ），原方块需要先通过RegisterOnStepOn接口注册才能触发
    原版的牵引球默认注册了，但是深层次牵引球并没有默认注册

    如果需要修改cancel，强烈建议与服务端事件同步修改，避免出现被服务端矫正等非预期现象
    """
    cancel = None
    blockX = None
    blockY = None
    blockZ = None
    entityId = None
    blockName = None
    dimensionId = None
