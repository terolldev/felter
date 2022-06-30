# -*- coding: utf8 -*-

#импорт модулей
from mem import memepost
from asyncio.tasks import sleep
from goldpass import goldserver
import datetime, time
import nextcord
from WebServer import keep_alive
from code1 import *
from bottoken import token
from nextcord.ext import commands
from nextcord.ext.commands import MissingPermissions
from Cybernator import Paginator
import asyncio
import random
import json
from backlist import blackmember
from discord.utils import get
import discord
import requests
from datetime import timedelta, datetime
import datetime
from speakIU import shards
from prefix import *
import psutil
import platform
import aiohttp
intents = discord.Intents.default()
intents.members = True
intents.all()

#префикс бота
bot = commands.AutoShardedBot(shard_count=shards, command_prefix=get_prefix)
bot.remove_command('help')
keep_alive()
#@commands.is_owner()


#статус бота
@bot.event
async def on_ready():
    print('Felter bot started!')

    #await bot.change_presence(
    #        activity=discord.Custom(
    #            name=f'f+help | https://bot.felterbot.ga/'))
    await bot.change_presence(
            activity=discord.Streaming(
                name=f'f+help | Hовый бот!', url='https://www.twitch.tv/tim_eiger', twitch_name="tim_eiger"))

@bot.event
async def on_message(message):
    prefixx = await bot.get_prefix(message)
    ping = round(bot.latency * 1000)
    p = prefixx
    find = "https://discord.gg/"
    if message.content == "felter":
      embed=nextcord.Embed(title="Справка по боту", description=f"Мой префикс - `{p}`\n Узнать мои команды - `{p}help`\n Мой пинг - ```cs\n#         {ping}ms     #\n```", colour=nextcord.Colour.random(), timestamp=datetime.datetime.now())
      embed.set_footer(text=f"{message.author}", icon_url=f"{message.author.avatar}")
      embed.set_author(name="Felter bot", icon_url="https://cdn.discordapp.com/attachments/888376246029918228/948743947088461834/777557308258517032.png")
      await message.reply(embed=embed)
    elif message.guild.id == 888347265482244116:
      if find in message.content:       
        if find in message.content:
            await message.reply(embed=nextcord.Embed(title="АнтиСпам!", description="Я обнаружил ссылку нa сервер, мне пришлось её удалить!", colour=nextcord.Color.random(), timestamp=datetime.datetime.now()))
            await message.delete()
    await bot.process_commands(message)

@bot.event
async def on_connect():
    print("-----------")

@bot.event
async def on_disconnect():
    print("Felter bot, disconnect on discord!\n---------")

@bot.event
async def on_shard_connect(shard_id):
    print(f"Shard: {shard_id}\n Connected!\n----------------")

@bot.event
async def on_invite_create(invite):
    print(f"New create invite URL - {invite}\n-----------")

@bot.event
async def on_shard_ready(shard_id):
    print(f"Shard: {shard_id}\nOn_Ready\n------------------")

@bot.event
async def on_shard_resumed(shard_id):
    print(f"Shard: {shard_id}\n Resume connection\n----------------")

@bot.event
async def on_command_error(ctx, error):
    #    if isinstance(error, commands.CommandNotFound):
    #        embed = await ctx.reply(embed=discord.Embed(
    #            title=f":no_entry: Erorr (404) ",
    #            description=
    #            f' {ctx.author.mention} , **Данной команды не существует, \n или она отключена разработчиком** :heart_eyes: .',
    #            color=discord.Color.red()))
    #       await embed.add_reaction('❌')

    if isinstance(error, commands.CommandOnCooldown):
        times = round(error.retry_after, 2)
        global ctxx
        ctxx = ctx.author.id
        if times <= 60:
            embed5 = await ctx.reply(embed=nextcord.Embed(
                title=f':no_entry: Erorr',
                description=
                f'Повторите через `{error.retry_after :.0f}` сек\n **Ид ошибки**: `{random.randint(81275782135,7126542153216851)}`',
                colour=0xe74c3c, timestamp=datetime.datetime.now()))
            await embed5.add_reaction('❌')
            await sleep(10)
            await embed5.delete()

        elif times > 60:
            embed4 = await ctx.reply(embed=nextcord.Embed(
                title=f':no_entry: Erorr',
                description=
                f'Повторите примерно через `{int(times//60)}` минут `{int(times%60)}` секунд\n **ID Error**: `{random.randint(81275782135,7126542153216851)}`',
                colour=discord.Color.red(), timestamp=datetime.datetime.now()))
            await embed4.add_reaction('❌')
            await sleep(10)
            await embed4.delete()

    if isinstance(error, commands.MissingRequiredArgument):
        fullCommandName = ctx.command.qualified_name
        split = fullCommandName.split(" ")
        executedCommand = str(split[0])
        prefix = await bot.get_prefix(ctx.message)
        p = prefix
        skm123 = await ctx.reply(embed=nextcord.Embed(
            title=f':no_entry: Erorr',
            description=
            f'Нет аргументов! Ведите их!\n Пример: {p}{executedCommand} <Arguments>\n **ID ERROR**: `{random.randint(81275782135,7126542153216851)}`\n```cs\n #Символы \'<\', \'>\' вставлять не надо!\n```',
            colour=nextcord.Color.red(), timestamp=datetime.datetime.now()))
        await skm123.add_reaction('❌')
        await sleep(10)
        await skm123.delete()

    if isinstance(error, MissingPermissions):
        skm = await ctx.reply(embed=nextcord.Embed(
            title=f":no_entry: Erorr!",
            description=f' {ctx.author.mention} , у вас недостаточно прав!.',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))
        await skm.add_reaction('❌')
        await sleep(10)
        await skm.delete()

    if isinstance(error, commands.MemberNotFound):
        skm1 = await ctx.reply(embed=nextcord.Embed(
            title=f":no_entry: Erorr!",
            description=
            f' {ctx.author.mention} , мне не удалось найти этого участника. Проверьте правильность написание всех букв и цифр!\n```cs\n#Пример: @участник\n```',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))
        await skm1.add_reaction('❌')
        await sleep(10)
        await skm1.delete()

    if isinstance(error, commands.BotMissingPermissions):
        skm12 = await ctx.reply(embed=nextcord.Embed(
            title=f":no_entry: Erorr!",
            description=
            f' {ctx.author.mention} , У меня нету прав для этого действия, выдайте мне роль с отметкой "Administator".',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))
        await skm12.add_reaction('❌')
        await sleep(10)
        await skm12.delete()

    if isinstance(error, commands.RoleNotFound):
        skm11 = await ctx.reply(embed=nextcord.Embed(
            title=f":no_entry: Erorr!",
            description=
            f' {ctx.author.mention} , мне не удалось найти эту роль. Проверьте правильность написание всех букв и цифр!\n```cs\n#Пример: @роль\n```',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))
        await skm11.add_reaction('❌')
        await sleep(10)
        await skm11.delete()

@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command()
async def meme_test(ctx):
    embed = discord.Embed(title="Random mem", description="", colour=nextcord.Colour.random(), timestamp=datetime.datetime.now())

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@commands.cooldown(rate=1, per=6, type=commands.BucketType.user)
@bot.command()
async def search(ctx, *, ja):
  s = ja
  ja = ja.replace(' ', '+')
  
  
  embed=nextcord.Embed(title="Поиск в Яндекс", description=f"[Ссылка на ваш запрос](https://yandex.ru/search/?lr=38&text=" + ja + ")", colour=nextcord.Colour.random(), timestamp=datetime.datetime.now())
  embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
  await ctx.reply(embed=embed)

