scoreboard players set cteam.hotbar.red B7O14L 1
scoreboard players set cteam.hotbar.blue B7O14L 2
scoreboard players set cteam.hotbar.green B7O14L 3
scoreboard players set cteam.hotbar.yellow B7O14L 4
scoreboard players set cteam.hotbar.op B7O14L 5
scoreboard players set cteam.hotbar.armor B7O14L 7

scoreboard players set cteam.people.red B7O14L 2
scoreboard players set cteam.people.blue B7O14L 2
scoreboard players set cteam.people.yellow B7O14L 2
scoreboard players set cteam.people.green B7O14L 2

execute if score mode O8P02W matches 5 run scoreboard players set cteam.people.red B7O14L 5
execute if score mode O8P02W matches 5 run scoreboard players set cteam.people.blue B7O14L 5
execute if score mode O8P02W matches 5 run scoreboard players set cteam.people.yellow B7O14L 5
execute if score mode O8P02W matches 5 run scoreboard players set cteam.people.green B7O14L 5


tellraw @a {"rawtext":[{"text":"§l§e§lCN§6PIXEL§7 >> §a队伍信息数据加载完成!"}]}

scoreboard players set team_tip_status B7O14L 2
