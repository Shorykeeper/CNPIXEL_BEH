# -*- coding: utf-8 -*-
# @Author  : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 计算对局人数
# @TeamCode: 1R 2B 3G 4Y

scoreboard players set rrs D1W04T 0
execute as @a[scores={A1T12P=1}] at @s run scoreboard players add rrs D1W04T 1

scoreboard players set grs D1W04T 0
execute as @a[scores={A1T12P=3}] at @s run scoreboard players add grs D1W04T 1

scoreboard players set yrs D1W04T 0
execute as @a[scores={A1T12P=4}] at @s run scoreboard players add yrs D1W04T 1

scoreboard players set brs D1W04T 0
execute as @a[scores={A1T12P=2}] at @s run scoreboard players add brs D1W04T 1