@commands.has_permissions(administrator=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command()
async def embed(ctx):
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel


    msg1 = await ctx.reply(embed = discord.Embed(title='Название', description='Укажите название!', color=0x2e2f33, timestamp=datetime.datetime.now()))
    title = await bot.wait_for('message', check=check)
  
    msg2 = await ctx.reply(embed = discord.Embed(title='Описание', description="Укажите описание", color=0x2e2f33, timestamp=datetime.datetime.now()))
    desc = await bot.wait_for('message', check=check)

    await ctx.send(embed=nextcord.Embed(title=f"{title.content}", description=f"{desc.content}", color=nextcord.Colour.random(), timestamp=datetime.datetime.now()))
    await msg1.delete()
    await msg2.delete()
    await desc.delete()
    await title.delete()

@commands.has_permissions(administrator=True)
@bot.command()
@commands.cooldown(rate=1, per=60, type=commands.BucketType.user)
async def checkuser(ctx, text):
    if f'{text}' in blackmember:
        await ctx.reply(embed=nextcord.Embed(
            title=f"Check for user",
            description=
            f'User: <@!{text}>\nID: {text}\n Находится в чёрном списке бота',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))

    elif text == None:
        skm12 = await ctx.reply(embed=nextcord.Embed(
            title=f":no_entry: Erorr!",
            description=
            f' {ctx.author.mention} , мне не удалось найти этого участника. Проверьте правильность написание всех букв и цифр!',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))
        await skm12.add_reaction('❌')

    else:
        await ctx.reply(embed=nextcord.Embed(
            title=f"Check for user",
            description=
            f'User: <@!{text}>\nID: {text}\nНе Находится в чёрном списке бота',
            color=nextcord.Color.blue(), timestamp=datetime.datetime.now()))


@bot.event
async def on_command_completion(ctx):
    channel = bot.get_channel(912328386658058251)
    fullCommandName = ctx.command.qualified_name
    split = fullCommandName.split(" ")
    executedCommand = str(split[0])

    #await channel.send(embed=nextcord.Embed(
    #       title=f"Пользователь: {ctx.message.author.id}",
    #       description=f'Ид Сервера:     {ctx.message.guild.id}\nКанал: {ctx.channel.name}\nУпоминание канала: <#{ctx.channel.id}>\nИд Канала: {ctx.channel.id}\n Пользователь: {ctx.message.author.mention}\nНазвание сервера: {ctx.guild.name}\n Команда: f+{executedCommand}',
    #color=nextcord.Color.from_rgb(88, 101, 242)))
    now = datetime.datetime.now()

    file = open(f"логи/{ctx.message.guild.id}.txt", "a")
    file.write(
        f"Название сервера: {ctx.guild.name}\nИд Сервера: {ctx.message.guild.id}\nКоманда: f+{executedCommand}\nПользователь: {ctx.message.author.id}\nНик пользователя: {ctx.message.author}\nИд Канала: {ctx.channel.id}\nВремя: {now.strftime('%Y-%m-%d %H:%M:%S')}\n-----------------\n"
    )


class Code(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @bot.command(aliases=["cod", "CODE", "cmd"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.guild)
    async def code(ctx, text, *, code):
        if text == send:
            await ctx.send(code)
        elif text == delete:
            await ctx.channel.purge(limit=2)
        elif text == mention:
            await ctx.send(f"<@{code}>")
        elif text == sendemb:
            await ctx.send(
                embed=nextcord.Embed(description=code, color=nextcord.Color.from_rgb(54, 57, 62), timestamp=datetime.datetime.now()))
        elif text == change_name_server:
            send1 = await ctx.reply(f"Server name change: {code}")
            server = bot.get_guild(ctx.guild.id)
            await server.edit(name=code)
            await sleep(5)
            await send1.delete()
        elif text == exit_bot:
            await ctx.reply(
                "вы захотели кикнуть себя, пока\n you they wanted to kick myself, good boy\n you kick in 5 second"
            )
            await sleep(5)
            author = ctx.author
            await author.kick(reason="Kick for cmd command")
        elif text == 'help':
            prefix = await bot.get_prefix(ctx.message)
            p = prefix
            message = await ctx.send(" \\ ")
            await sleep(0.1)
            await message.edit(content="|")
            await sleep(0.1)
            await message.edit(content="/")
            await sleep(0.3)
            await message.delete()
            await ctx.reply(
                f"ℹ️\n`{p}code send <you text>` send message \n `{p}code delete 1` delete 1 message\n `{p}code mention <id member>` mention for id member\n `{p}code sendemb <you text>` send text in embed\n`{p}code change_name_server <New name server>` Change guild name! \n`{p}code exit_bot 1` you kick is from server\nℹ️ By felter bot CMD\n"
            )
        else:
            await ctx.reply("Команда не найдена\nComand not found")

@bot.command(aliases=["donate"])
async def donation(ctx):
  embed=nextcord.Embed(
    title="Ссылки где покупать донат",
    description="ДонейшенАлтертс = https://www.donationalerts.com/r/felterbotdnt\n для доната нужно в коментарии указать айди своего сервера, узнать его можно с помощью команды check", colour=netxcord.Colour.random(), timestamp=datetime.datetime.now()
  )
  embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
  await ctx.reply(embed=embed)



@bot.command(aliases=["Case_cs", "cs", "Case_Cs"])
@commands.cooldown(rate=1, per=75, type=commands.BucketType.user)
async def case_csgo_open(ctx):
    gold = goldserver
    if f'{ctx.message.guild.id}' in gold:
        gama = ["Рубин", "Эмеральд", "Сапфир", "Фаза 1", "Фаза 2", "Фаза 3", "Фаза 4", "Фаза 5", "Фаза 6", "Фаза 7", "Фаза 8"]
        gloves = ["★ Перчатки спецназа | Мраморный градиент", "★ Перчатки спецназа | Полевой агент", "★ Спортивные перчатки | Кровавый шемах","★ Мотоциклетные перчатки | Бросаю дымовую", "★ Спортивные перчатки | Ноктс", "★ Спортивные перчатки | Ящик Пандоры", "★ Мотоциклетные перчатки | Мята", "★ Перчатки спецназа | Изумрудная сеть", "★ Перчатки спецназа | Кровавое кимоно", "★ Мотоциклетные перчатки | Мятная прохлада", "★ Перчатки спецназа | Основа", "★ Мотоциклетные перчатки | Бах!", "★ Водительские перчатки | Лунный узор"]
        knife = ["★ Штык-нож M9 | Вороненая сталь", "★ Штык-нож M9 | Кровавая паутина", "★ Штык-нож M9 | Северный лес", "★ Штык-нож M9 | Поверхностная закалка", "★ Штык-нож M9 | Пиксельный камуфляж «Лес»", "★ Штык-нож M9 | Патина", "★ Штык-нож M9 | Градиент", "★ Штык-нож M9 | Городская маскировка", "★ Штык-нож M9 | Убийство", f"★ Фальшион | Волны ({random.choice(gama)})", "★ Нож Бабочка | Легенды", "★ Нож бабочка | Автотроника", f"★ Нож бабочка | Волны ({random.choice(gama)})", "★ Стилет | Убийство", "★ Стилет", "★ Штык-нож M9", "★ Медвежий нож | Пыльник", "★ Медвежий нож", f"★ Стилет | Волны ({random.choice(gama)})", "★ Тычковые ножи | Автотроника", "★ Тычковые ножи | Убийство", "★ Фальшион | Дамасская сталь", "★ Фальшион | Легенды", f"★ Фальшион | Волны ({random.choice(gama)})", "★ Керамбит | Gold", "★ Керамбит"]
        pat = ["Прямо с завода", "Немного поношенное", "После полевых испытаний", "После полевых испытаний", "После полевых испытаний", "Немного поношенное", "Поношенное", "Закалённое в боях", "Закалённое в боях", "Закалённое в боях", "Закалённое в боях", "Закалённое в боях", "Закалённое в боях"]
        stattrack = ["StatTrak™", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . ", " . "]
        blue = random.choice(["UMP-45 | Дневная лилия(Армейское(синие))", "CZ75-Auto | Красный ястреб(Армейское(Синие))", "Револьвер R8 | Выживший(Армейское(Синие))", "P90 | Сцепление(Армейское(Синие))", "MP9 | Капилляры(Армейское(Синие))", "G3SG1 | Лазурная зебра(Армейское[Синие])", "ПП-19 Бизон | Знак воды(Армеское[Синее])", "ПП-19 Бизон | Знак воды(Армеское[Синее])", "SCAR-20 | Латунь(Армейское(Синее))", "Five-SeveN | Городская опасность(Армейское(Синие))"])
        blue1 = random.choice(["UMP-45 | Дневная лилия(Армейское(синие))", "CZ75-Auto | Красный ястреб(Армейское(Синие))", "Револьвер R8 | Выживший(Армейское(Синие))", "P90 | Сцепление(Армейское(Синие))", "MP9 | Капилляры(Армейское(Синие))", "G3SG1 | Лазурная зебра(Армейское[Синие])", "ПП-19 Бизон | Знак воды(Армеское[Синее])", "ПП-19 Бизон | Знак воды(Армеское[Синее])", "SCAR-20 | Латунь(Армейское(Синее))", "Five-SeveN | Городская опасность(Армейское(Синие))"])
        purple = random.choice(["SSG 08 | Призрачный фанатик(Запрещенное(Фиолетовое))", "P90 | Слепое пятно(Запрещенное[Фиолетовое])", "AK-47 | Синий глянец(Запрещенное[Фиолетовое])", "Glock-18 | Полимерные листья(Запрещеное(Фиолетовое))", "Desert Eagle | Изумрудный Ёрмунганд(Запрещенное(Фиолетовое))", "USP-S | Взгляд в прошлое(Запрещенное(Фиолетовое))"])
        pink = random.choice(["USP-S | Орион(Засекреченное(Розовое))", "M4A1-S | Нитро(Засекреченное(Розовое))", "AWP | Электрический улей(Засекреченное[Розовое])", "Usp-s | Извилины(Засекреченое(розовое))", "MP9 | Дикая лилия(Засекреченное(Розовое))", "Desert Eagle | Механо-пушка(Засекреченное(Розовое))", "SG 553 | Сайрекс(Засекреченное(Розовое))", f"AK-47 | Поверхностная закалка(Засекреченное(Розовое)) - Patern=({random.randint(1,20)})"])
        seriy = random.choice(["Tec-9 | Армейская сетка(Ширпотреб(серое))", "MP5-SD | Бамбуковый(ШирПотреб(Серое))"])
        golden = random.choice([f"Перчатки! - {random.choice(gloves)}", "M4A4 | Вой(Контрабанда(золотой))", "Нож! - " + str(random.choice(knife))])
        red = random.choice(["USP-S | Подтвержденное убийство(Тайное(Красное))", "AK-47 | Вулкан(Тайное(Красное))", "M4A4 | Азимов(Тайное(Красное))", "M4A4 | Рентген(Тайное[Красное])", "AK-47 | Золотая Арабеска(Тайное(Красное))", "Desert Eagle | Поток информации(Тайное(Красное))", "Mac-10 | Неоновый гонщик(Тайное(Красное))", "AWP | История о драконе(Тайное(Красное))", "AK-47 | Азимов(Тайное(красное))"])
        msg = await ctx.reply(embed=nextcord.Embed(
            title="Кейс из Кс-го",
            description=f"`----------------------------------`\n`||`  {random.choice([blue, purple, pink, seriy, golden, red])}  `||`\n`----------------------------------`", color=nextcord.Colour.random()
            ))
        await sleep(0.2)
        await msg.edit(embed=nextcord.Embed(
            title="Кейс из Кс-го",
            description=f"`----------------------------------`\n`||`  {random.choice([blue, purple, pink, seriy, golden, red])}  `||`\n`----------------------------------`", color=nextcord.Colour.random()
            ))
        await sleep(0.2)
        await msg.edit(embed=nextcord.Embed(
            title="Кейс из Кс-го",
            description=f"`----------------------------------`\n`||`  {random.choice([blue, purple, pink, seriy, golden, red])}  `||`\n`----------------------------------`", color=nextcord.Colour.random()
            ))
        await sleep(0.3)
        await msg.edit(embed=nextcord.Embed(
            title="Кейс из Кс-го",
            description=f"`----------------------------------`\n`||`  {random.choice([blue, purple, pink, seriy, golden, red])}  `||`\n`----------------------------------`", color=nextcord.Colour.random()
            ))
        await sleep(0.4)
        await msg.edit(embed=nextcord.Embed(
            title="Кейс из Кс-го",
            description=f"`----------------------------------`\n`||`  {random.choice([blue, purple, pink, seriy, golden, red])}  `||`\n`----------------------------------`", color=nextcord.Colour.random()
            ))
        await sleep(1)
        await msg.edit(embed=nextcord.Embed(
            title="Кейс из Кс-го",
            description=f"`----------------------------------`\n`||`  {random.choice([blue, purple, pink, seriy, golden, red])}  `||`\n`----------------------------------`", color=nextcord.Colour.random()
            ))
        case_end_drop = random.choice([blue, purple, pink, seriy, golden, red, blue, blue, blue, seriy, seriy])
        await sleep(1.5)
        await msg.edit(embed=nextcord.Embed(
            title="Кейс из Кс-го",
            description=f"`----------------------------------`\n`||`  {random.choice([blue, purple, pink, seriy, golden, red])}  `||`\n`----------------------------------`", color=nextcord.Colour.random()
            ))
        drop_case = random.choice([blue, purple, pink, seriy, golden, red, blue, blue, blue, blue, seriy, seriy, blue, blue, blue, blue, blue, blue, blue])
        await sleep(2)
        if drop_case == blue:
            await msg.edit(embed=nextcord.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=nextcord.Colour.blue(), timestamp=datetime.datetime.now()))   
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await msg.edit(embed=embed)
        elif drop_case == purple:
            await msg.edit(embed=nextcord.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=nextcord.Colour.purple(), timestamp=datetime.datetime.now()))
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await msg.edit(embed=embed)
        elif drop_case == seriy:
            await msg.edit(embed=nextcord.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=nextcord.Colour.from_rgb(54, 57, 62), timestamp=datetime.datetime.now()))
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await msg.edit(embed=embed)
        elif drop_case == golden:
            embed=nextcord.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=nextcord.Colour.gold(), timestamp=datetime.datetime.now())
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await msg.edit(embed=embed)
        elif drop_case == red:
            embed=nextcord.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}|| {random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=nextcord.Colour.red(), timestamp=datetime.datetime.now())
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await msg.edit(embed=embed)
        elif drop_case == pink:
            embed=nextcord.Embed(
                title="Кейс Кс-го",
                description=f"Информация о вашем дропе:\nНазвание: ||{drop_case}||{random.choice(stattrack)}\nИзнос: {random.choice(pat)}",
                color=nextcord.Colour.from_rgb(255, 20, 147), timestamp=datetime.datetime.now())
            embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)
            await msg.edit(embed=embed)

    else:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Извините эта команда доступна только для тех у кого есть золотой сервер, купить его вы можете на сервере тех.поддержки \"Felter News\"',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))

  

