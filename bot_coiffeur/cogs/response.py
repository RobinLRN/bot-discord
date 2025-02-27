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

        # Définition des triggers
        triggers_feur = ["quoi", "quoi?", "quoi ?", "kwa", "quoa", "koa"]
        triggers_c_feur = ["c'est quoi", "c'est quoi?", "c'est quoi ?", "c quoi", "c quoi?", "c quoi ?", "c kwa"]

        message_content = message.content.lower().strip()

        # Vérification si le message contient un des triggers
        if any(message_content.endswith(trigger) for trigger in triggers_feur):
            await message.channel.send("feur")
        elif any(message_content.startswith(trigger) for trigger in triggers_c_feur):
            await message.channel.send("c'est feur")

async def setup(bot):
    await bot.add_cog(Responses(bot))
