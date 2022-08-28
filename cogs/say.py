from discord.ext import commands
from discord_slash import SlashContext, cog_ext
# The below will `import discord` and override some of its stuff
from discord_slash.dpy_overrides import *
from discord_slash.model import SlashCommandOptionType
import logging

class say(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name='say',
                       description='The bot will repeat after you...',
                       options=[{'name':'message',
                                 'description': 'Hello World!',
                                 'type': SlashCommandOptionType.STRING,
                                 'required': True}])        
    @commands.command()
    async def say(self, ctx: SlashContext, message: str):
        """Says hello"""
        await ctx.send(message)
        logging.info(str(ctx.author.name)+"("+(ctx.author.id)+") used say: "+message)

        
def setup(bot):
    bot.add_cog(say(bot))
