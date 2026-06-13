# coding=utf-8
# Created on 2020-04-20
from ..base_event import BaseEvent


class AddEntityServerEvent(BaseEvent):
    """服务端创建新实体，或实体从存档加载时触发

    - id : str 实体id
    - posX : float 位置x
    - posY : float 位置y
    - posZ : float 位置z
    - dimensionId : int 实体维度
    - isBaby : bool 是否为婴儿
    - engineTypeStr : str 实体类型
    - itemName : str 物品identifier（仅当物品实体时存在此字段）
    - auxValue : int 物品附加值（仅当物品实体时存在此字段）

    """
    pass


class AddServerPlayerEvent(BaseEvent):
    """触发时机：玩家加入时触发

    - id : str 玩家id
    - isTransfer : bool 是否为切服时进入服务器，仅用于Apollo。如果为True，则表示切服时进入服务器，如果为False，则表示登录进入网络游戏
    - isReconnect : bool 是否为断线重连，仅用于Apollo。如果为True，则表示本次登录为断线重连，如果为False，则表示本次为正常登录或转服
    - isPeUser : bool 是否从手机端登录，仅用于Apollo。如果为True，则表示本次登录为从手机端登录，如果为False，则表示本次登录为从PC端登录
    - transferParam : str 切服传入参数，仅用于Apollo。调用[TransferToOtherServer]或[TransferToOtherServerById]传入的切服参数
    - uid : int/long 仅用于Apollo，玩家的netease uid，玩家的唯一标识
    - proxyId : int 仅用于Apollo，当前客户端连接的proxy服务器id

    """
    pass


class ChunkAcquireDiscardedServerEvent(BaseEvent):
    """服务端区块即将被卸载时触发

    - dimension : int 区块所在的维度
    - chunkPosX : int 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15]
    - chunkPosZ : int 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15]
    - entities : list(str) 随机区块卸载而从世界移除的实体id的列表。注意事件触发时已经无法获取到这些实体的信息，仅供脚本资源回收用。
    - blockEntities : list(dict) 随机区块卸载而从世界移除的自定义方块实体的坐标列表，列表元素dict包含posX, posY, posZ三个int表示自定义方块实体的坐标。注意事件触发时已经无法获取到这些方块实体的信息，仅供脚本资源回收用。

    """
    pass


class ChunkGeneratedServerEvent(BaseEvent):
    """触发时机：服务端区块生成完成时触发

    - dimension : int 该区块所在的维度
    - blockEntityData : [{"blockName":str,"posX":int,"posY":int,"posZ":int}...]/None 该区块中的自定义方块实体坐标列表，通常是由于自定义特性生成的自定义方块，没有自定义方块实体时此值为None

    """
    pass


class ChunkLoadedServerEvent(BaseEvent):
    """触发时机：服务端区块加载完成时

    - dimension : int 区块所在维度
    - chunkPosX : int 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15]
    - chunkPosZ : int 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15]

    """
    pass


class ClientLoadAddonsFinishServerEvent(BaseEvent):
    """触发时机：客户端mod加载完成时，服务端触发此事件。服务端可以使用此事件，向客户端发送数据给其初始化

    - playerId : str 玩家id

    """
    pass


class CommandEvent(BaseEvent):
    """玩家请求执行命令时触发

    - entityId : str 玩家ID
    - command : str 命令字符串
    - cancel : bool 是否取消

    该事件是玩家请求执行命令时触发的Hook，该事件不影响命令模块的命令和通过modSDK调用的命令，阻止玩家的该条命令只需将cancel设置为True
    """
    pass


class CustomCommandTriggerServerEvent(BaseEvent):
    """服务端自定义命令触发

    - command : str 自定义命令名称，对应json中的name字段
    - args : list(dict) 自定义命令参数，详情见下方
    - origin : str 自定义命令来源，对应json中的origin字段
    - variant : int	表示是哪条变体，范围[0, 9]，对应json中args键中的数字，未配置变体则为0
    - return_failed : bool 设置自定义命令是否执行失败，默认为False，如果执行失败，返回信息以红色字体显示
    - return_msg_key : str 设置返回给玩家或命令方块的信息，支持在语言文件(.lang)中定义，默认值为commands.custom.success(自定义命令执行成功)

    备注

        args中的某个dict参数说明如下

        键	类型	解释
        name	str	参数名称，对应json中的name字段
        type	str	参数类型，对应json中的type字段
        value	any	参数的值，若玩家没传，则采用json中填写的default的值，但会转为python变量格式。如null转为None，array转为tuple
        当type为pos、entity、item时，value的格式如下

        type	value类型	解释
        pos	tuple	一个含有三个float的坐标，如(-0.93, 81.25, -5.67)
        entity	dict	一个含有entityType的字典，如{'entityType': 'minecraft:cow'}
        item	dict	一个含有itemName的字典，如{'itemName': 'minecraft:apple'}
        origin参数说明如下

        键	类型	解释
        entityId	str	触发指令的实体id，若由命令方块触发，则不会含有此字段
        dimension	int	指令触发的维度id，0-主世界; 1-下界; 2-末地; 或其他自定义维度
        blockPos	tuple	触发指令的实体或命令方块的整数坐标
    """
    pass


