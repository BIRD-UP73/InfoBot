# File used to add commands to the bot
from discord.ext.commands import Bot

from commands.avatar import avatar
from commands.channel import channel_info
from commands.guild import guild_info
from commands.message import message_info
from commands.permissions import permissions
from commands.role import role_info
from commands.servericon import server_icon
from commands.user import user_info


def setup(bot: Bot):
    bot.add_command(avatar)
    bot.add_command(channel_info)
    bot.add_command(guild_info)
    bot.add_command(message_info)
    bot.add_command(permissions)
    bot.add_command(role_info)
    bot.add_command(server_icon)
    bot.add_command(user_info)
