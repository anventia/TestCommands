import discord
from discord.ext import commands
import asyncio
import json

# Startup
bot = commands.Bot(command_prefix=">>", case_insensitive=True, intents=discord.Intents.all())
bot.remove_command("help") #Removes default help command\

print("Starting up...")
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name="for commands | >>help", type=discord.ActivityType.watching))
    print('Status Updated')
    print('Logged in as {0.user}'.format(bot))

@bot.event  # Ignores commands sent by bots
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


# Core functions
def read_file(filename):
    with open(filename, 'r') as f:
        load = json.load(f)
    return load

def write_file(dictionary, filename):
    with open(filename, 'w') as f:
        json.dump(dictionary, f, indent=4)




# Run
data = read_file("config.json")
token = data["token"]
bot.run(token)
