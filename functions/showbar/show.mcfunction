# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ ShoreKeep ]
# @Function : 显示计分板

execute if score start B7O14L = num_-1 B7O14L run function showbar/lobby

execute if score start B7O14L = num_0 B7O14L run function showbar/lobby

execute if score start B7O14L = num_1 B7O14L run function showbar/wait

execute if score start B7O14L >= num_2 B7O14L run function showbar/fight
