import nextcord
from nextcord.ext import commands


class descriptor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TO-DO: Add /help command
    @commands.Cog.listener()
    async def on_connect(self):
        await self.bot.change_presence(status=nextcord.Status.idle,
                                       activity=nextcord.Activity(type=nextcord.ActivityType.listening,
                                                                  name='/help | On ' + str(
                                                                      len(self.bot.guilds)) + ' servers!'))


def setup(bot):
    bot.add_cog(descriptor(bot))