@bot.command(aliases=["case", "open_case"])
@commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
async def case_open(ctx):
    gold = goldserver
    global case
    case = ["<:coins:919381565837025290> Монетка", "<a:avatar_servers:919973036650803210> Радужный квадрат", "Деньги", "Алмазы", "Кнопка", "Золото", "Метал", "Перчатки!", "Буква (п)", "Буква (м)", "Буква (у)", "Дорогие часы", "Не-че-го", "Нечего", "Нечего", "Число (5)", "Палка капалка", "Буква (и)", "Буква (р)", "Желатин", "{p} (Переменная префикса) - (если вам выпала то можете сменить префикс бота на любом сервере)", "DROP_CASE_NOT_FOUND. ERROR 404"]
    case1 = random.choice(case)
    msg = await ctx.reply(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....\n\n `|.......`",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....\n\n `||......`",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....\n\n `|||.....`",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....\n\n `||||....`",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....\n\n `|||||...`",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....\n\n `||||||..`",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....\n\n `|||||||.`",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description="Открываем....\n\n `||||||||`",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
        title="Открытие Кейса",
        description=f"Поздравляем вам выпало: {case1}",
        color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(2)
    channel = bot.get_channel(925125586828005426)
    await channel.send(embed=nextcord.Embed(
        title="Case command!",
        description=f"Пользователь: {ctx.author.mention}, {ctx.author}\n\n Drop: {case1}\n\nServer: {ctx.guild.id}",
        color=nextcord.Color.from_rgb(54, 57, 62), timestamp=datetime.datetime.now()
    ))

@bot.command(aliases=["box"])
#@commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
async def box_open_case_requier_admin_shop_rorkes(ctx):
  #await ctx.reply(embed=nextcord.Embed(title="Ошибка!", description="Извините эта команда доступна только во время праздников", color=nextcord.Colour.red(), timestamp=datetime.datetime.now()))
    drop = ["Земля", "Семечки", "Дерево", "Метал", "Золото", "Конфеты", "Рюкзак", "Вейп", "Алмаз", "Ламинат", "Ленолиум", "Кнопка", "Лошка", "Перчатки", "Премиум на 1 месяц(в боте)", "Золотой билет", "Премиум на 2 месяца", "Земля", "Семечки", "Палка", "Земля", "Земля", "Премиум на 3 месяца", "Земля", "Пустота", "Премиум на 4 месяца", "Земля","Воздух", "Носки", "Пенал", "Роль на сервере поддержки", "Земля", "Конфеты", "Земля", "Семечки", "Носки", "Пустота", "Метал", "Вейп", "Земля", "Земля", "Земля", "Земля", "Воздух", "Земля", "Земля", "Земля", "Земля", "Земля", "Земля", "Земля"]
    channel = bot.get_channel(925125586828005426)
    global drop1
    drop1 = random.choice(drop)
    msg = await ctx.reply(embed=nextcord.Embed(
      title="Открытие подарка",
      description="Открываем....",
      color=nextcord.Color.from_rgb(54, 57, 62)
    ))
    await sleep(1)
    await msg.edit(embed=nextcord.Embed(
      title="Подарок",
      description=f"Вам выпало: ||**{drop1}**||\n\nПодсказка: Подарки по типу: Премиум на 1 месяц можно активировать. На сервере тех.Поддержки",
      color=nextcord.Color.from_rgb(54, 57, 62)
      ))
    await sleep(1)
    await channel.send(embed=nextcord.Embed(
      title=f"Пользователю: {ctx.author}",
      description=f"Выпало: {drop1}\n mention: {ctx.author.mention}\n Server: {ctx.guild.id}",
      color=nextcord.Color.from_rgb(54, 57, 62)
    ))
@bot.command()
@commands.cooldown(rate=2, per=23, type=commands.BucketType.user)
async def returndrop(ctx):
  await ctx.reply(embed=nextcord.Embed(
    title=f"Ваш прошлый дроп",
    description=f"{drop1}",
    color=nextcord.Color.from_rgb(54, 57, 62), timestamp=datetime.datetime.now()
  ))

@bot.event
async def on_guild_join(guild):
    channel = bot.get_channel(916027696721592410)
    await channel.send(embed=nextcord.Embed(
        title=f"бот был добавлен!",
        description=
        f'<@&888351447434027049>\n ID сервера: {guild.id}\n Name servers: {guild.name}',
        color=nextcord.Color.from_rgb(88, 101, 242), timestamp=datetime.datetime.now()))
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "f+"
    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f)
    role1 = await guild.create_role(name="felter bot")

