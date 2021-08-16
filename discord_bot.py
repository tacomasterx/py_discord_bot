import discord
import os
              # Variable de entorno para el id del canal/canales
channel = int(os.environ['DISCORDCHANNELS'])

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def hello(ctx):
    await bot.get_channel(channel).send("Mensaje de prueba :3")

@bot.command()
async def algo(ctx):
    await bot.get_channel(channel).send("Otra cosa")

@bot.command()
async def insulto(ctx):
    await bot.get_channel(channel).send("Gorzed es puto!")

@bot.command()
async def texto(ctx, string):
    await bot.get_channel(channel).send("No se que signifique \"" + string + "\"")

@bot.command()
async def potencia(ctx, base, exponente):
    total = 1
    base = int(base)
    exponente = int(exponente)
    for i in range(exponente):
        total = total * base
    #string = "La {}a potencia de {} es {}.".format(exponente,base,total)
    await bot.get_channel(channel).send("La {}a potencia de {} es {}.".format(exponente,base,total))

@bot.command()
async def factorial(ctx, base):
    base = int(base)
    total = base
    for i in range(1,base):
        total = total * (base - i)
    #string = "La {}a potencia de {} es {}.".format(exponente,base,total)
    await bot.get_channel(channel).send("El factorial de {} es {}.".format(base,total))

        # Variable de entorno para el token del bot
bot.run(os.environ['TDBTOKEN'])