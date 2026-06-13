
# sounds
execute as @a at @s run playsound note.hat @s

#titleraw
titleraw @a title {"rawtext":[{"translate":"style.hyp.startdown_2.title"}]}

#tellraw
tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.startdown_2.msg"}]}
tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.startdown_2.msg"}]}
