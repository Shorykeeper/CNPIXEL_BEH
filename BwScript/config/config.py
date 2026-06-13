# coding=utf-8
NAMESPACE = 'Bw'
SERVER_SYSTEM_NAME = 'BwServer'
CLIENT_SYSTEM_NAME = 'BwClient'
SERVER_SYSTEM_PATH = 'BwScript.server.BwServer.BwServerSys'
CLIENT_SYSTEM_PATH = 'BwScript.client.BwClient.BwClientSys'

configscoreName = 'BedWars_score'
configkickName = 'BedWars_kick'


gameRuleDict = {
    'option_info': {
        'pvp': True,  # 玩家间伤害
        'show_coordinates': True,  # 显示坐标
        'fire_spreads': False,  # 火焰蔓延
        'tnt_explodes': True,  # TNT爆炸
        'mob_loot': False,  # 生物战利品
        'natural_regeneration': True,  # 自然生命恢复
        'respawn_block_explosion': False,  # 重生方块爆炸
        'respawn_radius': 0,  # 重生半径
        'tile_drops': True,  # 方块掉落
        'immediate_respawn': True  # 立即重生
    },
    'cheat_info': {
        'enable': True,  # 激活作弊
        'always_day': True,  # 终为白日
        'mob_griefing': False,  # 生物破坏
        'keep_inventory': True,  # 保留物品栏
        'weather_cycle': False,  # 天气更替
        'mob_spawn': False,  # 生物生成
        'entities_drop_loot': False,  # 实体掉落战利品
        'daylight_cycle': False,  # 开启昼夜更替
        'command_blocks_enabled': True,  # 启用命令方块
        'random_tick_speed': 1,  # 随机刻速度
    }
}



ore_resource_list = {
    'minecraft:iron_ingot',
    'minecraft:gold_ingot',
    'minecraft:diamond',
    'minecraft:emerald'
}




BANWORD = { 
    "唐": "宋",
    "糖": "甜",
    "原神": "MC",
    "恶心": "暖胃",
    "飞舞": "佩服",
    "最强": "最弱",
    "逃": "心动",
    "fw": "猫头鹰",
    "Fw": "咕唔",
    "陶艺": "撤硕",
    "叫唤": "喵呜",
    "fv": "厉害",
    "导管": "断欲",
    "骂": "爱",
    "挂": "喵",
    "坨": "只",
    "单刀": "和我交往吧",
    "制裁": "做恨",
    "沙": "呜",
    "本事": "精妙",
    "老": "少",
    "冯": "凤",
    "全家": "我家",
    "浮木": "南梁",
    "l": "佩服",
    "L": "厉害",
    "丨_": "爱你",
    "rz": "聪慧",
    "ou": "Yuno~",
    "zz": "谢谢",
    "oser": "sensei",
    "FW": "尤物",
    "脸": "足",
    "nt": "聪敏",
    "狗": "猫",
    "ez": "nb",
    "公益": "骗钱",
    "崩服": "维护",
    "人机": "小岸"
}

SERVER_VIRUS_POOL = [
    '▁', '▂', '▃', '▄', '▅', '▆', '▇', '█',
    '░', '▒', '▓', '▏', '▎', '▍', '▌', '▋',
    '▊', '▉', '▬', '卍', '卐', '', '◪',
    '●', '▶', '◀', '@e', '§', '◐'
]


InterFlow_Scoreboard = [ #互通的计分板 S9T03A
    '落月币',
    'U2C44V',
    'T8R43H',
    'K8T78F',
    'V5G28k',
    'S9T03A',
    'C4D31J',
    'S0F06V',
    'Q0A59I',
    'E1B36G',
    'G7C23S',
    'Y5T96B',
    'V3P49H',
    'D2K48A',
    'S8Q83P'
]

ScoreboardDataKey = {
    "落月币": "Coin",
    "U2C44V": "Prefix",
    "K8T78F": "elo",
    "S9T03A": "sta",
    "T8R43H": "Awin",
    "V5G28k": "Ank",
    "C4D31J": "Afk",
    "S0F06V": "Adb",
    "Q0A59I": "Ac",
    "E1B36G": "Aexp",
    "G7C23S": "Alev",
    "V3P49H": "Almt",
    "Y5T96B": "Amd",
    "D2K48A": "Ad",
    "S8Q83P": "Apo"
}

ScoreboardDataKeyBack = { #反向字典
    "Coin": "落月币",
    "Prefix":"U2C44V",
    "elo": "K8T78F",
    "sta": "S9T03A",
    "Awin": "T8R43H",
    "Ank": "V5G28k",
    "Afk": "C4D31J",
    "Adb": "S0F06V",
    "Ac": "Q0A59I",
    "Aexp": "E1B36G",
    "Alev": "G7C23S",
    "Almt": "V3P49H",
    "Amd": "Y5T96B",
    "Ad": "D2K48A",
    "Apo": "S8Q83P"
}

server_can_destroy_blocks = [
    'minecraft:red_wool',
    'minecraft:blue_wool',
    'minecraft:lime_wool',
    'minecraft:yellow_wool',
    'minecraft:obsidian',
    'minecraft:end_stone',
    'minecraft:cake',
    'minecraft:bed',
    'minecraft:ladder',
    'minecraft:web',
    'minecraft:trapped_chest',
    'minecraft:tnt',
    'minecraft:slime',
    'minecraft:oak_planks',
    'minecraft:sponge',
    'minecraft:wet_sponge',
    'minecraft:red_terracotta',
    'minecraft:blue_terracotta',
    'minecraft:yellow_terracotta',
    'minecraft:green_terracotta',
    'minecraft:lime_stained_glass',
    'minecraft:red_stained_glass',
    'minecraft:yellow_stained_glass',
    'minecraft:blue_stained_glass'
]#可破坏的方块