@bot.command()
async def unban(ctx, member):
  await unban(member, reason=f"unbaned for - ({ctx.author})")
  await ctx.reply(embed=nextcord.Embed(title="<:yes:945469612076720128> Разбан", description=f"Пользователь: <@&{member}>\n\nАдминистратор: {ctx.author.mention}", color=nextcord.Color.blue(), timestamp=datetime.datetime.now()))

@bot.event
async def on_guild_remove(guild):
    channel = bot.get_channel(916027696721592410)
    await channel.send(embed=nextcord.Embed(
        title=f"бот был Удалён",
        description=
        f'<@&888351447434027049>\n ID сервера: {guild.id}\n Name servers: {guild.name}',
        color=nextcord.Color.from_rgb(88, 101, 242), timestamp=datetime.datetime.now()))


@commands.has_permissions(administrator=True)
@bot.command()
@commands.cooldown(rate=1, per=3600, type=commands.BucketType.user)
async def premtick(ctx, *, text):
    channel = bot.get_channel(916316833827651604)

    gold = goldserver

    if f'{ctx.message.author.id}' in blackmember:

        await ctx.reply(
            "Извините но вы в чёрном списке бота, причину можно узнать у модераторов/сапортов/разработчиков"
        )

    elif len(text) < 20:
        iiiii = await ctx.reply(embed=nextcord.Embed(
            title=f':no_entry: Erorr',
            description=
            f'```cs\n#Извините, но вип обращение к разработчикам должно содержать минимум 20 символов!\n```',
            colour=nextcord.Color.red(), timestamp=datetime.datetime.now()))
        await iiiii.add_reaction('❌')

    elif len(text) > 100:
        iiiiii = await ctx.reply(embed=nextcord.Embed(
            title=f':no_entry: Erorr',
            description=
            f'```cs\n#Извините, но вип обращение может содержать максимум 100 символов!\n```',
            colour=nextcord.Color.red(), timestamp=datetime.datetime.now()))
        await iiiiii.add_reaction('❌')

    elif f'{ctx.message.guild.id}' in gold:

        await channel.send(embed=nextcord.Embed(
            title=
            f"Новое вип обращение! \nПользователь: {ctx.message.author.id}",
            description=
            f'Ид Сервера:     {ctx.message.guild.id}\nКанал: {ctx.channel.name}\n Пользователь: {ctx.message.author.mention}\nУпоминание канала: <#{ctx.channel.id}>\nНазвание сервера: {ctx.guild.name}\nТекст: {text}',
            color=nextcord.Color.from_rgb(88, 101, 242), timestamp=datetime.datetime.now()))

        file = open(f"ticket's/premtick{ctx.message.guild.id}.txt", "a")
        file.write(
            f"Premium tick\nID Members: {ctx.message.author.id}\nGUILD ID:      {ctx.message.guild.id}\nTEXT: {text}\n---------------"
        )

        await ctx.reply(embed=nextcord.Embed(
            title=f"{ctx.author}",
            description=
            f'Ваше вип обращение было отправлено разработчикам\nВаш текст: `{text}`',
            color=nextcord.Color.from_rgb(88, 101, 242), timestamp=datetime.datetime.now()))

    else:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Извините эта команда доступна только для тех у кого есть золотой сервер, купить его вы можете на сервере тех.поддержки \"Felter News\"',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))


@commands.has_permissions(administrator=True)
@bot.command(aliases=["pr", "set"])
@commands.cooldown(rate=1, per=30, type=commands.BucketType.guild)
async def prefix(ctx, prefix):
    gold = goldserver
    prefixx = await bot.get_prefix(ctx.message)

    if len(prefix) > 10:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Извините, ваш префикс может содержать максимум 10 символов.',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))

    elif prefix == prefixx:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Извините, вы не можете поменять префикс на {prefix} он уже на сервере',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))
  
    elif f'{ctx.message.guild.id}' in gold:

        with open("prefixes.json", "r") as f:
            prefixes = json.load(f)
        prefixes[str(ctx.guild.id)] = prefix
        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)

        await ctx.reply(embed=nextcord.Embed(
            title="<a:dot:923208542410919996> Смена префикса",
            description=f'Вы изменили префикс сервера на: {prefix}',
            color=nextcord.Color.blue(), timestamp=datetime.datetime.now()))


    else:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Извините эта команда доступна только для тех у кого есть золотой сервер, купить его вы можете на сервере тех.поддержки \"Felter News\"',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))


@bot.command()
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def check(ctx):
    gold = goldserver

    if f'{ctx.message.author.id}' in blackmember:

        await ctx.reply(
            "Извините но вы в чёрном списке бота, причину можно узнать у модераторов/сапортов/разработчиков. вот тут "
        )

    elif f'{ctx.message.guild.id}' in gold:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Название сервера: {ctx.guild.name}\nID сервера: {ctx.message.guild.id}\nСостояние премиума: Включён',
            color=nextcord.Color.from_rgb(88, 101, 242), timestamp=datetime.datetime.now()))
    else:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Название сервера: {ctx.guild.name}\nID сервера: {ctx.message.guild.id}\nСостояние премиума: Выключен',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))



#@bot.command()
#async def get_links(ctx):
#  invites = []
#  for guild in bot.guilds:
#    for c in guild.text_channels:
#      if c.permissions_for(guild.me).create_instant_invite:  # make sure the bot can actually create an invite
#          invite = await c.create_invite()
#          invites.append(invite)
#          await ctx.send(invites)


@commands.has_permissions(administrator=True)
@bot.command()
@commands.cooldown(rate=1, per=36000, type=commands.BucketType.user)
async def tick(ctx, *, tick):
    channel = bot.get_channel(913521469831663626)

    if f'{ctx.message.author.id}' in blackmember:

        await ctx.reply(
            "Извините но вы в чёрном списке бота, причину можно узнать у модераторов/сапортов/разработчиков. вот тут "
        )

    elif '@everyone' in tick:
        iii = await ctx.reply("Извините но данное содержимое запрещено")
        await iii.add_reaction('❌')

    elif '@here' in tick:
        ii = await ctx.reply("Извините но данное содержимое запрещено")
        await ii.add_reaction('❌')

    elif len(tick) < 20:
        iiiii = await ctx.reply(
            "Извините, но обращение к разработчикам должно содержать мин `20` символов"
        )
        await iiiii.add_reaction('❌')

    elif len(tick) > 100:
        iiiiii = await ctx.reply(
            "Извините, но обращение к разработчикам может содержать макс `100` символов"
        )
        await iiiiii.add_reaction('❌')

    else:
        await channel.send(embed=nextcord.Embed(
            title=f"Пользователь: {ctx.message.author.id}",
            description=
            f'Ид Сервера:     {ctx.message.guild.id}\nКанал: {ctx.channel.name}\n Пользователь: {ctx.message.author.mention}\nНазвание сервера: {ctx.guild.name}\nТекст: {tick}',
            color=nextcord.Color.from_rgb(88, 101, 242), timestamp=datetime.datetime.now()))

        file = open(
            f"ticket's/{random.randint(81275782135,712654215312323216851)}.txt",
            "a")
        file.write(
            f"---------------\nID Members: {ctx.message.author.id}\nGUILD ID:      {ctx.message.guild.id}\nTEXT: {tick}"
        )

        await ctx.reply(embed=nextcord.Embed(
            title=f"{ctx.author}",
            description=
            f'Ваше обращение было отправлено разработчикам\nВаш текст: `{tick}`',
            color=nextcord.Color.from_rgb(88, 101, 242), timestamp=datetime.datetime.now()))


@bot.command()
@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
async def привет(ctx):
    await ctx.reply("Привет, привет)")


@bot.command()
@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
async def пока(ctx):
    await ctx.reply("Пока. Надеемся ты придёшь снова :(")


@bot.command()
@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
async def asd(ctx):
    user = ctx.author.mention
    await ctx.reply(user + "\nЧё команды проверяешь?")


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    @commands.cooldown(rate=2, per=10, type=commands.BucketType.user)
    async def user(ctx,
                   member: nextcord.Member = None,
                   guild: nextcord.Guild = None):
        await ctx.message.delete()
        if member == None:
            emb = nextcord.Embed(title="Информация о пользователе",
                                 color=ctx.message.author.color, timestamp=datetime.datetime.now())
                                 
            emb.add_field(name="Имя:",
                          value=ctx.message.author.display_name,
                          inline=False)
            emb.add_field(name="Айди пользователя:",
                          value=ctx.message.author.id,
                          inline=False)
            t = ctx.message.author.status
            if t == nextcord.Status.online:
                d = " В сети"

            t = ctx.message.author.status
            if t == nextcord.Status.offline:
                d = " Не в сети"

            t = ctx.message.author.status
            if t == nextcord.Status.idle:
                d = " Не активен"

            t = ctx.message.author.status
            if t == nextcord.Status.dnd:
                d = " Не беспокоить"

            emb.add_field(name="Активность:", value=d, inline=False)
            emb.add_field(name="Статус:",
                          value=ctx.message.author.activity,
                          inline=False)
            emb.add_field(name="Самая высокая роль на сервере:",
                          value=f"{ctx.author.top_role.mention}",
                          inline=False)
            emb.set_thumbnail(url=ctx.message.author.avatar)
            await ctx.send(embed=emb)
        else:
            emb = nextcord.Embed(title="Информация о пользователе",
                                 color=member.color, timestamp=datetime.datetime.now())
            emb.add_field(name="Имя:", value=member.display_name, inline=False)
            emb.add_field(name="Айди пользователя:",
                          value=member.id,
                          inline=False)
            t = member.status
            if t == nextcord.Status.online:
                d = " В сети"

            t = member.status
            if t == nextcord.Status.offline:
                d = " Не в сети"

            t = member.status
            if t == nextcord.Status.idle:
                d = " Не активен"

            t = member.status
            if t == nextcord.Status.dnd:
                d = " Не беспокоить"
            emb.add_field(name="Активность:", value=d, inline=False)
            emb.add_field(name="Статус:", value=member.activity, inline=False)
            emb.add_field(name="Самая высокая роль на сервере:",
                          value=f"{member.top_role.mention}",
                          inline=False)
            await ctx.send(embed=emb)


