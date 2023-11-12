import datetime

import nextcord
from nextcord import Locale
from nextcord.ext import commands, application_checks

class reports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="report",
        name_localizations={
            Locale.ru: "репорт",
        },
        description="Report specific member/mod",
        description_localizations={
            Locale.ru: "Пожаловаться на участника/модератора",
        },
        guild_ids=[1115253435210666014],
    )
    @application_checks.guild_only()
    async def report(self, interaction: nextcord.Interaction, member: nextcord.Member = None):
        modal = InvokeReportForm(bot=self.bot)  # Pass the bot object to the Pet class
        reported_member = member.id
        await interaction.response.send_modal(modal)


class InvokeReportForm(nextcord.ui.Modal):
    def __init__(self, bot, reported_member):
        super().__init__(
            "Отправить репорт",
        )
        self.bot = bot  # Store the bot object
        self.reported_member = reported_member
        self.description = nextcord.ui.TextInput(
            label="Объясните ситуацию",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="Он кидал мне мемы в ЛС!\nЭто просто возмутительно!\nМоя жизнь изменилась навеки!",
            required=True,
            max_length=600,
        )
        self.add_item(self.description)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        report = nextcord.Embed(title="Проверьте перед отправкой", color=0x2b2d30)
        report.add_field(name="На кого репорт", value=f"<@{self.reported_member}>", inline=False)
        report.add_field(name="Обоснование", value=f"{self.description.value}", inline=False)
        report.set_footer(text="За необоснованный или неконструктивный репорт последует наказание")
        await interaction.send(embed=report, ephemeral=True,
                               view=ReportSend(self.bot, self.reported_member,
                                               self.description.value))  # Pass the bot object to the ReportSend class


class ReportSend(nextcord.ui.View):
    def __init__(self, bot, reported_member, description):
        super().__init__()
        self.bot = bot  # Store the bot object
        self.reported_member = reported_member  # Store the reported member ID
        self.report_description = description

    @nextcord.ui.button(label="Отправить", custom_id="send_report", style=nextcord.ButtonStyle.blurple)
    async def reportconfirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        if interaction.user.id == self.reported_member:
            button.style = nextcord.ButtonStyle.red
            button.disabled = True
            button.label = "❌ Зачем.."
            await interaction.response.edit_message(view=self)
            return
        elif self.reported_member == self.bot.user.id:
            button.style = nextcord.ButtonStyle.red
            button.disabled = True
            button.label = "😿 За что.."
            await interaction.response.edit_message(view=self)
            return
        button.style = nextcord.ButtonStyle.green
        button.disabled = True
        button.label = "✅ Успешно."
        await interaction.response.edit_message(view=self)
        # TO-DO: Add environment variable for sending reports in specific channel
        channel = self.bot.get_channel(1166447443232174242)
        a = nextcord.Embed(title="Репорт", color=0x2b2d30)
        a.add_field(name="Репорт отправил", value=f"<@{interaction.user.id}>", inline=False)
        a.add_field(name="На кого репорт", value=f"<@{self.reported_member}>",
                    inline=False)  # Use the reported_member variable
        a.add_field(name="Обоснование", value=f"{self.report_description}", inline=False)
        ru_offset = datetime.timezone(datetime.timedelta(hours=3))
        a.timestamp = datetime.datetime.now(ru_offset)
        case = +1
        a.set_footer(text=f'Case #{case} | SenderID: {interaction.user.id} | ReportedID: {self.reported_member}')
        await channel.send(embed=a)


class reports(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(
        name="report",
        name_localizations={
            Locale.ru: "репорт",
        },
        description="Report a specific member/mod",
        description_localizations={
            Locale.ru: "Пожаловаться на участника/модератора",
        },
        guild_ids=[1115253435210666014],
    )
    async def report(self, interaction: nextcord.Interaction, member: nextcord.Member = None):
        modal = InvokeReportForm(bot=self.bot, reported_member=member.id)  # Pass the bot object to the Pet class
        await interaction.response.send_modal(modal)


def setup(bot):
    bot.add_cog(reports(bot))
