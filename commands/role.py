from discord import Role
from discord.ext.commands import Context, command, guild_only

from config import datetime_format
from embed import generic_embed
from util import bool_to_str

data = {
    'name': 'roleinfo',
    'description': 'Display info of a role',
    'aliases': ['role']
}


@guild_only()
@command(**data)
async def role_info(ctx: Context, role: Role):
    """
    Shows information about a role
    :param ctx: command invocation context
    :param role: the role
    """
    embed = generic_embed(ctx.bot)

    embed.title = role.name
    embed.colour = role.colour

    embed.add_field(name='Created at', value=role.created_at.strftime(datetime_format))
    embed.add_field(name='Member amount', value=str(len(role.members)), inline=False)

    embed.add_field(name='Hoisted', value=bool_to_str(role.hoist), inline=True)
    embed.add_field(name='Mentionable', value=bool_to_str(role.mentionable), inline=True)

    if role.mentionable:
        embed.add_field(name='Mention', value=role.mention)

    embed.add_field(name='Position', value=role.position)

    await ctx.send(embed=embed)
