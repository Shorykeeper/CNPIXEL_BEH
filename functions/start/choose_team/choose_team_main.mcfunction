# -*- coding: utf-8 -*-
# @Author : AerMini. [ QID: FinishDre ]
# @Function : 选队系统-主体


scoreboard objectives add team_c dummy
scoreboard players add team_tip_status B7O14L 0
execute if score team_tip_status B7O14L matches 0 run tellraw @a {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §a队伍或人数数据需要刷新, 请STAFF接入检查!"}]}
execute if score team_tip_status B7O14L matches 0 run scoreboard players set team_tip_status B7O14L 1
execute if score team_tip_status B7O14L matches 2 run tellraw @a {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §a队伍 'normal' 配置成功加载! §7(该消息来自 'main')"}]}
execute if score team_tip_status B7O14L matches 2 run scoreboard players set team_tip_status B7O14L 3

scoreboard players set team_online B7O14L 0
execute as @a run scoreboard players add team_online B7O14L 1
scoreboard players operation team_online_old B7O14L -= team_online B7O14L
execute if score team_online_old B7O14L matches -10..-1 run scoreboard players set team_tip_status B7O14L 0
scoreboard players operation team_online_old B7O14L = team_online B7O14L



replaceitem entity @a[scores={team_c=1}] slot.armor.head 0 fam:helmet_red 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=1}] slot.armor.legs 0 fam:leggings_red 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=1}] slot.armor.chest 0 fam:chestplate_red 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=1}] slot.armor.feet 0 fam:boots_red 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}

replaceitem entity @a[scores={team_c=2}] slot.armor.head 0 fam:helmet_blue 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=2}] slot.armor.chest 0 fam:chestplate_blue 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=2}] slot.armor.legs 0 fam:leggings_blue 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=2}] slot.armor.feet 0 fam:boots_blue 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}

replaceitem entity @a[scores={team_c=4}] slot.armor.head 0 fam:helmet_yellow 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=4}] slot.armor.chest 0 fam:chestplate_yellow 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=4}] slot.armor.legs 0 fam:leggings_yellow 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=4}] slot.armor.feet 0 fam:boots_yellow 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}

replaceitem entity @a[scores={team_c=3}] slot.armor.head 0 fam:helmet_green 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=3}] slot.armor.chest 0 fam:chestplate_green 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=3}] slot.armor.legs 0 fam:leggings_green 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}
replaceitem entity @a[scores={team_c=3}] slot.armor.feet 0 fam:boots_green 1 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}


scoreboard players set red_pnum B7O14L 0
scoreboard players set blue_pnum B7O14L 0
scoreboard players set yellow_pnum B7O14L 0
scoreboard players set green_pnum B7O14L 0
execute as @a[scores={team_c=1}] run scoreboard players add red_pnum B7O14L 1
execute as @a[scores={team_c=2}] run scoreboard players add blue_pnum B7O14L 1
execute as @a[scores={team_c=3}] run scoreboard players add green_pnum B7O14L 1
execute as @a[scores={team_c=4}] run scoreboard players add yellow_pnum B7O14L 1

execute as @a[tag=team_join_red,tag=nogame] run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §c你不被允许选择队伍!"}]}
execute as @a[tag=team_join_red,tag=team_hidden] run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §c你不被允许选择队伍!"}]}
execute as @a[tag=team_join_blue,tag=nogame] run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §c你不被允许选择队伍!"}]}
execute as @a[tag=team_join_blue,tag=team_hidden] run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §c你不被允许选择队伍!"}]}
execute as @a[tag=team_join_yellow,tag=nogame] run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §c你不被允许选择队伍!"}]}
execute as @a[tag=team_join_yellow,tag=team_hidden] run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §c你不被允许选择队伍!"}]}
execute as @a[tag=team_join_green,tag=nogame] run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §c你不被允许选择队伍!"}]}
execute as @a[tag=team_join_green,tag=team_hidden] run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §c你不被允许选择队伍!"}]}


execute as @a[tag=team_join_red,tag=!nogame,tag=!team_hidden] unless score mode O8P02W = num_5 B7O14L if score red_pnum B7O14L >= cteam.people.red B7O14L run tag @s add team_failed
execute as @a[tag=team_join_blue,tag=!nogame,tag=!team_hidden] unless score mode O8P02W = num_5 B7O14L if score blue_pnum B7O14L >= cteam.people.blue B7O14L run tag @s add team_failed
execute as @a[tag=team_join_green,tag=!nogame,tag=!team_hidden] unless score mode O8P02W = num_5 B7O14L if score green_pnum B7O14L >= cteam.people.green B7O14L run tag @s add team_failed
execute as @a[tag=team_join_yellow,tag=!nogame,tag=!team_hidden] unless score mode O8P02W = num_5 B7O14L if score yellow_pnum B7O14L >= cteam.people.yellow B7O14L run tag @s add team_failed

execute if score mode O8P02W matches 5 run tag @a[tag=team_failed] remove team_failed

execute as @a[tag=team_join_red,tag=!nogame,tag=!team_hidden] if score red_pnum B7O14L < cteam.people.red B7O14L run tag @s add team_success
execute as @a[tag=team_join_blue,tag=!nogame,tag=!team_hidden] if score blue_pnum B7O14L < cteam.people.blue B7O14L run tag @s add team_success
execute as @a[tag=team_join_green,tag=!nogame,tag=!team_hidden] if score green_pnum B7O14L < cteam.people.green B7O14L run tag @s add team_success
execute as @a[tag=team_join_yellow,tag=!nogame,tag=!team_hidden] if score yellow_pnum B7O14L < cteam.people.yellow B7O14L run tag @s add team_success

