import discord, time, traceback

from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print('OK >> BOT IS READY!')
    print(discord.__version__)

if __name__ == "__main__":
    for extension in [f.replace('.py', '') for f in listdir("cogs") if isfile(join("cogs", f))]:
        try:
            bot.load_extension("cogs." + extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.')
            traceback.print_exc() #here we are loading all the cogs that are in a folder named "cogs" and have .py at the end of the file.
            #pro tip: use cogs.

bot.run("token")
