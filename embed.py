from datetime import datetime

from discord import Embed, Color
from discord.ext.commands import Bot


def error_embed(bot: Bot, error_msg: str):
    """
    Creates an embed displaying an error message

    :param bot: the bot
    :param error_msg: the error message
    """
    embed = generic_embed(bot)

    embed.title = 'Error'
    embed.description = error_msg
    embed.colour = Color.red()

    return embed


def generic_embed(bot: Bot) -> Embed:
    """
    Creates a generic embed, which includes
    - Bot name in the footer
    - Bot avatar in the footer
    - Timestamp

    :param bot: the bot
    :return: the embed
    """
    embed = Embed()

    embed.timestamp = datetime.now()
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)

    return embed
