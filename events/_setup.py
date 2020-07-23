from discord.ext.commands import Bot

from events.on_ready import on_ready


def setup(bot: Bot):
    bot.add_listener(on_ready)
