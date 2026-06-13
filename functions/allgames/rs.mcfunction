# -*- coding: utf-8 -*-
# @Author  : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 总人数计算

# 计算全部
scoreboard players set rs D1W04T 0
execute as @a at @s run scoreboard players add rs D1W04T 1

# 计算战斗对局
execute if score start B7O14L = num_2 B7O14L run function allgames/fightingrs


