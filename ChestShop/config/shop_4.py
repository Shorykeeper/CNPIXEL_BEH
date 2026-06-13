# coding=utf-8 xp
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
                "price": 8,
                "type": "wool",  # 商品类型
                "currency": "experience",  # 货币,中文在modConfig.py中的"CURRENCY_ENUM"配置
                "description": "§7极适合用来跨越岛屿\n§7其颜色取决于你的队伍",
                "itemDict": {
                    "newItemName": "minecraft:white_wool",
                    "newAuxValue": 0,
                    "count": 16
                }
            },
            1 : {
                "price": 45,
                "currency": "experience",  
                "description": "伤害一般的近战武器\n适用于快速战斗情形",
                "itemDict": {
                    "newItemName": "minecraft:stone_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            2 : {
                "price": 120,
                "currency": "experience",  # 货币
                "description": "§7永久的 锁链盔甲",
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
                        "price": 20,
                        "currency": "experience",
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
                        "price": 30,
                        "currency": "experience",
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
                        "price": 50,
                        "currency": "experience",
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
                        "price": 90,
                        "currency": "experience",
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
            4 : {
                "price": 52,
                "currency": "experience",  
                "description": "§7全面治愈",
                "itemDict": {
                    "newItemName": "minecraft:golden_apple",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            5 : {
                "price": 120,
                "currency": "experience",  
                "description": "§7基础的远程武器",
                "itemDict": {
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            6 : {
                "price": 320,
                "currency": "experience",  
                "description": "§1跳跃增益(0:45)",
                "itemDict": {
                    "newItemName": "minecrafts:speed_potion",
                    "newAuxValue": 9,
                    "count": 1
                }
            },

            7 : {
                "price": 45,
                "currency": "experience",  
                "description": "§7用于保卫床的坚固方块",
                "itemDict": {
                    "newItemName": "minecraft:end_stone", #snowball
                    "newAuxValue": 0,
                    "count": 12
                }
            },
            8 : {
                "price": 220,
                "currency": "experience",  
                "description": "伤害较高的近战武器\n可快速击败你的对手",
                "itemDict": {
                    "newItemName": "minecraft:iron_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },                   
            9 : {
                "price": 420,
                "currency": "experience",  # 货币
                "description": "§7永久的 铁盔甲\n在重生时自动装备",
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
                        "price": 20,
                        "currency": "experience",
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
                        "price": 30,
                        "currency": "experience",
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
                        "price": 60,
                        "currency": "experience",
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
                        "price": 100,
                        "currency": "experience",
                        "description": "等级: §eIII (满级) §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
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
                "price": 64,
                "currency": "experience",  
                "description": "§7右键或长按发射!\n击飞在桥上行走的敌人!",
                "itemDict": {
                    "newItemName": "minecrafts:fire_charge", 
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            12 : {
                "price": 20,
                "currency": "experience",  
                "description": "§7补充弹药\n如果要当一名弓猫,那至少两组起步",
                "itemDict": {
                    "newItemName": "minecraft:arrow",
                    "newAuxValue": 0,
                    "count": 6
                }
            },        
            13 : {
                "price": 320,
                "currency": "experience",  
                "description": "§1速度增益(0:45)",
                "itemDict": {
                    "newItemName": "minecrafts:jumpboost_potion",
                    "newAuxValue": 0,
                    "count": 1
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
                "price": 8,
                "type": "wool",  # 商品类型
                "currency": "experience",
                "description": "§7可用于搭桥穿越岛屿\n羊毛的颜色会对应你队伍的颜色",
                "itemDict": {
                    "newItemName": "minecraft:white_wool",
                    "newAuxValue": 0,
                    "count": 16
                }
            },
            1 : {
                "price": 12,
                "currency": "experience",
                "description": "快速保护你的基地",
                "type": "clay",
                "itemDict": {
                    "newItemName": "minecraft:hardened_clay",
                    "newAuxValue": 0,
                    "count": 16
                }
            },            
            2 : {
                "price": 35,
                "currency": "experience",
                "description": "§7用于保卫床的优质方块\n能有效抵御镐子的破坏",
                "itemDict": {
                    "newItemName": "minecraft:planks",
                    "newAuxValue": 0,
                    "count": 16
                }
            },            
            3 : {
                "price": 35,
                "currency": "experience",
                "description": "§7用于保卫床的坚固方块",
                "itemDict": {
                    "newItemName": "minecraft:end_stone",
                    "newAuxValue": 0,
                    "count": 12
                }
            },            
            4 : {
                "price": 12,
                "currency": "experience",
                "description": "免疫爆炸.",
                "type": "glass",
                "itemDict": {
                    "newItemName": "minecraft:glass",
                    "newAuxValue": 0,
                    "count": 8
                }
            },
            5 : {
                "price": 750,
                "currency": "experience",
                "description": "守卫床的最坚固的方块",
                "itemDict": {
                    "newItemName": "minecraft:obsidian",
                    "newAuxValue": 0,
                    "count": 4
                }
            },           
            6 : {
                "price": 30,
                "currency": "experience",
                "description": "可用于救助困在树上的猫",
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
                "price": 45,
                "currency": "experience",
                "description": "伤害一般的近战武器",
                "itemDict": {
                    "newItemName": "minecraft:stone_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 220,
                "currency": "experience",
                "description": "伤害较高的近战武器",
                "itemDict": {
                    "newItemName": "minecraft:iron_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            2 : {
                "price": 450,
                "currency": "experience",
                "description": "伤害极高的近战武器",
                "itemDict": {
                    "newItemName": "minecraft:diamond_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            3 : {
                "price": 520,
                "currency": "experience",
                "description": "聚以天上繁星之吐息,辉煌生命之奔流\n接下吧! (请输入文本)",
                "itemDict": {
                    "newItemName": "minecraft:golden_sword",
                    "newAuxValue": 0,
                    "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 4}, 'id': {'__type__': 2, '__value__': 9}},{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 28}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§bEX Calibur'}}},
                    "count": 1
                }
            },
            4 : {
                "price": 1,
                "currency": "experience",
                "description": "一把神奇的短剑,留存有些许萤火的微芒\n旧日的萤火已经散去,须臾的生命周期彻底告罄前要做点什么事情.\n§o§8「在梦想融汇之地,以三死向命运知会我存续的意义」§r",
                "itemDict": {
                    "newItemName": "minecrafts:firefly_sword",
                    "newAuxValue": 0,
                    "userData": {
                             'display': {'Name': {'__type__': 8, '__value__': '§s§l萤火§n末光'}}},
                    "count": 1
                }
            },
            5 : {
                "price": 288,
                "currency": "experience",
                "description": "一把??的短剑,由带着些许腥涩的梦泡铸成\n§o§8「死亡贯穿胸膛之刻,痛苦与决绝又湮没了其对何人的愧疚?」§r",
                "itemDict": {
                    "newItemName": "minecrafts:firefly_deathblood_sword",
                    "userData": {'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 12}},{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 13}}]},
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            6 : {
                "price": 75,
                "currency": "experience",
                "description": "§7在伤害上,这只是根没有咖喱的棒子\n但是对于多快好省的投机...",
                "itemDict": {
                     "newItemName": "minecraft:stick",
                     "newAuxValue": 1,
                     "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 2}, 'id': {'__type__': 2, '__value__': 12}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c击退棒'}}},
                     "count": 1
                    }
                },
            7 : {
                "price": 38,
                "currency": "experience",
                "description": "§7愿者上钩",
                "itemDict": {
                     "newItemName": "minecraft:fishing_rod",
                     "newAuxValue": 1,
                     "count": 1
                    }
                },
            8 : {
                "price": 452,
                "currency": "experience",
                "description": "§7来自沙漠的普通的铁剑\n只是能多造成一点击退,凝固着名为辉煌时代的曾经\n§o§f(但是有这闲钱为啥不选择高爆咖喱棒呢?)",
                "itemDict": {
                     "newItemName": "minecraft:iron_sword",
                      "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 12}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§6沙漠铁剑§7(击退I)'}}},
                     "newAuxValue": 1,
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
                "price": 120,
                "currency": "experience",  # 货币
                "description": "§7永久的锁链盔甲\n在重生时自动装备",
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
                "price": 420,
                "currency": "experience",  # 货币
                "description": "§7永久的铁盔甲\n在重生时自动装备",
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
                "price": 880,
                "currency": "experience",  # 货币
                "description": "§7永久的钻石盔甲\n在重生时自动装备",
                "type": "armour",  
                "level": 3,  # 盔甲等级
                "itemList": {  # type:dict[tuple[ItemPosType, slotPos]:ItemDict]  # 物品列表
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
                        "price": 20,
                        "currency": "experience",
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
                        "price": 30,
                        "currency": "experience",
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
                        "price": 50,
                        "currency": "experience",
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
                        "price": 90,
                        "currency": "experience",
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
                        "price": 20,
                        "currency": "experience",
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
                        "price": 30,
                        "currency": "experience",
                        "description": "等级: §eI-II §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
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
                        "price": 60,
                        "currency": "experience",
                        "description": "等级: §eII-III §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
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
                        "price": 100,
                        "currency": "experience",
                        "description": "等级: §eIII-§cIV (满级) §7\n\n该道具可升级.\n死亡将会导致损失一级!\n\n每次重生时,至少为最低等级.",
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
                "price": 30, 
                "currency": "experience",
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
                "price": 125,
                "currency": "experience",
                "description": "基础的远程武器",
                "itemDict": {
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 245,
                "currency": "experience",  
                "description": "§7力量Ⅰ附魔弓\n进阶的远程武器",
                "itemDict": {
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 19}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c力量弓'}}},
                    "count": 1
                }
            },
            2 : {
                "price": 725,
                "currency": "experience",
                "description": "§7力量Ⅰ冲击Ⅰ附魔弓\n高等级的远程武器,解决对手能出家门的BUG",
                "itemDict": {
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 19}},{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 20}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§c冲击力量弓'}}},
                    "count": 1
                }
            },
            3 : {
                "price": 1200,
                "currency": "experience",
                "description": "§7力量Ⅰ冲击Ⅰ火矢附魔弓\n半神之弓,要从那个被称为弓无罪的无名客说起",
                "itemDict": {
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "userData": {
                             'ench': [{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 19}},{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 21}},{'lvl': {'__type__': 2, '__value__': 1}, 'id': {'__type__': 2, '__value__': 20}}],
                             'display': {'Name': {'__type__': 8, '__value__': '§r§e弓无罪#§c冲击力量火弓'}}},
                    "count": 1
                }
            },
            4 : {
                "price": 20,
                "currency": "experience",
                "description": "§7补充弹药",
                "itemDict": {
                    "newItemName": "minecraft:arrow",
                    "newAuxValue": 0,
                    "count": 6
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
                "price": 320,
                "currency": "experience",
                "description": "§1速度增益(0:45)",
                "itemDict": {
                    "newItemName": "minecrafts:speed_potion",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 320,
                "currency": "experience",
                "description": "§1跳跃增益(0:45)",
                "itemDict": {
                    "newItemName": "minecrafts:jumpboost_potion",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            2 : {
                "price": 560,
                "currency": "experience",
                "description": "§1完全隐身(0:30)",
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
                "price": 52,
                "currency": "experience",
                "description": "§7全面治愈.",
                "itemDict": {
                    "newItemName": "minecraft:golden_apple",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            2 : {
                "price": 64,
                "currency": "experience",
                "description": "§7右键或长按发射!\n击飞在桥上行走的敌人!",
                "itemDict": {
                    "newItemName": "minecrafts:fire_charge",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            3 : {
                "price": 620,
                "currency": "experience",
                "description": "§7铁傀儡能守护你的基地",
                "itemDict": {
                    "newItemName": "minecraft:spawn_egg",
                    "newAuxValue": 20,
                    "count": 1
                }
            },         
            4 : {
                "price": 180,
                "currency": "experience",
                "description": "§7干扰你的对手",
                "itemDict": {
                    "newItemName": "minecraft:snowball",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            5 : {
                "price": 160,
                "currency": "experience",
                "description": "瞬间点燃\n适用于摧毁沿途防御工事",
                "itemDict": {
                    "newItemName": "minecraft:tnt",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            6 : {
                "price": 535, #疾速是2
                "currency": "experience",
                "description": "§7快速入侵敌方基地",
                "itemDict": {
                    "newItemName": "minecraft:ender_pearl",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            7 : {
                "price": 60,
                "currency": "experience",
                "description": "很好的降低来犯之敌的速度\n水满溢时井亦镜，缘散尽时情已清",
                "itemDict": {
                    "newItemName": "minecraft:water_bucket",
                    "newAuxValue": 0,
                    "count": 1
                }
            },                     
            8 : {
                "price": 200,
                "currency": "experience",
                "description": "掷出后在路径上快速生成一座桥\n颜色与你的队伍相适配",
                "itemDict": {
                    "newItemName": "minecraft:egg",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            9 : {
                "price": 55, #ec50
                "currency": "experience",
                "description": "饮用后获得三十秒防陷阱能力",
                "itemDict": {
                    "newItemName": "minecraft:milk_bucket",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            10 : {
                "price": 60,
                "currency": "experience",
                "description": "吸收水分",
                "itemDict": {
                    "newItemName": "minecraft:sponge",
                    "newAuxValue": 0,
                    "count": 4
                }
            },
            11 : {
                "price": 45,
                "currency": "experience",
                "description": "建造一个可速建的防御塔\n建造的颜色与你的队伍相适配",
                "itemDict": {
                    "newItemName": "minecraft:trapped_chest",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            12 : {
                "price": 200,
                "currency": "experience",
                "description": "§7右键或长按使用\n在坠落时生成一个平台垫底!",
                "itemDict": {
                    "newItemName": "minecraft:experience_bottle",
                    "newAuxValue": 0,
                    "count": 1
                }
            }, 
            13 : {
                "price": 45,
                "currency": "experience",
                "description": "造成范围小范围爆炸击退和伤害\n新版本的实惠选择",
                "itemDict": {
                    "newItemName": "minecraft:wind_charge",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            14 : {
                "price": 256,
                "currency": "experience",
                "description": "带着淡淡的海盐味的一份礼物\n也许使用后会有很大的益处\n§o§t「你就像黑夜,拥有寂静与群星」§r",
                "itemDict": {
                    "newItemName": "minecrafts:shorykeeper",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            15 : {
                "price": 1,
                "currency": "experience",
                "description": "§7将经验转换为实体资源,以安全存储",
                "itemDict": {
                    "newItemName": "minecraft:iron_ingot",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            16 : {
                "price": 10,
                "currency": "experience",
                "description": "§7将经验转换为实体资源,以安全存储",
                "itemDict": {
                    "newItemName": "minecraft:gold_ingot",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            17 : {
                "price": 80,
                "currency": "experience",
                "description": "§7将经验转换为实体资源,以安全存储",
                "itemDict": {
                    "newItemName": "minecraft:diamond",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            18 : {
                "price": 150,
                "currency": "experience",
                "description": "§7将经验转换为实体资源,以安全存储",
                "itemDict": {
                    "newItemName": "minecraft:emerald",
                    "newAuxValue": 0,
                    "count": 1
                }
            }
        }
    }
}