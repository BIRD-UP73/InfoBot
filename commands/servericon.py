from discord import Guild
from discord.ext.commands import Context, guild_only, command

from embed import generic_embed

data = {
    'name': 'servericon',
    'brief': 'Shows server icon'
}


@guild_only()
@command(**data)
async def server_icon(ctx: Context):
    """
    Shows the server icon
    :param ctx: command invocation context
    """
    guild: Guild = ctx.guild

    embed = generic_embed(ctx.bot)

    embed.title = 'Icon'
    embed.description = f'Sever icon for {guild.name}'

    embed.set_image(url=str(guild.icon_url_as(size=2048)))

    await ctx.send(embed=embed)
