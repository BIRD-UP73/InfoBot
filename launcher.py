from discord.ext import commands
from config import prefix, token
from events import EventHandler

bot = commands.Bot(command_prefix=prefix)

bot.load_extension('commands._setup')

bot.add_cog(EventHandler(bot))

bot.run(token)
