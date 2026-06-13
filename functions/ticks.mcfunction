# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 20刻执行使用
# @Ticks: 20


#  丨 ----- 计时器 ----- 丨
#  四位正反计时引用
execute if score start B7O14L = num_2 B7O14L run function global/timer/44

#  丨 ----- 小文字tips ----- 丨
scoreboard players add tips M3F75C 1
execute if score tips M3F75C matches 90.. run function allgames/showtips

#  丨 ----- 检测升级 ----- 丨
execute as @r[scores={E1B36G=5000..}] run function allgames/levelTest

#  丨 ----- 游戏开始倒计时 ----- 丨
#  倒计时效果引用
execute if score start B7O14L = num_1 B7O14L run function global/timer/countdown
execute if score start B7O14L = num_1 B7O14L run scoreboard players remove count M3F75C 1
execute if score start B7O14L = num_1 B7O14L if score rs D1W04T >= num_2 B7O14L if score count M3F75C >= num_1 B7O14L run xp -1L @a


# 丨 ----- 时长奖励 ----- 丨
# 统一倒计时 不给各客户端单独计算 我故意的
# 使用Reward自定义指令 time方法
scoreboard players add reward_time M3F75C 1
execute if score reward_time M3F75C matches 120.. run reward time


# 丨 ----- 铁金矿石刷新 ----- 丨
# 激活并引用节点
execute if score start B7O14L = num_2 B7O14L unless entity @a[tag=winn] run function global/ore/timer/base_ig


#  丨 ----- 玩家救援平台CD递减 ----- 丨
execute if score start B7O14L = num_2 B7O14L as @a[scores={N5L93G=0..}] at @s run scoreboard players remove @s N5L93G 1


# 丨 ----- 床保护 ----- 丨
execute if score start B7O14L = num_2 B7O14L if score 床保护 B7O14L matches 97 unless score mode O8P02W = num_1 B7O14L unless score mode O8P02W = num_2 B7O14L run function global/event/race/bedProtectTitle
execute if score start B7O14L = num_2 B7O14L if score 床保护 B7O14L >= num_0 B7O14L unless score mode O8P02W = num_1 B7O14L unless score mode O8P02W = num_2 B7O14L run scoreboard players remove 床保护 B7O14L 1
execute if score start B7O14L = num_2 B7O14L if score 床保护 B7O14L <= num_0 B7O14L unless score mode O8P02W = num_1 B7O14L unless score mode O8P02W = num_2 B7O14L run function global/event/race/bedProtectEnd


# 丨 ----- 治愈池 ----- 丨
execute if score start B7O14L = num_2 B7O14L run function global/upgrade/regeneration_pool





