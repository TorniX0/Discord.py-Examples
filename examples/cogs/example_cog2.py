import discord
import asyncio   # you could always use from asyncio import sleep :)

from discord.ext import commands

class example_cog2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['cd', 'ctd'])
    async def countdown(self, ctx):
        for a in range(-5, 0):
            await ctx.send(f"{abs(a)}...")
            await asyncio.sleep(1)
        await ctx.send("**GO!**")

def setup(bot):
    bot.add_cog(example_cog2(bot))
