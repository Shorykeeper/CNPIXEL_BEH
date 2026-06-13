# -*- coding: utf-8 -*-
# @Author : 柑云宫音. [ ShoreKeep ]
# @Function : 人数达到合适则快进倒计时
# 这里设定的是快进到22 (目的是20)



execute if score count M3F75C matches 31.. run scoreboard players set count M3F75C 30
xp -999l @a
xp 30l @a

