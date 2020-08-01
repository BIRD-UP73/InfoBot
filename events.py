from discord.ext.commands import Cog, Bot, Context, CommandError

from embed import error_embed


class EventHandler(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError):
        embed = error_embed(ctx.bot, str(error))
        await ctx.send(embed=embed)
