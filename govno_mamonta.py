active = False
import time
import random
import discord
import requests
import os
import requests
from discord.ext import commands
client = commands.Bot(command_prefix = ".", self_bot = True)
client.remove_command("help")


osk = ["пытками sаsеш мне", "закадрил тя хуjем ", "на доsуге епу тя ", "хуjем тя абделал", "ТЫ ПОНИМАЕШЬ ЧТО Я ПИЗДАК ВТЕОЙ МАТРЕИ НА СВОЙ УЙ КАК МАКАРОНИНУ НАМОТАЛ БЛЯДЬ И НАЧАЛ РАСКРУЧИВАТЬ ЕЁ ПОСЛЕ ЧЕГО ВЫКИНУЛ В КОСМОС ЧТОБ ЕЁ ТАМ ИНОПЛАНЕТЯНЫ ХУЯМИ РВАЛИ?)", "Говноед Насаси Уже МОй Хуй ", "Нашёл Твою Мать На Берегу Озере Она Пасасала Чет", "Ты Зачастую На Мой Хуй Садилса Чоли?", "Ποεβαλ Τια ΛαΨκα", "НаигралсЯ С Моим Хуем?", "После Того Как Я Вкрутил Все Саморезы Тебе В Башку Я Вкрутил Свой Хуй Твоей Матери В Горло", "Паебал Тя В Попачку", "ТЫ ПОНИМАЕШЬЧ ТО МОЙ ХУЙ В ПИЗДАКЕ ТВОЕЙ МТАЕРИ НЛО, И ВСЕ БЛОХИ КОТОРЫЕ ТАМ ЖИВУТ БЛЯДЬ, ПЫТАЮТСЯ ВЗЯТЬ ЕГО В ПЛЕННИКИ И ИЗУЧИТЬ, НО МОЯ ЗАЛУПА ИХ ВСЕХ ТРАВИТ))", "СЛЫШЬ, ИДИ ОТДАЙ МОЙ ХУЙ В АРЕНДУ СВОЕЙ МАМАШИ, ЧТОБ ОНА ЕГО СПОКОЙНО ПОЛИЗАЛА))", "Мне кристально похуй на твое мнение)))", "Сын бляди я твою маму на цепь ставил и кормил вас Ты мне должен пятки целовать чучело", "все вместе е6али твою мать ты чё наhуй написал сынуля шлюхи", "ору cbIHok wлюхи че пастb разинул? ща )(уй туда положу будеш отрабатывать waBka cJluтая", "ору cbIHok wлюхи ebaJL TBoi-0 MepTByi-0 Matb))", "твой папашка аутист что кончил в твою мамашу и родился такой еблан как ты", "Я опозорил твой род алкаша папашки который сосет за бутылку коньяка", "слышь ты араб арабсыкие истории потом расказывай", "да уж твоя матушка солнца боится потому что она думает это мои яйца", "нахуй ты высер ебаный моим хуем прикрываешься когда мусора тебя начинают трахать в жопу", "axaxaxa opy 4e pactb OTkPiL wa XuY tuda PoloJy otrobativatb Bydew", "все вместе е6али твою мать ты чё наhуй написал сынуля шлюхи", "бамбиш клаsна шолаvа", "ез ез sоsеш как архитектурныj", "хехе sаsала ты мне как многоsтупенчатыj", "ты понимаешь, что клитор твоей матери эта зона чрезвычайно опасная ??", "слышь, что может служить защитой от воздействия проникающей радиации в пизду твоей матери ? ??", "ебу тя ару нахуй", "на счет три ты будешь сосать ок?если согласен то напиши что то", "помнишь как ты пытался соси как твоя мамка?))))00 мне понравилось", "курю сигарету )а те дал хуй курить мой )", "стати, ты зря так стараешься, ведь ещё в Библии указано, что кусок говна не имеет право на личное мнение.", "Это тебе мать перед смертью шепнула", "И вновь прозвучал слив", "Ну, что, дружок, проебал вспышку?", "Я из пробирки, меня воспитывали боги, я с олимпа, ты с канавы!", "Для тебя слово (что), как собаке команда фас, только та бежит за жертвой, а ты повторяешь фразу!", "Ты своим мозгом можешь осознать, что апостериория это знания полученные опытным путем, а априории наоборот"]
@client.event
async def on_ready():
    print("Loading...")
    os.system("cls && color c")
    os.system("color c")
    print("""
                              
                                Developed by GovnoTrep
                                created with 5 steallers (cutted by javivi) <3
▒█░▄▀ ▒█▀▀█ ▒█▀▀▀ ▒█▀▀▀█ ▒█▀▀█ ░█▀▀█ 　 ▒█▀▀█ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ░█▀▀█ ▒█▀▀▀█ ▒█▀▀▀ 　 ▄█░ ░ █▀▀█ 
▒█▀▄░ ▒█▄▄▀ ▒█▀▀▀ ▒█░░▒█ ▒█▄▄▀ ▒█▄▄█ 　 ▒█▄▄▀ ▒█▀▀▀ ▒█░░░ ▒█▀▀▀ ▒█▄▄█ ░▀▀▀▄▄ ▒█▀▀▀ 　 ░█░ ▄ █▄▀█ 
▒█░▒█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄▄█ ▒█░▒█ ▒█░▒█ 　 ▒█░▒█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄▄ ▒█░▒█ ▒█▄▄▄█ ▒█▄▄▄ 　 ▄█▄ █ █▄▄█
                               **  Version : 1.0  **
                                        """)

@client.command()
async def bullon(ctx):
    global stop_spam_flag
    stop_spam_flag = False
    active = True
    await ctx.message.delete()
    while active:
      if stop_spam_flag:
          break
      await ctx.send(random.choice(osk))
      time.sleep(1)

