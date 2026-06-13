

execute unless entity @a[scores={A1T12P=1..4}] run tellraw @s[tag=语言] {"rawtext":[{"translate":"style.cnp.view_failed.msg"}]}

execute unless entity @a[scores={A1T12P=1..4}] run tellraw @s[tag=language] {"rawtext":[{"translate":"style.hyp.view_failed.msg"}]}

execute unless entity @a[scores={A1T12P=1..4}] run playsound random.break @s

execute if entity @a[scores={A1T12P=1..4}] as @s run function global/command/view 

