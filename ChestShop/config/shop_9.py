# coding=utf-8 经验团队商店
GOODS_DATA = {
    #["X5T99R", "C1T28Q","A1B23C","Z3K56L","Q7M04P","Y9V88N"]
    0 : { #急迫 保护 锋利 龙 治愈池 铁锻炉
        "description": "§a团队升级\n§e点击查看!",
        "itemDict": {"newItemName": "minecraft:beacon","newAuxValue": 0,"count": 1},
        "goods": {
            0 :{
                "type": "enchant_item",
                "title": "§e锋利增益",
                "enchantType": "A1B23C",
                "itemList": { # type:dict[level:ItemDict] # 物品列表
                    0 : {
                        "price": 400,
                        "currency": "experience",
                        "description": "己方所有成员的剑和斧将永久获得锋利I附魔\n\n§71级: 锋利Ⅰ §2400 经验\n§72级: 锋利ⅠⅠ §21000 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_sword","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 1000,
                        "currency": "experience",
                        "description": "己方所有成员的剑和斧将永久获得锋利II附魔\n\n§a1级: 锋利Ⅰ §2400 经验\n§72级: 锋利ⅠⅠ §21000 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_sword","newAuxValue": 0,"count": 1}
                    },
                    2 : {
                        "price": 24751,
                        "currency": "experience",
                        "description": "己方所有成员的剑和斧将永久获得锋利II附魔\n\n§a1级: 锋利Ⅰ §2400 经验\n§a2级: 锋利ⅠⅠ §21000 经验\n\n§e该增益已满级!§r",
                        "itemDict": {"newItemName": "minecrafts:iron_sword","newAuxValue": 0,"count": 1}
                    }
                }
            },
            1 :{
                "type": "enchant_item",
                "title": "§e盔甲强化",
                "enchantType": "C1T28Q",
                "itemList": {
                    0 : {
                        "price": 250,
                        "currency": "experience",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§71级: 保护Ⅰ §2250 经验\n§72级: 保护ⅠⅠ §2500 经验\n§73级: 保护ⅠⅠⅠ §21000 经验\n§74级: 保护ⅠⅣ §21500 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_chestplate","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 500,
                        "currency": "experience",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§a1级: 保护Ⅰ §2250 经验\n§72级: 保护ⅠⅠ §2500 经验\n§73级: 保护ⅠⅠⅠ §21000 经验\n§74级: 保护ⅠⅣ §21500 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_chestplate","newAuxValue": 0,"count": 1}
                    },
                    2 : {
                        "price": 1000,
                        "currency": "experience",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§a1级: 保护Ⅰ §2250 经验\n§a2级: 保护ⅠⅠ §2500 经验\n§73级: 保护ⅠⅠⅠ §21000 经验\n§74级: 保护ⅠⅣ §21500 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_chestplate","newAuxValue": 0,"count": 1}
                    },
                    3 : {
                        "price": 1500,
                        "currency": "experience",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§a1级: 保护Ⅰ §2250 经验\n§a2级: 保护ⅠⅠ §2500 经验\n§a3级: 保护ⅠⅠⅠ §21000 经验\n§74级: 保护ⅠⅣ §21500 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_chestplate","newAuxValue": 0,"count": 1}
                    },
                    4 : {
                        "price": 24751,
                        "currency": "experience",
                        "description": "己方所有成员盔甲获得保护附魔\n\n§a1级: 保护Ⅰ §2250 经验\n§a2级: 保护ⅠⅠ §2500 经验\n§a3级: 保护ⅠⅠⅠ §21000 经验\n§a4级: 保护ⅠⅣ §21500 经验\n\n§e该增益已满级!§r",
                        "itemDict": {"newItemName": "minecrafts:iron_chestplate","newAuxValue": 0,"count": 1}
                    }
                }
            },
            2 :{
                "type": "enchant_item",
                "title": "§e疯狂矿工",
                "enchantType": "X5T99R",
                "itemList": {
                    0 : {
                        "price": 200,
                        "currency": "experience",
                        "description": "己方所有成员获得永久急迫效果\n\n§71级: 急迫Ⅰ §2200 经验\n§72级: 急迫ⅠⅠ §2300 经验",
                        "itemDict": {"newItemName": "minecrafts:golden_pickaxe","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 300,
                        "currency": "experience",
                        "description": "己方所有成员获得永久急迫效果\n\n§a1级: 急迫Ⅰ §2200 经验\n§72级: 急迫ⅠⅠ §2300 经验",
                        "itemDict": {"newItemName": "minecrafts:golden_pickaxe","newAuxValue": 0,"count": 1}
                    },
                    2 : {
                        "price": 24751,
                        "currency": "experience",
                        "description": "己方所有成员获得永久急迫效果\n\n§a1级: 急迫Ⅰ §2200 经验\n§a2级: 急迫ⅠⅠ §2300 经验\n\n§e该增益已满级!§r",
                        "itemDict": {"newItemName": "minecrafts:golden_pickaxe","newAuxValue": 0,"count": 1}
                    }
                }
            },
            3 :{
                "type": "enchant_item",
                "title": "§e缓冲靴子",
                "enchantType": "C5H77S",
                "itemList": {
                    0 : {
                        "price": 100,
                        "currency": "experience",
                        "description": "§7己方成员的靴子获得永久摔落缓冲\n\n§71级: 摔落缓冲Ⅰ §2100 经验\n§72级: 摔落缓冲ⅠⅠ §2200 经验",
                        "itemDict": {"newItemName": "minecrafts:diamond_boots","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 200,
                        "currency": "experience",
                        "description": "§7己方成员的靴子获得永久摔落缓冲\n\n§a1级: 摔落缓冲Ⅰ §2100 经验\n§72级: 摔落缓冲ⅠⅠ §2200 经验",
                        "itemDict": {"newItemName": "minecrafts:diamond_boots","newAuxValue": 0,"count": 1}
                    },
                    2 : {
                        "price": 24751,
                        "currency": "experience",
                        "description": "§7己方成员的靴子获得永久摔落缓冲\n\n§a1级: 摔落缓冲Ⅰ §2100 经验\n§a2级: 摔落缓冲ⅠⅠ §2200 经验\n\n§e该增益已满级!§r",
                        "itemDict": {"newItemName": "minecrafts:diamond_boots","newAuxValue": 0,"count": 1}
                    }
                }
            }
        }
    },
    1 : { #陷阱
        "description": "§a团队陷阱\n§e点击查看!",
        "itemDict": {"newItemName": "minecraft:string","newAuxValue": 0,"count": 1},
        "goods": {
            0 :{
                "type": "enchant_item",
                "title": "§e这是个陷阱!",
                "enchantType": "G6Y81U",
                "itemList": {
                    0 : {
                        "price": 50,
                        "currency": "experience",
                        "description": "造成失明和缓慢效果,持续8秒\n\n§7花费: §250 经验",
                        "itemDict": {"newItemName": "minecraft:tripwire_hook","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 150,
                        "currency": "experience",
                        "description": "造成失明和缓慢效果,持续8秒\n\n§7花费: §2150 经验",
                        "itemDict": {"newItemName": "minecraft:tripwire_hook","newAuxValue": 0,"count": 1}
                    },
                    2 : {
                        "price": 300,
                        "currency": "experience",
                        "description": "造成失明和缓慢效果,持续8秒\n\n§7花费: §2300 经验",
                        "itemDict": {"newItemName": "minecraft:tripwire_hook","newAuxValue": 0,"count": 1}
                    }
                }
            },
            1 :{
                "type": "enchant_item",
                "title": "§e反击陷阱",
                "enchantType": "P4J90M",
                "itemList": {
                    0 : {
                        "price": 50,
                        "currency": "experience",
                        "description": "我方成员获得速度和跳跃效果,持续8秒\n\n§7花费: §250 经验",
                        "itemDict": {"newItemName": "minecraft:feather","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 150,
                        "currency": "experience",
                        "description": "我方成员获得速度和跳跃效果,持续8秒\n\n§7花费: §2150 经验",
                        "itemDict": {"newItemName": "minecraft:feather","newAuxValue": 0,"count": 1}
                    },
                    2 : {
                        "price": 300,
                        "currency": "experience",
                        "description": "我方成员获得速度和跳跃效果,持续8秒\n\n§7花费: §2300 经验",
                        "itemDict": {"newItemName": "minecraft:feather","newAuxValue": 0,"count": 1}
                    }
                }
            },
            2 :{
                "type": "enchant_item",
                "title": "§e报警陷阱",
                "enchantType": "E3Q28N",
                "itemList": {
                    0 : {
                        "price": 50,
                        "currency": "experience",
                        "description": "使隐身的敌人显形\n\n§7花费: §250 经验",
                        "itemDict": {"newItemName": "minecraft:redstone_torch","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 150,
                        "currency": "experience",
                        "description": "使隐身的敌人显形\n\n§7花费: §2150 经验",
                        "itemDict": {"newItemName": "minecraft:redstone_torch","newAuxValue": 0,"count": 1}
                    },
                    2 : {
                        "price": 300,
                        "currency": "experience",
                        "description": "使隐身的敌人显形\n\n§7花费: §2300 经验",
                        "itemDict": {"newItemName": "minecraft:redstone_torch","newAuxValue": 0,"count": 1}
                    }
                }
            },
            3 :{
                "type": "enchant_item",
                "title": "§e挖掘疲劳陷阱",
                "enchantType": "F2W73J",
                "itemList": {
                    0 : {
                        "price": 50,
                        "currency": "experience",
                        "description": "造成挖掘疲劳效果,持续10秒\n\n§7花费: §250 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_pickaxe","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 150,
                        "currency": "experience",
                        "description": "造成挖掘疲劳效果,持续10秒\n\n§7花费: §2150 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_pickaxe","newAuxValue": 0,"count": 1}
                    },
                    2 : {
                        "price": 300,
                        "currency": "experience",
                        "description": "造成挖掘疲劳效果,持续10秒\n\n§7花费: §2300 经验",
                        "itemDict": {"newItemName": "minecrafts:iron_pickaxe","newAuxValue": 0,"count": 1}
                    }
                }
            },
            4 :{
                "type": "enchant_item",
                "title": "§e迷梦陷阱",
                "enchantType": "H1G22F",
                "itemList": {
                    0 : {
                        "price": 300,
                        "currency": "experience",
                        "description": "将附近的敌人送回他们的基地!\n\n§7花费: §2300 经验\n§7剩余购买次数: §21 \n\n§o§8迷梦陷阱 是一个版本轮换物品!§r",
                        "itemDict": {"newItemName": "minecraft:end_portal_frame","newAuxValue": 0,"count": 1}
                    },
                    1 : {
                        "price": 24751,
                        "currency": "experience",
                        "description": "将附近的敌人送回他们的基地!\n\n§7花费: §2300 经验\n§7剩余购买次数: §c0 \n\n§o§8迷梦陷阱 是一个版本轮换物品!§r",
                        "itemDict": {"newItemName": "minecraft:end_portal_frame","newAuxValue": 0,"count": 1}
                    }
                }
            }
            # ,}
        }
    }
}