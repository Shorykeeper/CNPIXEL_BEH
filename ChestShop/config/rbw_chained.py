# coding=utf-8 选择队伍
GOODS_DATA = {
    0: {  # tab_type
        "description": "选择队伍",   # 标签描述
        "itemDict": {  # 标签物品
            "newItemName": "minecraft:netherstar",
            "newAuxValue": 0,
            "count": 1
        },
        "goods": {   # 商品列表
            0 : {
                "price": 0,   # 价格
                "type": "ct",  # 商品类型
                "currency": "minecraft:kelp",  
                "description": "§7点击加入 §a绿之队\n§7选中点击以加入",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:bed",
                    "newAuxValue": 5,
                    "count": 1  # 数量
                }
            },
            1 : {
                "price": 0,   # 价格
                "type": "ct",  # 商品类型
                "currency": "minecraft:kelp",  
                "description": "§7点击加入 §e黄之队\n§7选中点击以加入",  # 商品描述
                "itemDict": {  # 商品信息字典
                    "newItemName": "minecraft:bed",
                    "newAuxValue": 4,
                    "count": 1  # 数量
                }
            }
        }
    }
}