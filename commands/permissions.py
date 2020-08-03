from typing import Union

from discord import Member, TextChannel, VoiceChannel, Permissions, Embed
from discord.ext.commands import command, Context, Bot

from embed import generic_embed
from util import bool_to_str

data = {
    'name': 'permissions',
    'brief': 'Shows user guild/channel permissions',
    'aliases': ['perms', 'perm']
}


@command(**data)
async def permissions(ctx: Context, user: Member = None, channel: Union[TextChannel, VoiceChannel] = None):
    """
    Shows user permissions in a guild or channel
    :param ctx: command invocation context
    :param user: the user, will be set to ctx.author if not provided
    :param channel: the channel, will give guild permissions of not provided
    """
    user = user or ctx.author

    if channel:
        perms = user.permissions_in(channel)
        desc = f'Permissions for {user.mention} in {channel.mention}'
    else:
        desc = f'Server permissions for {user.mention}'
        perms = user.guild_permissions

    embed = make_embed(ctx.bot, user, perms, desc)
    await ctx.send(embed=embed)


def make_embed(bot: Bot, user: Member, perms: Permissions, desc: str) -> Embed:
    """
    Sends the embed showing user permissions
    :param bot: the bot itself
    :param user: the user for which the permissions are shown
    :param perms: the permissions
    :param desc: embed description indicating if guild or channel permissions are shown
    :return: the embed displaying user permissions
    """
    embed = generic_embed(bot)

    embed.title = 'Permissions'
    embed.description = desc

    embed.set_thumbnail(url=user.avatar_url)

    for perm_name, perm_val in perms:
        disp_name = perm_name.replace('_', ' ').capitalize()
        embed.add_field(name=disp_name, value=bool_to_str(perm_val))

    return embed
