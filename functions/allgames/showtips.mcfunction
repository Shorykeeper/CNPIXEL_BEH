# -*- coding: utf-8 -*-
# @Author  : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 全局的系统的小Tips 被执行一次

# msg是一瞬间创建的用于随机分数的计分板

## 前置创建随机计分板
scoreboard objectives add msg dummy

## 随机提示样式分数
scoreboard players random use msg 1 13

## 执行显示
execute if score use msg = num_1 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"tips.cnp.warn.noct.msg"}]}
execute if score use msg = num_1 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"tips.hyp.warn.noct.msg"}]}

execute if score use msg = num_2 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"tips.cnp.shory.sys.msg"}]}
execute if score use msg = num_2 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"tips.hyp.shory.sys.msg"}]}

execute if score use msg = num_3 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"tips.cnp.rejoin.noct.msg"}]}
execute if score use msg = num_3 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"tips.hyp.rejoin.noct.msg"}]}

execute if score use msg = num_4 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"tips.cnp.group.msg"}]}
execute if score use msg = num_4 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"tips.hyp.group.msg"}]}

execute if score use msg = num_5 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"tips.cnp.ultraVires.report.msg"}]}
execute if score use msg = num_5 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"tips.hyp.ultraVires.report.msg"}]}

execute if score use msg = num_6 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"tips.cnp.tryLuoYueMap.msg"}]}
execute if score use msg = num_6 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"tips.hyp.tryLuoYueMap.msg"}]}

execute if score use msg = num_7 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"tips.cnp.AuroraConsiderates.msg"}]}
execute if score use msg = num_7 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"tips.hyp.AuroraConsiderates.msg"}]}

execute if score use msg = num_8 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.smwy_PCPE_warning.msg"}]}
execute if score use msg = num_8 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.smwy_PCPE_warning.msg"}]}

execute if score use msg = num_9 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.smwy_PCPE_warning.msg"}]}
execute if score use msg = num_9 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.smwy_PCPE_warning.msg"}]}

execute if score use msg = num_10 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.smwy_PCPE_warning.msg"}]}
execute if score use msg = num_10 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.smwy_PCPE_warning.msg"}]}

execute if score use msg = num_11 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.tips_011.msg"}]}
execute if score use msg = num_11 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.tips_011.msg"}]}

execute if score use msg = num_12 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.tips_012.msg"}]}
execute if score use msg = num_12 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.tips_012.msg"}]}

execute if score use msg = num_13 B7O14L run tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.tips_013.msg"}]}
execute if score use msg = num_13 B7O14L run tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.tips_013.msg"}]}


## 重置计时时间
scoreboard players set tips M3F75C 0

## 直接销毁临时计算计分板
scoreboard objectives remove msg




