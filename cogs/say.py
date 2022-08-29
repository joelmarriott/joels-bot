import discord
import logging

class Say(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def say(self, ctx, message: discord.Option(str)):
        """Says hello"""
        await ctx.respond(message)
        logging.info(str(ctx.author.name)+"("+str(ctx.author.id)+") used say: "+message)

        
def setup(bot):
    bot.add_cog(Say(bot))
