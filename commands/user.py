from discord import User, Embed, Member
from discord.ext.commands import Context, command, Bot

from config import datetime_format

data = {
    'name': 'userinfo',
    'description': 'Shows info for a user',
    'aliases': ['user']
}


@command(name='userinfo', aliases=['user'])
async def user_info(ctx: Context, user: User = None):
    """
    Displays user information
    :param ctx: command invocation context
    :param user:
    """
    user = user or ctx.author

    embed = Embed()

    embed.title = 'User info'
    embed.description = f'User info for {user.mention}'

    embed.colour = user.colour
    embed.set_thumbnail(url=str(user.avatar_url_as(size=2048)))

    embed.add_field(name='User ID', value=user.id, inline=False)

    created_at = user.created_at.strftime(datetime_format)
    embed.add_field(name='Created at', value=created_at, inline=False)

    if isinstance(user, Member):
        joined_at = user.joined_at.strftime(datetime_format)
        embed.add_field(name='Joined at', value=joined_at)

    await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_command(user_info)
