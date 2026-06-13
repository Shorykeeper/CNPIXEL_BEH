# -*- coding: utf-8 -*-
# 欢迎参观我的史山
# Create Origin: 凡安梦 // 功能大改增补: Witz
import __future__
import time
import random
import math
import re
from time import localtime
import mod.server.extraServerApi as sapi # type: ignore
from ..config.config import *
from ..config.fastListen import *
cf = sapi.GetEngineCompFactory()
levelId = sapi.GetLevelId()
setCommand = lambda cmdStr, playerId=None, showOutput=False: cf.CreateCommand(levelId).SetCommand(cmdStr, playerId, showOutput)
hasTag = lambda tag, entityId: cf.CreateTag(entityId).EntityHasTag(tag)
addTag = lambda tag, entityId: cf.CreateTag(entityId).AddEntityTag(tag)
removeTag = lambda tag, entityId : cf.CreateTag(entityId).RemoveEntityTag(tag)
getTagList = lambda entityId: cf.CreateTag(entityId).GetEntityTags()
showMsg = lambda msg, playerId=None: setCommand('/tellraw @%s {"rawtext":[{"text":"%s"}]}' % (('s', 'a')[playerId == None], msg.replace('"', '\\"')), playerId)
setExData = lambda key, value, Id: cf.CreateExtraData(Id).SetExtraData(key, value)
getExData = lambda key, Id: cf.CreateExtraData(Id).GetExtraData(key)
cleanExData = lambda key, Id: cf.CreateExtraData(Id).CleanExtraData(key)
function = lambda mcfunc, Id: setCommand('/execute as @s at @s run function %s' % mcfunc, Id)

def BedColor(itemColor):
    """映射-获取床的颜色"""
    if itemColor == 1:
        return "RED"
    elif itemColor == 10:
        return "GREEN"
    elif itemColor == 4:
        return "BLUE"
    elif itemColor == 11:
        return "YELLOW"
    else:
        return "ERROR"


