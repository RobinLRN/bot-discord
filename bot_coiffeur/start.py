import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from keep_alive import keep_alive

load_dotenv()

token=os.getenv('DISCORD_TOKEN')

class Coiffeur(commands.Bot):
    async def setup_hook(self):
        for extension in ['response']:
            await self.load_extension(f'cogs.{extension}')

intens = discord.Intents.all()
bot = Coiffeur(command_prefix='!', intents=intens)

keep_alive()
bot.run(token=token)