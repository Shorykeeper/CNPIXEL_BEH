

tellraw @s[tag=语言] {"rawtext":[{"translate":"style.cnp.config_function_check.msg"}]}
tellraw @s[tag=language] {"rawtext":[{"translate":"style.hyp.config_function_check.msg"}]}



execute as @s[tag=语言] at @s run tellraw @s {"rawtext":[{"text":"§e----------------------------------------\n§f账号名称:§7 "},{"text":"§7["},{"score":{"objective":"G7C23S","name":"@s"}},{"text":"✿] "},{"selector":"@s"},{"text":"\n\n§f参与局数: §a§l0"},{"score":{"objective":"V3P49H","name":"@s"}},{"text":"\n\n§r§f击杀: §a§l0"},{"score":{"objective":"V5G28k","name":"@s"}},{"text":" §r§f最终击杀: §l§a0"},{"score":{"objective":"C4D31J","name":"@s"}},{"text":" §r§f死亡: §a§l0"},{"score":{"objective":"D2K48A","name":"@s"}},{"text":"\n§r§f胜利场数: §l§a0"},{"score":{"objective":"T8R43H","name":"@s"}},{"text":" §r§f破坏床数: §l§a0"},{"score":{"objective":"S0F06V","name":"@s"}},{"text":"§e\n--------------------------------------"}]}

execute as @s[tag=language] at @s run tellraw @s {"rawtext":[{"text":"§e----------------------------------------\n§fName:§7 "},{"text":"§7["},{"score":{"objective":"G7C23S","name":"@s"}},{"text":"✿] "},{"selector":"@s"},{"text":"\n\n§fJoin games: §a§l0"},{"score":{"objective":"V3P49H","name":"@s"}},{"text":"\n\n§r§fKill: §a§l0"},{"score":{"objective":"V5G28k","name":"@s"}},{"text":" §r§fFinal Kill: §l§a0"},{"score":{"objective":"C4D31J","name":"@s"}},{"text":" §r§fDied: §a§l0"},{"score":{"objective":"D2K48A","name":"@s"}},{"text":"\n§r§fWin: §l§a0"},{"score":{"objective":"T8R43H","name":"@s"}},{"text":" §r§fBed Broken: §l§a0"},{"score":{"objective":"S0F06V","name":"@s"}},{"text":"§e\n-------------------------------------"}]}
