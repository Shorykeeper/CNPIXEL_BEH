# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ QID: ShoreKeep ]

scoreboard players reset @s FlyVl
scoreboard players reset @s A2S33B
scoreboard players reset @s Tspeed

execute as @s[tag=!banned] run camera @a fade time 0.1 2.5 1 color 235 86 75

title @a times 0 100 0

execute as @s[tag=!banned] run titleraw @a title {"rawtext":[{"text":"§l§bAur§fora\n§r§f检测到作弊者"}]}
execute as @s[tag=!banned] run titleraw @a subtitle {"rawtext":[{"text":"§f报请比赛中止\n作弊者已受到惩罚,游戏取消则所有玩家的输赢均不计入"}]}

tag @s[tag=!wtf,tag=!banned] add 封禁