class DelServerPlayerEvent(BaseEvent):
    """触发时机：删除玩家时触发该事件。

    - id : str 玩家id
    - isTransfer : bool 是否为切换服务器时退出服务器，仅用于Apollo。如果是True，则表示切换服务器时退出服务器；如果是False，则表示退出网络游戏
    - uid : int/long 玩家的netease uid，玩家的唯一标识

    玩家离开网络游戏时，会在PlayerLeftEvent之后触发
    """
    pass


class EntityRemoveEvent(BaseEvent):
    """实体被删除时触发

    - id : str 实体id

    触发情况：实体从场景中被删除，例如：生物死亡，生物被清除 (opens new window)，玩家退出网络游戏，船/舰桥被破坏，获得物/经验球被捡起或清除

    关于实体的清除：当生物远离wiki所说的距离，并且还在玩家的模拟距离内时，会被清除。也就是说，如果玩家距离变远，原地的生物马上了离开模拟距离了，并且不会被清除

    玩家退出网络游戏时，PlayerLeftEvent，EntityRemoveEvent，DelServerPlayerEvent按顺序依次触发
    """
    id = None


class ExplosionServerEvent(BaseEvent):
    """
    当发生爆炸时触发。

    - blocks : list[[x,y,z,cancel],...] 爆炸波及到的方块坐标(x,y,z)，cancel是一个bool值
    - victims : list/None 受害实体id列表，当该爆炸创建者id为None时，victims也为None
    - sourceId : str/None 爆炸创建者id
    - explodePos : list 爆炸位置[x,y,z]
    - dimensionId : int 维度id

    通过设置blocks中cancel的bool值为True可以将该方块的爆炸取消，例如(x,y,z,True)

    有些情况下爆炸创建者id为None，此时受害实体id列表也为None，例如：海盗所造成的爆炸。
    """
    pass


class LoadServerAddonScriptsAfter(BaseEvent):
    """服务端加载完mod时触发"""
    pass


class NewOnEntityAreaEvent(BaseEvent):
    """触发时机：通过RegisterEntityAOIEvent注册过AOI事件后，当有实体进入或离开注册感应区域时触发该事件

    - name : str 注册感应区域名称
    - enteredEntities : list[str] 进入该感应区域的实体id列表
    - leftEntities : list[str] 离开该感应区域的实体id列表

    """
    pass


class OnCommandOutputServerEvent(BaseEvent):
    """Command命令执行成功事件

    - command : str 命令名称
    - message : str 命令返回的信息

    """
    pass


class OnContainerFillLoottableServerEvent(BaseEvent):
    """触发时机：随机战利品箱第一次打开根据loottable生成物品时

    - loottable : str 随机战利品子所读取的loottable的json路径
    - playerId : str 打开随机战利品子的玩家的playerId
    - itemList : list 获得物品列表，每个元素为一个itemDict，格式可参考物品信息字典
    - dirty : bool 默认为False，如果需要修改获得列表需将此值设为True

    """
    pass


class OnLightningLevelChangeServerEvent(BaseEvent):
    """打雷强度发生改变

    - oldLevel : float 改变前的打雷强度
    - newLevel : float 改变后的打雷强度

    """
    pass


class OnLocalLightningLevelChangeServerEvent(BaseEvent):
    """独立维度天气打雷强度发生改变时触发

    - oldLevel : float 改变前的打雷强度
    - newLevel : float 改变后的打雷强度
    - dimensionId : int 独立天气维度id

    """
    pass


