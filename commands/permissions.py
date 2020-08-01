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
    user = user or ctx.author

    if channel:
        perms = user.permissions_in(channel)
        desc = f'Permissions for {user.mention} in {channel.mention}'
    else:
        desc = f'Server permissions for {user.mention}'
        perms = user.guild_permissions

    embed = send_embed(ctx.bot, user, perms, desc)
    await ctx.send(embed=embed)


def send_embed(bot: Bot, user: Member, perms: Permissions, desc: str) -> Embed:
    embed = generic_embed(bot)

    embed.title = 'Permissions'
    embed.description = desc

    embed.set_thumbnail(url=user.avatar_url)

    for perm_name, perm_val in perms:
        disp_name = perm_name.replace('_', ' ').capitalize()
        embed.add_field(name=disp_name, value=bool_to_str(perm_val))

    return embed
