from typing import Union

from discord import TextChannel, VoiceChannel, DMChannel
from discord.ext.commands import Context, command

from config import datetime_format
from embed import generic_embed

data = {
    'name': 'channelinfo',
    'brief': 'Displays channel information'
}


@command(**data)
async def channel_info(ctx: Context, channel: Union[TextChannel, VoiceChannel, DMChannel] = None):
    channel = channel or ctx.channel

    embed = generic_embed(ctx.bot)

    embed.title = 'Channel info'
    embed.description = f'Channel info for {channel.mention}'

    embed.add_field(name='Channel ID', value=f'`{channel.id}`')
    embed.add_field(name='Members', value=str(len(channel.members)))
    embed.add_field(name='Created at', value=channel.created_at.strftime(datetime_format))

    if isinstance(channel, VoiceChannel):
        roles_txt = ', '.join([role for role in channel.changed_roles])
        embed.add_field(name='Overriden roles', value=roles_txt)

    await ctx.send(embed=embed)
