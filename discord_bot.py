import discord
import os
import numpy as np
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

@bot.command()
async def lineal(ctx, equation):
    members = equation.split("=")
    message = ""
    if len(members) == 2 and members[1].isnumeric():
        terms = []
        buffer = ""
        for i in range(len(members[0])):
            if i == 0 and members[0][i] == '-':
                buffer += members[0][i]
                continue
            if i != 0 and members[0][i] == '+':
                terms.append(int(buffer))
                buffer = ""
                continue
            if i != 0 and members[0][i] == '-':
                terms.append(int(buffer))
                buffer = "-"
                continue
            if members[0][i].isnumeric() and i < len(members[0]) - 1:
                buffer += members[0][i]
                continue
            if i == len(members[0]) - 1:
                if members[0][i].isnumeric():
                    buffer += members[0][i]
                terms.append(int(buffer))
                break

        A = np.array(terms)
        B = np.array([int(members[1])])
        x = ((A[1] * -1) + B[0]) / A[0]
        message = "El valor de x es: " + str(x)
    else:
        message = "Arregla tu ecuación {} prro".format(equation)
    await bot.get_channel(channel).send(message)


@bot.command()
async def sistemal(ctx, *args):
    equations = []
    for n in args:
        equations.append(n)
    message = ""
    term_list = []
    member = []
    member_list = []
    for j in range(len(equations)):
        terms = []
        buffer = ""
        members = equations[j].split("=")
        if len(members) == 2 and members[1].isnumeric():
            member = int(members[1])
            member_list.append(member)
            for i in range(len(members[0])):
                if i == 0 and members[0][i] == '-':
                    buffer += members[0][i]
                    continue
                if i != 0 and members[0][i] == '+':
                    terms.append(int(buffer))
                    buffer = ""
                    continue
                if i != 0 and members[0][i] == '-':
                    terms.append(int(buffer))
                    buffer = "-"
                    continue
                if members[0][i].isnumeric() and i < len(members[0]) - 1:
                    buffer += members[0][i]
                    continue
                if i == len(members[0]) - 1:
                    if members[0][i].isnumeric():
                        buffer += members[0][i]
                    terms.append(int(buffer))
                    break
        else:
            message = "Arregla tu ecuación {} prro".format(j+1)
            return message

        term_list.append(terms)

    A = np.array(term_list)
    B = np.array(member_list)
    X = np.linalg.inv(A).dot(B)
    message = "Los valores de las incógnitas son: {}".format(X)
    await bot.get_channel(channel).send(message)

        # Variable de entorno para el token del bot
bot.run(os.environ['TDBTOKEN'])
