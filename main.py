#!/usr/bin/python3
from discord_slash import SlashCommand, SlashContext
import discord
import logging
import os
import sys


client = discord.Client()
slash = SlashCommand(client, sync_commands=True)
token = os.environ["JOELTOK"]
client.run(token)


def main():
    """
    Run the bot
    """
    start = sys.path[0]
    os.chdir(start)

    if not os.path.exists("data"):
        os.makedirs("data")

    today = date.today().strftime("%Y-%m-%d")
    logging.basicConfig(filename=os.path.join(sys.path[0],
                                          "logs",
                                          today+".log"),
                        level=logging.INFO)

    

if __name__ == "__main__":
    main()
