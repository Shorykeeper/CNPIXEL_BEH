# -*- coding: utf-8 -*-
# @Author  : 柑云宫音. [ QID: ShoreKeep ]
# @Function : 切床模式1之发布装备 需要at @s run使用
# @TeamCode: 1R 2B 3G 4Y

# 仅部署一次 该模式必须关闭方块掉落和清除对局相关掉落物

# 常规武器
execute if score mode O8P02W = num_1 B7O14L run replaceitem entity @s[tag=inf] slot.hotbar 0 stone_sword 
execute if score mode O8P02W = num_1 B7O14L run replaceitem entity @s[tag=inf] slot.hotbar 1 stone_pickaxe 
execute if score mode O8P02W = num_1 B7O14L run replaceitem entity @s[tag=inf] slot.hotbar 2 stone_axe
execute if score mode O8P02W = num_1 B7O14L run replaceitem entity @s[tag=inf] slot.hotbar 3 bow
execute if score mode O8P02W = num_1 B7O14L run replaceitem entity @s[tag=inf] slot.hotbar 4 shears
execute if score mode O8P02W = num_1 B7O14L run replaceitem entity @s[tag=inf] slot.inventory 1 arrow 32 0 {"minecraft:item_lock":{"mode":"lock_in_slot"}}

# 方块羊毛 64 + 64 + 32
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_1 B7O14L run replaceitem entity @s slot.hotbar 5 red_wool 64
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_2 B7O14L run replaceitem entity @s slot.hotbar 5 blue_wool 64
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_4 B7O14L run replaceitem entity @s slot.hotbar 5 yellow_wool 64
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_3 B7O14L run replaceitem entity @s slot.hotbar 5 lime_wool 64

execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_1 B7O14L run replaceitem entity @s slot.hotbar 6 red_wool 64
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_2 B7O14L run replaceitem entity @s slot.hotbar 6 blue_wool 64
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_4 B7O14L run replaceitem entity @s slot.hotbar 6 yellow_wool 64
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_3 B7O14L run replaceitem entity @s slot.hotbar 6 lime_wool 64

execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_1 B7O14L run replaceitem entity @s slot.hotbar 7 red_wool 32
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_2 B7O14L run replaceitem entity @s slot.hotbar 7 blue_wool 32
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_4 B7O14L run replaceitem entity @s slot.hotbar 7 yellow_wool 32
execute as @s[tag=inf] at @s if score mode O8P02W = num_1 B7O14L if score @s A1T12P = num_3 B7O14L run replaceitem entity @s slot.hotbar 7 lime_wool 32


effect @s[tag=inf] haste 9999 0 true

