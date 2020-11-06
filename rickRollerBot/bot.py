import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='-rr ')
@bot.event
async def on_ready():
    print(bot.user.name)
@bot.command(name='spoiler')
async def spoiler_rr(ctx):
    response = "https://cdn.discordapp.com/attachments/763436050118606849/771357435826798632/image0.png"
    await ctx.send(response)

bot.run(TOKEN)