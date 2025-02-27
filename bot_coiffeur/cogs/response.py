import discord
from discord.ext import commands

class Responses(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(activity=discord.Game(name='Bot fait par Jaimyo'))
        print("Le bot est prêt et son statut a été mis à jour !")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.lower().strip().endswith(("quoi", "quoi?", "quoi ?", "kwa", "quoa", "koa")):
            await message.channel.send("feur")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        if message.content.lower().strip().startswith(("c'est quoi","c'est quoi?","c'est quoi ?","c quoi","c quoi?","c quoi ?", "c kwa")):
            await message.channel.send("c'est feur")

async def setup(bot):
    await bot.add_cog(Responses(bot))
