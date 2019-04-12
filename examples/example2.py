import discord

from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('OK >> BOT IS READY!')
    print(discord.__version__)

@bot.command()
async def embed(ctx):
    #note: you can't mention in titles, author and footer. 
    embed = discord.Embed(colour=discord.Colour.yellow())   # this is the definition of the embed, also you can use color=0x000000 with hex codes.
    embed.set_author(name="Hello, this is the author.")   # this is the author
    embed.add_field(name='Hey there!', value='This is a field', inline=True)   # this is a field
    embed.add_field(name='Howdy!', value='This is a field with inline=true', inline=True)   # this is a inline=True field
    embed.add_field(name='Ayy!', value='This is a field with inline=false', inline=False)   # this is a inline=False field
    embed.set_image(url='URL For a image!')   # this is a set_image
    embed.set_thumbnail(url='URL For a thumbnail!')   # this is a thumbnail
    embed.set_footer(text='This is a footer.')   # this is the footer
    await ctx.send(embed=embed)   # here we are sending it to the channel

@bot.command()
async def mention(ctx):
    await ctx.send(f"{ctx.author.mention}, you have been pinged!")   # ctx.author is basically short for ctx.message.author same for: ctx.guild, ctx.send, etc..

bot.run("token")