Durability_Canchanged_items = [
    'minecrafts:firefly_sword',
    'minecraft:golden_sword',
    'minecraft:golden_axe'
]#可掉耐久的物品



TAG_RENDER_NAME_PREFIX = {
    'wtf': '§e§l[§b开§e发§c作§a者§f] §f',
    'wtf1': '§c[OWNER]',
    'wdf': '§c[ADMIN] §f',
    'chuji': '§2[GM] §f',
    'vip': '§a[VIP] §f',
    'mvp': '§b[MVP] §f',
    'mvp1': '§6[MVP§c++§6] §f',
    'friends': '§u[FRIENDS] §f',
    'prime': '§6[PRIME] §f',
    'elite': '§8[ELITE] §f',
    'pm': '§d[PM] §f',
    'wup': '§d[§fMEDIA§d] §f',
    'vip1': '§a[VIP§6+§a] §f',
    'help': '§8[HELPER] §f'
}     #名称的前缀 key是身份Tag Value是前缀内容


tag_to_message = {
    'wtf': '§e§l[§b开§e发§c作§a者§f]§r§e',
    'wtf1': '§c[OWNER]',
    'wdf': '§c[ADMIN]',
    'chuji': '§2[GM]',
    'vip': '§a[VIP]',
    'mvp': '§b[MVP]',
    'mvp1': '§6[MVP§c++§6]',
    'friends': '§u[FRIENDS]',
    'prime': '§6[PRIME]',
    'elite': '§8[ELITE]',
    'pm': '§d[PM]',
    'wup': '§d[§fMEDIA§d]',
    'vip1': '§a[VIP§6+§a]',
    'help': '§8[HELPER]'
}     # Chat的前缀 同

tag_to_ban = {
    'ac_ban': 'AutoClick(A)',
    'interact_ban': 'Fucker(B)',
    'speed_ban': 'Speed(E)',
    'fly_ban': 'Fly(A)'
}


MAX_MESSAGE_LENGTH = 125 #发言len限制,中文字符3节,英文和数字半角标点1节
GLOBAL_KB_COUNTDOWN = 0.09  #击退冷却 (该变量未启用)

max_chat_count = 7# 最大刷屏次数
mute_time = 45# 刷屏禁言时间
chat_reset_delay = 6# 刷屏重置时间(秒)
max_honk_time = 120 #挂机时间,挂机时间x0.5会提示挂机过长

max_cps = 16 #最大CPS (该变量未启用)

#MGE规则
#有床的击杀
MATCH_REWARD_HAVE_BED_NK_SCORE = 1
#无床绝境击杀
MATCH_REWARD_NO_BED_NK_SCORE = 2

#任何最终击杀
MATCH_REWARD_FK_SCORE = 2

#有床破坏敌方床
MATCH_REWARD_HAVE_BED_DBED_SCORE = 5
#无床绝境破坏敌方床
MATCH_REWARD_NO_BED_DBED_SCORE = 8

#有床获胜
MATCH_REWARD_HAVE_BED_WIN_SCORE = 3
#无床绝境翻盘获胜
MATCH_REWARD_NO_BED_WIN_SCORE = 5

#有床使用弓箭射死人
MATCH_REWARD_HAVE_BED_HUNT_NK_SCORE = 1
#无床绝境使用弓箭射死人
MATCH_REWARD_NO_BED_HUNT_NK_SCORE = 2


COMMAND_STAFFONLY_POOL = [
    'ban', 'forbid', 'slience', 'tag', 'give', 'function',
    'gamemode', 'scoreboard', 'summon', 'tickingarea',
    'gamerule', 'me', 'slience', 'rec', 'kik', 'end', 'utu'
]



max_attack_distance = 7 #最大攻击距离

explosion_damage = 3 #tnt爆炸伤害



white_list = [
    '落月_LYue',
    'DewierMC',
    '志云工作室',
    'star_幸存者',
    '麻杯服务站',
    '落_XenClare',
    '普通的贝利亚罢了',
    '一只很菜的清雪',
    '普通的小晴川罢了',
    '普通的小清猫罢了',
    'zest_yingzi',
    '流萤_Firefly',
    'NotLyingzi',
    'ShoryKeeper',
    '丨菜鱼丨',
    'YJ叶格宁',
    '我嘞个夏冰雹',
    'HSZAQ',
    '叶格宁',
    'B站丶Kaway柠檬',
    '拾暖记'
] #白名单(无限获得操作员权限和可以使用命令,不在白名单的玩家获得成员权限和无法使用命令)

ShoryKeepeR_ID_list = [
     '流萤_Firefly',
     'ShoryKeeper',
     '愿戴荣光坠入天渊'
] #岸名单 特殊文案

Id_list = [] #uid白名单

op_list = [
    'ShoryKeeper',
    '流萤_Firefly',
    'star_幸存者',
    '普通的小晴猫罢了',
    '麻杯服务站',
    'zest_yingzi',
    'YJ叶格宁',
    '西瓜云',
    '西瓜云工作室',
    '拾暖记',
    '叶格宁',
    '落月_LYue'
] #最高级权限名单

LIMIT_DISTANCE = 5 #格内的玩家会突进
VERTICAL_SPEED = 0.42 #竖直方向速度(会弹多高的高度,尽量不要超出1.1)
HORIZONTAL_SPEED = 0.58 #水平方向速度(向前突进一段距离,尽量不要超出0.7)

TAG_TO_ENCHANT = {
    '保护1': (0, 1),  # (附魔ID，等级)
    '摔落1': (2, 1),
    '保护2': (0, 2),
    '摔落2': (2, 2),
    '保护3': (0, 3),
    '保护4': (0, 4)
}
