from discord import User
from discord.ext.commands import Context, command

from embed import generic_embed

data = {
    'name': 'avatar',
    'brief': 'Shows a users avatar'
}


@command(**data)
def avatar(ctx: Context, user: User = None):
    user = user or ctx.author

    embed = generic_embed(ctx.bot)

    embed.title = 'Avatar'
    embed.description = f'Avatar for {user}'

    embed.set_image(url=str(user.avatar_url_as(size=2048)))

    await ctx.send(embed=embed)
