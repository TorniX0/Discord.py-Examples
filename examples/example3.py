import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('OK >> BOT IS READY!')
    print(discord.__version__)

@bot.command()
async def dm_me(ctx):
    await ctx.author.send("I've just dm'd you!")   # sends a dm
    await ctx.message.delete()   # deletes the sent message by the user

@bot.command(aliases=['permc', 'pc'])   # aliases
async def permissions_check(ctx):
    if ctx.author.guild_permissions.administrator:   # check if user has administrator
        await ctx.send('You are allowed to proceed.')
    else:
        await ctx.send('You are denied to proceed.')

bot.run("token")
