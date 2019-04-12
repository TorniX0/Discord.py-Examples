import discord, time

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType   # importing the cooldown for the next cooldown command

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('OK >> BOT IS READY!')
    print(discord.__version__)

@bot.event
async def on_command_error(ctx, err):   # a error handler
    if isinstance(err, commands.CommandOnCooldown):   # down there i was talking about that it raises commands.CommandOnCooldown
        await ctx.send(f"You got ratelimited! Wait {round(err.retry_after, 2)}s more!")   # sending the user a message that he got ratelimited and how much he has to wait until it expires.

@bot.event
async def on_member_join(member):   # a on_member_join event
    await ctx.send(f"Welcome, {member.mention}!")   # sending him a greet message

@bot.command()
@bot.cooldown(5, 5, commands.BucketType.user)   # basically like (rate,per,BucketType). and it raises commands.CommandOnCooldown.
async def cooldown(ctx):
    await ctx.author.send("Hey! If you spam this command 5 times, you'll get ratelimited for 5 seconds!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Ping: **`{round(bot.latency * 1000)}ms`**.")   # sends the bot.latency
    #-------------------------- down here is the api latency -----------------
    #you can use it if you want but it's not necesarry.
    #
    #start = time.perf_counter()
    #message = await ctx.send('Ping...')
    #end = time.perf_counter()
    #duration = (end - start) * 1000
    #await message.edit(content='Pong! {:.2f}ms'.format(duration))

bot.run("token")
