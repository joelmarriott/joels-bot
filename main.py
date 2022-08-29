#!/usr/bin/python3
from datetime import date
import discord
import logging
import os
import sys


bot = discord.Bot()
@bot.event
async def on_ready(): 
    logging.info("We have logged in as {self.user}!")

@bot.slash_command(
    name="hello",
    description="Say hello to the bot",
    guild_ids=[232293743112355851]
)
async def hello(ctx):
    await ctx.respond("Hello!")

        
def main():
    """
    Run the bot
    """
    start = sys.path[0]
    os.chdir(start)

    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists("logs"):
        os.makedirs("logs")
        
    today = date.today().strftime("%Y-%m-%d")
    logging.basicConfig(filename=os.path.join(sys.path[0],
                                          "logs",
                                          today+".log"),
                        level=logging.INFO)

    cogs_list = [
        "help",
        "say",
    ]

    for cog in cogs_list:
        bot.load_extension(f'cogs.{cog}')
    
    bot.run(os.environ["JOELTOK"])

               
if __name__ == "__main__":
    main()
