from datetime import datetime

from discord import Embed, Color
from discord.ext.commands import Bot


def error_embed(bot: Bot, error_msg: str):
    embed = generic_embed(bot)

    embed.title = 'Error'
    embed.description = error_msg
    embed.colour = Color.red()

    return embed


def generic_embed(bot: Bot) -> Embed:
    embed = Embed()

    embed.timestamp = datetime.now()
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)

    return embed
