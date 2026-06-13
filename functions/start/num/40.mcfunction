
# sounds
execute as @a at @s run playsound note.hat @s

#titleraw
titleraw @a title {"rawtext":[{"translate":"style.hyp.startdown_40.title"}]}

#tellraw
tellraw @a[tag=语言] {"rawtext":[{"translate":"style.cnp.startdown_40.msg"}]}
tellraw @a[tag=language] {"rawtext":[{"translate":"style.hyp.startdown_40.msg"}]}
