from discord import Message
from discord.ext.commands import Context, command

from config import datetime_format
from embed import generic_embed

data = {
    'name': 'messageinfo',
    'description': 'Shows info for a message',
    'aliases': ['message', 'msg', 'msginfo']
}


@command(**data)
async def message_info(ctx: Context, message: Message):
    embed = generic_embed(ctx.bot)

    embed.title = 'Message'
    embed.description = message.content

    embed.set_thumbnail(url=message.author.avatar_url)

    embed.add_field(name='Sent by', value=message.author.mention)
    embed.add_field(name='Created at', value=message.created_at.strftime(datetime_format))
    embed.add_field(name='Message ID', value=f'`{message.id}`')
    embed.add_field(name='URL', value=message.jump_url)

    if message.edited_at:
        embed.add_field(name='Edited at', value=message.edited_at.strftime(datetime_format))

    await ctx.send(embed=embed)
