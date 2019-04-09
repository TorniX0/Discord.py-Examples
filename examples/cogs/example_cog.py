import discord

from discord.ext import commands

class example_cog(commands.Cog): #it must inherit from commands.Cog
    def __init__(self, bot):
        self.bot = bot #so you're gonna use self.bot in cogs if you have it like this.

    #listeners now must have a decorator
    @commands.Cog.listener()
    async def on_message(self, message):
        if "cookie" in message.content.lower():
            await message.channel.send('But I want to keep them :(.. :cookie: :cookie: :cookie: :cookie: :cookie:')
        await self.bot.process_commands(message)
        
    @commands.command(aliases=['dtcw'])
    async def does_the_cog_work(self, ctx): #first 2 arguments must be self and ctx
        await ctx.send('The cog works! Everything works correctly and fine.')

def setup(bot):
    bot.add_cog(example_cog(bot))