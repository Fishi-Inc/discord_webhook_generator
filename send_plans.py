from dataclasses import field
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import time
import os
from PIL import Image
import requests
from io import BytesIO
from colorama import init, Fore, Style
init(autoreset=True)


with open('./plans/plans.json') as json_file:
    data = json.load(json_file)

with open('./config.json') as json_file:
    config = json.load(json_file)

os.system('cls' if os.name == 'nt' else 'clear')
print('\n')

x = input('Enter Webhook URL or Press enter to exit...\n> ')
while 'https://discord.com/api/webhooks' not in x:
    print(Style.BRIGHT + Fore.RED + 'Webhook URL is valid\n')
    x = input('Enter Webhook URL or Press enter to exit...\n> ')
else:
    url = x

print('\nSending webhook...')

for plan in data:
    webhook = DiscordWebhook(url=url)
    embed = DiscordEmbed(title=plan['desc'], description=plan['price'], color=plan['color'])
    embed.set_author(name=plan['title'], icon_url=plan['icon']) 
    webhook.add_embed(embed)
    webhook.avatar_url = config['webhook_avatar']
    webhook.username = config['webhook_name']
    webhook.execute()
    time.sleep(1)

print(Style.BRIGHT + Fore.GREEN + 'Successfully sent webhook!\n')
input('Press enter to exit...')