def setup(bot):
    bot.add_cog(User(bot))


#команда сай в эмбед


class Sayem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.guild_only()
    async def sayem(ctx, *, names):

        if f'{ctx.message.author.id}' in blackmember:

            await ctx.reply(
                "Извините но вы в чёрном списке бота, причину можно узнать у модераторов/сапортов/разработчиков. вот тут "
            )

        elif f'{ctx.message.guild.id}' in goldserver:
            await ctx.reply(embed=nextcord.Embed(
                title=f'{ctx.author}',
                description=names,
                colour=nextcord.Colour.from_rgb(0, 204, 102), timestamp=datetime.datetime.now()))
        else:
            await ctx.reply(embed=nextcord.Embed(
                description=
                f'Извините эта команда доступна только для тех у кого есть золотой сервер, купить его вы можете на сервере тех.поддержки \"Felter News\"',
                color=nextcord.Color.red(), timestamp=datetime.datetime.now()))


def setup(bot):
    bot.add_cog(Sayem(bot))


class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot


@bot.command()
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def calc(ctx, *, operation: str):

    if f'{ctx.message.author.id}' in blackmember:

        await ctx.reply(
            "Извините но вы в чёрном списке бота, причину можно узнать у модераторов/сапортов/разработчиков. вот тут "
        )

    else:

        async with ctx.typing():
            await sleep(1)
        await ctx.reply(
            embed=nextcord.Embed(title=f"Калькулятор!",
                                 description=f"Ответ: `{eval(operation)}` ",
                                 colour=nextcord.Colour.random(), timestamp=datetime.datetime.now()))


def setup(bot):
    bot.add_cog(Calc(bot))


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def per(ctx, *, names):
    a = names
    await ctx.reply(embed=nextcord.Embed(title=f"Перевернуть текст!",
                                         description=a[::-1],
                                         color=discord.Color.blue(), timestamp=datetime.datetime.now()))


#Команда инфо о сервере


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    @commands.guild_only()
    async def info(ctx):
        role_count = len(ctx.guild.roles)
        shard_id = ctx.guild.shard_id
        shard = bot.get_shard(shard_id)
        shard_ping = round(shard.latency * 1000)

        serverinfoEmbed = nextcord.Embed(color=ctx.author.color, timestamp=datetime.datetime.now())

        serverinfoEmbed.add_field(
            name=" :diamond_shape_with_a_dot_inside:  Имя сервера",
            value=f"{ctx.guild.name}",
            inline=True)
        serverinfoEmbed.add_field(name=" :family_mwbb:  Всего участников",
                                  value=f"{ctx.guild.member_count}",
                                  inline=True)
        serverinfoEmbed.add_field(name=" :scroll:  Проверка сервера",
                                  value=f"{ctx.guild.verification_level}",
                                  inline=True)
        serverinfoEmbed.add_field(name=" :ledger:  ролей на сервере",
                                  value=f"{role_count}",
                                  inline=True)
        serverinfoEmbed.add_field(name=" :vibration_mode:  Пинг шарда сервера",
                                  value=f"{shard_ping}",
                                  inline=True)
        serverinfoEmbed.add_field(
            name=" :card_box:  Шард",
            value=f"Название:{shard_id}one\nID: {shard_id}",
            inline=False)

        await ctx.send(embed=serverinfoEmbed)


def setup(bot):
    bot.add_cog(Info(bot))


#клеар
class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    async def clear(ctx, amount: int):
        if amount < 1:
            number12 = await ctx.send(embed=await ctx.send(
                embed=nextcord.Embed(title=f":no_entry: Erorr ",
                                     description=f' **Число не меньше**: `1` ',
                                     color=nextcord.Color.red(), timestamp=datetime.datetime.now())))
            await number12.add_reaction('❌')
        elif amount > 100:
            number2 = await ctx.send(embed=nextcord.Embed(
                title=f":no_entry: Erorr ",
                description=f' **Число не больше**: `100` ',
                color=nextcord.Color.red(), timestamp=datetime.datetime.now()))
            await number2.add_reaction('❌')
        else:
            await ctx.channel.purge(limit=int(amount + 1))
            embed = await ctx.send(embed=nextcord.Embed(
                title=f"Очистка чата!",
                description=
                f' {ctx.author.mention} , Я очистил `{amount}` сообщений',
                color=nextcord.Color.blue(), timestamp=datetime.datetime.now()))
        await embed.add_reaction('✅')
        await asyncio.sleep(10)
        await embed.delete()


def setup(bot):
    bot.add_cog(Clear(bot))


#ответы на вопросы
class Helpp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.user)
    @commands.guild_only()
    async def helpp(ctx):
        embed1 = nextcord.Embed(
            title="Зачем мы делаем бота если фитБека нету?",
            description='Просто ради Забавы и обучение в общем')
        embed21 = nextcord.Embed(
            title="Кто вы такие?",
            description='Не мы а он, Я ТимЕйджер разработчик ботов')
        embed22 = nextcord.Embed(title="Когда Бот выйдет в релиз",
                                 description='Уже вышел')
        embed31 = nextcord.Embed(title="Почему именно  \"Felter?\" ",
                                 description='Незнаю но мне нравится Филтер')
        embed32 = nextcord.Embed(
            title="Как стать модератором на сервере Тех.Под?",
            description='Никак..')
        embed33 = nextcord.Embed(
            title="Как стать Саппортом на сервере Тех.Под?",
            description=
            'Если вы хороший модератор,\n и вы хорошо обьясняйте то вам к <@665271319545511939>'
        )
        embed34 = nextcord.Embed(title="Почему именно Python?",
                                 description='Он мне очень пригледелся')
        embeds = [
            embed1, [embed21, embed22], [embed31, embed32, embed33, embed34]
        ]
        message = await ctx.send(embed=embed1)
        page = Paginator(bot,
                         message,
                         only=ctx.author,
                         use_more=True,
                         embeds=embeds)
        await page.start()


def setup(bot):
    bot.add_cog(Helpp(bot))


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def rand(ctx):
    embed: nextcord.Embed = nextcord.Embed(
        title="Рандомное число!",
        description=f"`{random.randint(0,10000)}`",
        color=nextcord.Color.blue(), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"Запросил: {ctx.author}",
                     icon_url=f"{ctx.author.avatar}")

    await ctx.send(embed=embed)


class Slmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @bot.command()
    @commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
    @commands.guild_only()
    async def slmd(ctx, time: int):

        if time < 1:
            await ctx.reply(embed=await ctx.reply(
                embed=discord.Embed(title=f":no_entry: Erorr ",
                                    description=f' **Число не меньше**: 1 ',
                                    color=discord.Color.red(), timestamp=datetime.datetime.now())))

        elif time > 21600:
            await ctx.reply(embed=await ctx.reply(embed=nextcord.Embed(
                title=f":no_entry: Erorr",
                description=f' **Число не больше**: 21600 секунд ',
                color=nextcord.Color.red(), timestamp=datetime.datetime.now())))
            return
        else:
            await ctx.channel.edit(slowmode_delay=time)
            await ctx.reply(embed=await ctx.reply(embed=nextcord.Embed(
                title=f"Слоу-Мод",
                description=f'Вы успешно поставили Слоу-Мод на `{time}` Секунд',
                color=nextcord.Color.blue(), timestamp=datetime.datetime.now())))


def setup(bot):
    bot.add_cog(Slmd(bot))


@bot.command(pass_context=True)
@commands.cooldown(rate=1, per=50, type=commands.BucketType.user)
async def randif(ctx):


  gold = goldserver
  if f'{ctx.message.guild.id}' in gold:
        ii1 = await ctx.reply(
            f"Рандомный номер телефона, - `+79{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}{random.randint(1,9)}`\n{ctx.author.mention} **Рандомный номер телефона удаляется через 50 секунд!**"
        )
        await asyncio.sleep(50)
        await ii1.delete()

  else:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Извините эта команда доступна только для тех у кого есть золотой сервер, купить его вы можете на сервере тех.поддержки \"Felter News\"',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))



