# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 玩家加入房间效果 被BwScript引用 

camera @s fade time 0.1 1 1 color 96 96 112

#初始add 0刷新跨局战绩
execute unless score @s G7C23S >= num_0 B7O14L run execute as @s at @s run function global/reload

scoreboard players set @s T2R10A 20

scoreboard players add @s S9T03A 0

function _1int1_

#语言
tag @s[tag=!语言,tag=!language] add 语言

tag @s[tag=!颗秒] add 颗秒

execute as @s unless score @s B7O14L = match_id B7O14L at @s run function allgames/join/clean_data
execute as @s if score @s B7O14L = match_id B7O14L at @s run function global/kad/l


scoreboard players reset @s A1T12P

effect @e[type=rabbit] instant_health 99999 255 true

tp @s 73 186 1824

spawnpoint @s 73 186 1824

title @s times 0 100 0

#teleport
tellraw @s[tag=语言] {"rawtext":[{"translate":"style.cnp.teleport.msg"}]}
tellraw @s[tag=language] {"rawtext":[{"translate":"style.hyp.teleport.msg"}]}


tellraw @s {"rawtext":[{"text":"§e"}]}
#level reward
tellraw @s[tag=语言,scores={G7C23S=1..}] {"rawtext":[{"translate":"style.cnp.level_reward_main.msg","with":{"rawtext":[{"score":{"objective":"G7C23S","name":"@s"}}]}}]}
tellraw @s[tag=语言,scores={G7C23S=1..}] {"rawtext":[{"translate":"style.cnp.level_reward_click.msg"}]}
tellraw @s[tag=language,scores={G7C23S=1..}] {"rawtext":[{"translate":"style.hyp.level_reward_main.msg","with":{"rawtext":[{"score":{"objective":"G7C23S","name":"@s"}}]}}]}
tellraw @s[tag=language,scores={G7C23S=1..}] {"rawtext":[{"translate":"style.hyp.level_reward_click.msg"}]}


titleraw @s title {"rawtext":[{"translate":"style.hyp.playerjoin_title"}]}
titleraw @s[tag=language] subtitle {"rawtext":[{"translate":"style.hyp.playerjoin_subtitle"}]}
titleraw @s[tag=语言] subtitle {"rawtext":[{"translate":"style.cnp.playerjoin_subtitle"}]}

# 挂接特殊权限赋值
function allgames/join/rightsRegister

