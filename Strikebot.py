#Dicord Strikebot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("laeuft\n")

@bot.command(pass_context=True)
async def strike(ctx, ctxuser):
    admins = []
    #Admins die online sind zaehlen
    #Abstimmung starten (jeder hat nur eine Stimme)
    await ctx.send(ctxuser + " striken?")


#Muell
###############################
#Sieg Heil
@bot.command(pass_context=True)
async def sieg(ctx):
    await ctx.send("Heil!")

#Apache der Gangster
@bot.command(pass_context=True)
async def apache(ctx):
    await ctx.send("der Gangster")

#Julian der Spast
@bot.command(pass_context=True)
async def spast(ctx):
    await ctx.send("<:spast:662428397703790612>")

@bot.command(pass_context=True)
async def hodensack(ctx):
    await ctx.send("HodiModi")
###############################

print ("bot wird gestartet\n")

bot.run("NjYzNTE4OTQ1MjAyMTQzMjMz.XhOW1Q.tq8_ZwYJc8NebpjYMHY9u2e-RI8")





#################################
#import os

#import discord
#from dotenv import load_dotenv

#load_dotenv()
#token = os.getenv('NjYzNTE4OTQ1MjAyMTQzMjMz.XhJvaA.IYhO6i-8yVb3FspTa8HsaOHiYL4')

#client = discord.Client()

#@client.event
#async def on_ready():
#    print(f'{client.user} has connected to Discord!')

#client.run(token)
