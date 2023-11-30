import random

import nextcord
from nextcord.ext import commands
from nextcord import Locale


class sfun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="question",
                            name_localizations={Locale.ru: "вопрос"})
    async def questions(self, interaction: nextcord.Interaction):
        """No actions can be done here -_-"""

    @questions.subcommand(
        name="ben",
        name_localizations={
            Locale.ru: "бен",
        },
        description="Ben will reply to the question!",
        description_localizations={
            Locale.ru: "Бен ответит на твой вопрос!",
        },
    )
    async def answer_ben(self, interaction: nextcord.Interaction, вопрос: str):
        answer_gif_map = {
            "Yes": "https://media.tenor.com/6St4vNHkyrcAAAAd/yes.gif",
            "No.": "https://media.tenor.com/3ZLujiiPc4YAAAAC/talking-ben-no.gif",
            "Ugh.": "https://media.tenor.com/aomZLSiXCQ8AAAAC/ugh.gif",
            "Hohoho!": "https://media.tenor.com/e8urEO5XU-kAAAAd/hohho-ho.gif",
        }
        answers = list(answer_gif_map.keys())
        answer = random.choice(answers)
        gif = answer_gif_map[answer]
        embed = nextcord.Embed(title="Бен ответил!", color=0x3d81ff)
        embed.add_field(name="Question:", value=вопрос, inline=False)
        embed.add_field(name="Answer:", value=answer, inline=False)
        embed.set_image(url=gif)
        await interaction.response.send_message(embed=embed, delete_after=5)


def setup(bot):
    bot.add_cog(sfun(bot))
