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
                "price": 1,   
                "type": "wool",
                "currency": "experience",
                "description": "§7极适合用来跨越岛屿\n§7其颜色取决于你的队伍",  
                "itemDict": {  
                    "newItemName": "minecraft:white_wool",
                    "newAuxValue": 0,
                    "count": 16  
                }
            },
            1 : {
                "price": 1,   
                "currency": "experience",  
                "description": "伤害一般的近战武器\n适用于快速战斗情形",  
                "itemDict": {  
                    "newItemName": "minecraft:stone_sword",
                    "newAuxValue": 0,
                    "count": 1  
                }
            },            
            2 : {
                "price": 1,   
                "currency": "experience",  
                "description": "§7永久的 锁链盔甲",  
                "type": "armour",
                "level": 1,
                "itemList": {  
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
                "itemDict": {
                    "newItemName": "minecraft:chainmail_boots",
                    "newAuxValue": 0,
                    "count": 1
                }
            },

            3 : {
                "price": 1,
                "currency": "experience",  
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:diamond_pickaxe",
                    "newAuxValue": 0,
                    "count": 1
                }
            },


            4 : {
                "price": 1,   
                "currency": "experience",  
                "description": "§7全面治愈",
                "itemDict": {
                    "newItemName": "minecraft:golden_apple",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            5 : {
                "price": 1,   
                "currency": "experience",  
                "description": "§7基础的远程武器",  
                "itemDict": {  
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "count": 1  
                }
            },
            6 : {
                "price": 1,   
                "currency": "experience",  
                "description": "§1跳跃增益(0:45)",  
                "itemDict": {  
                    "newItemName": "minecrafts:speed_potion",
                    "newAuxValue": 9,
                    "count": 1  
                }
            },

            7 : {
                "price": 1,   
                "currency": "experience",  
                "description": "§7用于保卫床的坚固方块",  
                "itemDict": {  
                    "newItemName": "minecraft:end_stone", 
                    "newAuxValue": 0,
                    "count": 12  
                }
            },
            8 : {
                "price": 1,   
                "currency": "experience",  
                "description": "",  
                "itemDict": {  
                    "newItemName": "minecraft:iron_sword",
                    "newAuxValue": 0,
                    "count": 1  
                }
            },                   
            9 : {
                "price": 1,   
                "currency": "experience",  
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
                "price": 1,   
                "currency": "experience",  
                "description": "",  
                "itemDict": {  
                    "newItemName": "minecraft:diamond_axe", 
                    "newAuxValue": 0,
                    "count": 1  
                }
            },
            11 : {
                "price": 1,   
                "currency": "experience",  
                "description": "§7右键/长按发射!\n击飞在桥上行走的敌人!",  
                "itemDict": {  
                    "newItemName": "minecrafts:fire_charge", 
                    "newAuxValue": 0,
                    "count": 1  
                }
            },
            12 : {
                "price": 1,   
                "currency": "experience",  
                "description": "",  
                "itemDict": {  
                    "newItemName": "minecraft:arrow",
                    "newAuxValue": 0,
                    "count": 6  
                }
            },        
            13 : {
                "price": 1,   
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
            "newItemName": "minecraft:end_stone",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 : {
                "price": 1,
                "type": "wool",
                "currency": "experience",
                "description": "§7可用于搭桥穿越岛屿\n羊毛的颜色会对应你队伍的颜色",
                "itemDict": {
                    "newItemName": "minecraft:white_wool",
                    "newAuxValue": 0,
                    "count": 16
                }
            },
            1 : {
                "price": 1,
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
                "price": 1,
                "currency": "experience",
                "description": "§7用于保卫床的优质方块\n能有效抵御镐子的破坏",
                "itemDict": {
                    "newItemName": "minecraft:planks",
                    "newAuxValue": 0,
                    "count": 16
                }
            },            
            3 : {
                "price": 1,
                "currency": "experience",
                "description": "§7用于保卫床的坚固方块",
                "itemDict": {
                    "newItemName": "minecraft:end_stone",
                    "newAuxValue": 0,
                    "count": 12
                }
            },            
            4 : {
                "price": 1,
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
                "price": 1,
                "currency": "experience",
                "description": "守卫床的最坚固的方块",
                "itemDict": {
                    "newItemName": "minecraft:obsidian",
                    "newAuxValue": 0,
                    "count": 4
                }
            },           
            6 : {
                "price": 1,
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
    2: {
        "description": "§a近战武器\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:stone_sword",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 : {
                "price": 1,
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:stone_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 1,
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:iron_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            2 : {
                "price": 1,
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:diamond_sword",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            3 : {
                "price": 1,
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
            4 : {
                "price": 1,
                "currency": "experience",
                "description": "§7愿者上钩",
                "itemDict": {
                     "newItemName": "minecraft:fishing_rod",
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
                "price": 1,   
                "currency": "experience",
                "description": "§7永久的锁链盔甲\n在重生时自动装备",  
                "type": "armour",  # 商品类型
                "level": 1,
                "itemList": {
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
                "itemDict": {
                    "newItemName": "minecraft:chainmail_boots",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 1,   
                "currency": "experience",  
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
                "price": 1,   
                "currency": "experience",  
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
                "price": 1, 
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:stone_pickaxe",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 1, 
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:iron_pickaxe",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            2 : {
                "price": 1, 
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:diamond_pickaxe",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            3 : {
                "price": 1, 
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:stone_axe",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            4 : {
                "price": 1, 
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:iron_axe",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            5 : {
                "price": 1, 
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:diamond_axe",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            6 : {
                "price": 30, 
                "currency": "experience", #自定义物品
                "description": "用于快速破坏羊毛,每次重生时会获得剪刀",
                "itemDict": {
                    "newItemName": "minecraft:shears",
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
                "price": 1,
                "currency": "experience",
                "description": "",
                "itemDict": {
                    "newItemName": "minecraft:bow",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 1,   
                "currency": "experience",  
                "description": "§7力量I附魔弓\n进阶的远程武器",  
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
                "price": 1,
                "currency": "experience",
                "description": "§7力量I冲击I附魔弓\n高等级的远程武器",
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
                "price": 1,
                "currency": "experience",
                "description": "§1速度增益(0:45)",
                "itemDict": {
                    "newItemName": "minecrafts:speed_potion",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            1 : {
                "price": 1,
                "currency": "experience",
                "description": "§1跳跃增益(0:45)",
                "itemDict": {
                    "newItemName": "minecrafts:jumpboost_potion",
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
                "price": 1,
                "currency": "experience",
                "description": "§7全面治愈.",
                "itemDict": {
                    "newItemName": "minecraft:golden_apple",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            2 : {
                "price": 1,
                "currency": "experience",
                "description": "§7右键或长按发射!\n击飞在桥上行走的敌人!",
                "itemDict": {
                    "newItemName": "minecrafts:fire_charge",
                    "newAuxValue": 0,
                    "count": 1
                }
            },            
            3 : {
                "price": 1,
                "currency": "experience",
                "description": "§7铁傀儡能守护你的基地",
                "itemDict": {
                    "newItemName": "minecraft:spawn_egg",
                    "newAuxValue": 20,
                    "count": 1
                }
            },         
            4 : {
                "price": 1,
                "currency": "experience",
                "description": "§7干扰你的对手",
                "itemDict": {
                    "newItemName": "minecraft:snowball",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            5 : {
                "price": 1,
                "currency": "experience",
                "description": "瞬间点燃\n适用于摧毁沿途防御工事",
                "itemDict": {
                    "newItemName": "minecraft:tnt",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            6 : {
                "price": 1,
                "currency": "experience",
                "description": "掷出后在路径上快速生成一座桥\n颜色与你的队伍相适配",
                "itemDict": {
                    "newItemName": "minecraft:egg",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            7 : {
                "price": 1,
                "currency": "experience",
                "description": "饮用后获得三十秒防陷阱能力",
                "itemDict": {
                    "newItemName": "minecraft:milk_bucket",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            8 : {
                "price": 1,
                "currency": "experience",
                "description": "让火焰烧的更大些",
                "itemDict": {
                    "newItemName": "minecraft:flint_and_steel",
                    "newAuxValue": 0,
                    "count": 4
                }
            },
            9 : {
                "price": 1, 
                "currency": "experience",
                "description": "建造一个可速建的防御塔\n建造的颜色与你的队伍相适配",
                "itemDict": {
                    "newItemName": "minecraft:trapped_chest",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            10 : {
                "price": 1,
                "currency": "experience",
                "description": "§7右键或长按使用\n在坠落时生成一个平台垫底!",
                "itemDict": {
                    "newItemName": "minecraft:experience_bottle",
                    "newAuxValue": 0,
                    "count": 1
                }
            }, 
            11 : {
                "price": 1,
                "currency": "experience",
                "description": "造成范围小范围爆炸击退和伤害\n新时代的更实惠选择",
                "itemDict": {
                    "newItemName": "minecraft:wind_charge",
                    "newAuxValue": 0,
                    "count": 1
                }
            },
            12 : {
                "price": 1,
                "currency": "experience",
                "description": "§7丢出使用\n生成一个爆炸垂直上升",
                "itemDict": {
                    "newItemName": "minecraft:feather",
                    "newAuxValue": 0,
                    "count": 1
                }
            }
        }
    }
}