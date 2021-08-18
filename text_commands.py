import import_list

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
