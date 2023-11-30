import logging
import os
import nextcord
import aioredis
from nextcord import Locale
from nextcord.ext import commands

# THIS SECTION IS HEAVILY WIP

redis_host = 'azura-db'
redis_port = 6379
redis_db = 0
booster_key = os.environ['BOOSTER_ROLEID']

experience_key = 'experience:{0.id}:{0.guild.id}'
money_key = 'money:{0.id}:{0.guild.id}'
level_key = 'level:{0.id}:{0.guild.id}'


class ecolvls(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        redis_client = await aioredis.Redis(host=redis_host, port=redis_port, db=redis_db)
        try:
            booster = os.environ[booster_key]
        except KeyError:
            logging.warning('[?!] Environment: some variables not set, restricted some functions.')
            booster = None

        user_experience = int(await redis_client.get(experience_key.format(message.author)) or 0)
        user_money = int(await redis_client.get(money_key.format(message.author)) or 0)

        if booster and any(role.id == booster for role in message.author.roles):
            user_experience += 5
            user_money += 10
        else:
            user_experience += 1
            user_money += 1

        await redis_client.set(experience_key.format(message.author), user_experience)
        await redis_client.set(money_key.format(message.author), user_money)

        user_level = int(await redis_client.get(level_key.format(message.author)) or 1)

        if user_experience >= 100:
            user_level += 1
            user_experience = 0

        await redis_client.set(experience_key.format(message.author), user_experience)
        await redis_client.set(level_key.format(message.author), user_level)

        await self.bot.process_commands(message)

    @nextcord.slash_command(
        name="profile",
        name_localizations={
            Locale.ru: "профиль",
        },
        description="Your profile on this server!",
        description_localizations={
            Locale.ru: "Ваш профиль на этом сервере!",
        }
    )
    async def profile(self, interaction: nextcord.Interaction):
        redis_client = await aioredis.Redis(host=redis_host, port=redis_port, db=redis_db)

        user_experience = int(redis_client.get(experience_key.format(interaction.user)) or 1)
        user_money = int(await redis_client.get(money_key.format(interaction.user)) or 0)
        user_level = int(await redis_client.get(level_key.format(interaction.user)) or 1)

        profile = nextcord.Embed(title=f"Aiwe, {interaction.user.name}!", color=0x3d81ff)
        profile.set_thumbnail(url=interaction.user.avatar.url)
        profile.set_footer(text=f"ID: {interaction.user.id}")
        profile.add_field(name="Trust rank:", value="🟧 Unknown", inline=False)
        profile.add_field(name="Level", value=f"{user_level}", inline=True)
        profile.add_field(name="EXP", value=f"{user_experience}/100", inline=True)
        profile.add_field(name="Money", value=f"{user_money} 🔥", inline=False)

        await interaction.response.send_message(embed=profile, ephemeral=True)

    @nextcord.user_command()
    async def Profile(self, interaction: nextcord.Interaction, member: nextcord.Member):
        redis_client = await aioredis.Redis(host=redis_host, port=redis_port, db=redis_db)

        user_experience = int(await redis_client.get(experience_key.format(member)) or 1)
        user_money = int(await redis_client.get(money_key.format(member)) or 0)
        user_level = int(await redis_client.get(level_key.format(member)) or 1)

        profile = nextcord.Embed(title=f"Aiwe, {member.name}!", color=0x3d81ff)
        profile.set_thumbnail(url=member.avatar.url)
        profile.set_footer(text=f"ID: {member.id}")
        profile.add_field(name="Trust rank:", value="🟧 Unknown", inline=False)
        profile.add_field(name="Level", value=f"{user_level}", inline=True)
        profile.add_field(name="EXP", value=f"{user_experience}/100", inline=True)
        profile.add_field(name="Money", value=f"{user_money} 🔥", inline=False)

        await interaction.response.send_message(embed=profile, ephemeral=True)


def setup(bot):
    bot.add_cog(ecolvls(bot))
