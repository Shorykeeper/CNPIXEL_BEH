# coding=utf-8 团队商店
GOODS_DATA = { #["X5T99R", "C1T28Q","A1B23C","Z3K56L","Q7M04P","Y9V88N"]
    0 : {          #急迫 保护 锋利 龙 治愈池 铁锻炉
        "description": "§a团队升级\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:beacon",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 :{
                "type": "enchant_item",
                "title": "§e锋利增益",
                "enchantType": "A1B23C",
                "itemList": {  # type:dict[level:ItemDict]  # 物品列表
                    0 : {
                        "price": 8,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员的剑和斧将永久获得锋利I附魔\n\n§71级: 锋利Ⅰ §b8 钻石\n§72级: 锋利ⅠⅠ §b20 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_sword",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 20,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员的剑和斧将永久获得锋利II附魔\n\n§a1级: 锋利Ⅰ §b8 钻石\n§72级: 锋利ⅠⅠ §b20 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_sword",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 999,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员的剑和斧将永久获得锋利II附魔\n\n§a1级: 锋利Ⅰ §b8 钻石\n§a2级: 锋利ⅠⅠ §b20 钻石\n\n§e该增益已满级!§r",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_sword",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            1 :{
                "type": "enchant_item",
                "title": "§e盔甲强化",
                "enchantType": "C1T28Q",
                "itemList": {  
                    0 : {
                        "price": 5,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§71级: 保护Ⅰ §b5 钻石\n§72级: 保护ⅠⅠ §b10 钻石\n§73级: 保护ⅠⅠⅠ §b20 钻石\n§74级: 保护ⅠⅤ §b30 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_chestplate",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 10,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§a1级: 保护Ⅰ §b5 钻石\n§72级: 保护ⅠⅠ §b10 钻石\n§73级: 保护ⅠⅠⅠ §b20 钻石\n§74级: 保护ⅠⅤ §b30 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_chestplate",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 20,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§a1级: 保护Ⅰ §b5 钻石\n§a2级: 保护ⅠⅠ §b10 钻石\n§73级: 保护ⅠⅠⅠ §b20 钻石\n§74级: 保护ⅠⅤ §b30 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_chestplate",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    3 : {
                        "price": 30,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§a1级: 保护Ⅰ §b5 钻石\n§a2级: 保护ⅠⅠ §b10 钻石\n§a3级: 保护ⅠⅠⅠ §b20 钻石\n§74级: 保护ⅠⅤ §b30 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_chestplate",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    4 : {
                        "price": 999,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§a1级: 保护Ⅰ §b5 钻石\n§a2级: 保护ⅠⅠ §b10 钻石\n§a3级: 保护ⅠⅠⅠ §b20 钻石\n§a4级: 保护ⅠⅤ §b30 钻石\n\n§e该增益已满级!§r",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_chestplate",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            2 :{
                "type": "enchant_item",
                "title": "§e疯狂矿工",
                "enchantType": "X5T99R",
                "itemList": {  
                    0 : {
                        "price": 4,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员获得永久急迫效果\n\n§71级: 急迫Ⅰ §b4 钻石\n§72级: 急迫ⅠⅠ §b6 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:golden_pickaxe",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 6,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员获得永久急迫效果\n\n§a1级: 急迫Ⅰ §b4 钻石\n§72级: 急迫ⅠⅠ §b6 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:golden_pickaxe",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 999,
                        "currency": "minecraft:diamond",
                        "description": "己方所有成员获得永久急迫效果\n\n§a1级: 急迫Ⅰ §b4 钻石\n§a2级: 急迫ⅠⅠ §b6 钻石\n\n§e该增益已满级!§r",
                        "itemDict": {
                            "newItemName": "minecrafts:golden_pickaxe",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },


            3 :{
                "type": "enchant_item",
                "title": "§e治愈池",
                "enchantType": "Q7M04P",
                "itemList": {  # type:dict[level:ItemDict]  # 物品列表
                    0 : {
                        "price": 3,
                        "currency": "minecraft:diamond",
                        "description": "基地附近的队伍成员将获得生命恢复效果!\n\n§7花费: §b3 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:beacon",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 999,
                        "currency": "minecraft:diamond",
                        "description": "基地附近的队伍成员将获得生命恢复效果!\n\n§a花费: §b3 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:beacon",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },


            4 :{
                "type": "enchant_item",
                "title": "§e末影龙增益",
                "enchantType": "Z3K56L",
                "itemList": {
                    0 : {
                        "price": 5,
                        "currency": "minecraft:diamond",
                        "description": "你的队伍在死亡竞赛中将会有两条末影龙而非一条!\n\n§7花费: §b5 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:dragon_egg",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 999,
                        "currency": "minecraft:diamond",
                        "description": "你的队伍在死亡竞赛中将会有两条末影龙而非一条!\n\n§a花费: §b5 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:dragon_egg",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            }, 

            5 :{
                "type": "enchant_item",
                "title": "§e缓冲靴子",
                "enchantType": "C5H77S",
                "itemList": {  
                    0 : {
                        "price": 2,
                        "currency": "minecraft:diamond",
                        "description": "§7己方成员的靴子获得永久摔落缓冲\n\n§71级: 摔落缓冲Ⅰ §b2 钻石\n§72级: 摔落缓冲ⅠⅠ §b4 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:diamond_boots",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 4,
                        "currency": "minecraft:diamond",
                        "description": "§7己方成员的靴子获得永久摔落缓冲\n\n§a1级: 摔落缓冲Ⅰ §b2 钻石\n§72级: 摔落缓冲ⅠⅠ §b4 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:diamond_boots",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 999,
                        "currency": "minecraft:diamond",
                        "description": "§7己方成员的靴子获得永久摔落缓冲\n\n§a1级: 摔落缓冲Ⅰ §b2 钻石\n§a2级: 摔落缓冲ⅠⅠ §b4 钻石\n\n§e该增益已满级!§r",
                        "itemDict": {
                            "newItemName": "minecrafts:diamond_boots",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            }
        }
    },
    1 : { #陷阱
        "description": "§a团队陷阱\n§e点击查看!",
        "itemDict": {
            "newItemName": "minecraft:string",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {
            0 :{
                "type": "enchant_item",
                "title": "§e这是个陷阱!",
                "enchantType": "G6Y81U",
                "itemList": {
                    0 : {
                        "price": 1,
                        "currency": "minecraft:diamond",
                        "description": "造成失明和缓慢效果,持续8秒\n\n§7花费: §b1 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:tripwire_hook",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 3,
                        "currency": "minecraft:diamond",
                        "description": "造成失明和缓慢效果,持续8秒\n\n§7花费: §b3 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:tripwire_hook",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 6,
                        "currency": "minecraft:diamond",
                        "description": "造成失明和缓慢效果,持续8秒\n\n§7花费: §b6 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:tripwire_hook",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            1 :{
                "type": "enchant_item",
                "title": "§e反击陷阱",
                "enchantType": "P4J90M",
                "itemList": {  
                    0 : {
                        "price": 1,
                        "currency": "minecraft:diamond",
                        "description": "我方成员获得速度和跳跃效果,持续8秒\n\n§7花费: §b1 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:feather",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 3,
                        "currency": "minecraft:diamond",
                        "description": "我方成员获得速度和跳跃效果,持续8秒\n\n§7花费: §b3 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:feather",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 6,
                        "currency": "minecraft:diamond",
                        "description": "我方成员获得速度和跳跃效果,持续8秒\n\n§7花费: §b6 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:feather",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            2 :{
                "type": "enchant_item",
                "title": "§e报警陷阱",
                "enchantType": "E3Q28N",
                "itemList": {  
                    0 : {
                        "price": 1,
                        "currency": "minecraft:diamond",
                        "description": "使隐身的敌人显形\n\n§7花费: §b1 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:redstone_torch",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 3,
                        "currency": "minecraft:diamond",
                        "description": "使隐身的敌人显形\n\n§7花费: §b3 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:redstone_torch",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 6,
                        "currency": "minecraft:diamond",
                        "description": "使隐身的敌人显形\n\n§7花费: §b6 钻石",
                        "itemDict": {
                            "newItemName": "minecraft:redstone_torch",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            3 :{
                "type": "enchant_item",
                "title": "§e挖掘疲劳陷阱",
                "enchantType": "F2W73J",
                "itemList": {  
                    0 : {
                        "price": 1,
                        "currency": "minecraft:diamond",
                        "description": "造成挖掘疲劳效果,持续10秒\n\n§7花费: §b1 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_pickaxe",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 3,
                        "currency": "minecraft:diamond",
                        "description": "造成挖掘疲劳效果,持续10秒\n\n§7花费: §b3 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_pickaxe",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    2 : {
                        "price": 6,
                        "currency": "minecraft:diamond",
                        "description": "造成挖掘疲劳效果,持续10秒\n\n§7花费: §b6 钻石",
                        "itemDict": {
                            "newItemName": "minecrafts:iron_pickaxe",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            },
            4 :{
                "type": "enchant_item",
                "title": "§e迷梦陷阱",
                "enchantType": "H1G22F",
                "itemList": {
                    0 : {
                        "price": 6,
                        "currency": "minecraft:diamond",
                        "description": "将附近的敌人送回他们的基地!\n\n§7花费: §b6 钻石\n§7剩余购买次数: §b1 \n\n§o§8迷梦陷阱 是一个版本轮换物品!§r",
                        "itemDict": {
                            "newItemName": "minecraft:end_portal_frame",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    },
                    1 : {
                        "price": 999,
                        "currency": "minecraft:diamond",
                        "description": "将附近的敌人送回他们的基地!\n\n§7花费: §b6 钻石\n§7剩余购买次数: §c0 \n\n§o§8迷梦陷阱 是一个版本轮换物品!§r",
                        "itemDict": {
                            "newItemName": "minecraft:end_portal_frame",
                            "newAuxValue": 0,
                            "count": 1
                        }
                    }
                }
            }#  ,
        }
    }
}