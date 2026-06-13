# coding=utf-8 rbw

TEAM_COLOR = {
    "BLUE": {"HEX": "§9", "COLOR": 0x313DB1, "NAME": "§r§9蓝", "WOOL": "light_blue_"},
    "RED": {"HEX": "§c", "COLOR": 0x8A1200, "NAME": "§r§c红", "WOOL": "red_"},
    "YELLOW": {"HEX": "§e", "COLOR": 0xE2D501, "NAME": "§r§e黄", "WOOL": "yellow_"},
    "GREEN": {"HEX": "§a", "COLOR": 0x317B00, "NAME": "§r§a绿", "WOOL": "lime_"},
    "ORANGE": {"HEX": "§6", "COLOR": 0xaa5500, "NAME": "§r§6橙", "WOOL": "orange_"},
    "GRAY": {"HEX": "§8", "COLOR": 0x555555, "NAME": "§r§8灰", "WOOL": "light_gray_"},
    "WHITE": {"HEX": "§f", "COLOR": 0xffffff, "NAME": "§r§f白", "WOOL": "white_"},
    "PINK": {"HEX": "§d", "COLOR": 0xff55ff, "NAME": "§r§d粉", "WOOL": "pink_"},
    "CYAN": {"HEX": "§b", "COLOR": 0x55ffff, "NAME": "§r§b青", "WOOL": "cyan_"},
    "PURPLE": {"HEX": "§5", "COLOR": 0xaa00aa, "NAME": "§r§5紫", "WOOL": "purple_"},
}  # 颜色配置

userData = {
    "minecraft:item_lock": {"__type__": 1, "__value__": 1},
    "display": {'Name': {'__type__': 8, '__value__': TEAM_COLOR["RED"]["NAME"] + "队"}},
    "customColor": {'__type__': 3, '__value__': TEAM_COLOR["RED"]["COLOR"]},
    "ItemCustomTips": {'__type__': 8, '__value__': '%name%%enchanting%'}
}