class OnLocalRainLevelChangeServerEvent(BaseEvent):
    """独立维度天气下雨强度发生改变时触发

    - oldLevel : float 改变前的下雨强度
    - newLevel : float 改变后的下雨强度
    - dimensionId : int 独立天气维度id

    """
    pass


class OnRainLevelChangeServerEvent(BaseEvent):
    """下雨强度发生改变

    - oldLevel : float 改变前的下雨强度
    - newLevel : float 改变后的下雨强度

    """
    pass


class OnScriptTickServer(BaseEvent):
    """服务端tick触发,1秒有30个tick"""
    pass


class PlaceNeteaseStructureFeatureEvent(BaseEvent):
    """触发时机：第一次生成地形时，结构特性即会被服务端抛出该事件

    - structureName : str 结构名称
    - x : int 结构坐标最小方块所在的x坐标
    - y : int 结构坐标最小方块所在的y坐标
    - z : int 结构坐标最小方块所在的z坐标
    - biomeType : int 该feature所放置区块的生物群系类型
    - biomeName : str 该feature所放置区块的生物群系名称
    - dimensionId : int 维度id
    - cancel : bool 设置为True时可阻止该结构的放置

    """
    pass


class PlayerIntendLeaveServerEvent(BaseEvent):
    """触发时机：即将删除玩家时触发该事件，此时可以通过各种API获取玩家的当前状态

    - playerId : str 玩家实体id

    与[DelServerPlayerEvent]事件不同，此时可以通过各种API获取玩家的当前状态
    """
    pass


class PlayerJoinMessageEvent(BaseEvent):
    """触发时机：准备显示“xxx加入游戏”的玩家登录提示文字时服务端抛出的事件

    - id : str 玩家实体id
    - name : str 玩家名称
    - cancel : bool 是否显示提示文字，允许修改。True：不显示提示
    - message : str 玩家加入游戏的提示文字，允许修改

    """
    pass


class PlayerLeftMessageServerEvent(BaseEvent):
    """触发时机：准备显示“xxx离开游戏”的玩家离开提示文字时服务端抛出的事件

    - id : str 玩家实体id
    - name : str 玩家名称
    - cancel : bool 是否显示提示文字，允许修改。True：不显示提示
    - message : str 玩家加入游戏的提示文字，允许修改
    """
    pass


class ServerChatEvent(BaseEvent):
    """玩家发送聊天信息时触发

    - username : str 玩家名称
    - playerId : str 玩家id
    - message : str 玩家发送的聊天信息内容
    - cancel : bool 是否取消该条聊天事件，如果取消可以设置为True
    - bChatById : bool 是否将聊天信息发送给指定在线玩家，而不是广播给所有在线玩家，如果只发送给某些玩家可以设置为True
    - bForbid : bool 是否禁言，仅Apollo可用。true：被禁言，玩家聊天会提示“你已被管理员禁言”
    - toPlayerIds : list(str) 接收聊天信息的玩家id列表，bChatById为True时有效

    """
    pass


class ServerPostBlockPatternEvent(BaseEvent):
    """触发时机：使用方块组合生成生物，生成生物后抛出该事件

    - entityId : str 生成生物的id
    - entityGenerated : str 生成生物的名称，如"minecraft:pig"
    - x : int 方块x坐标
    - y : int 方块y坐标
    - z : int 方块z坐标
    - dimensionId : int 维度id

    """
    pass


class ServerPreBlockPatternEvent(BaseEvent):
    """触发时机：使用方块组合生成生物，在放置最后方块时抛出该事件

    - enable : bool 是否允许继续生成。如果设为False，可阻止生成生物
    - x : int 方块x坐标
    - y : int 方块y坐标
    - z : int 方块z坐标
    - dimensionId : int 维度id
    - entityWillBeGenerated : str 即将生成生物的名称，如"minecraft:pig"

    """
    pass


class ServerSpawnMobEvent(BaseEvent):
    """游戏中自动生成生物时触发

    - identifier : str 生成实体的命名空间
    - type : int 生成实体的类型，参考EntityType
    - baby : bool 生成生物是否为婴儿
    - x : float 生成实体坐标x
    - y : float 生成实体坐标y
    - z : float 生成实体坐标z
    - dimensionId : int 生成实体的维度，默认值为0（0为主世界，1为地狱，2为末地）
    - realIdentifier : str 生成实体的命名空间，通过MOD API生成的实体在此参数也能获取到正确的命名空间，而不是以custom开头的
    - cancel : bool 是否取消生成该实体

    """
    pass
