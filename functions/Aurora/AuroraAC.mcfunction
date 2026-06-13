# -*- coding: utf-8 -*-
# @Author : AerMini ISUREGOD
# @CreateTime : 2025/1/13
# Copyright @AerMini All Rights Reserved


# del xy1
scoreboard players remove @a[scores={A2S33B=0..}] A2S33B 1
execute as @p[scores={A2S33B=0..,Tspeed=24..}] run tag @s add speed_ban
execute as @p[scores={A2S33B=0..,Tspeed=24..}] run function Aurora/Aurora_Ban
scoreboard players reset @a[scores={A2S33B=..0,Tspeed=1..}] Tspeed
scoreboard players reset @a[scores={A2S33B=..0}] A2S33B

#del xy0
tag @a remove falling
execute as @a at @s anchored feet if entity @s[y=~-2,dy=-9999,dx=9999,dz=9999] run tag @s add falling

# fly 46
execute as @a[tag=!falling,tag=!wtf] at @s[m=0] if block ~~-0.9~ air if block ~-1~-0.9~ air if block ~1~-0.9~ air if block ~~-0.9~-1 air if block ~~-0.9~1 air if block ~-1~-0.9~-1 air if block ~-1~-0.9~1 air if block ~1~-0.9~-1 air if block ~1~-0.9~1 air if block ~~-2~ air unless block ~~-0.4~ oak_stairs unless block ~~-0.4~ wooden_slab unless block ~~-0.4~ spruce_stairs unless block ~~-0.4~ stone_slab unless block ~~-0.4~ stone_brick_stairs unless block ~~-0.4~ smooth_quartz_stairs unless block ~~-0.4~ chest unless block ~~-0.4~ ender_chest unless block ~~-0.1~ trapdoor unless block ~~-0.4~ weathered_cut_copper_slab unless block ~~-0.4~ weathered_cut_copper_stairs unless block ~~-0.3~ soul_lantern run scoreboard players add @s ac.fly.time 1
scoreboard players reset @a[tag=falling] ac.fly.time
execute as @a[tag=!falling] at @s unless block ~~-0.9~ air unless block ~-1~-0.9~ air unless block ~1~-0.9~ air unless block ~~-0.9~-1 air unless block ~~-0.9~1 air unless block ~-1~-0.9~-1 air unless block ~-1~-0.9~1 air unless block ~1~-0.9~-1 air unless block ~1~-0.9~1 air if block ~~-0.4~ oak_stairs if block ~~-0.4~ wooden_slab if block ~~-0.4~ spruce_stairs if block ~~-0.4~ stone_slab if block ~~-0.4~ stone_brick_stairs if block ~~-0.4~ smooth_quartz_stairs if block ~~-0.4~ chest if block ~~-0.4~ ender_chest if block ~~-0.1~ trapdoor if block ~~-0.4~ weathered_cut_copper_slab if block ~~-0.4~ weathered_cut_copper_stairs if block ~~-0.3~ soul_lantern run scoreboard players remove @s[scores={ac.fly.time=1..}] ac.fly.time 1
execute as @a[tag=!falling] at @s unless block ~~-1~ air run scoreboard players remove @s[tag=!winn,scores={ac.fly.time=1..}] ac.fly.time 1
execute as @a at @s if score @s ac.fly.time > num_flytime B7O14L run tellraw @a[tag=wtf] {"rawtext":[{"text":"§l§bAur§fora §8| §r§e"},{"selector":"@s"},{"text":" §7failed §cFly(A)"}]}
execute as @a at @s if score @s ac.fly.time > num_flytime B7O14L run scoreboard players add @s[tag=!winn,m=0] FlyVl 1
execute as @a at @s if score @s ac.fly.time > num_flytime B7O14L run scoreboard players set @s ac.fly.time 0
execute as @a[scores={FlyVl=3..},tag=!winn] run tag @s add fly_ban
execute as @a[scores={FlyVl=3..},tag=!winn] run function Aurora/Aurora_Ban


# speed
execute as @a[tag=!falling] at @s unless block ~~-0.01~ air anchored feet if entity @s[rm=1.9] run tag @s add AuroraNPCBX
execute as @a[tag=!falling] at @s if block ~~-0.01~ air anchored feet if entity @s[rm=2.8] run tag @s add AuroraNPCBY
execute as @a[tag=AuroraNPCBX] at @s run scoreboard players add @s Tspeed 1
execute as @a[tag=AuroraNPCBX] run tellraw @a[tag=wtf] {"rawtext":[{"text":"§l§bAur§fora §8| §r§e"},{"selector":"@s"},{"text":" §7failed §cSpeed(A) §7(VL."},{"score":{"objective":"Tspeed","name":"@s"}},{"text":")"}]}
execute as @a[tag=AuroraNPCBY] at @s run scoreboard players add @s Tspeed 1
execute as @a[tag=AuroraNPCBY] run tellraw @a[tag=wtf] {"rawtext":[{"text":"§l§bAur§fora §8| §r§e"},{"selector":"@s"},{"text":" §7failed §cSpeed(B)§7(VL."},{"score":{"objective":"Tspeed","name":"@s"}},{"text":")"}]}
execute as @a[tag=AuroraNPCBX] run scoreboard players set @s A2S33B 100
execute as @a[tag=AuroraNPCBY] run scoreboard players set @s A2S33B 100
execute as @a[tag=AuroraNPCBX] run tag @s remove AuroraNPCBX
execute as @a[tag=AuroraNPCBY] run tag @s remove AuroraNPCBY