@commands.has_permissions(manage_messages=True)
@bot.command(pass_context=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def say(ctx, *, Sya):
    async with ctx.typing():
        await sleep(1)
        await ctx.send(Sya)


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def meme(ctx):
        gold = goldserver
        post = memepost

        if f'{ctx.message.author.id}' in blackmember:

            await ctx.reply(
                "Извините но вы в чёрном списке бота, причину можно узнать у модераторов/сапортов/разработчиков. вот тут "
            )

        elif f'{ctx.message.guild.id}' in gold:
            async with ctx.typing():
                await sleep(2)
                await ctx.reply(random.choice(post))
        else:
            await ctx.reply(embed=nextcord.Embed(
                description=
                f'Извините эта команда доступна только для тех у кого есть золотой сервер, купить его вы можете на сервере тех.поддержки \"Felter News\"',
                color=nextcord.Color.red(), timestamp=datetime.datetime.now()))


def setup(bot):
    bot.add_cog(Meme(bot))


class Oldtimer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    @commands.cooldown(rate=1, per=30, type=commands.BucketType.guild)
    @commands.guild_only()
    async def oldtimer(ctx, number: int):
        try:
            if number < 1:
                number12 = await ctx.reply(embed=await ctx.reply(
                    embed=nextcord.Embed(
                        title=f":no_entry: Erorr",
                        description=f' **Число не меньше**: 1 ',
                        color=nextcord.Color.red(), timestamp=datetime.datetime.now())))
                await number12.add_reaction('❌')
            elif number > 500:
                number2 = await ctx.reply(embed=nextcord.Embed(
                    title=f":no_entry: Erorr",
                    description=f' **Число не больше**: 500 ',
                    color=nextcord.Color.red(), timestamp=datetime.datetime.now()))
                await number2.add_reaction('❌')
            else:
                message = await ctx.reply(number)
                while number != 0:
                    number -= 1
                    await message.edit(content=number)
                    await asyncio.sleep(1)
                await message.edit(
                    content=(f'`Таймер Завершён!` {ctx.author.mention}'))
                await message.add_reaction('✅')
            await asyncio.sleep(30)
            await message.delete()
            await ctx.message.delete()
        except ValueError:
            return


def setup(bot):
    bot.add_cog(Oldtimer(bot))

#команда бан
class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot


@commands.has_permissions(ban_members=True)
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def ban(ctx, user: nextcord.Member, *, reason="Отсутсвует"):
    await user.ban(reason=reason + f" ({ctx.author})")
    ban = nextcord.Embed(
        title=f"⛔  Участник  {user.name} был забанен!",
        description=
        f"Причина: {reason}\nМодератор: {ctx.author.mention} \n Сервер: {ctx.guild}", colour=nextcord.Colour.dark_red()
, timestamp=datetime.datetime.now()    )
    await ctx.channel.send(embed=ban)
    await ban.add_reaction('✅')
    await user.send(embed=ban)


def setup(bot):
    bot.add_cog(Ban(bot))


@commands.has_permissions(kick_members=True)
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def kick(ctx, user: nextcord.Member, *, reason="Отсутсвует"):
    await user.kick(reason=reason)
    ban1 = nextcord.Embed(
        title=f":burrito: Участник  {user.name} был кикнут!",
        description=
        f"Причина: {reason}\nМодератор: {ctx.authom.mention}.\n Сервер: {ctx.guild} ", colour=nextcord.Colour.dark_red()
, timestamp=datetime.datetime.now()     )
    await ctx.message.delete()
    await ctx.channel.send(embed=ban)
    await ban1.add_reaction('✅')
    await user.send(embed=ban)


#команда инвайт
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def inv(ctx):
    await ctx.reply(embed=nextcord.Embed(
        title="Добавить бота на свой сервер!",
        description=" `Naso4ekTiam!` ",
        url=
        'https://discord.com/oauth2/authorize?client_id=815315388073639948&guild_id=774867044927406120&scope=applications.commands%20bot&permissions=980937982'
    ))


#права для администратора
@commands.has_permissions(administrator=True)
#команда мут
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def mu(ctx, member: nextcord.Member, time: int, arg):
    emb = nextcord.Embed(title="Участник Был Замучен! По причине: " + arg,
                         colour=nextcord.Color.blue(), timestamp=datetime.datetime.now())
    await ctx.channel.purge(limit=1)
    emb.set_author(name=member.name, icon_url=member.avatar)
    emb.set_footer(text="Его замутил {}".format(ctx.author.name),
                   icon_url=ctx.author.avatar)

    await ctx.send(embed=emb)
    muted_role = nextcord.utils.get(ctx.message.guild.roles, name="Muted")
    await member.add_roles(muted_role)
    await emb.add_reaction('✅')

    await asyncio.sleep(time)

    await member.remove_roles(muted_role)
    await ctx.message.delete()


@commands.has_permissions(administrator=True)
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
@bot.command()
async def cr(ctx, *, content):
  role = await ctx.guild.create_role(name=content, reason="Command=CR")
  await ctx.reply(embed=nextcord.Embed(title="Создание роли", description=f"Название: <@&{role.id}>\n Создал: {ctx.author.mention}",color=nextcord.Color.blue(), timestamp=datetime.datetime.now()))



#хелп в меню с кликами


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def help(ctx):
    prefix = await bot.get_prefix(ctx.message)
    p = prefix
    embed2 = nextcord.Embed(
        title="Информация",
        description=
        f'• `{p}con` Связатся с разработчиком \n • `{p}binfo` Узнать информацию о боте \n •  `{p}faq` Помощь в боте \n •  `{p}helpp` Ответы на вопросы \n •  `{p}inv`  Приглaсить бота на свой сервер \n • `{p}t` Просто так \n • `{p}ava` @участник, Узнать аватарку участника \n  • `{p}ping` узнать пинг бота! \n • `{p}dock` Зайти на сервер бота!\n • `{p}oldhelp` настольгический хелп(самый 1 хелп)\n • `{p}user` @user Показывает инфо о юзере \n • `{p}jon` показывает на сколько % вы `?` животное\n • `{p}aus` покажет импестер ли вы? \n • `{p}calc` Вопрос пример: 2+2 и бот ответит 4\n • `{p}check` Проверить есть ли у вас золотой сервер?\n • `{p}sponsor` Показать кто помогал в создании бота\n • `{p}donate` Узнать как купить донат',
        colour=ctx.author.color)
    embed11 = nextcord.Embed(
        title="Модерация",
        description=
        f"•  `{p}ban` @участник Причина \n •  `{p}kick` @Участник причина \n • `{p}mu` @участник \"Время\" \"Причина\" - Что-бы заглушить участника \n •  `{p}gol` [Тексt] команда для голосование!\n • `{p}say` [тексt] \n • `{p}clear` \"Кол-во сообщений\" удаляет сообщения в чате(Не больше 100 не меньше 1) \n • `{p}slmd` \"Время в секундах\" Поставить Слоу-мод(Задержку) в канале (Не больше 21600 не меньше 1) \n • `{p}cr` \"Название роли\" Создать роль \n • `{p}nick` @участник \"Новый ник\" Изменить ник участнику \n • `f+addr` @Участник @role . Для выдачи роли участнику \n • `{p}tick` <Ваш Текст которые вы хотите отправить разработчикам> Команда для обращение к разработчикам, откройте лс, иначе разработчики не смогу с вами связатся.\n • `{p}checkuser` « id »(только айди подругому никак!) Проверить есть ли пользователь в чёрном списке бота?\n • `{p}code help 1` Открыть оболочку выполнение команд задаными пользователем(выполняет команды который скажет пользователь)",
        colour=ctx.author.color)
    embed90 = nextcord.Embed(
        title="Для участников ",
        description=
        f' •  `{p}баг` контакты для сообщение о баге разработчику \n • `{p}rand` Рандомное число! \n • `{p}timer` "Число" **Примечание!** число не больше 500 и не меньше 1\n • `{p}ball` \"Ваш вопрос\" бот отвечает на ваш вопрос \n ответсвености за испольнителя команды!)\n • `{p}coin` Бот подкинет монетку!\n • `{p}ships` @участник and id показывает `%` вашей любви\n • `{p}gay` показывает на сколько `%` вы гей)\n • `{p}iq` показывает ваш iq\n • `{p}per` \"Текст в ковычках\" Первевернуть текст \n • `{p}dog` Бот пришлёт рандомную фотку собаки(Если сообщение не отправилось подождите боту нужно сгенерировать фотку) \n • `{p}cat` Бот отправит рандомное фото кошки(та)\n • `{p}привет` Новая мини игра с ботом! Ваша задача успеть написать команду {p}привет за 3 секунды. Тоже самое с командой {p}пока\n • `{p}???` Секретная команда! Найдите её!!\n • `{p}box` Открыть подарок(Активация подарка на сервере тех.поддержки(нужен скрин))\n • `{p}returndrop` Узнать свой прошлый подарок из бокса({p}box) (Хранится до рестарта бота)\n • `{p}case` Открытие кейса!\n • `{p}search` [Ваш запрос в яндекс]',
        colour=ctx.author.color)
    embed87 = nextcord.Embed(
        title="Премиум команды",
        description=
        f' • `{p}meme` Отправляет рандомный мем из файлов бота\n • `{p}randif` Показать рандомный номер телефона(Данные номера делаются при помощи рандома! все события связеные с реальной жизнью совпадение автор не несёт \n •  `{p}sayem` [Текст] сказать от имени бота\n • `{p}premtick` <TEXT> отправить вип обращение к разработчикам (разрешены `@everyone` and `@here`) - (За спам или оффтоп ваш премиум снимается)\n • `{p}popit` Активировать поп ит в дискорде!\n • `{p}sd` Аквивировать Симпл-димпл\n • `{p}prefix` <ваш префикс> меняет префикс на сервере\n • `{p}Case_cs` Открыть кейс из кс-го',
        colour=ctx.author.color)
    embeds = [embed2, [
        embed11,
    ], [embed90], [embed87]]
    message = await ctx.send(embed=embed2)
    page = Paginator(bot,
                     message,
                     only=ctx.author,
                     use_more=False,
                     embeds=embeds)
    await page.start()


def setup(bot):
    bot.add_cog(Help(bot))


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def cat(ctx):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = nextcord.Embed(title='Рандомное фото кошки(та)) 🐈',
                           colour=nextcord.Colour.purple(), timestamp=datetime.datetime.now() )
    embed.set_image(url=data['file'])
    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
    await ctx.reply(embed=embed)

@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def api(ctx):
    response = requests.get('https://felter.jkvityaofficial.repl.co/api')
    data = response.json()
    embed = nextcord.Embed(title='Status API',                    colour=nextcord.Colour.random(), timestamp=datetime.datetime.now() )
    embed.set_image(url=data['bot'])
    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
    await ctx.reply(embed=embed)

class Pop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot


@bot.command()
@commands.cooldown(rate=1, per=59, type=commands.BucketType.user)
async def popit(ctx):

    embed = nextcord.Embed(
        title=f"POP IT!",
        description=
        f"||:red_circle:|| ||:red_circle:|| ||:red_circle:|| ||:red_circle:|| ||:red_circle:||\n||:blue_circle:|| ||:blue_circle:|| ||:blue_circle:|| ||:blue_circle:|| ||:blue_circle:||\n||:purple_circle:|| ||:purple_circle:|| ||:purple_circle:|| ||:purple_circle:|| ||:purple_circle:||\n||:orange_circle:|| ||:orange_circle:|| ||:orange_circle:|| ||:orange_circle:|| ||:orange_circle:||\n||:green_circle:|| ||:green_circle:|| ||:green_circle:|| ||:green_circle:|| ||:green_circle:||",
        colour=nextcord.Color.dark_blue(), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
    gold = goldserver

    if f'{ctx.message.guild.id}' in gold:
        await ctx.send(embed=embed)

    else:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Извините эта команда доступна только для тех у кого есть золотой сервер, купить его вы можете на сервере тех.поддержки \"Felter News\"',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))


def setup(bot):
    bot.add_cog(Pop(bot))


class Jon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def jon(ctx):
    variable = [
        "Корова", "Курица", "Кошка", "Собака", "Волк", "Абу бандит", "Осминог",
        "Баран", "Кабан", "Зебра", "Лошадь", "Тигр", "Леопард", "Пантера",
        "Felter"
    ]

    await ctx.reply(embed=nextcord.Embed(
        title="На сколько % вы животное",
        description=
        f"{ctx.author.mention} Мне кажется ты : {random.choice(variable)} на {random.randint(0,100)}%",
        color=discord.Color.blue(), timestamp=datetime.datetime.now()))
    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jon(bot))


class Sd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.command()
@commands.cooldown(rate=1, per=59, type=commands.BucketType.user)
async def sd(ctx):

    embed = nextcord.Embed(
        title=f"Симпл-димпл!",
        description=
        f":white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:||:red_square: :red_square: :red_square:||:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:||:red_square: :red_square: :red_square:||:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:||:red_square: :red_square: :red_square:||:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:||:red_square: :red_square: :red_square:||:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:||:blue_square: :blue_square: :blue_square:||:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:||:blue_square: :blue_square: :blue_square:||:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:||:blue_square: :blue_square: :blue_square:||:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square:||:blue_square: :blue_square: :blue_square:||:white_large_square::white_large_square::white_large_square:\n:white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square::white_large_square:",
        colour=nextcord.Color.blue(), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")

    gold = goldserver
    if f'{ctx.message.guild.id}' in gold:

        await ctx.message.delete()
        await ctx.send(embed=embed)
    else:
        await ctx.reply(embed=nextcord.Embed(
            description=
            f'Извините эта команда доступна только для тех у кого есть золотой сервер, купить его вы можете на сервере тех.поддержки \"Felter News\"',
            color=nextcord.Color.red(), timestamp=datetime.datetime.now()))


def setup(bot):
    bot.add_cog(Sd(bot))


class Ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def ball(ctx, *, names):

    variable = [
        "Нет", "Да :clap:", "Наверное :sweat_smile: ", "Что вам надо Уточнить",
        "100% да", "50 на 50", "Определённо да! :ok_hand:"
    ]

    embed: nextcord.Embed = nextcord.Embed(
        title="Ваш вопрос: " + names,
        description=f"Мне кажется : {random.choice(variable)}".format(
            random.choice(variable)),
        color=nextcord.Color.blue(), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"Понял?: {ctx.author}",
                     icon_url=f"{ctx.author.avatar}")

    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Ball(bot))


class Coin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def coin(ctx):

    variable = [
        "Выпала: Решка! Норм.", "Выпал: Орёл! :eagle: Воу.",
        "Хм! Монетка выпала ребром)", "Выпал: Орёёёёёл! :eagle: ",
        "Выпала: Реешка!"
    ]

    embed: nextcord.Embed = nextcord.Embed(
        title=":coin: Монетка!",
        description=f"{random.choice(variable)}".format(
            random.choice(variable)),
        color=nextcord.Color.blue(), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"Выполнил команду: {ctx.author}",
                     icon_url=f"{ctx.author.avatar}")

    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Coin(bot))


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def dog(ctx):
    async with aiohttp.ClientSession() as session:
        request = await session.get('https://some-random-api.ml/img/dog')
        dogjson = await request.json()

    embed = nextcord.Embed(title="Рандомная собака)!",
                           color=nextcord.Color.purple(), timestamp=datetime.datetime.now())
    embed.set_image(url=dogjson['link'])
    embed.set_footer(text=f"Выполнил команду: {ctx.author}",
                     icon_url=f"{ctx.author.avatar}")
    await ctx.send(embed=embed)


