import discord
import os
import random

client = discord.Client()

definiciones = []
diccionario = {}
mensaje = ""

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if ( message.content.startswith('cual') or message.content.startswith('Cual') or message.content.startswith('Cuál') or message.content.startswith('cuál') ) and ( message.content.endswith('recibo') or message.content.endswith('recibo?') or message.content.endswith('monto?') or message.content.endswith('monto') or message.content.endswith('beso?')  or message.content.endswith('beso') or message.content.endswith('experimento') or message.content.endswith('experimento?') ):
        await message.channel.send('¡Esta!')

    if message.content.endswith('nalgas'):
        lista_albures = ['a travieso que eres']
        await message.channel.send(lista_albures[0])

    if message.content.endswith('cola'):
        lista_albures = ['chingo y hago bola']
        await message.channel.send(lista_albures[0])

    if message.content.endswith('chile') or message.content.endswith('chile?') or message.content.endswith('chile!') or message.content.endswith('chile.') :
        lista_albures = ['comes', 'chupas', 'te sientas', 'me agarras', 'cómo dijiste... auch, autogol', 'más callado']
        random.shuffle(lista_albures)
        await message.channel.send(lista_albures[0])

    if message.content.endswith('culo') or message.content.endswith('culo?') or message.content.endswith('culo!') or message.content.endswith('culo.') :
        lista_albures = ['prestas', 'me das']
        random.shuffle(lista_albures)
        await message.channel.send(lista_albures[0]) 

    if message.content.endswith('verga de mono') :
        lista_albures = ['te lo volteo y dejo como cono']
        #random.shuffle(lista_albures)
        await message.channel.send(lista_albures[0]) 

    if message.content.endswith('bai') or message.content.endswith('Bai') :
        lista_albures = ['me dijeron del beso', 'si te entregaron el recibo?', 'ya pagaste el monto?', 'hiciste el experimento?']
        random.shuffle(lista_albures)
        await message.channel.send("Oye {}  {}".format( message.author.mention, lista_albures[0])) 

    if message.content.endswith('pito') or message.content.endswith('chorizo') :
        lista_albures = ['sumo cuidado']
        await message.channel.send(lista_albures[0])

    if message.content.endswith('def') :
        await message.channel.send(definiciones)

    if message.content.endswith('dic') :
        await message.channel.send(diccionario)

    if str(message.content) in definiciones:
        await message.channel.send(diccionario[str(message.content)])

    if message.content.startswith('def$') :
        definicion =  str(message.content).split("$")
        if definicion[1].strip() in definiciones:
            mensaje = "Esa frese ya existe en el sistema"
        else:
            definiciones.append(definicion[1].strip())
            diccionario[definicion[1].strip()] = definicion[2].strip()
            mensaje = "Añadido {}, respuesta: {} ?".format(definicion[1].strip(), definicion[2].strip() )
        await message.channel.send(mensaje)

client.run(os.environ['TDBTOKEN'])
