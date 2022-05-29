from dataclasses import field
from prettytable import PrettyTable
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import os
from colorama import init, Fore, Back
init(autoreset=True)

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

print(Back.WHITE + Fore.BLACK + '\nAvailable Arguments:')
table = PrettyTable()
table.field_names = ['Status', 'Description']
table.align['Status'] = 'c'
table.align['Description'] = 'l'
table.add_row(['1', 'up',])
table.add_row(['2', 'bug'])
table.add_row(['3', 'down'])

print(table)

status = input('\nEnter status: ')
title = input('Enter title: ')
print('\nEnter description:')
desc = input('> ')
if (status == '1'):
    color = '309430'
    icon = '🟢'
elif (status == '2'):
    color = 'F98B00'
    icon = '🟠'
elif (status == '3'):
    color = 'D62D42'
    icon = '🔴'
else:
    color = '000000'
    icon = '⚪'

print('\nSending webhook...')

webhook = DiscordWebhook(url=url)
embed = DiscordEmbed(title=(icon + ' ' + title), description=desc, color=color)
embed.set_timestamp()
webhook.add_embed(embed)
webhook.avatar_url = config['webhook_avatar']
webhook.username = config['webhook_name']
webhook.execute()

print(Fore.GREEN + 'Successfully sent webhook!\n')
input('Press enter to exit...')