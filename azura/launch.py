import os

import nextcord
from nextcord.ext import commands
from rgbprint import rgbprint
from rgbprint import Color
# ENV Checks
try:
    token = os.environ['TOKEN']
    if token == 'yourtoken':
        rgbprint(
            'Uh-Oh!\nPlease, find TOKEN variable in docker-compose.yml and enter your Discord-Bot Token!\nThen, '
            'rerun docker-compose: docker-compose up -d', color="yellow")
    rgbprint('[OK] Environment: TOKEN detected!', color="green")
except:
    rgbprint(f'[{Color.red}@#?!{Color.reset}] FAILED TO GET TOKEN FROM .ENV')
# Init
bot = commands.Bot(intents=nextcord.Intents().all(), help_command=None)
print(' ▄▄▄· ·▄▄▄▄•▄• ▄▌▄▄▄   ▄▄▄· \n▐█ ▀█ ▪▀·.█▌█▪██▌▀▄ █·▐█ ▀█ \n▄█▀▀█ ▄█▀▀▀•█▌▐█▌▐▀▀▄ ▄█▀▀█ \n▐█ '
      '▪▐▌█▌▪▄█▀▐█▄█▌▐█•█▌▐█ ▪▐▌\n ▀  ▀ ·▀▀▀ • ▀▀▀ .▀  ▀ ▀  ▀\nAzura-Forever\nInitial Release: '
      '"Catbird"\nWritten and wrapped by Ruecat')
for filename in os.listdir("./modules"):
    try:
        if filename.endswith(".py"):
            bot.load_extension(f"modules.{filename[:-3]}")
            rgbprint(f'[+] {filename[:-3]} registered as Cog', color="green")
        if filename.endswith(".disabled"):
            rgbprint(f'[?] {filename[:-9]} skipped, unverified!', color="yellow")
    except Exception as module_error_display:
        rgbprint(f'[X] CAUGHT FAULT IN {filename[:-3]}!\n[{filename[:-3]}-FAULT] {module_error_display}')
print("\nDisplaying logs from now on..\n--------------------------------\nmeow~\n...")
try:
    bot.run(token)
except:
    rgbprint(f'[{Color.red}AZURA-CRITICAL{Color.reset}] TOKEN/AUTH ERROR')
    exit(code="TOKEN_ERR_NOT_PROVIDED")
