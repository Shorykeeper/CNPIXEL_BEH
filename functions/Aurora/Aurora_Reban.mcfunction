# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 解封

tag @s remove banned

clear @s

scoreboard players reset @s ac.fly.time
scoreboard players reset @s FlyVl


title @s[tag=语言] title {"translate":[{"text":"aurora.cnp.reban.title"}]}
title @s[tag=语言] subtitle {"translate":[{"text":"aurora.cnp.reban.subtitle"}]}


title @s[tag=language] title {"translate":[{"text":"aurora.hyp.reban.title"}]}
title @s[tag=language] subtitle {"translate":[{"text":"aurora.hyp.reban.subtitle"}]}

tellraw @s {"rawtext":[{"translate":"CNPIXEL.name.starting"}]}
tellraw @s[tag=language] {"rawtext":[{"translate":"aurora.hyp.reban.msg"}]}
tellraw @s[tag=语言] {"rawtext":[{"translate":"aurora.cnp.reban.msg"}]}


