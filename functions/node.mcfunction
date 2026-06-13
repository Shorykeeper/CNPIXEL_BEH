# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 总启驱动


# 主城部分功能
function lobby/catapult

# 计算人数驱动
function allgames/rs

# 显示计分板驱动
function showbar/show

# 拘束模式
execute if entity @a[tag=banned] run function Aurora/Aurora_forbid

# 战斗功能驱动
execute if score start B7O14L = num_2 B7O14L run function fighting

# 计算开局倒计时
execute unless score start B7O14L >= num_2 B7O14L run function start/main

# 驱动Aurora反作弊
function Aurora/AuroraAC

execute positioned 0 100 1000 run tp @a[r=250,tag=!wtf] 73 186 1824