#аватар команда
class Ava(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def ava(ctx, member: nextcord.Member = None):
    if member == None:
        await ctx.message.add_reaction('❌')
    else:
        members = member.avatar
    avatarEmbed = nextcord.Embed(title=f"Аватарка - {member}")
    color=nextcord.Colour.blue(), 
    timestamp=datetime.datetime.now()
    avatarEmbed.set_image(url=members)
    await ctx.send(embed=avatarEmbed)


def setup(bot):
    bot.add_cog(Ava(bot))


class Ships(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def ships(ctx, member: nextcord.Member = None):

    if f'{ctx.message.author.id}' in blackmember:

        await ctx.reply(
            "Извините но вы в чёрном списке бота, причину можно узнать у модераторов/сапортов/разработчиков. вот тут "
        )

    elif member == None:
        await ctx.message.add_reaction('❌')
        await ctx.reply("Укажите пользователя")

    elif member == ctx.author:
        await ctx.message.add_reaction('❌')

    else:

        embed = nextcord.Embed(
            title=f"Любовь %",
            description=
            f"{ctx.author.mention} и {member.mention} Ваша любовь состовляет - `{random.randint(0,100)}%` ",
            colour=nextcord.Colour.blue(), timestamp=datetime.datetime.now())
        embed.set_footer(text=f"Выполнил команду: {ctx.author}")
        async with ctx.typing():
            await sleep(1)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Ships(bot))


class Aus(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def aus(ctx):

    variable = ["ЧТО ВЫ ИМПОСТЕР!", "что вы не импостер)"]

    embed: nextcord.Embed = nextcord.Embed(
        title="Импостер! Рулетка!",
        description=
        f"{ctx.author.mention} Мне Кажется что : {random.choice(variable)}".
        format(random.choice(variable)),
        color=nextcord.Color.blue(), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"Выполнил команду: {ctx.author}",
                     icon_url=f"{ctx.author.avatar}")

    async with ctx.typing():
        await sleep(1)
    await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Aus(bot))


@bot.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def nick(ctx, member: nextcord.Member, *, nick):
    if member == None:
        await ctx.send(
            embed=nextcord.Embed(title=f":no_entry: Erorr",
                                 description=f' Укажите Участника! ',
                                 color=nextcord.Color.red(), timestamp=datetime.datetime.now()))

    else:

        await member.edit(nick=nick)
        await ctx.reply(embed=nextcord.Embed(
            title=f"Изменение ник-нейма",
            description=f'Вы изменили ник на {member.mention}',
            color=nextcord.Color.blue(), timestamp=datetime.datetime.now()))


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def iq(ctx):

    embed = nextcord.Embed(
        title=f"IQ",
        description=
        f"{ctx.author.mention} Ваш IQ - `{random.randint(50,300)}` ",
        colour=nextcord.Colour.blue(), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
    await ctx.message.delete()
    await ctx.send(embed=embed)


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def gay(ctx):

    embed = nextcord.Embed(
        title=f"Гей %",
        description=
        f"**{ctx.author}** Ваш уровень гейства равен - `{random.randint(0,100)}%` ",
        colour=nextcord.Colour.blue(), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar}")
    await ctx.message.delete()
    await ctx.send(embed=embed)


#права администратора
@commands.has_permissions(administrator=True)
@bot.command()
@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
async def addr(ctx, member: nextcord.Member, role: nextcord.Role):
    idrole = await member.add_roles(role, reason="Command=ADDR")
    await ctx.send(embed=nextcord.Embed(title="<:yes:945469612076720128> Изменение ролей", description=f"Участник: {member.mention} id-({member.id})\n\nДобавленые роли: <@&{role.id}>",
    colour=nextcord.Colour.blue(), timestamp=datetime.datetime.now()))
    await embed.add_reaction('✅')


#команда баг
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def баг(ctx):
    emb = nextcord.Embed(title=f'Инфо о - { ctx.author } ',
                         color=nextcord.Color.green(), timestamp=datetime.datetime.now(), 
                         description=f'Discord id - {ctx.author.id} ')
    emb.set_thumbnail(url=ctx.author.avatar)
    emb.add_field(name='FAQ',
                  value=f'Используете свой id для сообщении о баге')
    emb.add_field(name='Репорт сюда', value=f'f+tick')
    await ctx.send(embed=emb)


#команда голосование
class Gol(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot


@commands.has_permissions(manage_messages=True)
@bot.command(pass_context=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def gol(ctx, *, names):
    embed = nextcord.Embed(title="голосование!!",
                           description=names,
                           colour=nextcord.Colour.from_rgb(0, 204, 102), timestamp=datetime.datetime.now())
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')


def setup(bot):
    bot.add_cog(Gol(bot))


#команда для доп инфо о боте
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def binfo(ctx):
    emb = nextcord.Embed(
        title=f'Запросил - { ctx.author } ',
        color=nextcord.Color.green(), timestamp=datetime.datetime.now(),
        description=f'{ctx.author.mention} - Вот тебе информация о боте')
    emb.set_thumbnail(url=ctx.author.avatar)
    emb.add_field(name='Язык програмирование бота', value=f' `nextcord.py` ')
    emb.add_field(name='Разработчик',
                  value=f'<@665271319545511939> `@Naso4ekTiam`')
    emb.add_field(
        name='Актуальный сервер',
        value=f'[Сервер тех. поддержки](https://discord.gg/gJ6m2VZS2C)')
    t = ctx.author.name
    emb.set_footer(text=t, icon_url=f"{ctx.author.avatar}")

    await ctx.send(embed=emb)


@bot.command(aliases=['спонсор', "sp", 'SP'])
async def sponsor(ctx):
    embed=nextcord.Embed(
        color=nextcord.Colour.random(), timestamp=datetime.datetime.now(),
        title='Спасибo, люди которые помогали в создании бота',
        description=
        "<@!468033389786824734>\n<@!831154427775418379>\n<@!310848622642069504>\n<@!357148372743880706>\n<@!445325759918112778>\n<@!875099117603414057>\n<@!820697908645986334>\n<@!606750630261948416>\n\n\n`GitHub inc`\nhttps://wiki.cs.money/ru\n\n\n Люди которые в этом списке очень помогли боту, спасибо вам)"
    )
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    await ctx.reply(embed=embed)


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def __init__(self, bot):
        self.bot


@bot.command(aliases=["PING"])  #пинг бота
@commands.cooldown(rate=1, per=20, type=commands.BucketType.user)
@commands.guild_only()
async def ping(ctx):
    msg = await ctx.reply(embed=nextcord.Embed(
        title=f"Ожидание",
        description=f"Ожидайте когда бот вам отправит данные с сервера",
        color=nextcord.Colour.gold(), timestamp=datetime.datetime.now()))

    shard_id = ctx.guild.shard_id
    shard = bot.get_shard(shard_id)
    shard_ping = round(shard.latency * 1000)
    shard_servers = len(
        [guild for guild in bot.guilds if guild.shard_id == shard_id])
    ping = round(bot.latency * 1000)
    ram = psutil.virtual_memory().percent
    cpu = psutil.cpu_percent()
    osps = platform.system()

    embed = nextcord.Embed(color=nextcord.Colour.random(), timestamp=datetime.datetime.now(), title=f'Статистика бота!')
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar)
    embed.add_field(name='<a:pinga:919972969198014515> `Пинг бота`',
                    value=f'```\n{ping}\n```')
    embed.add_field(name='<:Poisk:923207017265504316> `Название вашего шарда`',
                    value=f"```\n{shard_id}one\n```")
    embed.add_field(name='<a:dot:923208542410919996> `Пинг в вашем шарде`',
                    value=f'```\n{shard_ping}\n```',
                    inline=True)
    embed.add_field(
        name='<:Glass:923208478208688149> `Кол-во серверов в вашем шарде`',
        value=f'```\n{shard_servers}\n```')
    embed.add_field(
        name='<a:avatar_servers:919973036650803210> `Айди вашего сервера`',
        value=f'```\n{ctx.message.guild.id}\n```')
    embed.add_field(
        name='<:delevop:945131792623624202>Ram',
        value=f'```\n{int(ram)}%\n```')
    embed.add_field(
        name='<:delevop:945131792623624202>Cpu',
        value=f'```\n{int(cpu)}%\n```')
    embed.add_field(
        name='<:windos:945132536596693012>Os',
        value=f'```\n{osps}\n```')
    embed.add_field(
        name='`Запросил:`',
        value=
        f"Ник: `{ctx.author}`\n ID: `{ctx.author.id}`\n Упоминание: {ctx.author.mention}"
    )
    embed.set_footer(text=f"{ctx.author} - Статистика может быть не правдивой!")

    await ctx.send(embed=embed)
    await msg.delete()

def setup(bot):
    bot.add_cog(Ping(bot))


#выдать устное придуперждене
@commands.has_permissions(kick_members=True)
@bot.command()
@commands.guild_only()
async def offw(ctx, *, names, member: nextcord.Member = None):

    if member == None:
        ctx.send("Укажите пользователя!")

    embed = nextcord.Embed(
        title=f"Администратор - {ctx.author} ",
        description=f":hammer: Предупредил - {member.mention} по причине: " +
        names,
        colour=nextcord.Colour.from_rgb(0, 255, 0), timestamp=datetime.datetime.now())
    embed.set_footer(text=f"{ctx.author}", icon_url=f"{ctx.author.avatar_url}")
    await ctx.message.delete()
    await ctx.send(embed=embed)


#команда тест
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def t(ctx):
    emb = nextcord.Embed(title="Це тестова команда нічого не означає!",
                         colour=nextcord.Color.blue(), timestamp=datetime.datetime.now())

    emb.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    emb.set_footer(text="Запитати - {}".format(ctx.author.name),
                   icon_url=ctx.author.avatar)

    await ctx.send(embed=emb)
    await ctx.message.delete()


@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@commands.guild_only()
async def oldhelp(ctx):
    embed = nextcord.Embed(
        title="Версия бота! 2.0.1",
        description="+update\nОбновить базу данных",
    )
    await ctx.send(embed=embed)


#команда кон
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def con(ctx):
    await ctx.reply(embed=nextcord.Embed(
        title="Ссылки на разработчиков",
        description=
        "[:regional_indicator_v: :regional_indicator_k: Вконтакте](https://vk.com/timeigervk) \n[:regional_indicator_y: :regional_indicator_t: YouTube](https://www.youtube.com/channel/UC4R0GWyynsw62CXMxt4zMsQ)"
        +
        "\n[:regional_indicator_g: :regional_indicator_h: GitHub](https://github.com/TimEiger)",
        color=nextcord.Colour.random(), timestamp=datetime.datetime.now()))


#команда dock
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def dock(ctx):
    embed = nextcord.Embed(title="Сервер документации!",
                           description="`Tim™Eiger#8639`",
                           url='https://discord.gg/gJ6m2VZS2C',
                           colour=nextcord.Colour.blue(), timestamp=datetime.datetime.now())
    await ctx.send(embed=embed)
    await ctx.message.delete()



#команда FAQ
@bot.command()
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def faq(ctx):
    embed = nextcord.Embed(
        title="FAQ",
        description=
        ":regional_indicator_h: :regional_indicator_e: :regional_indicator_l: :regional_indicator_l: :regional_indicator_o: ! Я Бот фелтер Мои команды **f+help** \nСвязатся с тех.под **f+con** или напеши <@665271319545511939> ",
        url='https://discord.gg/3SstTNx4RG',
        colour=nextcord.Colour.from_rgb(0, 0, 255), timestamp=datetime.datetime.now())
    await ctx.send(embed=embed)

bot.run(token)
