import nextcord
from nextcord.ext import commands, application_checks
from nextcord import Locale

class ButtonManager(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(nextcord.ui.Select(options=[
            nextcord.SelectOption(label="🔄 На проверке", value="status_checking"),
            nextcord.SelectOption(label="🟩 Хорошее", value="status_good"),
            nextcord.SelectOption(label="🟨 Средне", value="status_average"),
            nextcord.SelectOption(label="🟧 Ниже среднего", value="status_below_average"),
            nextcord.SelectOption(label="🟥 Плохое", value="status_bad"),
        ], placeholder="Сменить статус аккаунта"))

    @nextcord.ui.button(label="🥾 Кикнуть", custom_id="kick_user", style=nextcord.ButtonStyle.red)
    async def drama_kick(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Approved.", ephemeral=True)

    @nextcord.ui.button(label="🚫 Забанить", custom_id="ban_user", style=nextcord.ButtonStyle.red)
    async def drama_ban(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Approved.", ephemeral=True)

    @nextcord.ui.button(label="🗑️ Удалить из БД", custom_id="vanish_user", style=nextcord.ButtonStyle.grey)
    async def drama_remredis(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("Approved.", ephemeral=True)
        # to-do
        # 🟩 В хорошем состоянии
        # 🟨 Есть нарушения
        # 🟧 Множество нарушений
        # 🟥 Плохое
        # 🔄 В процессе проверки


class fireplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def check_if_it_is_me(self: nextcord.Interaction):
        return self.user.id == 336578057294970881

    @nextcord.user_command(guild_ids=[1115253435210666014])
    @application_checks.check(check_if_it_is_me)
    async def DramaPanel(self, interaction: nextcord.Interaction, member: nextcord.Member):
        pview = nextcord.Embed(title=f"DramaPanel: {member.name}", description="Что предпринять?", color=0x2b2d30)
        pview.set_thumbnail(url=member.avatar.url)
        pview.set_footer(text=f"AzuraDramaPanel | MemberID: {member.id}")
        pview.add_field(name="Уровень доверия:", value=f"🔄 На проверке", inline=False)
        await interaction.response.send_message(f"Становится интереснее..", embed=pview, ephemeral=True,
                                                view=ButtonManager())

    @nextcord.slash_command(name="sandctl")
    async def sandctl(self, interaction: nextcord.Interaction):
        """a"""

    @sandctl.subcommand(name="oreo", description="Шаблон для OreoNetwork",)
    async def oreo_template(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(title="Приветствуем вас на проекте OreoNetwork!", color=0xBEE5BF)
        embed.add_field(name="IP", value="`beta.oreo.re`", inline=False)
        embed.add_field(name="Репорт багов", value="Если вы заметили уязвимость или баг, смело отправляйте его в канал [<#1133510531282645082>]", inline=False)
        await interaction.response.send_message(embed=embed)
    @sandctl.subcommand(name="welcome", description="Шаблон для правил сервера",)
    async def welcome_template(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(title="С прибытием на сервер!", color=0xBEE5BF)
        embed.add_field(name="Быстрая навигация по основным каналам", value=">>> [**Текущий канал**] Подробные объяснения что и как работает на сервере  👀\n**Все обновления сервера**\n<#956264392884912169>\n**Розыгрыши от нас или участников сервера!**\n<#1164603669308772373>", inline=False)
        await interaction.response.send_message(embed=embed)
    @sandctl.subcommand(name="block", description="Шаблон для правил сервера",)
    async def info(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(title="ClarLand отвязан от AzuraCMS", color=0xFF0000)
        embed.add_field(name="Статус сервера", value="В чёрном списке", inline=False)
        embed.add_field(name="Причина", value="Уязвимость False-Positive типа: При использование DiscordCDN идет "
                                              "блокировка аккаунта.", inline=False)

        await interaction.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(fireplace(bot))
    # profile = nextcord.Embed(title=f"Уведомление для аккаунта", description="⬇︎ Статус доверия изменён.",
    # color=0xFF8000) profile.set_thumbnail(url=member.avatar.url) profile.set_footer(text=f"AzuraCoreTrust | Случай:
    # #10 | UID: {member.id}") profile.add_field(name="Уровень доверия:", value=f"🟧 Ниже среднего", inline=False)
    # profile.add_field(name="Причина", value=f"Возможный твинк-аккаунт (Незаполненный профиль)", inline=False) await
    # member.send(embed=profile)
