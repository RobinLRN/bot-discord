import discord
from discord.ext import commands

class Responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.lower().strip().endswith(("quoi", "quoi?", "quoi ?", "kwa")):
            await message.channel.send("feur")

async def setup(bot):
    await bot.add_cog(Responses(bot))
