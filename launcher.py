from discord.ext import commands
from config import prefix, token

bot = commands.Bot(command_prefix=prefix)

bot.load_extension('commands._setup')


@bot.listen()
async def on_ready():
    print(f'Logged in as {bot.user}')


bot.run(token)
