import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix="f+")

@bot.command()
async def test(ctx):
  ctxx = ctx.author.id
  return