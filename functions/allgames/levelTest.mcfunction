# -*- coding: utf-8 -*-
# @Author  : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 被执行 升级效果


execute as @s[scores={E1B36G=5000..},tag=language] run titleraw @s title {"rawtext":[{"translate":"style.hyp.playerLevelUp.title"}]}
execute as @s[scores={E1B36G=5000..},tag=语言] run titleraw @s title {"rawtext":[{"translate":"style.cnp.playerLevelUp.title"}]}

execute as @s[scores={E1B36G=5000..}] run tag @s add le

scoreboard objectives add lel dummy
execute as @s[tag=le] run scoreboard players operation @s lel = @s G7C23S
execute as @s[tag=le] run scoreboard players add @s lel 1


execute as @s[tag=le] run titleraw @s subtitle {"rawtext":[{"text":"§l§b"},{"score":{"objective":"G7C23S","name":"@s"}},{"text":"§c✿ §f丨 §e➠ §f丨 §b"},{"score":{"objective":"lel","name":"@s"}},{"text":"§c✿"}]}

execute as @s[tag=le] run tellraw @a {"rawtext":[{"text":"§l\n§eCN§6PIXEL §7>> §f"},{"selector":"@s"},{"text":" §b"},{"score":{"objective":"G7C23S","name":"@s"}},{"text":"§c✿ §e➠ §b"},{"score":{"objective":"lel","name":"@s"}},{"text":"§c✿\n§f"}]}

execute as @s[tag=le] run summon fireworks_rocket ~~~
execute as @s[tag=le] run summon fireworks_rocket ~~~
execute as @s[tag=le] run summon fireworks_rocket ~~~


scoreboard objectives remove lel


execute as @s[tag=le] run playsound random.toast @s ~~~
execute as @s[tag=le] run scoreboard players remove @s E1B36G 5000
execute as @s[tag=le] run scoreboard players add @s G7C23S 1

tag @s remove le


