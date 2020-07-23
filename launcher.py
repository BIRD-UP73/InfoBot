from discord.ext import commands
from config import prefix, token

bot = commands.Bot(command_prefix=prefix)

bot.load_extension('commands._setup')
bot.load_extension('events._setup')

bot.run(token)
