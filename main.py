import os
import discord
TOKEN = os.environ["token"]
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("what we doin"):
    await message.channel.send("Farming commits.")
    
  if message.content.startswith("link my git"):
    await message.channel.send("https://github.com/josh894")

client.run(TOKEN)