GOODS_DATA = {
    0: {  # tab_type
        "description": "§a快捷购买\n§e点击查看!",   # 标签描述 
        "itemDict": {  # 标签物品
            "newItemName": "minecraft:netherstar",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {   # 商品列表
            0 : {
                "price": 4,   # 价格
                "type": "wool",  # 商品类型
                "currency": "minecraft:iron_ingot",  # 货币,中文在modConfig.py中的"CURRENCY_ENUM"配置
                "description": "§7极适合用来跨越岛屿\n§7其颜色取决于你的队伍",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:white_wool",
                    "newAuxValue": 0,
                    "count": 16  # 数量
                }
            },
            1 : {
                "price": 10,   # 价格
                "currency": "minecraft:iron_ingot",  
                "description": "伤害一般的近战武器\n适用于快速战斗情形",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:stone_sword",
                    "newAuxValue": 0,
                    "count": 1  # 数量
                }
            },            
            2 : {
                "price": 35,   # 价格
                "currency": "minecraft:iron_ingot",  # 货币
                "description": "§7永久的 锁链盔甲",  # 商品描述
                "type": "armour",  # 商品类型
                "level": 1,  # 盔甲等级
                "itemList": {  # type:dict[tuple[ItemPosType, slotPos]:ItemDict]  # 物品列表
                    (3, 2) : {
                        "newItemName": "minecraft:chainmail_leggings",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    },
                    (3, 3) : {
                        "newItemName": "minecraft:chainmail_boots",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    }
                },
                "itemDict": {  # 商品物品渲染
                    "newItemName": "minecraft:chainmail_boots",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            3 : {
                "type": "X2C07R",  # 商品类型，同时也是计分板名字，需要在"modConfig.py"中的"SCOREBOARD_LIST"配置
                "itemList": {  # type:dict[level:ItemDict]  # 物品列表
                    0 : {
                        "price": 10,
                        "currency": "minecraft:iron_ingot",
                        "description": "等级: §eI §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:wooden_pickaxe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c木镐'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 10,
                        "currency": "minecraft:iron_ingot",
                        "description": "等级: §eI-II §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:stone_pickaxe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c石镐'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 3,
                        "currency": "minecraft:gold_ingot",
                        "description": "等级: §eII-III §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:iron_pickaxe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c铁镐'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    3 : {
                        "price": 6,
                        "currency": "minecraft:gold_ingot",
                        "description": "等级: §eIII-§cIV (已满级) §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:diamond_pickaxe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 3}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c钻镐'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            4 : {
                "price": 3,   # 价格
                "currency": "minecraft:gold_ingot",  
                "description": "§7全面治愈",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:golden_apple",
                    "newAuxValue": 0,
                    "count": 1  # 数量
                }
            },
            5 : {
                "price": 8,   # 价格
                "currency": "minecraft:tnt",  
                "description": "§7瞬间点燃\n适用于摧毁沿途防御工事\n\n§a§o(该物品全局可使用)§r",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:tnt",
                    "newAuxValue": 0,
                    "count": 1  # 数量
                }
            },
            6 : {
                "price": 1,   # 价格
                "currency": "minecraft:emerald",  
                "description": "§1跳跃增益(0:45)\n§e§o(该物品只能在任意方无床后都允许使用)§r",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecrafts:speed_potion",
                    "newAuxValue": 9,
                    "count": 1  # 数量
                }
            },                        

            7 : {
                "price": 24,   # 价格
                "currency": "minecraft:iron_ingot",  
                "description": "§7用于保卫床的坚固方块",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:end_stone", #snowball
                    "newAuxValue": 0,
                    "count": 12  # 数量
                }
            },                 
            8 : {
                "price": 7,   # 价格
                "currency": "minecraft:gold_ingot",  
                "description": "伤害较高的近战武器\n可快速击败你的对手",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:iron_sword",
                    "newAuxValue": 0,
                    "count": 1  # 数量
                }
            },                   
            9 : {
                "price": 12,   # 价格
                "currency": "minecraft:gold_ingot",  # 货币
                "description": "§7永久的 铁盔甲\n在重生时自动装备",  # 商品描述
                "type": "armour",  # 商品类型
                "level": 2,  # 盔甲等级
                "itemList": {  
                    (3, 2) : {
                        "newItemName": "minecraft:iron_leggings",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    },
                    (3, 3) : {
                        "newItemName": "minecraft:iron_boots",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    }
                },
                "itemDict": {  # 商品物品渲染
                    "newItemName": "minecraft:iron_boots",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            10 : {
                "type": "I0S08X",  # 商品类型，同时也是计分板名字，需要在"modConfig.py"中的"SCOREBOARD_LIST"配置
                "itemList": {  # type:dict[level:ItemDict]  # 物品列表
                    0 : {
                        "price": 10,
                        "currency": "minecraft:iron_ingot",
                        "description": "等级: §eI §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:wooden_axe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c木斧'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 10,
                        "currency": "minecraft:iron_ingot",
                        "description": "等级: §eII §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:stone_axe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c石斧'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 3,
                        "currency": "minecraft:gold_ingot",
                        "description": "等级: §eIII §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:iron_axe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c铁斧'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    3 : {
                        "price": 6,
                        "currency": "minecraft:gold_ingot",
                        "description": "等级: §eIV§c(满级) §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:diamond_axe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 3}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c钻斧'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            11 : {
                "price": 40,   # 价格
                "currency": "minecraft:iron_ingot",  
                "description": "§7右键/长按发射!\n击飞在桥上行走的敌人!\n§c§o(你不能使用此来炸毁敌方钻石)",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecrafts:fire_charge", 
                    "newAuxValue": 0,
                    "count": 1  # 数量
                }
            },
            12 : {
                "price": 2,   # 价格
                "currency": "minecraft:gold_ingot",  
                "description": "§7",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:arrow",
                    "newAuxValue": 0,
                    "count": 6  # 数量
                }
            },        
            13 : {
                "price": 1,   # 价格
                "currency": "minecraft:emerald",  
                "description": "§1速度增益(0:45)\n§e§o(该物品只能在任意方无床后都允许使用)§r",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecrafts:jumpboost_potion",
                    "newAuxValue": 0,
                    "count": 1  # 数量
                }
            }
        }
    },
    1: {  # tab_type
        "description": "§a方块\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:end_stone",  # 这个地方不知道为啥,羊毛的话如果选中没有附魔效果,但是换成其他方块选中时就有
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 : {
                "price": 4,
                "type": "wool",  # 商品类型
                "currency": "minecraft:iron_ingot",
                "description": "§7可用于搭桥穿越岛屿\n羊毛的颜色会对应你队伍的颜色",
                "itemDict": {
                    "newItemName": "minecraft:white_wool",
                    "newAuxValue": 0,
                    "count": 16
                }
            },
            1 : {
                "price": 12,
                "currency": "minecraft:iron_ingot",
                "description": "快速保护你的基地",
                "type": "clay",
                "itemDict": {
                    "newItemName": "minecraft:hardened_clay",
                    "newAuxValue": 0,
                    "count": 16
                }
            },            
            2 : {
                "price": 4,
                "currency": "minecraft:gold_ingot",
                "description": "§7用于保卫床的优质方块\n能有效抵御镐子的破坏",
                "itemDict": {
                    "newItemName": "minecraft:planks",
                    "newAuxValue": 0,
                    "count": 16
                }
            },            
            3 : {
                "price": 24,
                "currency": "minecraft:iron_ingot",
                "description": "§7用于保卫床的坚固方块",
                "itemDict": {
                    "newItemName": "minecraft:end_stone",
                    "newAuxValue": 0,
                    "count": 12
                }
            },            
            4 : {
                "price": 12,
                "currency": "minecraft:iron_ingot",
                "description": "免疫爆炸.",
                "type": "glass",
                "itemDict": {
                    "newItemName": "minecraft:glass",
                    
                    "newAuxValue": 0,
                    "count": 8
                }
            },
            5 : {
                "price": 4,
                "currency": "minecraft:iron_ingot",
                "description": "可用于救助困在树上的猫\n§a§o(该物品全局可使用)§r",
                "itemDict": {
                    "newItemName": "minecraft:ladder",
                    "newAuxValue": 0,
                    "count": 12
                }
            }           
        }
    },
    2: {  # tab_type
        "description": "§a近战武器\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:stone_sword",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 : {
                "price": 10,
                "currency": "minecraft:iron_ingot",
                "description": "伤害一般的近战武器",
                "itemDict": {
                    "newItemName": "minecraft:stone_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 7,
                "currency": "minecraft:gold_ingot",
                "description": "伤害较高的近战武器",
                "itemDict": {
                    "newItemName": "minecraft:iron_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            2 : {
                "price": 3,
                "currency": "minecraft:emerald",
                "description": "伤害极高的近战武器\n§a§o(该物品全局可使用)§r",
                "itemDict": {
                    "newItemName": "minecraft:diamond_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            3 : {
                "price": 4,
                "currency": "minecraft:gold_ingot",
                "description": "§7在伤害上,这只是根没有咖喱的棒子\n§e§o(该物品只能在任意方无床后都允许使用)§r",
                "itemDict": {
                     "newItemName": "minecraft:stick",
                     "newAuxValue": 1,
                     "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 12}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c击退棒'}}},
                     "count": 1
                    }
                }
        }
    },
    3: {  # tab_type
        "description": "§a盔甲\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:chainmail_leggings",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 : {
                "price": 35,   # 价格
                "currency": "minecraft:iron_ingot",  # 货币
                "description": "§7永久的锁链盔甲\n在重生时自动装备",  # 商品描述
                "type": "armour",  # 商品类型
                "level": 1,  # 盔甲等级
                "itemList": {  # type:dict[tuple[ItemPosType, slotPos]:ItemDict]  # 物品列表
                    (3, 2) : {
                        "newItemName": "minecraft:chainmail_leggings",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    },
                    (3, 3) : {
                        "newItemName": "minecraft:chainmail_boots",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    }
                },
                "itemDict": {  # 商品物品渲染
                    "newItemName": "minecraft:chainmail_boots",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 12,   # 价格
                "currency": "minecraft:gold_ingot",  # 货币
                "description": "§7永久的铁盔甲\n在重生时自动装备",  # 商品描述
                "type": "armour",  # 商品类型
                "level": 2,  # 盔甲等级
                "itemList": {  
                    (3, 2) : {
                        "newItemName": "minecraft:iron_leggings",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    },
                    (3, 3) : {
                        "newItemName": "minecraft:iron_boots",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    }
                },
                "itemDict": {  # 商品物品渲染
                    "newItemName": "minecraft:iron_boots",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            2 : {
                "price": 6,
                "currency": "minecraft:emerald",
                "description": "§7永久的钻石盔甲\n在重生时自动装备\n§a§o(该物品全局可使用)§r",
                "type": "armour",  
                "level": 3,
                "itemList": {
                    (3, 2) : {
                        "newItemName": "minecraft:diamond_leggings",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    },
                    (3, 3) : {
                        "newItemName": "minecraft:diamond_boots",
                        "newAuxValue": 0,
                        "count": 1,
                        "userData": userData
                    }
                },
                "itemDict": {  
                    "newItemName": "minecraft:diamond_boots",
                    "newAuxValue": 0,
                    "count": 1
                }
            }          
        }
    },
    4: {  # tab_type
        "description": "§a工具\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:stone_pickaxe",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 : {
                "type": "X2C07R",  # 商品类型，同时也是计分板名字，需要在"modConfig.py"中的"SCOREBOARD_LIST"配置
                "itemList": {  # type:dict[level:ItemDict]  # 物品列表
                    0 : {
                        "price": 10,
                        "currency": "minecraft:iron_ingot",
                        "description": "等级: §eI §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:wooden_pickaxe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c木镐'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 10,
                        "currency": "minecraft:iron_ingot",
                        "description": "等级: §eII §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:stone_pickaxe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c石镐'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 3,
                        "currency": "minecraft:gold_ingot",
                        "description": "等级: §eIII §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:iron_pickaxe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c铁镐'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    3 : {
                        "price": 6,
                        "currency": "minecraft:gold_ingot",
                        "description": "等级: §eIV§c(满级) §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:diamond_pickaxe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 3}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c钻镐'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            1 : {
                "type": "I0S08X",  # 商品类型，同时也是计分板名字，需要在"modConfig.py"中的"SCOREBOARD_LIST"配置
                "itemList": {  # type:dict[level:ItemDict]  # 物品列表
                    0 : {
                        "price": 10,
                        "currency": "minecraft:iron_ingot",
                        "description": "等级: §eI §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:wooden_axe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c木斧'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 10,
                        "currency": "minecraft:iron_ingot",
                        "description": "等级: §eII §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:stone_axe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c石斧'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 3,
                        "currency": "minecraft:gold_ingot",
                        "description": "等级: §eIII §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:iron_axe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c铁斧'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    3 : {
                        "price": 6,
                        "currency": "minecraft:gold_ingot",
                        "description": "等级: §eIV§c (满级) §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
                        "itemDict": {
                            "newItemName": "minecraft:diamond_axe",
                            "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 3}, 'id': {'__type__': 2, '__value__': 15}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c钻斧'}}},
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            2 : {
                "price": 20, 
                "currency": "minecraft:iron_ingot", #自定义物品
                "description": "用于快速破坏羊毛,每次重生时会获得剪刀",
                "itemDict": {
                    "newItemName": "minecrafts:shears",
                    "newAuxValue": 0,
                    "count": 1
                }
            }
        }
    },
    5: {  # tab_type
        "description": "§a远程武器\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:bow",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 : {
                "price": 12,
                "currency": "minecraft:gold_ingot",
                "description": "基础的远程武器.\n§e(只能在无床后使用)",
                "itemDict": {
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 24,   # 价格
                "currency": "minecraft:gold_ingot",  
                "description": "§7力量Ⅰ附魔弓\n进阶的远程武器§e\n(只能在无床后使用)§r",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 19}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c力量弓'}}},
                    "count": 1  # 数量
                }
            },
            2 : {
                "price": 2,   # 价格
                "currency": "minecraft:gold_ingot",  
                "description": "§7补充弹药",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:arrow",
                    "newAuxValue": 0,
                    "count": 6  # 数量
                }
            },
        }
    },
    6: {  # tab_type
        "description": "§a酿造\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:brewing_stand",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 : {
                "price": 1,
                "currency": "minecraft:emerald",
                "description": "§1速度增益(0:45)",
                "itemDict": {
                    "newItemName": "minecrafts:speed_potion",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 1,
                "currency": "minecraft:emerald",
                "description": "§1跳跃增益(0:45)\n§e§o(该物品只能在任意方无床后都允许使用)§r",
                "itemDict": {
                    "newItemName": "minecrafts:jumpboost_potion",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            2 : {
                "price": 2,
                "currency": "minecraft:emerald",
                "description": "§1完全隐身(0:30)\n§a§o(在绿宝石二级或有床被破坏后使用\n每个队仅限一个玩家同时使用)§r",
                "itemDict": {
                    "newItemName": "minecrafts:invisibility_potion",
                    "newAuxValue": 0,
                    "count": 1
                }
            }
        }
    },
    7: {  
        "description": "§a实用道具\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:tnt",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            1 : {
                "price": 3,
                "currency": "minecraft:gold_ingot",
                "description": "§7全面治愈.",
                "itemDict": {
                    "newItemName": "minecraft:golden_apple",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            2 : {
                "price": 40,
                "currency": "minecraft:iron_ingot",
                "description": "§7右键或长按发射!\n击飞在桥上行走的敌人!\n§c§o(你不能使用此来炸毁敌方钻石)§r",
                "itemDict": {
                    "newItemName": "minecrafts:fire_charge",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            3 : {
                "price": 8,
                "currency": "minecraft:gold_ingot",
                "description": "瞬间点燃\n适用于摧毁沿途防御工事\n§a§o(该物品全局可使用)§r",
                "itemDict": {
                    "newItemName": "minecraft:tnt",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            4 : {
                "price": 1,
                "currency": "minecraft:emerald",
                "description": "掷出后在路径上快速生成一座桥\n颜色与你的队伍相适配\n§e§o(该物品只能在任意方无床后都允许使用)§r",
                "itemDict": {
                    "newItemName": "minecraft:egg",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            5 : {
                "price": 6,
                "currency": "minecraft:gold_ingot",
                "description": "我曾经放了一片海\n§e§o(该物品只能在任意方无床后都允许使用)§r",
                "itemDict": {
                    "newItemName": "minecraft:water_bucket",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            6 : {
                "price": 4,
                "currency": "minecraft:emerald",
                "description": "快速入侵敌方基地\n§e§o(该物品只能在任意方无床后都允许使用)§r",
                "itemDict": {
                    "newItemName": "minecraft:ender_pearl",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            7 : {
                "price": 6,
                "currency": "minecraft:gold_ingot",
                "description": "吸收水分",
                "itemDict": {
                    "newItemName": "minecraft:sponge",
                    "newAuxValue": 0,
                    "count": 4
                }
            }
        }
    }
} #all end line