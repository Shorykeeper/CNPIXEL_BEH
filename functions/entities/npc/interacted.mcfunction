# -*- coding: utf-8 -*-
# @Copyright (c) YZBWDLT 2025-2026
# @授权User: 柑云宫音. [ ShoreKeep ]
# 未经权利人许可，禁止使用/复制/抄袭/搬运本代码

# ===== NPC 被交互后，NPC 执行的命令 =====

# 播放一次交互音效
execute as @s run execute as @p at @s run playsound random.pop @p

# 选队计算,当处于重置阶段.OWNER可以选择模式
# 这一段被脚本计算 @选模TAG- canmap @目标TAG- inChossingMode
# 脚本先给NPC交互对象加Tag 再被引用

# 丨 ----- 床斗模式 [ is Unavailable / stabled ] ----- 丨
execute as @e[c=1,tag=inChossingMode,x=113,y=183,z=1815,r=1] at @s run function start/choose_mode/bedfight

# 丨 ----- 疾速模式 [ is Unavailable /  ] ----- 丨
execute as @e[c=1,tag=inChossingMode,x=115,y=183,z=1818,r=1] at @s run function start/choose_mode/speed

# 丨 ----- 经典模式 [ is available / stabled ] ----- 丨
execute as @e[c=1,tag=inChossingMode,x=117,y=183,z=1821,r=1] at @s run function start/choose_mode/classic

# 丨 ----- 普通经验模式 [ is available / stabled ] ----- 丨
execute as @e[c=1,tag=inChossingMode,x=117,y=183,z=1827,r=1] at @s run function start/choose_mode/xp

# 丨 ----- 无尽一经验模式 [ is Unavailable / not stabled ] ----- 丨
#execute as @e[c=1,tag=inChossingMode,x=115,y=183,z=1830,r=1] at @s run function start/choose_mode/eternal

# 丨 ----- rbw特殊模式 需要一个可用者激活可用权限 ----- 丨
execute as @e[c=1,tag=inChossingMode,x=113,y=183,z=1833,r=1] if entity @r[tag=canrbw] run function start/choose_mode/rbw
execute if entity @e[c=1,tag=inChossingMode,x=113,y=183,z=1833,r=1] unless entity @p[tag=canrbw] as @p[tag=canmap] run function global/reward/rbwUnavailable


# 闭环选队计算 排除情况
tag @e[tag=inChossingMode] remove inChossingMode



#其他的NPC使用.
execute as @s[x=109,y=185,z=1795,r=2] run execute as @p at @s run function lobby/npc/states
execute as @s[x=101,y=182,z=1819,r=2] run execute as @p at @s run function lobby/npc/lobbyshop

execute as @s[x=109,y=185,z=1853,r=2] run execute as @p at @s run function lobby/npc/config
execute as @s[x=124,y=182,z=1824,r=2] run execute as @p at @s run function lobby/npc/view