execute as @a[tag=team_join_red,tag=!nogame,tag=!team_hidden] unless score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§f"},{"selector":"@s"},{"text":" §7正在加入§l §c红队 §r§f反馈: "},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_failed]"},{"text":"§c§lFALSE"}]}},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_success]"},{"text":"§a§lTRUE"}]}},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_failed]"},{"text":" §r§fREASON: §c该队伍已满, 请选择其他队伍!"}]}}]}
execute as @a[tag=team_join_blue,tag=!nogame,tag=!team_hidden] unless score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§f"},{"selector":"@s"},{"text":" §7正在加入§l §b蓝队 §r§f反馈: "},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_failed]"},{"text":"§c§lFALSE"}]}},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_success]"},{"text":"§a§lTRUE"}]}},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_failed]"},{"text":" §r§fREASON: §c该队伍已满, 请选择其他队伍!"}]}}]}
execute as @a[tag=team_join_green,tag=!nogame,tag=!team_hidden] unless score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§f"},{"selector":"@s"},{"text":" §7正在加入§l §a绿队 §r§f反馈: "},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_failed]"},{"text":"§c§lFALSE"}]}},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_success]"},{"text":"§a§lTRUE"}]}},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_failed]"},{"text":" §r§fREASON: §c该队伍已满, 请选择其他队伍!"}]}}]}
execute as @a[tag=team_join_yellow,tag=!nogame,tag=!team_hidden] unless score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§f"},{"selector":"@s"},{"text":" §7正在加入§l §e黄队 §r§f反馈: "},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_failed]"},{"text":"§c§lFALSE"}]}},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_success]"},{"text":"§a§lTRUE"}]}},{"translate":"%%2","with":{"rawtext":[{"selector":"@s[tag=team_failed]"},{"text":" §r§fREASON: §c该队伍已满, 请选择其他队伍!"}]}}]}
execute as @a[tag=team_join_red,tag=!nogame,tag=!team_hidden] if score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§f"},{"selector":"@s"},{"text":" §7正在加入§l §c红队 §r§f反馈: §a§lTRUE"}]}
execute as @a[tag=team_join_blue,tag=!nogame,tag=!team_hidden] if score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§f"},{"selector":"@s"},{"text":" §7正在加入§l §b蓝队 §r§f反馈: §a§lTRUE"}]}
execute as @a[tag=team_join_green,tag=!nogame,tag=!team_hidden] if score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§f"},{"selector":"@s"},{"text":" §7正在加入§l §a绿队 §r§f反馈: §a§lTRUE"}]}
execute as @a[tag=team_join_yellow,tag=!nogame,tag=!team_hidden] if score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§f"},{"selector":"@s"},{"text":" §7正在加入§l §e黄队 §r§f反馈: §a§lTRUE"}]}


execute as @a[tag=team_join_red,tag=!nogame,tag=!team_hidden] if score @s team_c matches 1 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§c无效的重复选择! 已加入该队伍!"}]}
execute as @a[tag=team_join_blue,tag=!nogame,tag=!team_hidden] if score @s team_c matches 2 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§c无效的重复选择! 已加入该队伍!"}]}
execute as @a[tag=team_join_green,tag=!nogame,tag=!team_hidden] if score @s team_c matches 3 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§c无效的重复选择! 已加入该队伍!"}]}
execute as @a[tag=team_join_yellow,tag=!nogame,tag=!team_hidden] if score @s team_c matches 4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§c无效的重复选择! 已加入该队伍!"}]}


execute as @a[tag=team_join_red,tag=team_success,tag=!nogame,tag=!team_hidden] run scoreboard players set @s team_c 1
execute as @a[tag=team_join_blue,tag=team_success,tag=!nogame,tag=!team_hidden] run scoreboard players set @s team_c 2
execute as @a[tag=team_join_green,tag=team_success,tag=!nogame,tag=!team_hidden] run scoreboard players set @s team_c 3
execute as @a[tag=team_join_yellow,tag=team_success,tag=!nogame,tag=!team_hidden] run scoreboard players set @s team_c 4

execute as @a[tag=team_join_red,tag=!nogame,tag=!team_hidden] unless score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§c加入队伍失败.. §fCODE: §eW2506011"}]}
execute as @a[tag=team_join_blue,tag=!nogame,tag=!team_hidden] unless score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§c加入队伍失败.. §fCODE: §eW2506012"}]}
execute as @a[tag=team_join_green,tag=!nogame,tag=!team_hidden] unless score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§c加入队伍失败.. §fCODE: §eW2506013"}]}
execute as @a[tag=team_join_yellow,tag=!nogame,tag=!team_hidden] unless score @s team_c matches 1..4 run tellraw @s {"rawtext":[{"text":"§l§eCN§6PIXEL§7 >> §r§c加入队伍失败.. §fCODE: §eW2506014"}]}


tag @a remove team_join_red
tag @a remove team_join_blue
tag @a remove team_join_green
tag @a remove team_join_yellow
tag @a remove team_success
tag @a remove team_failed