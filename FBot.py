import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import random


from Dependency import *


client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity=discord.Activity(type= discord.ActivityType.watching, name= 'over the Fens'))
    print("I am ready my g!")
    print("-----------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("`Hello there Fen.`")

AudioPunList = ['Joke1.mp3', 'Joke2.mp3', 'Joke3.mp3', 'Joke4.mp3', 'Joke5.mp3', 'Joke6.mp3', 'Joke7.mp3', 'Joke8.mp3', 'Joke9.mp3', 'Joke10.mp3', 'Joke11.mp3', 'Joke12.mp3', 'Joke13.mp3', 'Joke14.mp3', 'Joke15.mp3', 'Joke16.mp3', 'Joke17.mp3', 'Joke18.mp3', 'Joke19.mp3', 'Joke20.mp3', 'Joke21.mp3', 'Joke22.mp3', 'Joke23.mp3', 'Joke24.mp3', 'Joke25.mp3', 'Joke26.mp3', 'Joke27.mp3', 'Joke28.mp3', 'Joke29.mp3', 'Joke30.mp3', 'Joke31.mp3', 'Joke32.mp3', 'Joke33.mp3', 'Joke34.mp3', 'Joke35.mp3', 'Joke36.mp3', 'Joke37.mp3', 'Joke38.mp3', 'Joke39.mp3', 'Joke40.mp3', 'Joke41.mp3', 'Joke42.mp3', 'Joke43.mp3', 'Joke44.mp3', 'Joke45.mp3']
ranAudioPunList = random.randint(0, (len(AudioPunList)))

punList = ["Are all maths jokes bad? \nNo just sum.",
           "To the guy who invented zero, thanks for nothing.",
           "Can February March? \nNo, but April May.",
           "I don’t trust stairs because they’re always up to something.",
           "I was wondering why the ball was getting bigger. \nThen it hit me.",
           "Never trust an atom, they make up everything!",
           "The guy who invented the door knocker got a no-bell prize.",
           "What do you call an alligator in a vest? \nAn investigator.",
           "Somebody stole all my lamps. \nI couldn’t be more de-lighted!",
           "What did the sushi say to the bee? \nWasabee!",
           "I asked a Frenchman if he played video games. \nHe said Wii.",
           "Why are elevator jokes so classic and good? \nThey work on many levels.",
           "Warning 18+ \n||19||", "Why are plants afraid of maths? \nBecause they don't like square roots.",
           "You know, a good hamburger pun is a rare  medium well done.",
           "A musician was told to tell some people a bunch of jokes. He failed because he didn't get the note.",
           "I got something for you...:microphone2: you mic like this.",
           "Wanna hear a joke about paper? \nNever mind, it's tear-able.",
           "How can you tell if a vampire is sick? \nBy how much he is coffin.",
           "A thief got arrested by policeman Jay. The thief was Jay-led.",
           "A competition limbo dancer walked into a bar ...and was immediately disqualified.",
           "What did one hat say to the other? \nYou wait here. I'll go on a head.",
           "What do frogs drink? \nCroak cra croala.",
           "I wouldn't buy anything with velcro. \nIt's a total rip-off.",
           "How do you make holy water? \nYou boil the hell out of it.",
           "I tried to take a nice picture of a farmers field. \nIt came out grainy though.",
           "I tried to sue an airline for loosing my louggage. \nI lost my case.",
           "How did I escape Iraq? \nI ran.",
           "Cop: Who's car is this, what do you do, where are you going? \nMiner: mine.",
           "How does NASA organise a party? \nThey planet.",
           "I never trust trees on a sunny day \nThey seem kinda shady.",
           "If slow old men use walking sticks what do fast old men use? \nHurry canes.",
           "I ate a clock yesterday and it was very TIME consuming especially when I went back for SECONDS.",
           "What says an Skeleton Before eating? \nBone apetit.",
           "How do you train people to travel in the subway? \nYou just train them.",
           "Some of these puns are so cheesy, I'm glad most of us aren't laughtose intolerant.",
           "The land mine is a ground breaking discovery.",
           "Two men walked into a bar. \nApparently, it hurt.",
           "Oxygen jokes aren't that difficult to make, it's just a lot to take in.",
           "To write with a broken pencil is, \nPointless.",
           "I lost my job at the bank on my very first day. \nA woman asked me to check her balance, so I pushed her over",
           "Last night, I dreamed I was swimming in an ocean of orange soda. But it was just a Fanta sea.",
           "I have a split personality, said Tom, being frank.",
           "I have a few jokes about unemployed people, but none of them work.",
           "What happens when you go to the bathroom in France? \nEuropean.",
           "What do you say too someone whose lost their tuba? \nThat's tubad.",
           "I have a joke on music, but its out of tempo.",
           "My friend got struck by lightning. \nThe news was shocking.",
           "Why can't you hear a pterodactyl go to the bathroom? \nBecause the pee is silent.",
           "Did you hear about a guy whose whole left side was cut off? \nHe's all right now.",
           "If you cant explain me about covid-19 then WHO can.",
           "Only the true king could remove the sword from the stone. \nNo one else could... Because... They didn't have arthurization. \n\n||(King Arthur)||",
           "Did you hear the one about barber simulator? \nThe cutscenes were short.",
           "How do you make one vanish? \nYou add a g and it's gone.",
           "I had some trouble maintaining my lawn. \nMow money mow problems",
           "What does a half minotaur half dinosaur that loves math called? \nDenominator.",
           "Why aren’t koalas real bears? \nThey don’t have the koalafications.",
           "Why did the taxi driver quit his job? \nBecause he can’t stand people talking behind his back.",
           "Why are the doctors so tired? \nToo much patience.",
           "What do you say to a sports car that doesn’t perform well? \nSome kind of Jag-u-ar.",
           "What is the difference between a jeweler and a jailer? \nOne sells watches, the other watches cells.",
           "What kind cheese is not yours? \nNacho Cheese",
           "How do tall people greet each other? \nHigh."
           "I can cut a piece of wood by staring at it. \nIt's true. \nI saw it with my own eyes.",
           "Adding an extra 's' when spelling needles is needless.",
           "Why do terminators who retire kill bugs? \nBecause they are ex terminators.",
           "Why can't you breed an eel with an eagle? \nBecause it's illegal.",
           "If a slice of apple pie costs $2.50 in Jamaica and $3 in the Bahamas, then these are the pie rates of the Carribean.",
           "The world's best tongue twister just got arrested by the police. \nI hear they're gonna give them a really tought sentence.",
           "A guy barged into my office today claiming he can turn people into wind turbines. \nI immediately became a huge fan.",
           "If iron man and the silver surfer teamed up, they would be alloys.",
           "I could tell you a joke about electricity. \nBut the punchline might shock you.",
           "I never understood jokes about planes, they always fly over my head.",
           "Did you hear about the limbless psychopath? \nI wouldn't worry about him, he's (h)armless.",
           "Why should you never trust a math teacher who's holding graph paper? \nThey must be plotting something.",
           "What do you a joke store to get a discount? \nA coupun.",
           "I'll do algebra, calculations, and trigonometry, but making graphs is where I draw the line.",
           "Why was the equal sign so humble? Because she knew she wasn’t greater than or less than anyone else.",
           "Why is the obtuse triangle always so frustrated? Because it is never right.",
           "Dear algebra, \nStop trying to find your X. \nHe's never coming back, don't ask Y. \nIt's not my problem, anyway."
           "Why did the man get a bald cut for his hair? \nHe wanted to make a BALD statement.",
           "How does a computer get drunk? \nThey take screenshots",
           "I asked my friend if he knew any chemistry puns. \nHe said NaH"]

@client.command()
async def pun(ctx):
    randomPunNum = random.randint(0, (len(punList) - 1))
    await ctx.send("`" + punList[randomPunNum] + "`")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        active = True
    else:
        await ctx.send("`You are not in a voice channel!`")

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.command(pass_context = True)
async def play(ctx):
    voice = ctx.guild.voice_client
    ranAudioPunList = random.randint(0, (len(AudioPunList) - 1))
    source = FFmpegPCMAudio("AudioFiles/" + AudioPunList[ranAudioPunList])
    player = voice.play(source)

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("`See you around Fen!`")
    else:
        await ctx.send("`I am no in a voice channel.`")





client.run('OTU1OTMxNDUzMDA5NTY3NzY0.Yjo2ig.ZbNPTEvQzpr2ShYTAbQXKwvapmw')