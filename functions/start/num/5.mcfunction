
# sounds
execute as @a at @s run playsound note.hat @s

#titleraw
titleraw @a title {"rawtext":[{"translate":"style.hyp.startdown_5.title"}]}

#tellraw
tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.startdown_5.msg"}]}
tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.startdown_5.msg"}]}

#停止选队
clear @a lime_concrete
clear @a yellow_concrete
clear @a blue_concrete

execute as @a run tp @s
clear @a ender_eye
