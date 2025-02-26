import discord

token = "YOUR_TOKEN"

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=discord.Intents.default())

client.run(token=token)