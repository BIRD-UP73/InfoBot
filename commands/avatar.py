from discord import User
from discord.ext.commands import Context, command

from embed import generic_embed

data = {
    'name': 'avatar',
    'brief': 'Shows a users avatar'
}


@command(**data)
async def avatar(ctx: Context, user: User = None):
    """
    Shows a users avatar
    :param ctx: command invocation context
    :param user: the user, set to ctx.author if no user is given
    """
    user = user or ctx.author

    embed = generic_embed(ctx.bot)

    embed.title = 'Avatar'
    embed.description = f'Avatar for {user.mention}'

    embed.set_image(url=str(user.avatar_url_as(size=4096)))

    await ctx.send(embed=embed)
