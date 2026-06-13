# -*- coding: utf-8 -*-
# @Author  : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 进入游戏时 给特定人员赋权

# S8Q83P list的前缀判别计分板
# U2C44V 发言前缀判别计分板

tag @s remove wtf
tag @s remove debug
tag @s remove 测试封禁
tag @s remove tfgrash
tag @s remove wtf
tag @s remove test1


scoreboard players set @s S8Q83P 0
scoreboard players set @s U2C44V 0

# VIP+ RANKS
tag @s[name="SAR_德育班"] add vip1
tag @s[name="BEST_FengYe"] add vip1
tag @s[name="CNP森"] add vip1
scoreboard players set @s[tag=vip1] S8Q83P 3
scoreboard players set @s[tag=vip1] U2C44V 3


# FRIENDS
tag @s[name="CNP_失言失望"] add friends
tag @s[name="我的心已千疮百孔"] add friends
#tag @s[name="落_XenClare"] add friends
scoreboard players set @s[tag=friends] S8Q83P 8
scoreboard players set @s[tag=friends] U2C44V 8

#  elite
tag @s[name="MXVR"] add elite
scoreboard players set @s[tag=elite] S8Q83P 6
scoreboard players set @s[tag=elite] U2C44V 6





# 顶级tag 也是测试用 
tag @s[name="NotLyingzi"] add wtf1
tag @s[name="DewierMC"] add wtf1
tag @s[name="zest_yingzi"] add wtf1
tag @s[name="ShoryKeeper"] add wtf
tag @s[name="叶格宁"] add wtf
tag @s[name="YJ叶格宁"] add wtf
tag @s[name="流萤_Firefly"] add wtf
tag @s[name="麻杯服务站"] add wtf
scoreboard players set @s[tag=wtf] S8Q83P 13
scoreboard players set @s[tag=wtf] U2C44V 13

# 特高级管理 比如天法. 落月和西瓜帮助大也在这
tag @s[name="拾暖记"] add wdf
tag @s[name="落月_LYue"] add wdf
tag @s[name="志云工作室"] add wdf
tag @s[name="普通的小晴猫罢了"] add wdf
tag @s[name="我嘞个夏冰雹"] add wdf
tag @s[name="西瓜云"] add wdf
tag @s[name="star_幸存者"] add wdf
tag @s[name="西瓜云工作室"] add wdf
scoreboard players set @s[tag=wdf] S8Q83P 11
scoreboard players set @s[tag=wdf] U2C44V 11

# 初级管理
tag @s[name="一只很菜的清雪"] add chuji
tag @s[name="落_XenClare"] add chuji
tag @s[name="普通的贝利亚罢了"] add chuji
tag @s[name="普通的小晴川罢了"] add chuji
tag @s[name="千里之Vape梦想"] add chuji
tag @s[name="Joyful233"] add chuji
tag @s[name="丨菜鱼丨"] add chuji
tag @s[name="HSZAQ"] add chuji 
scoreboard players set @s[tag=chuji] S8Q83P 10
scoreboard players set @s[tag=chuji] U2C44V 10


# UP主 比如光隐和五哥
tag @s[name="GY光隐"] add wup
tag @s[name="圃会"] add wup
tag @s[name="浅狼君闯世界吖"] add wup
tag @s[name="B站丶Kaway柠檬"] add wup
scoreboard players set @s[tag=wup] S8Q83P 1
scoreboard players set @s[tag=wup] U2C44V 1


# 协助制作和参测人员 比如console
tag @s[name="Console"] add help
tag @s[name="B站_MC五哥解说"] add help
tag @s[name="FAM_璃"] add help
scoreboard players set @s[tag=help] U2C44V 12
scoreboard players set @s[tag=help] S8Q83P 12

#
tag @s[name="YaolingYa"] add pm
scoreboard players set @s[tag=pm] S8Q83P 9


#播报一次提示 translate显示
execute as @s[scores={U2C44V=1..}] at @s run tellraw @a {"rawtext":[{"text":"§b\n§l§eCN§6PIXEL §7>> \n§f尊敬的 "},{"translate":"%%9","with":{"rawtext":[{"selector":"@s[scores={U2C44V=!..0,U2C44V=!2..}]"},{"selector":"@s[scores={U2C44V=!..0,U2C44V=!3..}]"},{"selector":"@s[scores={U2C44V=!..0,U2C44V=!4..}]"},{"selector":"@s[scores={U2C44V=!..0,U2C44V=!5..}]"},{"selector":"@s[scores={U2C44V=!..0,U2C44V=!6..}]"},{"selector":"@s[scores={U2C44V=!..0,U2C44V=!7..}]"},{"selector":"@s[scores={U2C44V=!..0,U2C44V=!8..}]"},{"selector":"@s[scores={U2C44V=!..0,U2C44V=!14..}]"},{"translate":"rights.refix_name_1"},{"translate":"rights.refix_name_2"},{"translate":"rights.refix_name_3"},{"translate":"rights.refix_name_4"},{"translate":"rights.refix_name_5"},{"translate":"rights.refix_name_6"},{"translate":"rights.refix_name_7"},{"translate":"%%7","with":{"rawtext":[{"selector":"@s[scores={U2C44V=!..7,U2C44V=!9..}]"},{"selector":"@s[scores={U2C44V=!..7,U2C44V=!10..}]"},{"selector":"@s[scores={U2C44V=!..7,U2C44V=!11..}]"},{"selector":"@s[scores={U2C44V=!..7,U2C44V=!12..}]"},{"selector":"@s[scores={U2C44V=!..7,U2C44V=!13..}]"},{"selector":"@s[scores={U2C44V=!..7,U2C44V=!14..}]"},{"translate":"rights.refix_name_8"},{"translate":"rights.refix_name_9"},{"translate":"rights.refix_name_10"},{"translate":"rights.refix_name_11"},{"translate":"rights.refix_name_12"},{"translate":"rights.refix_name_13"}]}}]}},{"text":"§7"},{"selector":"@s"},{"text":"§a§l[✔认证] §f进入了本服务器!欢迎!\n§f"}]}






 