@client.command(name="stopbull")
async def stopbull(ctx):
    await ctx.message.delete()
    global stop_spam_flag
    stop_spam_flag = True
    await ctx.send("лол")


@client.command()
async def help(ctx):
    await ctx.message.delete()
    await ctx.send("**Kreora RELEASE **\n`.say(текст) - отправляет сообщение`\n`.spam(количество)(текст) - спамит сообщением`\n`.bullon - буллит человека ` \n`.popit отправляет попыт`\n`.invspam(количество) - спам невидимыми сообщениями`\n`.ben(вопрос) - спрашивает бена`\n`.lagspam(количество) - заставляет лагать дискорд`\n`.anime(Вид) - Генерирует аниме картинку`\n`.anekdot - расказывает анекдот `\n`.zalgospam(количество) - спамит зальго (на телефоне лаги)`\n`.stopbull - останавливает буллинг`")

@client.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)

@client.command()
async def spam(ctx, kv, *, text):
    await ctx.message.delete()
    print("спамер активирован...")
    while int(kv) !=0:
        await ctx.send(text)
        kv = int(kv)-1

@client.command()
async def popit(ctx):
   await ctx.message.delete()
   await ctx.send("||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||\n||:white_large_square:||||:black_large_square:|||| :white_large_square: ||||:black_large_square:|| ||:white_large_square:|| ||:black_large_square: ||||:white_large_square: ||\n||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||\n||:white_large_square:||||:black_large_square:|||| :white_large_square: ||||:black_large_square:|| ||:white_large_square:|| ||:black_large_square: ||||:white_large_square: ||\n||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||\n||:white_large_square:||||:black_large_square:|||| :white_large_square: ||||:black_large_square:|| ||:white_large_square:|| ||:black_large_square: ||||:white_large_square: ||\n||:black_large_square:||||:white_large_square:|||| :black_large_square: ||||:white_large_square:|| ||:black_large_square:|| ||:white_large_square: ||||:black_large_square: ||")

@client.command()
async def invspam(ctx, number):
    await ctx.message.delete()
    print("невидимый спам включен...")
    for i in range(int(number)):
        await ctx.send("||\n||")
        time.sleep(0.10)

@client.command()
async def ball(ctx, *, text):
    ballik = random.randint(1, 5)
    if ballik == 1:
        await ctx.send("Возможно")
    if ballik == 2:
        await ctx.send("вот тибе 🦣")
    if ballik == 3:
        await ctx.send("Да")
    if ballik == 4:
        await ctx.send("Нет")
    if ballik == 5:
        await ctx.send("хз")

@client.command()
async def ben(ctx, *, text):
    ballik = random.randint(1, 4)
    if ballik == 1:
        await ctx.send("Да")
    if ballik == 2:
        await ctx.send("Угрх..")
    if ballik == 3:
        await ctx.send("Нет")
    if ballik == 4:
        await ctx.send("Хо-хо-хо")

@client.command()
async def lagspam(ctx, number):
    for i in range(int(number)):
        await ctx.send(":chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: :chains: ")
        time.sleep(0.10)

@client.command()
async def anime(ctx):
    await ctx.message.delete()
    await ctx.send("```\nsfw [категория]\nвот все категории\n" + """
waifu, neko ,shinobu
megumin, bully, cuddle
cry, hug, awoo
kiss, lick, pat
smug, bonk, yeet
blush, smile, wave
highfive, handhold, nom
bite, glomp, slap
kill, kick, happy
wink, poke, dance
cringe
```""")
    await ctx.send("```\nnsfw [категория]\nвот все категории\n" + """
neko, trap, blowjob
```""")
    

@client.command()
async def sfw(ctx, category):
    picture = requests.get("https://api.waifu.pics/sfw/" + category)
    url = picture.json()["url"]
    await ctx.send(url)


@client.command()
async def nsfw(ctx, category):
    picture = requests.get("https://api.waifu.pics/nsfw/" + category)
    url = picture.json()["url"]
    await ctx.send(url)

@client.command()
async def bеn(ctx, *, text):
    ballik = random.randint(1, 3)
    if ballik == 1:
        await ctx.send("Нет")
    if ballik == 2:
        await ctx.send("Угрх..")
    if ballik == 3:
        await ctx.send("Хо-хо-хо")

@client.command()
async def anekdot(ctx):
    ballik = ["А вы замечали, что когда к вам обращаются с фразой (Нам надо поговорить), вам-то это как раз совершенно не надо?", "Считать, что современные люди заложники своих гаджетов это большое преувеличение.Они заложники аккумуляторов своих гаджетов.", "Доктор, полгода назад я развелся с женой. Прибавил в весе 30 кило. — Это же элементарно лечится! Просто перестаньте уже праздновать.", "Покурил сигареты Президент, но президентом не стал. Выпил водку Парламент, но в парламенте не заседаю. И только когда пью пиво Козел, чувствую — действует…", "Дед, а у вас тут куда вечером сходить-то можно? — В ведро.", "— Какая у больного температура? — Нормальная, комнатная, +18 градусов...", "— А существуют таблетки от голода? — Да, котлеты называются! ", "Хочу себе свой портрет Дориана Грея, только чтобы он тупил вместо меня.", "Все мы когда-то были друг другу чужими, а потом нет, а потом снова да."]
    await ctx.send(random.choice(ballik))

@client.command()
async def zalgospam(ctx, number): 
    for i in range(int(number)):
        await ctx.send("⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟]꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟꙰⃟꙰⃟꙰꙰⃟")
        time.sleep(0.10)

client.run("UR DISCORD TOKEN", bot = False)
