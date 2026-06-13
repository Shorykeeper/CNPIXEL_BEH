
## 选择模式

tellraw @a {"rawtext":[{"translate":"mode.cnp.pickmode.msg","with":{"rawtext":[{"translate":"mode.cnp.rbw.name"}]}}]}

title @a title §f
titleraw @a subtitle {"rawtext":[{"translate":"mode.cnp.pickmode.msg","with":{"rawtext":[{"translate":"mode.cnp.rbw.name"}]}}]}

execute as @a at @s run playsound random.toast @s

scoreboard players set mode O8P02W 5

title @a title §a§l排位起床已激活!
title @a subtitle §7@a[tag=canrbw]§f使下局为rbw特殊模式


