from InquirerPy import inquirer
from InquirerPy import get_style
import subprocess
from colorama import init, Fore, Style, Back

init(autoreset=True)

print('\n')
print(''' 
 _       __     __    __                __      ______                           __            
| |     / /__  / /_  / /_  ____  ____  / /__   / ____/__  ____  ___  _________ _/ /_____  _____
| | /| / / _ \/ __ \/ __ \/ __ \/ __ \/ //_/  / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
| |/ |/ /  __/ /_/ / / / / /_/ / /_/ / ,<    / /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
|__/|__/\___/_.___/_/ /_/\____/\____/_/|_|   \____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                                                                                by Fishi_Inc
''')

style = get_style({"question": "fg:black bg:white"}, style_override=True)

x = inquirer.select(
        message='What type of webhook do you want to send?',
        style=style,
        choices=['CUSTOM', 'PLANS', 'STATUS', 'FAQ'],
        pointer='>',
        ).execute()
print(x)

if (x == 'PLANS'):
    subprocess.call('send_plans.py', shell=True)
elif (x == 'STATUS'):
    subprocess.call('send_status.py', shell=True)
elif (x == 'FAQ'):
    subprocess.call('send_faq.py', shell=True)
elif (x == 'CUSTOM'):
    subprocess.call('send_custom.py', shell=True)
