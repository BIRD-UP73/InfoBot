from discord.ext.commands import Cog, Bot, Context, CommandError

from embed import error_embed


class EventHandler(Cog):
    """
    Cog used to handle server events
    """

    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        """
        Called when the client is done preparing the data received from Discord. Usually after login is successful
        and the Client.guilds and co. are filled up.
        """
        print(f'Logged in as {self.bot.user}')

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError):
        """
        An error handler that is called when an error is raised inside a command either through user input error,
        check failure, or an error in your own code.

        :param ctx: command invocation context
        :param error: the error that was raised
        """
        embed = error_embed(ctx.bot, str(error))
        await ctx.send(embed=embed)
