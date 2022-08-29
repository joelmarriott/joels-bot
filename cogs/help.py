from discord.ext.pages import Paginator, Page
from discord import Colour
import discord
import logging


class Help(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    async def help(self, ctx):
        """Help"""
        my_pages = [
            Page(
                embeds=[
                    discord.Embed(
                        colour=Colour.green(),
                        title="Help",
                        description="**Fun**\n"+\
                        "`/say` will repeat any message you send\n"
                    )
                ]
            ),
            Page(
                embeds=[
                    discord.Embed(
                        colour=Colour.green(),
                        title="Help",
                        description="**Oops**\n"+\
                        "Nothing here, but isn't this cool?"
                    )
                ]
            )
        ]
        paginator = Paginator(
            pages=my_pages,
            show_indicator=True
        )
        await paginator.respond(ctx.interaction)
        logging.info(str(ctx.author.name)+"("+str(ctx.author.id)+") used help")

        
def setup(bot):
    bot.add_cog(Help(bot))
