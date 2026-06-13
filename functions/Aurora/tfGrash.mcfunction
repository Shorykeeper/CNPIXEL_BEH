# -*- coding: utf-8 -*-
# @Author : AerMini ISUREGOD


# 1. 木剑 - 造成4点伤害
execute as @a[tag=tfgrash,tag=wtf,hasitem={item=wooden_sword,location=slot.weapon.mainhand}] at @s run execute as @a[r=7,tag=!tfgrash] at @s unless score @s team = @p[tag=tfgrash,tag=wtf,r=7] team run damage @s 4 entity_attack entity @p[r=7,tag=tfgrash]
# 2. 铁剑 - 造成6点伤害
execute as @a[tag=tfgrash,tag=wtf,hasitem={item=iron_sword,location=slot.weapon.mainhand}] at @s run execute as @a[r=7,tag=!tfgrash] at @s unless score @s team = @p[tag=tfgrash,tag=wtf,r=7] team run damage @s 6 entity_attack entity @p[r=7,tag=tfgrash]
# 5. 石剑 - 造成5点伤害
execute as @a[tag=tfgrash,tag=wtf,hasitem={item=stone_sword,location=slot.weapon.mainhand}] at @s run execute as @a[r=7,tag=!tfgrash] at @s unless score @s team = @p[tag=tfgrash,tag=wtf,r=7] team run damage @s 5 entity_attack entity @p[r=7,tag=tfgrash]
# 6. 钻石剑 - 造成7点伤害
execute as @a[tag=tfgrash,tag=wtf,hasitem={item=diamond_sword,location=slot.weapon.mainhand}] at @s run execute as @a[r=7,tag=!tfgrash] at @s unless score @s team = @p[tag=tfgrash,tag=wtf,r=7] team run damage @s 7 entity_attack entity @p[r=7,tag=tfgrash]


# 3. 铁剑 - 播放动画
execute as @a[tag=tfgrash,tag=wtf,hasitem={item=iron_sword,location=slot.weapon.mainhand}] at @s run execute as @a[r=7,tag=!tfgrash] at @s unless score @s team = @p[tag=tfgrash,tag=wtf,r=7] team run playanimation @p[tag=tfgrash] animation.piglin.crossbow.charge default 0.3
# 4. 钻石剑 - 播放动画
execute as @a[tag=tfgrash,tag=wtf,hasitem={item=diamond_sword,location=slot.weapon.mainhand}] at @s run execute as @a[r=7,tag=!tfgrash] at @s unless score @s team = @p[tag=tfgrash,tag=wtf,r=7] team run playanimation @p[tag=tfgrash] animation.piglin.crossbow.charge default 0.3
# 7. 石剑 - 播放动画
execute as @a[tag=tfgrash,tag=wtf,hasitem={item=stone_sword,location=slot.weapon.mainhand}] at @s run execute as @a[r=7,tag=!tfgrash] at @s unless score @s team = @p[tag=tfgrash,tag=wtf,r=7] team run playanimation @p[tag=tfgrash] animation.piglin.crossbow.charge default 0.3
# 8. 木剑 - 播放动画
execute as @a[tag=tfgrash,tag=wtf,hasitem={item=wooden_sword,location=slot.weapon.mainhand}] at @s run execute as @a[r=7,tag=!tfgrash] at @s unless score @s team = @p[tag=tfgrash,tag=wtf,r=7] team run playanimation @p[tag=tfgrash] animation.piglin.crossbow.charge default 0.3
