# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ ShoreKeep ]
# @Function : 部署一次倒计时开始效果

#Tips: 这里只在main条件达标的时唯引一次
function start/choose_team/config/normal

#设置游戏状态为 [倒计时 , 1]
scoreboard players set start B7O14L 1

#验证模式判断是否清除疾速保护
execute unless score mode O8P02W = num_2 B7O14L run function global/reset/unless_speed_reset

#设置倒计时为 180
scoreboard players set count M3F75C 180

#播报即将开始文本title
titleraw @a[tag=语言] title {"rawtext":[{"translate":"style.cnp.can_start.title"}]}
titleraw @a[tag=语言] subtitle {"rawtext":[{"translate":"style.cnp.can_start.subtitle"}]}

titleraw @a[tag=language] title {"rawtext":[{"translate":"style.hyp.can_start.title"}]}
titleraw @a[tag=language] subtitle {"rawtext":[{"translate":"style.hyp.can_start.subtitle"}]}

#如果排位模式则设置区分地图tag



#传到战场玻璃屋
tp @a @e[name="§f"]

#加经验条数字倒计时显示 1l = 1s
xp -9999l @a
xp 180L @a

# 播放一次开始一次音效
execute as @a at @s run playsound random.levelup @s