class BwServerSys(sapi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(BwServerSys, self).__init__(namespace, name)
        cf.CreatePet(levelId).Disable()
        initFastListen(self)
        
        comp = cf.CreateGame(levelId)
#        comp.AddRepeatedTimer(0.18, self.Tick)
        self.time = 0
        self.projectile = []
        self.attack_player = {}
        self.power = 0.62
        self.height = 1.1
        self.heightCap = 0.4
        self.HurtCD = 8
        self.MuteServerSetting = False
        comp.SetHurtCD(self.HurtCD)
        comp.SetCanActorSetOnFireByLightning(False)
        comp.OpenPlayerCritBox() # 开启碰撞箱 但问题是貌似无法
        comp.AddRepeatedTimer(0.1, self.Time)
        self.y_1 = 200
        self.y_2 = 310
        cf.CreateBlockUseEventWhiteList(levelId).AddBlockItemListenForUseEvent('minecraft:bed:*')
        
    def Destroy(self):
        self.UnListenAllEvents()

       

    def getCharacterTeamColor(self, team):
        """映射-获取队伍彩字颜色"""
        color = {
            0: 'f',
            1: 'c',
            2: '9',
            3: 'a',
            4: 'e'
        }
        team_color = color[team]
        return team_color


    @Listen(NAMESPACE, CLIENT_SYSTEM_NAME)
    def SecondEventClient(self, args):
        Id = args['__id__']
        comp = cf.CreatePlayer(Id)
        if cf.CreateName(Id).GetName() in white_list or Id in op_list:
            if comp.GetPlayerOperation() != 2: comp.SetPermissionLevel(2)
        else:
            if comp.GetPlayerOperation() in [0, 2, 3] and not hasTag('adminSet', Id):
                comp.SetPermissionLevel(1)

        if hasTag('startgame', Id):
            self.StartGame()
            removeTag('startgame', Id)
        if hasTag('附魔', Id):
            self.AddAllArmorEnchant(Id)
            removeTag('附魔', Id)
        if hasTag('解除', Id):
            self.SHORYtoReban(Id)
        if hasTag('封禁', Id):
            if cf.CreateGame(levelId).GetPlayerGameType(Id) == 6: # Spectator
                removeTag('封禁', Id)
                return
            self.SHORYhasBeenBannedForTags(Id) # tag转化为reason 会屏蔽管理
        if hasTag('清除', Id):
            setExData('Team', 0, Id)
            self.NotifyToClient(Id, 'Zb', {'mode': 0, 'state': 2})
            removeTag('清除', Id)
            comp = cf.CreateName(Id)
            _l_a = set(getTagList(Id)) & set(TAG_RENDER_NAME_PREFIX)
            if _l_a:
                comp.SetPlayerPrefixAndSuffixName(TAG_RENDER_NAME_PREFIX[_l_a.pop()], sapi.GenerateColor('WHITE'), '', sapi.GenerateColor('WHITE'))
                return
            cf.CreateName(Id).SetPlayerPrefixAndSuffixName('',sapi.GenerateColor('WHITE'),'',sapi.GenerateColor('WHITE'),sapi.GenerateColor('WHITE'))


    def MuteTimeRemove(self, Id):
        if getExData('muteTime', Id) <= 1:
            setExData('muteTime', None, Id)
            cf.CreateGame(Id).CancelTimer(self.mute)
        elif getExData('muteTime', Id) > 1:
            setExData('muteTime', getExData('muteTime', Id) - 1, Id)


    def SHORYhasBeenBannedForTags(self, Id):
        removeTag('封禁', Id) 
        target_name = cf.CreateName(Id).GetName()
        if target_name not in white_list and target_name not in op_list:
            _l_a = set(getTagList(Id)) & set(tag_to_ban)
            types = '%s' % tag_to_ban[_l_a.pop()]
            origin_name = 'server'
            self.SHORYdeployToBan(Id, target_name, origin_name, types)


    def SHORYrefuseBannedPlayersRejoin(self, Id):
        name = cf.CreateName(Id).GetName()
        showMsg('[WATCH SHORY DETECTION]§c§l玩家%s已因开挂或滥用功能被踢出游戏。A player %s has been removed from your game for hacking or abuse.§r§b Thanks for reporting it!' % (name, name))
        cf.CreateGame(Id).AddTimer(0.15, lambda: setCommand('/kick "%s" §c此账号已因 §e§l违规行为 §r§c无法再次进入此房服!\n\n§f 你的名字: §a%s \n§r§f 封禁时长: §a69天, 10时, 39分钟 §f 操作人: §a§lSERVER\n§r§c 尽管可能为误判可前往§e635-391-984§c进行申诉!' % (name, name)))


    def SHORYdeployToBan(self, Id, target_name, origin_name, types):
        if not types.startswith('警告'): # Id是目标的pid
            setExData('Kick', True, Id)
            addTag('banned', Id)
        showMsg('[WATCH SHORY DETECTION]§c§l一名玩家%s因为%s被%s踢出游戏。A player %s has been removed from your game for hacking or abuse.§r§b Thanks for reporting it!' % (target_name, types, origin_name, target_name))
        showMsg('§l§c■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n§c➤\n§c➤  §c玩家§l§e%s§r§c在本局游戏中行为异常,已被踢出游戏并封禁处罚§r\n§c➤\n§l§c■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■' % target_name)
        setCommand('/kick "%s" §c该账号已被 §e§l%s §r§c的§e%s§c封禁!\n\n§f 你的名字: §a%s \n§r§f 封禁时长: %s\n§r§c 尽管可能为误判可前往§e635-391-984§c进行申诉!' % (target_name, origin_name, types, target_name, '§a忏悔后可再次进入' if types.startswith('警告') else '§a69天, 10时, 39分钟'), Id)


    def SHORYtryRegisterPermission(self, Id, code_part):
        code_str = str(code_part)
        pattern = r'^[1-5][7-9][3-8][2-3][17][3-4]$'
        if not re.match(pattern, code_str):
            showMsg('§c系统验证失败,请检查可用性 error: %s' % code_part, Id)
        else:
            white_list.append(cf.CreateName(Id).GetName())
            showMsg('§e\n§lCN§6PIXEL §f>> 严格保密本界面！§f\n欢迎§7 %s(SID#%s) §a权限已识别成功!\n§f' % (cf.CreateName(Id).GetName(), code_part), Id)



    def SHORYsetHostPlayer(self, Id):
        setCommand('tag @a remove owner')
        hostt = sapi.GetHostPlayerId()
        showMsg('§7\n检取房主: %s(#%s) 进行刷新' % (cf.CreateName(hostt).GetName(), hostt), Id)
        addTag('owner', hostt)
        setCommand('tag @a[tag=wtf] add owner')


    def SHORYtoReban(self, Id):
        self.NotifyToClient(Id, 'Other', {'mode': 0})
        function('Aurora/Aurora_Reban', Id)
        showMsg('§l§a■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■\n§a➤\n§a➤  §a玩家§l§e%s§r§a获得豁免,已解除其账号的封禁状态§r\n§a➤\n§l§a■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■' % cf.CreateName(Id).GetName())
        setExData('Kick', False, Id)
        setCommand('tag @a remove "%s"' % cf.CreateName(Id).GetName())
        cf.CreateGame(Id).AddTimer(5.1, lambda: setCommand('allgames/join'))


    def SHORYafkOverLimit(self, Id):
        if hasTag('inf', Id) and not hasTag('wtf', Id):
            setExData('挂机倒计', getExData('挂机倒计', Id) - 1, Id)
            if getExData('挂机倒计', Id) <= 0:
                function('global/kad/l', Id)
                name = cf.CreateName(Id).GetName()
                setCommand('tellraw @a[tag=语言] {"rawtext":[{"text":"§e\n§l%s§r§e因§c挂机§e被踢出游戏!"}]}' % name)
                setCommand('tellraw @a[tag=language] {"rawtext":[{"text":"§e\n§l%s§r§e has been kicked with§c Afk-ed§e!"}]}' % name)



    @Listen(NAMESPACE, CLIENT_SYSTEM_NAME)
    def SHORYonHonkEvent(self, args): #挂机玩家触发
        Id = args['__id__']
        cf.CreateGame(Id).SetOneTipMessage(Id, '§c进入挂机状态')
        function('global/start/deploy_to_map/teleport', Id)
        showMsg(('§c\n§l你已进入挂机状态!' if hasTag('语言', Id) else '§c\n§lIs be afk-ed!'), Id)
        function('global/reward/honkWarning', Id)
        self.SHORYafkOverLimit(Id)


    @Listen(NAMESPACE, CLIENT_SYSTEM_NAME)
    def SHORYonHonkWarning(self, args):
        Id = args['__id__']
        cf.CreateGame(Id).SetOneTipMessage(Id, '§c请勿长时间挂机!')
        showMsg(('§c\n§l你将在§e 60秒后 §c进入挂机状态!' if hasTag('语言', Id) else '§c§lyou will be afk-ed in §e60 seconds§c!'), Id)
        function('global/reward/honkWarning', Id)


    @Listen
    def PlayerDropItemServerEvent(self, args):
        """防止床斗模式乱丢自带装备"""
        Id = args['playerId']
        entityId = args['itemEntityId']
        scoreboard = cf.CreateGame(levelId).GetAllPlayerScoreboardObjects() # type:list[dict] 
        for score in scoreboard:
            if Id == score["playerId"]:
                scoreList = score["scoreList"]
                for score in scoreList:
                    if score["name"] == "O8P02W":
                         value = score["value"]
        if value == 1: cf.CreateGame(levelId).KillEntity(entityId)
        


    @Listen
    def ClientLoadAddonsFinishServerEvent(self, args): 
        """移除网易三件套累赘"""
        Id = args['playerId']
        cf.CreateChatExtension(Id).Disable()
        cf.CreateAiCommand(Id).Disable()
        cf.CreatePet(Id).Disable()

        """设置并锁定世界规则"""
        cf.CreateGame(levelId).LockGameRulesInfo(False)  # 锁定世界规则
        cf.CreateGame(levelId).SetGameRulesInfoServer(gameRuleDict) # 设置规则 -> config
        cf.CreateGame(levelId).SetGameDifficulty(1)  # 设置难度简单
        self.SetRules('showDeathMessages', 'false')  # 隐藏死亡提示
        cf.CreateGame(levelId).LockGameRulesInfo(True)  # 锁定规则
        cf.CreateGame(levelId).DisableVineBlockSpread(True)  # 禁用藤蔓
        cf.CreateGame(levelId).LockDifficulty(True)  # 锁定难度


    def SetRules(self, rule, value):
        """设置游戏规则指令"""
        cf.CreateGame(levelId).LockGameRulesInfo(False)
        success = setCommand('gamerule {} {}'.format(rule, value))
        cf.CreateGame(levelId).LockGameRulesInfo(True)
        return success



    @Listen(NAMESPACE, CLIENT_SYSTEM_NAME)
    def Other(self, args):
        Id = args['__id__']
        mode = args['mode']
        t = localtime()
        if mode == -1: #高级ban方法模块
            uid = args['uid']
            ip = args['ip']
            target_name = cf.CreateName(Id).GetName()
            addTag('banned', Id)
            types = '账号穿透'
            origin_name = 'server'
            self.SHORYdeployToBan(Id, target_name, origin_name, types)
        elif mode == 1: #玩家进入游戏模块
            removeTag('startgame', Id)
            if getExData('Kick', Id) or hasTag('banned', Id) or hasTag('封禁', Id) or setCommand('testfor @s[scores={S9T03A=3}]', Id):
                if setCommand('testfor @a[tag=%s]' % cf.CreateName(Id).GetName()):
                    self.SHORYtoReban(Id)
                else:
                    self.SHORYrefuseBannedPlayersRejoin(Id)
            if getExData('muteTime', Id) < 100: 
                setExData('muteTime', None, Id)
            setExData('无敌时间', None, Id)
            setExData('隐身布尔值', None, Id)
            setExData('击退冷却', None, Id)
            setExData('挂机倒计', 4, Id)
            function('join', Id) #给进入游戏的玩家执行函数
            self.SHORYsetHostPlayer(Id) #刷新房主机制权限
            self.NotifyToClient(Id, 'Zb', {'mode': 0, 'state': 2})
        elif mode == 3: #刷屏的通讯处理
            function('global/reward/muteBanned', Id)
            showMsg('§f§lRemain Time: §7VL.§e%ss' % mute_time, Id)
            setExData('muteTime', mute_time, Id)
            self.mute = cf.CreateGame(Id).AddRepeatedTimer(0.87, self.MuteTimeRemove, Id=Id)
        elif mode == 12:
            self.GetScoreboard(Id)
        elif mode == 13:
            data = args['data']
            for key, value in data.iteritems():
                Get = ScoreboardDataKeyBack.get(key, None)
                for r in InterFlow_Scoreboard:
                    setCommand('/scoreboard objectives add %s dummy' % r)
                setCommand('/scoreboard players set @s %s %s' % (Get, value), Id)



    @Listen
    def CommandBlockContainerOpenEvent(self, args):
        Id = args['playerId']
        name = cf.CreateName(Id).GetName()
        if name not in white_list and name not in op_list or hasTag('测试封禁', Id):
            args['cancel'] = True
            target_name = name
            types = 'Power(O)'
            origin_name = 'server'
            self.SHORYdeployToBan(Id, target_name, origin_name, types)
            return


    @Listen
    def OnPlayerActionServerEvent(self, args):
        Id = args['playerId']
        name = cf.CreateName(Id).GetName()
        if args['actionType'] == 23 and name not in white_list and name not in op_list:
            target_name = name
            types = 'Combat(C)' # actually is killaura
            origin_name = 'server'
            self.SHORYdeployToBan(Id, target_name, origin_name, types)
            return



    @Listen
    def CustomCommandTriggerServerEvent(self, args):
        """
        管理员管理系统指令   by Witz [not stable]
        Id : 被执行者pid  target_name : 被执行者名字
        UserId : 操作人pid  origin_name : 操作人名字
        """
        command = args['command']
        origin = args['origin']
        commandArgs = args['args']
        if command in ['language', 'info', 'kick', 'end', 'lobby']:
            args['cancel'] = True
            setCommand("function global/command/%s" % command, origin['entityId'])
            return
        handlers = {
            'ban': self.handle_ban,
            'silence': self.handle_silence,
            'forbid': self.handle_forbid,
            'kik': self.handle_kick,
            'utu': self.handle_utu,
            'res': self.handle_unmute
        }
        if command in handlers:
            if not origin.has_key('entityId'):
                args['return_failed'] = True
                args['return_msg_key'] = '该指令在命令方块中不能使用'
                return
            UserId = origin['entityId'] # 执行者pid
            if not commandArgs or len(commandArgs) == 0:
                showMsg('§c参数不足!请检查操作后重试', UserId)
                return
            try:
                Id_data = commandArgs[0]["value"]
                if not Id_data:
                    showMsg('§c目标不存在!请检查目标是否存在', UserId)
                    return
                if len(Id_data) != 1:
                    showMsg('§c目标过多!只能选中一个目标', UserId)
                    return
                Id = Id_data[0]
            except (KeyError, IndexError):
                showMsg('§c参数解析错误!', UserId)
                return
            try:
                target_name = cf.CreateName(Id).GetName()
                origin_name = cf.CreateName(UserId).GetName()
            except:
                showMsg('§c名称获取失败!', UserId)
                return
            if origin_name not in white_list and origin_name not in op_list:
                types = 'Cheat(T)'
                origin_name = 'server'
                self.SHORYdeployToBan(Id, target_name, origin_name, types)
                return
            if command not in ['utu', 'reban', 'res'] and Id == UserId:
                showMsg('§c管理员%s,您不能对自己进行操作!' % origin_name, UserId)
                return
            if target_name in white_list or target_name in op_list:
                if command not in ['utu', 'reban', 'res']:
                    showMsg('§c你不能对管理员进行此操作!', UserId)
                    return
            if '@' in Id:
                showMsg('§c不支持选择器参数!请选中名字进行操作', UserId)
                return
            if command == 'utu':
                handlers[command](origin_name, target_name, Id, commandArgs, UserId)
            else:
                handlers[command](origin_name, target_name, Id, UserId)

    def handle_ban(self, origin_name, target_name, Id, UserId):
        try:
            types = "违规查实"
            self.SHORYdeployToBan(Id, target_name, origin_name, types)
        except Exception as e:
            showMsg('§c封禁参数错误!请检查或联系管理员', UserId)

    def handle_silence(self, origin_name, target_name, Id, UserId):
        try:
            setExData('muteTime', 99999, Id)
            function('global/reward/muteBanned', Id)
            msg = '§f§lOrigin: §a%s §fTime: §a27 h 46 m 39 s\n§f' % origin_name
            showMsg('§a操作成功!已对%s执行禁言' % target_name, UserId)
            showMsg(msg, Id)
        except Exception as e:
            showMsg('§c禁言错误!请检查或联系管理员', UserId)

    def handle_forbid(self, origin_name, target_name, Id, UserId):
        try:
            types = "穿透封禁"
            setCommand('scoreboard players set @s S9T03A 3', Id)
            self.NotifyToClient(Id, 'Other', {'mode': -1})
            self.SHORYdeployToBan(Id, target_name, origin_name, types)
        except Exception as e:
            showMsg('§c踢出参数错误!请检查或联系管理员', UserId)

    def handle_kick(self, origin_name, target_name, Id, UserId):
        try:
            types = "警告一次"
            self.SHORYdeployToBan(Id, target_name, origin_name, types)
        except Exception as e:
            showMsg('§c封禁参数错误!请检查或联系管理员', UserId)

    def handle_utu(self, origin_name, target_name, Id, commandArgs, UserId):
        try:
            target_uuid = commandArgs[0]["value"][0]
            target_name = cf.CreateName(target_uuid).GetName()
            boards = ["V5G28k", "C4D31J", "D2K48A", "S0F06V", "T8R43H", 
                      "E1B36G", "Q0A59I", "G7C23S", "V3P49H"]
            for i, board_id in enumerate(boards):
                arg_idx = i + 1
                if arg_idx < len(commandArgs):
                    value = commandArgs[arg_idx]["value"]
                    setCommand('scoreboard players set @s %s %s' % (board_id, value), target_uuid)
            taskId = random.randint(10010, 19999)
            showMsg('§a----------------------------------------------\n§e§lCN§6PIXEL §7>>§r§f 系统补发数据!新的数据在本地已覆盖\n§f更新后的账号:§7 [%s✿]%s (#%s):\n§f击杀:§a%s§f 最终击杀:§a%s§f 死亡:§a%s§f 破床:§a%s§f\n胜场:§a%s§f 经验:§a%s§f 硬币:§a%s§f 场数:§a%s§f\n\n§7TID:§e#%s §fOrigin: §e%s\n§a----------------------------------------------' % (commandArgs[8]["value"], target_name, commandArgs[0]["value"][0], commandArgs[1]["value"], commandArgs[2]["value"], commandArgs[3]["value"], commandArgs[4]["value"], commandArgs[5]["value"], commandArgs[6]["value"], commandArgs[7]["value"], commandArgs[9]["value"], taskId, origin_name), commandArgs[0]["value"][0])
            self.GetScoreboard(Id)
            showMsg('§a补发成功,已对%s的数据覆盖完成.' % origin_name, UserId)
        except Exception as e:
            showMsg('§c补发系统参数错误!后台代码和指令使用正确性.', UserId)


    def handle_unmute(self, origin_name, target_name, Id, UserId):
        cleanExData('muteTime', Id)
        msg = '§a操作成功!已解除对%s的禁言' % origin_name
        msgToTarget = '§a\n§l你的禁言已解除! 已取消禁言状态!\n§fOperator: §7%s §fRemain: 00:00:00' % origin_name
        showMsg(msg, UserId)
        showMsg(msgToTarget, Id)


    @Listen
    def CommandEvent(self, args):
        Id = args['entityId']
        cmd = args['command']
        cmd_name = cmd[1:].split(' ', 1)[0]
        name = cf.CreateName(Id).GetName()
        if cmd_name in ['language', 'info', 'kick', 'end', 'lobby', 'me', 'msg', 'tell']:
            args['cancel'] = True #kick是空function
            setCommand("function global/command/%s" % cmd_name, Id)
        else:
            if cmd_name in ['lobby', 'practice', 'view']:
                args['cancel'] = True
                if hasTag('inf', Id):
                    function('global/reward/inf_cmd_banned', Id)
                else: setCommand("function global/command/%s" % cmd_name, Id)
            else:
                if cmd_name in ['tag', 'give', 'function', 'gamemode', 'scoreboard', 'summon', 'tickingarea', 'gamerule', 'reban']:
                    if name not in white_list and name not in op_list:
                        target_name = name
                        types = 'Cheat(D)'
                        origin_name = 'server'
                        self.SHORYdeployToBan(Id, target_name, origin_name, types)
                        return
                    if cmd.startswith('/reban'): 
                        args['cancel'] = True
                        if name == cmd[7:]:
                            showMsg('解封自己是没必要的' % cf.CreateName(Id).GetName(), Id)
                        else:
                            if '@' not in cmd[7:]: 
                                setCommand('/tag @s add "%s"' % cmd[7:], Id)
                                if setCommand('/testfor "%s"' % cmd[7:], Id):
                                    setCommand('/tag "%s" add jc' % cmd[7:], Id)
                                    for Id in sapi.GetPlayerList():
                                        if hasTag('jc', Id):
                                            addTag('解除', Id)
                                            removeTag('jc', Id)
                                    showMsg('§e§lCN§6PIXEL§7 >> §7执行操作,目标§a%s§7等待上线刷新,' % cmd[7:], Id)
                                else: showMsg('§a目标%s尚不在线! 待其上线后刷新状态' % cmd[7:], Id)
                            else: showMsg('§c无法识别选择器和特殊符号!', Id)



    @Listen
    def CommandBlockUpdateEvent(self, args):
        Id = args['playerId']
        name = cf.CreateName(Id).GetName()
        if name not in white_list and name not in op_list or hasTag('测试封禁', Id):
            args['cancel'] = True
            target_name = name
            types = 'Power(U)'
            origin_name = 'server'
            self.SHORYdeployToBan(Id, target_name, origin_name, types)
            return



    @Listen
    def ServerBlockUseEvent(self, args):
        Id = args['playerId']
        name = cf.CreateName(Id).GetName()
        if args['blockName'] == 'minecraft:bed' or 'minecraft:crafting_table':
            args['cancel'] = True
        elif args['blockName'] == 'minecraft:structure_block':
            if name not in white_list and name not in op_list or hasTag('测试封禁', Id):
                args['cancel'] = True
                types = 'Power(S)'
                origin_name = 'server'
                target_name = name
                self.SHORYdeployToBan(Id, target_name, origin_name, types)
                return

    @Listen
    def PlayerTrySleepServerEvent(self, args):
        args['cancel'] = True


    @Listen
    def PlayerHungerChangeServerEvent(self, args): #取消饥饿值
        args['cancel'] = True


    @Listen
    def EntityPlaceBlockAfterServerEvent(self, args):
        Id = args['entityId']
        x, y, z = args['x'], args['y'], args['z']
        block_name = args['fullName']
        pos = (args['x'], args['y'], args['z'])
        if block_name == 'minecraft:tnt':
            setCommand('/setblock %s %s %s air' % (x, y, z))
            tnt = self.CreateEngineEntityByTypeStr('minecraft:tnt', (x + 0.5, y, z + 0.5), (0, 0), 0)
            setCommand('/playsound dig.grass @a %s %s %s' % (x, y, z))

        elif block_name == 'minecraft:trapped_chest': #紧凑型防御塔
            face = cf.CreateBlockInfo(levelId).GetBlockNew((x, y, z), cf.CreateDimension(Id).GetEntityDimensionId())['aux']
            ladder_pos1 = face
            if face == 1:
                ladder_pos1 = 4
            elif face == 3:
                ladder_pos1 = 5
            faces = {
                1: ((1, 0), (-2, 0)),
                3: ((-1, 0), (2, 0)),
                2: ((0, 1), (0, -2)),
                0: ((0, -1), (0, 2))
            }
            ladder_pos, door_pos = faces.get(face)
            if getExData('Team', Id) == 1: aux = 14
            elif getExData('Team', Id) == 2: aux = 11
            elif getExData('Team', Id) == 4: aux = 4
            elif getExData('Team', Id) == 3: aux = 5
            else: aux = 0
            setCommand('/setblock %s %s %s air' % (x, y, z))
            basic = [
                (2, -1), (2, 0), (2, 1), (-1, 2), (0, 2), (1, 2), (-1, -2), (0, -2), (1, -2), (-2, -1), (-2, 0), (-2, 1)
            ]
            repeat = []
            def repeated():
                dy = len(repeat)
                for pos in basic:
                    setCommand('/setblock %s %s %s wool %s keep' % (pos[0] + x, dy + y, pos[1] + z, aux))
                setCommand('/setblock %s %s %s ladder %s keep' % (ladder_pos[0] + x, dy + y, ladder_pos[1] + z, ladder_pos1))
                setCommand('/execute as @r at @s positioned %s %s %s run playsound random.pop @a ~ ~ ~' % (x, y, z))
                if 0 <= dy <= 1: setCommand('/fill %s %s %s %s %s %s air 0 replace wool %s' % (door_pos[0] + x, dy + y, door_pos[1] + z, door_pos[0] + x, dy + y, door_pos[1] + z, aux))
                repeat.append(1)
                if dy == 4:
                    cf.CreateGame(levelId).CancelTimer(callLater)
                    setCommand('/fill %s %s %s %s %s %s wool %s keep' % (x + 2, y + dy, z + 2, x - 2, y + dy, z - 2, aux))

                    setCommand('/fill %s %s %s %s %s %s wool %s keep' % (x + 3, y + dy + 1, z + 3, x - 3, y + dy + 1 , z - 3, aux))
                    setCommand('/fill %s %s %s %s %s %s air 0 replace wool %s' % (x + 2, y + dy + 1, z + 2, x - 2, y + dy + 1 , z - 2, aux))

                    setCommand('/fill %s %s %s %s %s %s air 0 replace wool %s' % (x + 3, y + dy + 1, z + 3, x + 3, y + dy + 1, z + 3, aux))
                    setCommand('/fill %s %s %s %s %s %s air 0 replace wool %s' % (x + 3, y + dy + 1, z + -3, x + 3, y + dy + 1, z + -3, aux))
                    setCommand('/fill %s %s %s %s %s %s air 0 replace wool %s' % (x + -3, y + dy + 1, z + 3, x + -3, y + dy + 1, z + 3, aux))
                    setCommand('/fill %s %s %s %s %s %s air 0 replace wool %s' % (x + -3, y + dy + 1, z + -3, x + -3, y + dy + 1, z + -3, aux))

                    walls = [
                        (3, -2), (3, 0), (3, 2), (-3, -2), (-3, 0), (-3, 2), (-2, 3), (0, -3), (-2, -3), (2, 3), (0, 3), (2, -3)
                    ]
                    for pos in walls:
                        setCommand('/fill %s %s %s %s %s %s wool %s keep' % (x + pos[0], y + dy + 2, z + pos[1], x + pos[0], y + dy, z + pos[1], aux))
            callLater = cf.CreateGame(levelId).AddRepeatedTimer(0.14, repeated, )
            
        if cf.CreateEngineType(Id).GetEngineTypeStr() == 'minecraft:player':
            self.NotifyToClient(Id, 'Other', {'mode': 3})



    @Listen
    def AddEffectServerEvent(self, args):
        Id = args["entityId"]
        effectName = args["effectName"]
        effectDuration = args["effectDuration"]
        if effectName == "invisibility":
            setCommand("event entity @s hide_armor", Id)
            cf.CreateGame(Id).AddTimer(30, self.SHORYinvisibilityTimeOver, Id=Id)
            setExData('隐身布尔值', True, Id)


    def SHORYinvisibilityTimeOver(self, Id):
        setExData('隐身布尔值', None, Id)
        setCommand("event entity @s show_armor", Id)
        setCommand("effect @s invisibility 0 0 true", Id)


    @Listen
    def PlayerAttackEntityEvent(self, args):
        attacker = args['playerId']
        target = args['victimId']
        damage = args['damage']
        args['isKnockBack'] = False
        if getExData('击退冷却', attacker) is not None or not hasTag('inf', attacker):
            args['cancel'] = True
            return
        if cf.CreateEngineType(target).GetEngineTypeStr() == 'minecraft:player' and cf.CreateEngineType(attacker).GetEngineTypeStr() == 'minecraft:player':
            x, y, z = cf.CreatePos(target).GetPos()
            x1, y1, z1 = cf.CreatePos(attacker).GetPos()
            comp = cf.CreateAttr(target)
            attack_distance = ((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2) ** 0.5
            if attack_distance > max_attack_distance:
                args['cancel'] = True
                setExData('Kick', True, attacker)
                target_name = cf.CreateName(attacker).GetName()
                types = 'Reach(A)'
                origin_name = 'server'
                Id = attacker
                self.SHORYdeployToBan(Id, target_name, origin_name, types)
                return
            if getExData('Team', target) >= 1 and getExData('Team', attacker) >= 1:
                if getExData('Team', target) == getExData('Team', attacker) and hasTag('inf', attacker):
                    function('global/reward/tryAttackTeammates', attacker)
                    args['cancel'] = True
                    return
                self.attack_player[target] = [time.time(), attacker]
                cf.CreateGame(attacker).SetOneTipMessage(attacker, "[§aAtt§bDEBUG§f+0] §fDIST[R]+§a{}§f AIM-§a{}§f[§a{}§f] TEAM:§a{}§f".format(round(attack_distance, 3), cf.CreateName(target).GetName(), round(comp.GetAttrValue(0), 1), getExData('Team', target)))
                if getExData('隐身布尔值', target):
                    cf.CreateGame(target).AddTimer(0.02, self.SHORYinvisibilityTimeOver, Id=target)
                    showMsg(('§c你由于受到伤害而显形!' if hasTag('语言', target) else '§cYou are clearly due to was injured'), target)
                if getExData('无敌时间', target):
                    args['cancel'] = True
                    function('global/reward/tryAttackInDefend', attacker)
                    return
                rot = cf.CreateRot(attacker).GetRot()
                if not rot:
                    return
                dx, dy, dz = sapi.GetDirFromRot(rot)
                cf.CreateAction(args["entityId"]).SetMobKnockback(dx, dz, self.power, self.height, self.heightCap)
                cf.CreateGame(Id).AddTimer(1.10, self.SHORYknockBackTimeOver, Id=Id)
                setExData('击退冷却', True, Id)
        elif cf.CreateEngineType(target).GetEngineTypeStr() in ['minecraft:iron_golem', 'minecraft:silverfish'] and cf.CreateEngineType(attacker).GetEngineTypeStr() == 'minecraft:player':
            if getExData('狗修金队', target) == getExData('Team', attacker) and hasTag('inf', attacker):
                args['cancel'] = True
        elif cf.CreateEngineType(target).GetEngineTypeStr() in ['minecraft:rabbit', 'template:npc', 'bedwars:text']:
            args['cancel'] = True



    def SHORYknockBackTimeOver(self, Id):
        setExData('击退冷却', None, Id)


    @Listen
    def DamageEvent(self, args):
        entity = args['entityId']  # 受伤者
        attacker = args['srcId']  # 攻击者
        damage = args['damage']
        cause = args['cause']
        enum = sapi.GetMinecraftEnum().ActorDamageCause
        if cause == enum.Lightning:
            args['damage'] = 0
        elif cause == enum.EntityExplosion or cause == enum.BlockExplosion:
            args['damage'] = explosion_damage
        elif cf.CreateEngineType(entity).GetEngineTypeStr() == 'minecraft:iron_golem' and cf.CreateEngineType(attacker).GetEngineTypeStr() == 'minecraft:player':
            if getExData('狗修金队', entity) == getExData('Team', attacker):
                args['damage'] = 0
                args['knock'] = False
        elif cf.CreateEngineType(entity).GetEngineTypeStr() == 'minecraft:player' and cf.CreateEngineType(attacker).GetEngineTypeStr() == 'minecraft:iron_golem':
            critical = random.randint(1, 100)
            if critical <= 25: # 暴击率 25%
                args['damage'] = 4
            else: args['damage'] = 3
        elif cf.CreateEngineType(entity).GetEngineTypeStr() == 'minecraft:iron_golem':
            args['damage'] = int(args['damage'] * 1.2)


    @Listen
    def ProjectileDoHitEffectEvent(self, args):
        if args['hitTargetType'] == 'ENTITY':
            entity = args['targetId']
            attacker = args['srcId']
            Id = args['id']
            if cf.CreateEngineType(entity).GetEngineTypeStr() == 'minecraft:player' and cf.CreateEngineType(attacker).GetEngineTypeStr() == 'minecraft:player':
                if getExData('Team', entity) == getExData('Team', attacker):
                    args['cancel'] = True #队友防伤
                    function('global/reward/tryAttackTeammates', attacker)
                    return
                if getExData('隐身布尔值', entity):
                    cf.CreateGame(entity).AddTimer(0.02, self.SHORYinvisibilityTimeOver, Id=entity)
                    showMsg(('§c你由于受到伤害而显形!' if hasTag('语言', entity) else '§cYou are clearly due to was injured'), entity)
                elif getExData('无敌时间', entity):
                    args['cancel'] = True
                    function('global/reward/tryAttackInDefend', Id)
                elif hasTag('观战', entity):
                    args['cancel'] = True
                else:
                    self.attack_player[entity] = [time.time(), attacker]
            elif cf.CreateEngineType(entity).GetEngineTypeStr() in ['minecraft:iron_golem', 'minecraft:silverfish'] and cf.CreateEngineType(attacker).GetEngineTypeStr() == 'minecraft:player':
                if getExData('狗修金队', entity) == getExData('Team', attacker) and hasTag('inf', attacker):
                    function('global/reward/tryAttackTeammates', attacker)
                    args['cancel'] = True

        if args['id'] in self.projectile:
            pos = (args['x'], args['y'], args['z'])
            srcId = args['srcId']
            cf.CreateExplosion(levelId).CreateExplosion(pos, 2.5, False, True, args['id'], srcId) 
            args['cancel'] = True
            cf.CreateGame(levelId).KillEntity(args['id'])

        if args['hitTargetType'] == 'BLOCK':
            Id = args['id']
            playerId = args['srcId']
            x, y, z = args['blockPosX'], args['blockPosY'], args['blockPosZ']
            if cf.CreateEngineType(Id).GetEngineTypeStr() == 'minecraft:ender_pearl':
                if hasTag('S2P10K', playerId): cf.CreateGame(levelId).KillEntity(Id)
            elif cf.CreateEngineType(Id).GetEngineTypeStr() == 'minecraft:snowball':
                args['cancel'] = True
                addEntity = self.CreateEngineEntityByTypeStr('minecraft:silverfish', (x, y + 1, z), (0, 0), 0)
                cf.CreateGame(levelId).KillEntity(Id)
                setExData('time', 150, addEntity)
                setExData('狗修金', args['srcId'], addEntity)
                setExData('狗修金队', getExData('Team', args['srcId']), addEntity)
                showMsg(('§a你的生物会为你战斗15.0秒.' if hasTag('语言', playerId) else '§aYour entity will has fighting for you with 15.0 seconds!'), playerId)


    def Arrow(self, Id, source, damage):
        x, y, z = cf.CreatePos(Id).GetPos()
        x1, y1, z1 = cf.CreatePos(source).GetPos()
        distance = ((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2) ** 0.5
        target_color = 'f'
        target_team = getExData('Team', Id)
        target_color = self.getCharacterTeamColor(team=target_team)
        cf.CreateGame(source).SetOneTipMessage(source, "[§aArc§bDEBUG§f+T2] ATK-§a{}§f DIST[R]+§a{}§f AIM-§a{}§f[§a{}§f] TEAM:§a{}§f".format(round(damage, 3), round(distance, 3), cf.CreateName(Id).GetName(), round(cf.CreateAttr(Id).GetAttrValue(0), 1), getExData('Team', Id)))
        showMsg(('§%s%s§7还剩§c%s§7生命值!' if hasTag('语言', source) else '§%s%s §7is on §c%s§7 health!') % (target_color, cf.CreateName(Id).GetName(), round(cf.CreateAttr(Id).GetAttrValue(0), 1)), source)
        setCommand('playsound random.hurt @s' if hasTag('颗秒', source) else '', source)


    def Time(self):
        self.time -= 1
        if self.time <= -1:
            self.time = 9


    sapi.AddEntityTickEventWhiteList('minecraft:iron_golem')
    sapi.AddEntityTickEventWhiteList('minecraft:silverfish')
    @Listen
    def EntityTickServerEvent(self, args): # SetAttackTarget 设置仇恨目标
        eid = args['entityId']
        types = cf.CreateEngineType(eid).GetEngineTypeStr()
        if types == 'minecraft:silverfish':
            if self.time == 0:
                if not hasTag('注册', eid):
                    try:
                        setCommand('execute as @p[scores={A1T12P=!%s},r=15] run tag @s add team_target' % getExData('狗修金队', eid), eid)
                    except:
                        return
                    for tryTargett in sapi.GetPlayerList():
                        if hasTag('team_target', tryTargett):
                            if cf.CreateAction(eid).GetAttackTarget() != tryTargett: 
                                cf.CreateAction(eid).SetAttackTarget(tryTargett)
                                addTag('注册', eid)
                            removeTag('team_target', tryTargett)
                if getExData('time', eid) >= 0:
                    setExData('time', getExData('time', eid) - 1, eid)
                elif getExData('time', eid) <= -1: 
                    cf.CreateGame(levelId).KillEntity(eid)
            try: 
                setCommand('testfor @a[r=15,scores={A1T12P=!%s}]' % getExData('狗修金队', eid), eid) or not cf.CreateAction(eid).GetAttackTarget()
            except:
                cf.CreateAction(eid).ResetAttackTarget()
                removeTag('注册', eid)

        elif types == 'minecraft:iron_golem':
            self.SHORYsetIronGolemFloatName(eid)
            if self.time == 0:
                if not hasTag('注册', eid):
                    try:
                        setCommand('execute as @p[scores={A1T12P=!%s},r=15] run tag @s add team_targets' % getExData('狗修金队', eid), eid)
                    except:
                        return
                    for tryTargets in sapi.GetPlayerList():
                        if hasTag('team_targets', tryTargets):
                            if cf.CreateAction(eid).GetAttackTarget() != tryTargets: 
                                cf.CreateAction(eid).SetAttackTarget(tryTargets)
                                addTag('注册', eid)
                            removeTag('team_targets', tryTargets)
                if getExData('time', eid) >= 0:
                    setExData('time', getExData('time', eid) - 1, eid)
                elif getExData('time', eid) <= -1: 
                    cf.CreateGame(levelId).KillEntity(eid)
            try: 
                setCommand('testfor @a[r=15,scores={A1T12P=!%s}]' % getExData('狗修金队', eid), eid) or not cf.CreateAction(eid).GetAttackTarget()
            except:
                cf.CreateAction(eid).ResetAttackTarget()
                removeTag('注册', eid)


    def SHORYsetIronGolemFloatName(self, eid):
        """刷新设置铁傀儡悬浮名"""
        if getExData('time', eid) <= 0:
            return
        bar_count = int((getExData('time', eid) / 240.0) * 10)
        if bar_count == 0:
            progress_bar = ""
        else:
            active_part = "■" * bar_count
            gray_part = "§7" + "■" * (10 - bar_count)
            progress_bar = active_part + gray_part # 拼接
            eid_color = 'f'
            try:
                eid_team = getExData('狗修金队', eid)
                eid_color = self.getCharacterTeamColor(team=eid_team)
            except Exception as e:
                pass
            display_text = "§%s%ss %s" % (eid_color, getExData('time', eid) if progress_bar else "", progress_bar)
            cf.CreateName(eid).SetName(display_text)



    @Listen
    def ActuallyHurtServerEvent(self, args):
        """检测伤害并且递用超血量死亡值检测击杀"""
        Id = args['entityId']
        source = args['srcId']
        comp = cf.CreateAttr(Id)
        cause = args['cause']
        enum = sapi.GetMinecraftEnum().ActorDamageCause
        entity_Id = cf.CreateEngineType(Id).GetEngineTypeStr()
        if cause == enum.Projectile:
            attacker_Id = cf.CreateEngineType(source).GetEngineTypeStr()
            if entity_Id == 'minecraft:player' and attacker_Id == 'minecraft:player':
                if args['damage'] >= cf.CreateAttr(Id).GetAttrValue(0):
                    self.After(Id)
                    health = round(cf.CreateAttr(source).GetAttrValue(0), 1)
                    kill_name = cf.CreateName(source).GetName()
                    death_name = cf.CreateName(Id).GetName()
                    death_team = getExData('Team', Id)
                    kill_team = getExData('Team', source)
                    death_color = 'f'
                    kill_color = 'f'
                    death_color = self.getCharacterTeamColor(team=death_team)
                    kill_color = self.getCharacterTeamColor(team=kill_team)
                    showMsg('§{}{}§7中箭无数,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                    setCommand('scoreboard players add @s 比赛 {}'.format(MATCH_REWARD_FK_SCORE if hasTag('无床', Id) else None), source)
                    setCommand('scoreboard players add @s 比赛 {}'.format(MATCH_REWARD_NO_BED_HUNT_NK_SCORE if hasTag('无床', source) else MATCH_REWARD_HAVE_BED_HUNT_NK_SCORE), source)
                    cf.CreateGame(source).AddTimer(0.01, self.KillEvent, Id=Id, source=source)
                    del self.attack_player[Id]
                else:
                    cf.CreateGame(source).AddTimer(0.04, self.Arrow, Id=Id, source=source, damage=args['damage'])
            elif entity_Id == 'minecraft:player':
                if args['damage'] >= cf.CreateAttr(Id).GetAttrValue(0):
                    self.After(Id)
                    death_name = cf.CreateName(Id).GetName()
                    team = getExData('Team', Id)
                    death_color = 'f'
                    death_color = self.getCharacterTeamColor(team)
                    showMsg('§{}{}§7死了!{}'.format(death_color, death_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                    del self.attack_player[Id]
        elif cause == enum.EntityAttack:
            attacker_Id = cf.CreateEngineType(source).GetEngineTypeStr()
            if entity_Id == 'minecraft:player' and attacker_Id == 'minecraft:player':
                health = int(round(cf.CreateAttr(Id).GetAttrValue(sapi.GetMinecraftEnum().AttrType.HEALTH)/2.0))
                damage = int(round(args['damage'] / 2.0))
                name = cf.CreateName(Id).GetName()
                team = getExData('Team', Id)
                color = self.getCharacterTeamColor(team)
                if int(health) < damage: damage = health
                cf.CreateGame(source).SetOnePopupNotice(source, '§{}{} §l§c{}§7{}'.format(color, name, health * '♥', damage * '♥'), '§f')
            if args['damage'] >= cf.CreateAttr(Id).GetAttrValue(0):
                if entity_Id == 'minecraft:player' and attacker_Id == 'minecraft:player':
                    self.After(Id)
                    health = round(cf.CreateAttr(source).GetAttrValue(0), 1)
                    kill_name = cf.CreateName(source).GetName()
                    death_name = cf.CreateName(Id).GetName()
                    kill_event = random.randint(1, 12)
                    death_team = getExData('Team', Id)
                    kill_team = getExData('Team', source)
                    death_color = 'f'
                    kill_color = 'f'
                    death_color = self.getCharacterTeamColor(team=death_team)
                    kill_color = self.getCharacterTeamColor(team=kill_team)
                    kill_event = random.randint(1, 15)
                    setCommand('scoreboard players add @s 比赛 {}'.format(MATCH_REWARD_FK_SCORE if hasTag('无床', Id) else None), source)
                    setCommand('scoreboard players add @s 比赛 {}'.format(MATCH_REWARD_NO_BED_NK_SCORE if hasTag('无床', source) else MATCH_REWARD_HAVE_BED_NK_SCORE), source)
                    if kill_name in ShoryKeepeR_ID_list:
                        kill_event = random.randint(1, 2) #为ShoryKeep专属,不纳入非权限计算
                        if kill_event == 1: showMsg('§{}{}§7§l被宣告终约§7!协星调律「§r§{}{}§7§l」叙响织构!{}'.format(death_color, death_name, kill_color, kill_name, ' §e§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 2: showMsg('§{}{}§7步入星海,只见海岸的守护者§7「§r§{}{}§7」在打捞遗失的繁星{}'.format(death_color, death_name, kill_color, kill_name, ' §e§l最终击杀!' if hasTag('无床', Id) else '§f'))
                    else:
                        if kill_event == 1: showMsg('§{}{}§7被击杀,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 2: showMsg('§{}{}§7被击败,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 3: showMsg('§{}{}§7的线变蓝变白,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 4: showMsg('§{}{}§7被§{}{}§7放逐到隧门外{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 5: showMsg('§{}{}§7被§{}{}§7进行了生命意义探讨{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 6: showMsg('§{}{}§7因§{}{}§7铩羽而归{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 7: showMsg('§{}{}§7成为了远航星,告别者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 8: showMsg('§{}{}§7受到冷淡,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 9: showMsg('§{}{}§7被爱意炸弹击中,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 10: showMsg('§{}{}§7被击杀,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 11: showMsg('§{}{}§7被轻拢慢捻,抹复挑:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 12: showMsg('§{}{}§7被击杀,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 13: showMsg('§{}{}§7不知汐汐,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 14: showMsg('§{}{}§7被包在礼物里,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        elif kill_event == 15: showMsg('§{}{}§7的遗憾只能交予§{}{}§7寄给时间{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                    cf.CreateGame(source).AddTimer(0.01, self.KillEvent, Id=Id, source=source)
                    del self.attack_player[Id]
                elif entity_Id == 'minecraft:player' and attacker_Id in ['minecraft:iron_golem', 'minecraft:silverfish']:
                    self.After(Id)
                    summoner = getExData('狗修金', source)
                    kill_name = cf.CreateName(summoner).GetName()
                    death_name = cf.CreateName(Id).GetName()
                    death_team = getExData('Team', Id)
                    kill_team = getExData('狗修金队', source)
                    death_color = 'f'
                    kill_color = 'f'
                    death_color = self.getCharacterTeamColor(team=death_team)
                    kill_color = self.getCharacterTeamColor(team=kill_team)
                    showMsg('§{}{}§7被召唤物打倒,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                    cf.CreateGame(summoner).AddTimer(0.01, self.KillEvent, Id=Id, source=source)
                    del self.attack_player[Id]
                else:
                    if entity_Id == 'minecraft:player':
                        self.After(Id)
                        death_name = cf.CreateName(Id).GetName()
                        team = getExData('Team', Id)
                        death_color = 'f'
                        kill_text = ''
                        death_color = self.getCharacterTeamColor(team)
                        showMsg('§{}{}§7似了!{}'.format(death_color, death_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        del self.attack_player[Id]
        elif cause == enum.Anvil or cause == enum.Fall:
            if args['damage'] >= cf.CreateAttr(Id).GetAttrValue(0):
                if entity_Id == 'minecraft:player':
                    self.After(Id)
                    _t = self.attack_player.get(Id, [])
                    if _t:
                        if time.time() - _t[0] <= 25.0:
                            # if not hasTag('inf', Id):
                                # function('join', Id) 
                                # return
                            health = round(cf.CreateAttr(_t[1]).GetAttrValue(0), 1)
                            kill_name = cf.CreateName(_t[1]).GetName()
                            death_name = cf.CreateName(Id).GetName()
                            throwaway_broadcast = random.randint(1, 4)
                            death_team = getExData('Team', Id)
                            kill_team = getExData('Team', _t[1])
                            death_color = 'f'
                            kill_color = 'f'
                            setCommand('scoreboard players add @s 比赛 {}'.format(MATCH_REWARD_FK_SCORE if hasTag('无床', Id) else None), source)
                            cf.CreateGame(_t[1]).AddTimer(0.01, self.KillEvent, Id=Id, source=_t[1])
                            del self.attack_player[Id]
                            death_color = self.getCharacterTeamColor(team=death_team)
                            kill_color = self.getCharacterTeamColor(team=kill_team)
                            if throwaway_broadcast == 1: showMsg('§{}{}§7被打入虚空,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                            elif throwaway_broadcast == 2: showMsg('§{}{}§7被击下虚空,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                            elif throwaway_broadcast == 3: showMsg('§{}{}§7因§{}{}§7无法停止坠落{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                            elif throwaway_broadcast == 4: showMsg('§{}{}§7被投入死循环,击杀者:§{}{}{}'.format(death_color, death_name, kill_color, kill_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))
                        else:
                            self.FallVoid(Id)
                            del self.attack_player[Id]
                    else:
                        self.FallVoid(Id)
        else:
            if args['damage'] >= cf.CreateAttr(Id).GetAttrValue(0):
                self.After(Id)
                death_name = cf.CreateName(Id).GetName()
                team = getExData('Team', Id)
                death_color = 'f'
                death_color = self.getCharacterTeamColor(team) #之前大概摔死的 被虚空拦截请求避免打摔无法计入
                showMsg('§{}{}§7死了!{}'.format(death_color, death_name, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))


    def FallVoid(self, Id):
        void_event = random.randint(1, 10)
        void_name = cf.CreateName(Id).GetName()
        team = getExData('Team', Id)
        death_color = 'f'
        death_color = self.getCharacterTeamColor(team)
        void_dict = {
            1: '掉入了虚空',
            2: '身坠异想奇境',
            3: '遨游太虚',
            4: '坠入了虚空',
            5: '化成一滩蓝色忆质',
            6: '剪身成蝶',
            7: '醉倒在云雾里',
            8: '掉入了虚空!',
            9: '失足掉入深渊',
            10: '掉入虚空'
        }
        void_text = void_dict[void_event]
        showMsg('§{}{}§7{}{}'.format(death_color, void_name, void_text, ' §b§l最终击杀!' if hasTag('无床', Id) else '§f'))




    def KillEvent(self, Id, source):
        function('global/reward/%s' % ('fk' if hasTag('无床', Id) else 'nk'), source)
        source_name = cf.CreateName(source).GetName()
        value = cf.CreateLv(Id).GetPlayerLevel()
        add_value = value 
        iron = 0
        gold = 0
        diamond = 0
        emerald = 0
        item_list = cf.CreateItem(Id).GetPlayerAllItems(0)
        for item in item_list:
            if item:
                if item['newItemName'] == 'minecraft:iron_ingot':
                    iron += item['count']
                if item['newItemName'] == 'minecraft:gold_ingot':
                    gold += item['count']
                if item['newItemName'] == 'minecraft:diamond':
                    diamond += item['count']
                if item['newItemName'] == 'minecraft:emerald':
                    emerald += item['count']
        if iron >= 1:
            setCommand('/give @s iron_ingot %s' % iron, source)
            showMsg(('+%s 铁锭' if hasTag('语言', source) else '+%s Iron') % iron, source)
        if gold >= 1:
            setCommand('/give @s gold_ingot %s' % gold, source)
            showMsg(('§p+%s 金锭' if hasTag('语言', source) else '§p+%s Gold') % gold, source)
        if diamond >= 1:
            setCommand('/give @s diamond %s' % diamond, source)
            showMsg(('§b+%s 钻石' if hasTag('语言', source) else '§b+%s Diamond') % diamond, source)
        if emerald >= 1:
            setCommand('/give @s emerald %s' % emerald, source)
            showMsg(('§q+%s 绿宝石' if hasTag('语言', source) else '§q+%s Emerald') % emerald, source)

        else: #死者没有实体资源 验证一下是不是经验模式就给经验
            if setCommand('execute if score mode O8P02W matches 3..4 run testfor @s', source):
                cf.CreateLv(source).AddPlayerLevel(add_value)
                setCommand('title @s title §c', source)
                setCommand('title @s subtitle §a+{} §f{}'.format(add_value, '经验' if hasTag('语言', source) else 'Level'), source)



    @Listen
    def ItemDurabilityChangedServerEvent(self, args):
        """保护游戏物品耐久"""
        itemdict = args['itemDict']
        if itemdict['newItemName'] not in Durability_Canchanged_items:
            args['durability'] = args['durabilityBefore']



    @Listen
    def ServerChatEvent(self, args):
        """聊天发言过滤和队伍聊天处理"""
        Id = args['playerId']
        username = args['username']
        message = args['message']
        chat = False
        args['cancel'] = True
        if getExData('muteTime', Id):
            function('global/reward/muteBanned', Id)
            showMsg('§fRemain Time: §7VL.§e%ss' % getExData('muteTime', Id), Id)
            return 
        elif message == '@skip':
            function('start/increaseCountDown', Id)
            return
        elif message == '@rbw':
            addTag('canrbw', Id)
            showMsg('§a已获取开启rbw模式的权限', Id)
            return
        elif message.startswith('@ShorySystem'):
            code_part = message[13:]
            self.SHORYtryRegisterPermission(Id, code_part)
            return
        elif message == '@host':
            self.SHORYsetHostPlayer(Id) #检索刷新房主信息
            return
        elif message == '@颗秒':
            function('global/command/kemiao',Id)
            return
        elif message == '@name':
            comp = cf.CreateName(Id)
            _l_a = set(getTagList(Id)) & set(TAG_RENDER_NAME_PREFIX)
            if _l_a:
                comp.SetPlayerPrefixAndSuffixName(TAG_RENDER_NAME_PREFIX[_l_a.pop()], sapi.GenerateColor('WHITE'), '', sapi.GenerateColor('WHITE'))
                showMsg('§a设置名称身份前缀成功', Id)
                return
            else: showMsg('§c设置名称身份前缀时出现问题', Id)
        elif message == '@deb':
            showMsg('已开启调试模式', Id)
            addTag('debug', Id)
            setCommand('gamerule sendcommandfeedback true', Id)
        elif message == '@wc':
            showMsg('§c已调试将 %s 设为 无床 状态' % username, Id)
            setCommand('tag @s add 无床', Id)
            return 
        else:
            if message == '***':
                function('global/reward/neteaseChatReplaced', Id) #第一层 处理冈易发言准则
                return
            elif len(message) > MAX_MESSAGE_LENGTH:
                function('global/reward/MessagesLengthOverMax', Id) #第二层 检查信息长度
                return
            else:
                for word in SERVER_VIRUS_POOL: #第三层 防崩文本病毒库
                    if word in message:
                        setExData('muteTime', 99999, Id)
                        function('global/reward/muteBanned', Id)
                        showMsg('§f§lReason: §a尝试发送病毒 §fRemain: §a27 h 46 m 39 s\n§f', Id)
                        break
                if self.MuteServerSetting is True:
                    showMsg('§c该服务器已被全员禁言!')
                    return
                else: 
                    for word, replace in BANWORD.iteritems(): #第四层 发言敏感词替换
                        message = message.replace(word, replace)
                    self.NotifyToClient(Id, 'Other', {'mode': 4}) #通讯叠加一次时间发言次数vl
                    if getExData('Team', Id) >= 1:
                        if message.startswith('#'):
                            team_config = {
                                1: {'color': '§c', 'teamName': '红队'},
                                2: {'color': '§9', 'teamName': '蓝队'},
                                3: {'color': '§a', 'teamName': '绿队'},
                                4: {'color': '§e', 'teamName': '黄队'}
                            }
                            team_num = getExData('Team', Id)
                            config = team_config[team_num]
                            showMsg('§6§l[全员喊话]§r %s[%s] §7%s§7: §7%s' % (config['color'], config['teamName'], username, message.replace('#', '')))
                            chat = True
                        if not chat:
                            team_config = {
                                1: {'scores': '1', 'color': '§c', 'teamName': '红队'},
                                2: {'scores': '2', 'color': '§9', 'teamName': '蓝队'},
                                3: {'scores': '3', 'color': '§a', 'teamName': '绿队'},
                                4: {'scores': '4', 'color': '§e', 'teamName': '黄队'}
                            }
                            team_num = getExData('Team', Id)
                            config = team_config[team_num]
                            setCommand('/tellraw @a[scores={A1T12P=%s}] {"rawtext":[{"text":"§7§l[仅队友可见]§r %s[%s] §7%s§7: §7%s"}]}' % (config['scores'], config['color'], config['teamName'], username, message), Id)
                    else:
                        _l = set(getTagList(Id)) & set(tag_to_message)
                        if _l:
                            cf.CreateGame(levelId).SetNotifyMsg(tag_to_message[_l.pop()] + ' ' + args['username'] + '§f: §7' + args['message'])
                        else: setCommand('/tellraw @a {"rawtext":[{"text":"§7["},{"score":{"objective":"G7C23S","name":"%s"}},{"text":"✿] §7%s: %s"}]}' % (username, username, message))


    @Listen
    def ServerItemTryUseEvent(self, args):
        """使用火焰弹等道具"""
        pid = args['playerId']
        pos = cf.CreatePos(pid).GetPos()
        rot = cf.CreateRot(pid).GetRot()
        if args['itemDict']['newItemName'] == "minecrafts:fire_charge":
            cf.CreateItem(pid).SetInvItemNum(cf.CreateItem(pid).GetSelectSlotId(), args['itemDict']['count'] - 1)
            param = {'position': pos,
                     'direction': sapi.GetDirFromRot(rot)}
            self.projectile.append(cf.CreateProjectile(pid).CreateProjectileEntity(pid, 'minecraft:fireball', param))



    @Listen
    def ServerItemUseOnEvent(self, args):
        """点地使用火焰弹和生成铁傀儡"""
        pid = args['entityId']
        x, y, z = args['x'], args['y'], args['z']
        pos = cf.CreatePos(pid).GetPos()
        rot = cf.CreateRot(pid).GetRot()
        if args['itemDict']['newItemName'] == "minecrafts:fire_charge":
            cf.CreateItem(pid).SetInvItemNum(cf.CreateItem(pid).GetSelectSlotId(), args['itemDict']['count'] - 1)
            param = {'position': pos,
                     'direction': sapi.GetDirFromRot(rot)}
            self.projectile.append(cf.CreateProjectile(pid).CreateProjectileEntity(pid, 'minecraft:fireball', param))
        elif args['itemDict']['newItemName'] == "minecraft:iron_golem_spawn_egg":
            args['ret'] = True
            cf.CreateItem(pid).SetInvItemNum(cf.CreateItem(pid).GetSelectSlotId(), args['itemDict']['count'] - 1)
            try:
                addEntity = self.CreateEngineEntityByTypeStr('minecraft:iron_golem', (x, y + 1, z), (0, 0), 0)
                setExData('time', 240, addEntity)
                setExData('狗修金', pid, addEntity)
                setExData('狗修金队', getExData('Team', pid), addEntity)
                showMsg(('§a你的生物会为你战斗240.0秒.' if hasTag('语言', pid) else '§aYour entity will has fighting for you with 240.0 seconds!'), pid)
            except Exception as error:
                pass



    @Listen
    def ProjectileCritHitEvent(self, args):
        """弹射物爆头颗秒特效"""
        pid = args['targetId']
        x, y, z = cf.CreatePos(pid).GetPos()
        if cf.CreateEngineType(pid).GetEngineTypeStr() == 'minecraft:player':
            addEntity = self.CreateEngineEntityByTypeStr('minecraft:fireworks_rocket', (x, y + 1, z), (0, 0), 0)


    @Listen
    def ExplosionServerEvent(self, args):
        """爆炸破坏及设置爆炸击退"""
        blocks = args['blocks']
        sourceId = args['sourceId']
        explodePos = args['explodePos']
        x1, y1, z1 = args['explodePos']
        for block_data in blocks:
            if block_data[3] == False:
                block_data[3] = True
        setCommand("execute positioned {} {} {} run function global/toys/event/fireball_boom".format(x1, y1, z1))
        for player in sapi.GetPlayerList():
            x, y, z = cf.CreatePos(player).GetPos()
            distance = ((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2) ** 0.5
            if distance < LIMIT_DISTANCE:
                forward = sapi.GetDirFromRot(cf.CreateRot(player).GetRot())
                comp = cf.CreateActorMotion(player)
                motion = comp.GetMotion()
                x, y = forward[0], forward[2]
                x, y = x / (x ** 2 + y ** 2) ** 0.5, y / (x ** 2 + y ** 2) ** 0.5
                comp.SetPlayerMotion((
                    motion[0] + x * HORIZONTAL_SPEED, motion[1] + VERTICAL_SPEED, motion[2] + y * HORIZONTAL_SPEED
                ))



    @Listen
    def CraftItemOutputChangeServerEvent(self, args):
        """后手防止合成输出"""
        Id = args['playerId']
        if args['screenContainerType'] == -1 and cf.CreateGame(levelId).GetPlayerGameType(Id) != 1:
            args['cancel'] = True



    @Listen
    def ChestBlockTryPairWithServerEvent(self, args):
        """防止防御塔和箱子粘连及游戏内外通讯"""
        args['cancel'] = True



    @Listen
    def ServerPlayerTryDestroyBlockEvent(self, args): # 破坏方块
        """地图保护及检测破坏床机制"""
        Id = args['playerId']
        team = getExData('Team', Id) 
        block_name = args['fullName'] 
        pos = (args['x'], args['y'], args['z'])
        x, y, z = args['x'], args['y'], args['z']
        bed_color = BedColor(cf.CreateBlockInfo(levelId).GetBedColor(pos, 0))
        if block_name not in server_can_destroy_blocks:
            args['cancel'] = True
            function('global/reward/des_cant_block', Id)
        else:
            if block_name == 'minecraft:bed': #非aux API床int: 红→14,蓝→11,绿→5,黄→4
                args['spawnResources'] = False
                name = cf.CreateName(Id).GetName()
                x1, y1, z1 = cf.CreatePos(Id).GetPos()
                desbed_distance = ((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2) ** 0.5
                if desbed_distance > max_attack_distance:
                    showMsg('§b§lAur§fora §r§7 >> §c玩家 §e%s §c因 §f绕权攻击类 §c已被系统封禁处理!' % name, Id)
                    target_name = name
                    types = 'Fucker(A)'
                    origin_name = 'server'
                    args['cancel'] = True
                    self.SHORYdeployToBan(Id, target_name, origin_name, types)
                    return
                else:
                    if hasTag("床保护", Id):
                        showMsg("§c床保护阶段不可破坏床!", Id)
                        args['cancel'] = True
                    else:
                        if (getExData('Team', Id) == 1 and bed_color == 'RED') or (getExData('Team', Id) == 2 and bed_color == 'BLUE') or (getExData('Team', Id) == 3 and bed_color == 'GREEN') or (getExData('Team', Id) == 4 and bed_color == 'YELLOW'):
                            function('global/reward/tryDestroyOwnBed', Id) #自破自床
                            args['cancel'] = True
                        else: #正常破床
                            if bed_color in ["RED", "BLUE", "GREEN", "YELLOW"] and hasTag("inf", Id):
                                setCommand('scoreboard players add @s 比赛 {}'.format(MATCH_REWARD_NO_BED_DBED_SCORE if hasTag('无床', Id) else MATCH_REWARD_HAVE_BED_DBED_SCORE), Id)
                                addTag('desb_{}'.format(bed_color), Id) #变量转换
                                function('global/bed/effect/{}'.format(bed_color), Id)
                                Destroyer_team = getExData('Team', Id)
                                Destroyer_color = self.getCharacterTeamColor(team=Destroyer_team)
                                setCommand("execute positioned {} {} {} run summon lightning_bolt ~~~".format(x, y, z))
                                setCommand("execute positioned {} {} {} run kill @e[r=3,type=bedwars:text]".format(x, y, z))
                                setCommand('summon bedwars:text "§7该队伍床已被 §l§{}{} §r§7所摧毁! " {} {} {}'.format(Destroyer_color, name, x, y - 1, z))
                            else: 
                                showMsg('§l\n§c本房间出现服务错误,进行重置尝试规避问题,请立即反馈!')
                                function("global/end/draw", Id)
            elif block_name == 'minecraft:slime':
                args['spawnResources'] = False



    @Listen
    def ServerEntityTryPlaceBlockEvent(self, args):
        """防止玩家越界放置方块"""
        Id = args['entityId']
        x, y, z = args['x'], args['y'], args['z']
        block_name = args['fullName']
        name = cf.CreateName(Id).GetName()
        block_aux = args['auxData']
        comp = cf.CreateBlockInfo(levelId)

        if block_name not in server_can_destroy_blocks and name not in white_list and name not in op_list:
            args['cancel'] = True
            target_name = name
            types = 'Cheat(P)'
            origin_name = 'server'
            self.SHORYdeployToBan(Id, target_name, origin_name, types)
            return

        else:
            if not hasTag('debug', Id):
                if args['y'] <= self.y_1:
                    args['cancel'] = True
                    showMsg(('§c达到建筑最低限制!' if hasTag('语言', Id) else '§build lowest limit reached!'), Id)
                elif args['y'] >= self.y_2:
                    args['cancel'] = True
                    showMsg(('§c达到建筑最高限制!' if hasTag('语言', Id) else '§cBuild height limit reached!'), Id)




    def StartGame(self):
        """脚本侧登记玩家队伍信息+设置限高"""
        for Id in sapi.GetPlayerList():
            if setCommand('/scoreboard players test @s A1T12P 1 1', Id):
                setExData('Team', 1, Id)
                cf.CreateName(Id).SetPlayerPrefixAndSuffixName('§c§l红§r§c ',sapi.GenerateColor('WHITE'),'',sapi.GenerateColor('WHITE'),sapi.GenerateColor('RED'))
            elif setCommand('/scoreboard players test @s A1T12P 2 2', Id):
                setExData('Team', 2, Id)
                cf.CreateName(Id).SetPlayerPrefixAndSuffixName('§9§l蓝§r§9 ',sapi.GenerateColor('WHITE'),'',sapi.GenerateColor('WHITE'),sapi.GenerateColor('BLUE'))
            elif setCommand('/scoreboard players test @s A1T12P 3 3', Id):
                setExData('Team', 3, Id)
                cf.CreateName(Id).SetPlayerPrefixAndSuffixName('§a§l绿§r§a ',sapi.GenerateColor('WHITE'),'',sapi.GenerateColor('WHITE'),sapi.GenerateColor('GREEN'))
            elif setCommand('/scoreboard players test @s A1T12P 4 4', Id):
                setExData('Team', 4, Id)
                cf.CreateName(Id).SetPlayerPrefixAndSuffixName('§e§l黄§r§e ',sapi.GenerateColor('WHITE'),'',sapi.GenerateColor('WHITE'),sapi.GenerateColor('YELLOW'))

        if hasTag('rbw_chained', Id):
            self.y_2 = 302
            removeTag('rbw_chained', Id)
            return
        elif hasTag('rbw_unt', Id):
            self.y_2 = 288
            removeTag('rbw_unt', Id)
            return
        elif not hasTag('rbw_unt', Id) and not hasTag('rbw_chained', Id) and setCommand('/scoreboard players test @s A1T12P 1..4', Id):
            self.y_2 = 310
            return





    @Listen
    def HealthChangeServerEvent(self, args):
        """设置玩家血量计分板"""
        Id = args['entityId']
        if cf.CreateEngineType(Id).GetEngineTypeStr() == 'minecraft:player': setCommand('/scoreboard players set @s T2R10A %s' % int(cf.CreateAttr(Id).GetAttrValue(0)), Id)


    @Listen
    def HealthChangeBeforeServerEvent(self, args):
        """制止致死伤害发生导致真死"""
        Id = args['entityId']
        if cf.CreateEngineType(Id).GetEngineTypeStr() == 'minecraft:player' and args['to'] <= 0:
            args['cancel'] = True


    def After(self, Id):
        comp = cf.CreateAttr(Id)
        dim, pos = cf.CreateDimension(Id).GetEntityDimensionId(), cf.CreatePos(Id).GetFootPos()
        respos = cf.CreatePlayer(Id).GetPlayerRespawnPos()
        cf.CreateDimension(Id).ChangePlayerDimension(respos['dimensionId'], respos['pos'])
        comp.SetAttrValue(0, comp.GetAttrMaxValue(0))
        self.PlayerDeath(Id)


    def PlayerDeath(self, Id):
        cf.CreateGame(Id).AddTimer(0.03, self.xp, Id=Id)
        function('global/kad/d', Id)
        self.SHORYinvisibilityTimeOver(Id)
        cf.CreateGame(Id).AddTimer(0, self.StartWd, Id=Id)


    def xp(self, Id):
        valu = cf.CreateLv(Id).GetPlayerLevel()
        add_valu = int(valu * 0.5)
        setCommand('/xp -%sL @s' % add_valu, Id)


    def StartWd(self, Id):
        cf.CreateGame(Id).AddTimer(7.0, self.WdTimeOver, Id=Id)
        setExData('无敌时间', True, Id)


    def WdTimeOver(self, Id):
        setExData('无敌时间', False, Id)



    @Listen
    def PlayerJoinMessageEvent(self, args):
        Id = args['id']
        self.GetScoreboar(Id)
        args['cancel'] = True
        setCommand('tellraw @a[tag=语言] {"rawtext":[{"text":"§7%s §e进入了游戏(§b"},{"score":{"name":"rs","objective":"D1W04T"}},{"text":"§e/§b10§e)"}]}' % args['name'])
        setCommand('tellraw @a[tag=language] {"rawtext":[{"text":"§7%s §ejoin the game(§b"},{"score":{"name":"rs","objective":"D1W04T"}},{"text":"§e/§b10§e)"}]}' % args['name'])


        
    @Listen
    def PlayerLeftMessageServerEvent(self, args):
        Id = args['id']
        self.GetScoreboard(Id)
        args['cancel'] = True
        setCommand('tellraw @a[tag=语言] {"rawtext":[{"text":"\n§7%s §c断开连接"}]}' % args['name'])
        setCommand('tellraw @a[tag=language] {"rawtext":[{"text":"\n§7%s §cdisconnect"}]}' % args['name'])
        function('playerDisconnect', Id)


    def GetScoreboard(self, Id):
        scoreboard_ = cf.CreateGame(levelId).GetAllPlayerScoreboardObjects()
        _scoreboard = {}
        if scoreboard_:
            for n in scoreboard_:
                dataPlayerId = n['playerId']
                if dataPlayerId == Id:
                    scoreList = n['scoreList']
                    for score in scoreList:
                        if score['name'] in InterFlow_Scoreboard:
                            _scoreboard[score['name']] = score['value']
                    break
        if _scoreboard:
            self.NotifyToClient(Id, 'LoadScoreboardEvent', {'data': _scoreboard})


    def GetScoreboar(self, Id):
        self.NotifyToClient(Id, 'ReloadScoreboardEvent', {})

    @Listen
    def OnCarriedNewItemChangedServerEvent(self, args):
        """武器附魔及检测使用指南针激活计算"""
        Id = args['playerId']
        self.AddWeaponEnchant(Id) # 刷一次武器附魔
        if args['newItemName'] == 'minecrafts:shears':
            addTag('shears', Id)
            itemDict = {'itemName': 'minecraft:shears','count': 1}
            comp = sapi.GetEngineCompFactory().CreateItem(Id)
            comp.SpawnItemToPlayerCarried(itemDict, Id)
        if args['newItemName'] == 'minecraft:compass':
            self.addcompass = cf.CreateGame(Id).AddRepeatedTimer(0.5, self.Compass, Id=Id)
        if args['oldItemName'] == 'minecraft:compass':
            cf.CreateGame(Id).CancelTimer(self.addcompass)


    def Compass(self, Id):
        """指南针功能运行"""
        item = cf.CreateItem(Id).GetPlayerItem(2, 0)
        if item['newItemName'] == 'minecraft:compass':
            handlerId = Id
            tag = 'compass%s' % handlerId
            stag = 'coom%s' % handlerId
            setCommand('/tag @a remove "%s"' % tag)
            addTag(stag, handlerId)
            if setCommand('/scoreboard players test @s A1T12P 1 1', Id):
                if not setCommand('/tag @p[scores={A1T12P=!1},tag=!S2P10K,tag=!"%s",tag=!观战] add "%s"' % (stag, tag), handlerId): cf.CreateGame(handlerId).SetOneTipMessage(handlerId, '§c未找到目标玩家!')
            elif setCommand('/scoreboard players test @s A1T12P 2 2', Id):
                if not setCommand('/tag @p[scores={A1T12P=!2},tag=!S2P10K,tag=!"%s",tag=!观战] add "%s"' % (stag, tag), handlerId): cf.CreateGame(handlerId).SetOneTipMessage(handlerId, '§c未找到目标玩家!')
            elif setCommand('/scoreboard players test @s A1T12P 3 3', Id):
                if not setCommand('/tag @p[scores={A1T12P=!3},tag=!S2P10K,tag=!"%s",tag=!观战] add "%s"' % (stag, tag), handlerId): cf.CreateGame(handlerId).SetOneTipMessage(handlerId, '§c未找到目标玩家!')
            elif setCommand('/scoreboard players test @s A1T12P 4 4', Id):
                if not setCommand('/tag @p[scores={A1T12P=!4},tag=!S2P10K,tag=!"%s",tag=!观战] add "%s"' % (stag, tag), handlerId): cf.CreateGame(handlerId).SetOneTipMessage(handlerId, '§c未找到目标玩家!')
            removeTag(stag, handlerId)
            for Id_ in sapi.GetPlayerList():
                if hasTag(tag, Id_):
                    nearestId = Id_
            x, y, z = cf.CreatePos(handlerId).GetPos()
            x1, y1, z1 = cf.CreatePos(nearestId).GetPos()
            block = ((x - x1) ** 2 + (y - y1) ** 2 + (z - z1) ** 2) ** 0.5
            block = round(block, 3)
            name = cf.CreateName(nearestId).GetName()
            target_color = 'f'
            target_team = getExData('Team', nearestId)
            target_color = self.getCharacterTeamColor(team=target_team)
            cf.CreateGame(handlerId).SetOneTipMessage(handlerId, '§f%s: §l§%s%s §f- §r§f%s: §l§a%sm' % ('正在追踪' if hasTag('语言', Id) else 'Target', target_color, name, '距离' if hasTag('语言', Id) else 'Distance', int(block)))
            setCommand('/tag @a remove "%s"' % tag)


    def AddWeaponEnchant(self, Id):
        """添加剑和斧附魔"""
        comp = cf.CreateItem(Id)
        item = comp.GetPlayerItem(2, 0)
        if hasTag('fengl', Id):
            if item['newItemName'] == 'minecraft:wooden_sword' or item['newItemName'] == 'minecraft:stone_sword' or item['newItemName'] == 'minecraft:iron_sword' or item['newItemName'] == 'minecraft:diamond_sword' or item['newItemName'] == 'minecraft:iron_axe' or item['newItemName'] == 'minecraft:diamond_axe' or item['newItemName'] == 'minecraft:stone_axe' or item['newItemName'] == 'minecraft:wooden_axe': comp.AddEnchantToInvItem(comp.GetSelectSlotId(), 9, 1)
        elif hasTag('fengll', Id):
            if item['newItemName'] == 'minecraft:wooden_sword' or item['newItemName'] == 'minecraft:stone_sword' or item['newItemName'] == 'minecraft:iron_sword' or item['newItemName'] == 'minecraft:diamond_sword' or item['newItemName'] == 'minecraft:iron_axe' or item['newItemName'] == 'minecraft:diamond_axe' or item['newItemName'] == 'minecraft:stone_axe' or item['newItemName'] == 'minecraft:wooden_axe': comp.AddEnchantToInvItem(comp.GetSelectSlotId(), 9, 2)


    @Listen
    def PlayerEatFoodServerEvent(self, args):
        """检测使用药水和牛奶"""
        Id = args['playerId']
        itemdict = args['itemDict']
        if itemdict['newItemName'] == 'minecrafts:instanthealth_potion': #瞬间治疗1
            comp = cf.CreateAttr(Id)
            comp.SetAttrValue(0, comp.GetAttrValue(0) + 4)
        elif itemdict['newItemName'] == 'minecrafts:instanthealth_potions': #瞬间治疗2
            comp = cf.CreateAttr(Id)
            comp.SetAttrValue(0, comp.GetAttrValue(0) + 8)
        elif itemdict['newItemName'] == 'minecraft:milk_bucket': #神奇牛奶
            args['cancel'] = True
            addTag('usemilk', Id)


    @Listen
    def PlayerPermissionChangeServerEvent(self, args):
        causeId = args['causePlayerId']
        why = args['changeCause']
        playerId = args['playerId']
        taskId = random.randint(10000, 76000)
        if cf.CreateName(causeId).GetName() in op_list or cf.CreateName(causeId).GetName() in white_list:
            addTag('adminSet', playerId)
            return
        else:
            if why == 3 and not hasTag('banned', causeId) and not hasTag('banned', playerId):
                showMsg('\n§c§l你的权限被尝试变化!§e(请立即截图反馈!)\n§7§l>> 如果你被无理神权,这是你的取证必备证据!\n\n§r§fargs[changeCause]: §aUserInterfaceCaused(玩家神权操作)\n§fCauseId: §a%s\n§7TID:%s log:[C]%s->[P]%s' % (cf.CreateName(causeId).GetName(), taskId, cf.CreateName(causeId).GetName(), cf.CreateName(playerId).GetName()), playerId)
                args['cancel'] = True




    @Listen
    def GameTypeChangeServerEvent(self, args): #模式保护
        """游戏模式保护防神权"""
        Id = args['playerId']
        target_name = cf.CreateName(Id).GetName()
        if args['newGameType'] == 1:
            if target_name not in white_list and target_name not in op_list or hasTag('测试封禁', Id): 
                showMsg('§l§bAur§fora §8| §r§e%s §7failed §cCreate(A)' % target_name, Id)
                types = 'Power(T)'
                origin_name = 'server'
                self.SHORYdeployToBan(Id, target_name, origin_name, types)
                return



    @Listen
    def ServerPlayerTryTouchEvent(self, args):
        Id = args['playerId']
        entity = args['entityId']
        item = args['itemDict']
        name = cf.CreateName(Id).GetName()
        if cf.CreateGame(levelId).GetPlayerGameType(Id) == 0:
            items = item['newItemName']
            item_name = items.split(":")[1].split("_")[0]
            if items in ore_resource_list: #cf.CreateLv(Id).AddPlayerLevel(xpp)
                setCommand('execute if score mode O8P02W matches 3..4 run playsound random.orb @s[m=0]', Id)
                if item['newItemName'] == 'minecraft:iron_ingot':
                    args['cancel'] = True
                    xpp = item['count'] * 1
                    setCommand('execute if score mode O8P02W matches 3..4 at @s run xp %sL @a[r=1.5,m=0]' % xpp, Id)
                    setCommand('/kill @s', entity)
                if item['newItemName'] == 'minecraft:gold_ingot':
                    args['cancel'] = True
                    xpp = item['count'] * 10
                    setCommand('execute if score mode O8P02W matches 3..4 at @s run xp %sL @a[r=1.5,m=0]' % xpp, Id)
                    setCommand('/kill @s', entity)
                if item['newItemName'] == 'minecraft:diamond':
                    args['cancel'] = True
                    xpp = item['count'] * 80
                    setCommand('execute if score mode O8P02W matches 3..4 at @s run xp %sL @s' % xpp, Id)
                    setCommand('/kill @s', entity)
                if item['newItemName'] == 'minecraft:emerald':
                    args['cancel'] = True
                    xpp = item['count'] * 150
                    setCommand('execute if score mode O8P02W matches 3..4 at @s run xp %sL @s' % xpp, Id)
                    setCommand('/kill @s', entity)
                # 自-非经验ONLY-正常拾取 给一次矿物自己
                setCommand('execute unless score mode O8P02W matches 3..4 run give @s[m=0] {} {}'.format(item['newItemName'], item['count']), Id)
                del xpp


    def AddAllArmorEnchant(self, Id):
        now_tags = set(getTagList(Id))
        enchant_id = set(now_tags) & set(TAG_TO_ENCHANT)
        for _ in enchant_id:
            AddAllArmorEnchant(Id, TAG_TO_ENCHANT[_])
            removeTag(TAG_TO_ENCHANT, Id)


def AddAllArmorEnchant(player_id, args):
    comp = cf.CreateItem(player_id)
    new_map = {}
    for index in range(4):
        item = comp.GetPlayerItem(3, index, True)
        if item:
            new_data = [args]
            for enchant in item['enchantData']:
                if enchant[0] != args[0]:
                    new_data.append(enchant)
            item['enchantData'] = new_data
            new_map[(3, index)] = item
    comp.SetPlayerAllItems(new_map)






