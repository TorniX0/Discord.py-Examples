import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('OK >> BOT IS READY!')
    print(discord.__version__)

@bot.command()
async def dm_me(ctx):
    """This command will DM you."""
    await ctx.author.send("I've just dm'd you!")   # sends a dm
    await ctx.message.delete()   # deletes the sent message by the user

@bot.command(aliases=['permc', 'pc'])   # aliases
@bot.has_permissions(administrator=True)
async def permissions_check(ctx):
    """This command checks if you have Administrator permission in your role/s."""
    await ctx.send('You are allowed to proceed.')

bot.run("token")
