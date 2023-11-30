import nextcord
from nextcord import Interaction
from nextcord.ext import commands, application_checks
from nextcord import Locale


class smod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="kick",
        name_localizations={
            Locale.ru: "кик",
        },
        description="Kick member -_-",
        description_localizations={
            Locale.ru: "Выгнать участника -_-",
        },
    )
    @application_checks.has_guild_permissions(kick_members=True)
    @application_checks.guild_only()
    async def kick(self, interaction: Interaction, member: nextcord.Member, reason: str):
        if member.id == interaction.user.id:
            await interaction.response.send_message(
                f'{interaction.user.mention}, вы не можете **кикнуть себя** <:nkr_tired:956634432712871966>',
                ephemeral=True)
            return
        if reason is None:
            reason = "Не указана"
        kick_dm = nextcord.Embed(title=f'Вас выгнали из {member.guild.name} 👢', color=0xFFC857)
        kick_dm.add_field(name='Причина', value=f'{reason}')
        kick_dm.set_footer(text='Вы можете вернуться обратно после приглашения на сервер')
        await member.send(embed=kick_dm)
        await member.kick(reason=reason)
        done = nextcord.Embed(title=f'Участник {member.name}#{member.discriminator} кикнут 👢', color=0xFFC857)
        done.add_field(name='Причина', value=f'{reason}')
        await interaction.response.send_message(embed=done, ephemeral=True)

    @nextcord.slash_command(
        name="delete",
        name_localizations={
            Locale.ru: "удалить",
        },
        description="Clear member messages [@Member] or everything - [amount]",
        description_localizations={
            Locale.ru: "Очистить сообщения участника @ или все подряд - количество",
        },
    )
    @application_checks.has_guild_permissions(manage_messages=True)
    @application_checks.guild_only()
    async def purge(self, interaction=Interaction, amount=50, member: nextcord.Member = None):
        msg = []
        amount = int(amount)
        if not member:
            await interaction.channel.purge(limit=amount)
            return await interaction.send(f"Сообщений удалено: {amount}", delete_after=3)
        async for m in interaction.channel.history():
            if len(msg) == amount:
                break
            if m.author == member:
                msg.append(m)
        await interaction.channel.delete_messages(msg)
        await interaction.send(f"Удалено {amount} сообщений от {member.name}", delete_after=3)


def setup(bot):
    bot.add_cog(smod(bot))
