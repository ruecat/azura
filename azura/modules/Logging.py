import nextcord
from nextcord.ext import commands

# This section might be deprecated
class triggers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        # TO-DO: Add placeholder as environment variable
        wmsg = nextcord.Embed(title=f"Welcome to {member.guild.name} <a:oreo_catJAM:1118539317032255508>",
                              description="{placeholder}",
                              color=nextcord.Color.blurple())
        await member.send(embed=wmsg)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.bot.user:
            return
        print(
            f'----\nMessageDeleted\nAuthorName: {message.author.name}#{message.author.discriminator}\nAuthorID:{message.author.id}\nMessage: {message.content}\n----')

    @commands.Cog.listener()
    async def on_voice_state_update(self, member: nextcord.Member, before: nextcord.VoiceState,
                                    after: nextcord.VoiceState):
        if before.channel is None:
            print(f"----\nJoinedVC\n{member.display_name} {after.channel.mention}")
        elif after.channel is None:
            print(f"{member.display_name} left {before.channel.mention}")
        elif before.channel != after.channel:
            print(
                f"----\nVoiceChat_logs\n{member.display_name} voicejumped\nFROM: {before.channel.mention}\nTO: {after.channel.mention}")


def setup(bot):
    bot.add_cog(triggers(bot))
