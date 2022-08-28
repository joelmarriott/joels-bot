#!/usr/bin/python3
from datetime import date
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
# The below will `import discord` and override some of it's stuff
from discord_slash.dpy_overrides import *
from discord_slash.model import SlashCommandOptionType
import discord
import logging
import os
import sys


client = commands.Bot(command_prefix='/')
slash = SlashCommand(client, sync_commands=True)
token = os.environ["JOELTOK"]


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

    # Load the Cogs
    cogs = [
        'say',
    ]
    for cog in cogs:
        try:
        client.load_extension(f'cogs.{cog}')
        logging.info(f" Cog loaded: {cog}\n")
        sys.stdout.flush()
        except Exception as ex:
            logging.error(f" Command load failed: {command}\n")
            sys.stderr.flush()       
    client.run(token)

    

if __name__ == "__main__":
    main()
