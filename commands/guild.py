from discord import Guild
from discord.ext.commands import Context, command, guild_only

from config import datetime_format
from embed import generic_embed

data = {
    'name': 'guildinfo',
    'description': 'Shows info for a guild',
    'aliases': ['serverinfo', 'guild', 'server']
}


@guild_only()
@command(**data)
async def guild_info(ctx: Context):
    """
    Shows guild information
    :param ctx: command invocation context
    """
    embed = generic_embed(ctx.bot)

    guild: Guild = ctx.guild

    embed.title = guild.name
    embed.description = guild.description

    embed.set_thumbnail(url=guild.icon_url)

    embed.add_field(name='Server ID', value=f'`{guild.id}`')
    embed.add_field(name='Created at', value=guild.created_at.strftime(datetime_format))
    embed.add_field(name='Members', value=str(len(guild.members)))
    embed.add_field(name='Region', value=str(guild.region).capitalize())
    embed.add_field(name='Owner', value=guild.owner.mention)

    await ctx.send(embed=embed)
