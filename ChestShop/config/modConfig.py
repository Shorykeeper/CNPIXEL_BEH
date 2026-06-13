# -*- coding: utf-8 -*-
# 以下为MOD配置信息
modName = "ChestShop"
version = "0.0.1"
systemName = "main"

debug = True  # 是否开启调试模式 千万别关

# 玩家网络延迟相关配置
FIRST_TEXT = "§b你正在§eCNPIXEL§b中国版服务器游玩"
LAST_TEXT = "§a遇到问题或建言献策?前往§c§l635-391-984进行反馈"
PING = (50, 100, 150, 300)  # <50=3格，<100=2格，<150=1格，300=最大显示
HEADSHOT_LIST = ["", "", ""]


# 计分板配置       镐子等级 盔甲等级 斧子等级
SCOREBOARD_LIST = ["X2C07R", "I3P77O", "I0S08X"]   # 记录升级装备的计分板列表
ENCH_SCOREBOARD_LIST = ["X5T99R", "C1T28Q","A1B23C","Z3K56L","Q7M04P","Y9V88N","G6Y81U","F2W73J","E3Q28N","P4J90M","C5H77S","H1G22F"]   # 记录附魔等级的计分板列表
ENCH_SCOREBOARD_TRAP_LIST = ["E3Q28N","F2W73J","H1G22F","G6Y81U","P4J90M"]   # 记录附魔等级的计分
SWORD_LIST = ["stone_sword","iron_sword","diamond_sword","golden_sword"]  # 武器列表
REFIX_SCOREBOARD = ["S8Q83P"]  # 记录前缀的计分板列表 %   急迫 保护 锋利 龙 治愈池 铁锻炉
REFIX_ENUM = {
    1: "§d[§fMEDIA§d]",
    2: "§a[VIP]",
    3: "§a[VIP§6+§a]",
    4: "§b[MVP]",
    5: "§6[MVP§c++§6]",
    6: "§8[ELITE]",
    7: "§6[PRIME]",
    8: "§u[FRIENDS]",
    9: "§d[PM]",
    10: "§2[GM]",
    11: "§c[ADMIN]",
    12: "§8[HELPER]",
    13: "§c[OWNER]"
}
TEAM_SCOREBOARD_LIST = ["A1T12P"]   # 记录团队等级的计分板列表

TEAM_ENUM = {
    0: {"name": "NONE", "color": "§f", "chinese": ""},
    1: {"name": "RED", "color": "§c", "chinese": "红"},
    2: {"name": "BLUE", "color": "§9", "chinese": "蓝"},
    3: {"name": "GREEN", "color": "§a", "chinese": "绿"},
    4: {"name": "YELLOW", "color": "§e", "chinese": "黄"},
}

CURRENCY_ENUM = {

    "minecraft:iron_ingot": "§f铁锭§f",
    "minecraft:gold_ingot": "§p金锭§p",
    "minecraft:diamond": "§b钻石§b",
    "minecraft:emerald": "§q绿宝石§q",
    "iron_ingot": "§f铁锭§f",
    "gold_ingot": "§p金锭§p",
    "diamond": "§b钻石§b",
    "emerald": "§q绿宝石§q",
    "experience": "§2经验§2"
}


# 商店设置
BUY_SUCCEED_SOUNDS = ("note.pling", 1, 2)  # (名字，音量，音调)
BUY_SUCCEED_TEXT = "§a你购买了 §6{item_name}"  # {item_name}为购买的物品名称，{currency}为货币名称，{price}为物品价格
BUY_FAIL_SOUNDS = ("mob.shulker.teleport", 1, 0.5)#mob.endermen.portal
#BUY_FAIL_TEXT = "§c资源不足以购买,还需要§c{need_currency}§c个{currency}！"  # {need_currency}为需要的货币数量
BUY_FAIL_TEXT = "§c资源不足以购买该物品!"
BUY_FAIL_TEXT_FOR_ARMOUR = "§c已经有相等等级或更高等级的盔甲!"
import shop_2, shop_3, shop_4, shop_5, shop_6, shop_7, shop_8, shop_9, rbw_chained, rbw_unt
SHOP_DATA = {
    "shop_2": {
        "name": "§0道具商店-疾速 CNPIXEL",
        "goods": shop_2.GOODS_DATA
    },    
    "shop_3": {
        "name": "§0道具商店-无尽 CNPIXEL",
        "goods": shop_3.GOODS_DATA
    },
    "shop_4": {
        "name": "§0道具商店-经验 CNPIXEL",
        "goods": shop_4.GOODS_DATA
    },
    "shop_5": {
        "name": "§0道具商店-排位 CNPIXEL",
        "goods": shop_5.GOODS_DATA
    },
    "shop_6": {
        "name": "§0道具商店-经典 CNPIXEL",
        "goods": shop_6.GOODS_DATA
    },
    "shop_7": {
        "name": "§0团队升级与陷阱 CNPIXEL",
        "goods": shop_7.GOODS_DATA
    },
    "shop_9": {
        "name": "§0经验团队升级陷阱 CNPIXEL",
        "goods": shop_9.GOODS_DATA
    },
    "rbw_chained": {
        "name": "§0排位起床选队-CHAINED CNPIXEL",
        "goods": rbw_chained.GOODS_DATA
    },
    "rbw_unt": {
        "name": "§0排位起床选队-KASTU CNPIXEL",
        "goods": rbw_unt.GOODS_DATA
    },
    "shop_8": {
        "name": "§0[限免] 选择你的队伍 CNPIXEL",
        "goods": shop_8.GOODS_DATA
    }
}

