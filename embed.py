from datetime import datetime

from discord import Embed
from discord.ext.commands import Bot


def generic_embed(bot: Bot) -> Embed:
    embed = Embed()

    embed.timestamp = datetime.now()
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)

    return embed
