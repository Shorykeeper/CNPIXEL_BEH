# -*- coding: utf-8 -*-
# @Author  : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 统括全战局 被other二级条件引用
# @TeamCode: 1R 2B 3G 4Y

#摔虚空
damage @a[x=0,y=195,z=0,dx=206,dy=5,dz=206] 999 anvil

#指令管辖的道具引用
execute unless score mode O8P02W matches 1 run function global/toys/main

#刷新矿石 有运作前提:结果未晓
execute unless score mode O8P02W matches 1 unless entity @a[tag=winn] run function global/ore/ksmain

#计算游戏结束
execute unless entity @a[tag=test1] if entity @a[tag=inf] run function global/end/ace

#执行复活
function global/kad/r

#计算事件
function global/event/event_main

#计算增益效果
execute unless score mode O8P02W matches 1 run function global/upgrade/A_manifest


 
#防止观战的乱跑
execute if entity @a[tag=观战] positioned 127 311 127 run tp @a[rm=145,tag=观战,m=spectator] 127 311 127


#执行模式效果
function mode/node/main

# 钓鱼竿钩子加轨迹
execute unless score mode O8P02W matches 1 as @e[type=fishing_hook] at @s run particle minecraft:villager_happy ~~~

#  当无床且人数大等一才计分板显示队伍人数
#  有床不用计算只显示勾 为零是unless管故这不用计算
execute if entity @a[tag=无床,scores={A1T12P=1}] if score rrs D1W04T >= num_1 B7O14L if entity @e[name="§a✔",tag=canace] run function global/end/team_state/r
execute if entity @a[tag=无床,scores={A1T12P=3}] if score grs D1W04T >= num_1 B7O14L if entity @e[name="§a2",tag=canace] run function global/end/team_state/g
execute if entity @a[tag=无床,scores={A1T12P=2}] if score brs D1W04T >= num_1 B7O14L if entity @e[name="§a1",tag=canace] run function global/end/team_state/b
execute if entity @a[tag=无床,scores={A1T12P=4}] if score yrs D1W04T >= num_1 B7O14L if entity @e[name="§c✘",tag=canace] run function global/end/team_state/y

