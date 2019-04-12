import discord, asyncio #you could always use from asyncio import sleep :)

from discord.ext import commands

class example_cog2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=['cd', 'ctd'])
    async def countdown(self, ctx):
        await ctx.send("5")
        await asyncio.sleep(1) #seconds, and you can always use asyncio import sleep as specified above, but you'll have to use
        #await sleep().
        await ctx.send("4..")
        await asyncio.sleep(1)
        await ctx.send("3...")
        await asyncio.sleep(1)
        await ctx.send("2....")
        await asyncio.sleep(1)
        await ctx.send("1.....")
        await asyncio.sleep(1)
        await ctx.send("**GO!**")

def setup(bot):
    bot.add_cog(example_cog2(bot))
