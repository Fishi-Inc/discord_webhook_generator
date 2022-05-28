from InquirerPy import inquirer
from InquirerPy import get_style
from dataclasses import field
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import time
import os
import re
from colorama import init, Fore, Style
init(autoreset=True)

with open('./config.json') as json_file:
    config = json.load(json_file)

os.system('cls' if os.name == 'nt' else 'clear')
print('\n')

help_msg = 'To see how webhooks are formatted, visit https://github.com/Fishi-Inc/discord_webhook_generator'
hint_msg = 'Leave blank if you don\'t need'
info = {}
fields = []
style = get_style({'questionmark': 'hidden','answer': 'fg:blue', 'long_instruction': 'bg:white fg:black', 'input': 'fg:aqua'}, style_override=True)

info['url'] = inquirer.secret(
    message='Enter Webhook URL:',
    validate=lambda x: 'https://discord.com/api/webhooks' in x,
    transformer=lambda _: '[Webhook URL]',
    long_instruction='Paste your webhook URL here',
    invalid_message='Invalid Webhook URL',
).execute()

print('\n')

info['author'] = inquirer.text(
    message='author:        ',
    style=style,
    long_instruction=help_msg,
).execute()

info['title'] = inquirer.text(
    message='title:         ',
    style=style,
).execute()

info['desc'] = inquirer.text(
    message='Description:   ',
    style=style,
    multiline=True,
).execute()

#fields

add_field = inquirer.confirm(
    message='add field?',
    style=style,
).execute()

while (add_field):
    get_fields = len(fields)
    field_title = inquirer.text(
        message='field title:   '
    ).execute()
    fields.append(field_title)
    field_desc = inquirer.text(
        message='field desc:    ',
    ).execute()
    fields.append(field_desc)
    add_field = inquirer.confirm(
        message='add another fields?',
        style=style,
    ).execute()


print(fields)
#info['field']

info['footer'] = inquirer.text(
    message='footer:        ',
    style=style,
).execute()

info['timestamp'] = inquirer.confirm(
    message='timestamp?     ',
    style=style,
).execute()

info['color'] = inquirer.text(
    message='color:         ',
    style=style,
    validate=lambda x: re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', "#" + x),
    transformer=lambda x: x.upper(),
    long_instruction='Input hex color without #',
).execute()

colors = {        
        'transparent': '36393F',
        'red': 'FF0000',
        'green': '008000',
        'blue': '0000FF',
        'orange': 'FFA500',
        'yellow': 'FFFF00',
        'purple': '800080',
        'magenta': 'FF00FF',
        'pink': 'FFC0CB',
        'grey': '808080',
        'aqua': '00FFFF',
        'dark_grey': '202225',
}

print('\nSending webhook...')

try:
    webhook = DiscordWebhook(url=info['url'])
    embed = DiscordEmbed()
    if (info['title'] != ''):       embed.set_title(info['title'])
    if (info['desc'] != ''):        embed.set_description(info['desc'])
    if (info['author'] != ''):      embed.set_author(name=info['author'])
    if (info['footer'] != ''):      embed.set_footer(text=info['footer'])
    if (info['timestamp']):         embed.set_timestamp()
    if (info['color'] != ''):       embed.set_color(info['color'])
    if (fields != []):
        for x in fields:
            embed.add_embed_field(name=field[x[0]], value[x[1]])
    webhook.add_embed(embed)
    webhook.avatar_url = config['webhook_avatar']
    webhook.username = config['webhook_name']
    webhook.execute()
    print(Style.BRIGHT + Fore.GREEN + 'Successfully sent webhook!\n')
except:
    print(Style.BRIGHT + Fore.RED + 'Something went wrong\n')
    input('Press enter to exit...')