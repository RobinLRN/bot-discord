import discord

token = "YOUR_TOKEN"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name='Bot fait par Jaimyo'))

@client.event
async def on_message(message: discord.Message):
  if message.author.bot:
    return
  


  elif message.content.lower().endswith("quoi") or message.content.lower().endswith("quoi?") or message.content.lower().endswith("quoi ?") or message.content.lower().endswith("kwa"):
    await message.channel.send("feur")


client.run(token=token)