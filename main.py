import import_list

              # Variable de entorno para el id del canal/canales
channel = int(os.environ['DISCORDCHANNELS'])

bot = commands.Bot(command_prefix='!')

        # Variable de entorno para el token del bot
bot.run(os.environ['TDBTOKEN'])