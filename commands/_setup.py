# File used to add commands to the bot
from discord.ext.commands import Bot

from commands.guild import guild_info
from commands.message import message_info
from commands.role import role_info
from commands.user import user_info


def setup(bot: Bot):
    bot.add_command(guild_info)
    bot.add_command(message_info)
    bot.add_command(role_info)
    bot.add_command(user_info)
