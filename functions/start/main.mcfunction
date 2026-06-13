# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 倒计时主体 当非战斗时会长引用

# 仅触发一次部署
execute unless entity @a[tag=inf] if score start B7O14L = num_0 B7O14L if score rs D1W04T >= num_2 B7O14L run function start/deploy

# 人数重新不足 则倒计时失败 引用中止 
execute unless entity @a[tag=inf] if score start B7O14L = num_1 B7O14L if score count M3F75C >= num_1 B7O14L if score rs D1W04T < num_2 B7O14L run function global/start/cancel
# 倒计时效果在 time-global/timer/countdown进行引用计算

#循环启用选队系统
execute if score start B7O14L = num_1 B7O14L unless entity @a[tag=inf] run function start/choose_team/choose_team_main

#给选队 
# ender_eye 道具检测使用
execute if score start B7O14L = num_1 B7O14L if score count M3F75C > num_7 B7O14L unless entity @a[tag=inf] run replaceitem entity @a slot.hotbar 0 ender_eye 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
execute if score start B7O14L = num_1 B7O14L if score count M3F75C > num_7 B7O14L if score mapp F3Q58B = num_6 B7O14L if score mode O8P02W matches 5 run tag @a add rbw_chained
execute if score start B7O14L = num_1 B7O14L if score count M3F75C > num_7 B7O14L if score mapp F3Q58B = num_3 B7O14L if score mode O8P02W matches 5 run tag @a add rbw_unt

#传送不在玻璃屋的人
execute if score start B7O14L = num_1 B7O14L unless entity @a[tag=inf] as @e[type=npc,name="§f"] at @s run tp @p[rm=15,tag=!debug] @s

#人数达到合适就快进进程
execute if score start B7O14L = num_1 B7O14L if score rs D1W04T >= num_4 B7O14L if score count M3F75C matches 31.. run function start/increaseCountDown

#隐身NPC
#execute as @e[type=npc] at @s run playanimation @e[type=npc] animation.creeper.swelling move 178178

