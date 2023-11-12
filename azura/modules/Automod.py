import aiohttp
import nextcord
from nextcord.ext import commands, tasks


class automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.banned_links = set()
        self.getlinks.start()

    def cog_unload(self):
        self.getlinks.cancel()

    @tasks.loop(minutes=60.0)
    async def getlinks(self):
        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get('https://phish.sinking.yachts/v2/all', timeout=5)
                if response.status == 200:
                    links = await response.json()
                    self.banned_links = set(links)
        except Exception as e:
            print(f'[ERROR] Failed to get banned links: {e}')

    @getlinks.before_loop
    async def before_logging(self):
        await self.bot.wait_until_ready()

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.banned_links is None:
            return
        # False-positive fixer (Members can get banned if they use "Nitro emoji bypass" thing
        elif 'https://cdn.discordapp.com/' in message.content:
            return
        # Ban any user that post scam-link(s)
        elif any(i in message.content for i in self.banned_links):
            # send to specific channel
            channel = self.bot.get_channel(1160602587662405723)
            modlog = nextcord.Embed(title=f'{message.author.name} получил молотком по голове 🔨', color=0xff0000)
            modlog.add_field(name='Причина', value='AzuraSL: Фишинг')
            modlog.set_footer(text='Использованы суперсилы AzuraSL 🐱🪄')
            await channel.send(embed=modlog)
            banc = nextcord.Embed(title=f'Вас забанили на {message.guild.name} 🔨', color=0xff0000)
            banc.add_field(name='Причина', value='AzuraAI: Скам-ссылки')
            banc.set_footer(text='Бан пермаментный, вы больше не сможете зайти на сервер')
            await message.author.send(embed=banc)
            await message.author.ban(reason="AzuraSL: Скам-ссылки", delete_message_days=1)


def setup(bot):
    bot.add_cog(automod(bot))
