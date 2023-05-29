"""
                                                                                                                                                                            
                                                                                                                                                                            
BBBBBBBBBBBBBBBBB                              tttt              tttt                                             BBBBBBBBBBBBBBBBB                           tttt          
B::::::::::::::::B                          ttt:::t           ttt:::t                                             B::::::::::::::::B                       ttt:::t          
B::::::BBBBBB:::::B                         t:::::t           t:::::t                                             B::::::BBBBBB:::::B                      t:::::t          
BB:::::B     B:::::B                        t:::::t           t:::::t                                             BB:::::B     B:::::B                     t:::::t          
  B::::B     B:::::B   eeeeeeeeeeee   ttttttt:::::ttttttttttttt:::::ttttttt       eeeeeeeeeeee   rrrrr   rrrrrrrrr  B::::B     B:::::B  ooooooooooo  ttttttt:::::ttttttt    
  B::::B     B:::::B ee::::::::::::ee t:::::::::::::::::t:::::::::::::::::t     ee::::::::::::ee r::::rrr:::::::::r B::::B     B:::::Boo:::::::::::oot:::::::::::::::::t    
  B::::BBBBBB:::::B e::::::eeeee:::::et:::::::::::::::::t:::::::::::::::::t    e::::::eeeee:::::er:::::::::::::::::rB::::BBBBBB:::::Bo:::::::::::::::t:::::::::::::::::t    
  B:::::::::::::BB e::::::e     e:::::tttttt:::::::ttttttttttt:::::::tttttt   e::::::e     e:::::rr::::::rrrrr::::::B:::::::::::::BB o:::::ooooo:::::tttttt:::::::tttttt    
  B::::BBBBBB:::::Be:::::::eeeee::::::e     t:::::t           t:::::t         e:::::::eeeee::::::er:::::r     r:::::B::::BBBBBB:::::Bo::::o     o::::o     t:::::t          
  B::::B     B:::::e:::::::::::::::::e      t:::::t           t:::::t         e:::::::::::::::::e r:::::r     rrrrrrB::::B     B:::::o::::o     o::::o     t:::::t          
  B::::B     B:::::e::::::eeeeeeeeeee       t:::::t           t:::::t         e::::::eeeeeeeeeee  r:::::r           B::::B     B:::::o::::o     o::::o     t:::::t          
  B::::B     B:::::e:::::::e                t:::::t    tttttt t:::::t    ttttte:::::::e           r:::::r           B::::B     B:::::o::::o     o::::o     t:::::t    tttttt
BB:::::BBBBBB::::::e::::::::e               t::::::tttt:::::t t::::::tttt:::::e::::::::e          r:::::r         BB:::::BBBBBB::::::o:::::ooooo:::::o     t::::::tttt:::::t
B:::::::::::::::::B e::::::::eeeeeeee       tt::::::::::::::t tt::::::::::::::te::::::::eeeeeeee  r:::::r         B:::::::::::::::::Bo:::::::::::::::o     tt::::::::::::::t
B::::::::::::::::B   ee:::::::::::::e         tt:::::::::::tt   tt:::::::::::tt ee:::::::::::::e  r:::::r         B::::::::::::::::B  oo:::::::::::oo        tt:::::::::::tt
BBBBBBBBBBBBBBBBB      eeeeeeeeeeeeee           ttttttttttt       ttttttttttt     eeeeeeeeeeeeee  rrrrrrr         BBBBBBBBBBBBBBBBB     ooooooooooo            ttttttttttt  
                                                                                                                                                     _        _             _____         _      _      
                                                                                                                                                    | |      | |           |  __ \       | |    (_)      
                                                                                                                                 _ __ ___   __ _  __| | ___  | |__  _   _  | |__) |__  __| |_ __ _ _ __  
                                                                                                                                | '_ ` _ \ / _` |/ _` |/ _ \ | '_ \| | | | |  ___/ _ \/ _` | '__| | '_ \ 
                                                                                                                                | | | | | | (_| | (_| |  __/ | |_) | |_| | | |  |  __/ (_| | |  | | | | |
                                                                                                                                |_| |_| |_|\__,_|\__,_|\___| |_.__/ \__, | |_|   \___|\__,_|_|  |_|_| |_|
                                                                                                                                                                     __/ |                               
                                                                                                                                                                    |___/                                                                                                                                                                                 
"""

#### REQUIREMENTS ####
# main file for the sniper must be named "main.py"
# config file for the sniper must be named "config.json"
                                                                                                                                                         
#### TUTORIAL ####
# 1 - put this file in your sniper folder
# 2 - change the "sniper_path" on the config BELOW (NOT CONFIG.JSON) to where your sniper is located. example: C:\Users\nuts\Downloads\ugc-sniper-main
# 3 - change the config to your liking
# 4 - go TO config.json file and set "discord" to "true" and put a token
# 5 - run this file as "Python" or "WindowsTerminal" and enjoy!

#### CONFIG ####
sniper_path = r"" # where your sniper is located (DONT REMOVE THE "r") | format: C:\Users\nuts\Downloads\ugc-sniper-main
press_f11 = False # if this is set to "True" it will press the F11 key when the commands: restart, norooms, rooms and run is executed
prefix = "." # prefix to use commands on the bot | example: .restart

############### DONT TOUCH THIS IF YOU DONT KNOW WHAT YOUR DOING ###############
############### DONT TOUCH THIS IF YOU DONT KNOW WHAT YOUR DOING ###############
############### DONT TOUCH THIS IF YOU DONT KNOW WHAT YOUR DOING ###############
############### DONT TOUCH THIS IF YOU DONT KNOW WHAT YOUR DOING ###############
############### DONT TOUCH THIS IF YOU DONT KNOW WHAT YOUR DOING ###############

import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

try:
    from pystyle import Colorate, Colors, Center
    import asyncio
    import requests
except ModuleNotFoundError:
    os.system('pip install pystyle')
    os.system('pip install asyncio')
    os.system('pip install requests')


version = "1.0.1"
title = f"""
                                                                                                          v{version}
                 /$$$$$$$              /$$     /$$                         /$$$$$$$              /$$    
                | $$__  $$            | $$    | $$                        | $$__  $$            | $$    
                | $$  \ $$  /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$ | $$  \ $$  /$$$$$$  /$$$$$$  
                | $$$$$$$  /$$__  $$|_  $$_/|_  $$_/   /$$__  $$ /$$__  $$| $$$$$$$  /$$__  $$|_  $$_/  
                | $$__  $$| $$$$$$$$  | $$    | $$    | $$$$$$$$| $$  \__/| $$__  $$| $$  \ $$  | $$    
                | $$  \ $$| $$_____/  | $$ /$$| $$ /$$| $$_____/| $$      | $$  \ $$| $$  | $$  | $$ /$$
                | $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$/|  $$$$$$$| $$      | $$$$$$$/|  $$$$$$/  |  $$$$/
                |_______/  \_______/   \___/   \___/   \_______/|__/      |_______/  \______/    \___/  
                                                                                                        
                                                                                                        

"""

print(Colorate.Vertical(Colors.cyan_to_blue, title))

response = requests.get("https://raw.githubusercontent.com/PedrinBlox/test/main/version")
if response.status_code != 200:
    pass
if not response.text.rstrip() == version:
        print(f"BETTERBOT HAS A NEW VERSION ({response.text.rstrip()}). PLEASE UPDATE YOUR FILE.")
        print(f"IF YOU PREFER THIS VERSION, IT WILL CONTINUE IN 10 SECONDS.")
        time.sleep(10)

title_printed = False

async def print_title(interval):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        buffer = Colorate.Vertical(Colors.cyan_to_blue, title)  # Prepare the output
        print(buffer, end='', flush=True)  # Print and flush buffer
        await asyncio.sleep(interval)
        time.sleep(0.2)

try:
    try:
        import pyautogui
        import discord
        from discord.ext import commands
        import subprocess
        import json
    except ModuleNotFoundError:
        print("Some modules may be missing. Installing them...")
        os.system('pip install discord')
        os.system('pip install pyautogui')

    os.system('title BetterBot')

    bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        asyncio.create_task(print_title(0.1))

    @bot.command()
    async def restart(ctx):
        try:
            current_pid = os.getpid()
            processes = subprocess.run(['tasklist'], capture_output=True, text=True).stdout.split('\n')
            programs_to_kill = ['python.exe', 'cmd.exe']

            for process in processes:
                for program in programs_to_kill:
                    if program in process:
                        pid = int(process.split()[1])
                        if pid != current_pid:
                            os.system(f'taskkill /PID {pid} /F')
            time.sleep(.5)
            os.system(r"start cmd")
            time.sleep(0.1)
            pyautogui.write(fr'python "{sniper_path}\main.py"')
            pyautogui.press('Enter')
            if press_f11:
                pyautogui.press('f11')
            await ctx.reply(':white_check_mark: | Sucessfully restarted Sniper process!')

        except Exception as e:
            print(sniper_path+"\main.py")
            await ctx.reply(f':x: | An error occured: {e}')
            print(e)

    @bot.command()
    async def norooms(ctx):
        try:
            with open('config.json', 'r') as file:
                data = json.load(file)
            data['rooms']['enabled'] = False
            with open('config.json', 'w') as file:
                json.dump(data, file, indent=4)
            time.sleep(.5)
            current_pid = os.getpid()
            processes = subprocess.run(['tasklist'], capture_output=True, text=True).stdout.split('\n')
            programs_to_kill = ['python.exe', 'cmd.exe']

            for process in processes:
                for program in programs_to_kill:
                    if program in process:
                        pid = int(process.split()[1])
                        if pid != current_pid:
                            os.system(f'taskkill /PID {pid} /F')
            time.sleep(.5)
            os.system(r"start cmd")
            time.sleep(0.1)
            pyautogui.write(fr'python "{sniper_path}\main.py"')
            pyautogui.press('Enter')
            if press_f11:
                pyautogui.press('f11')
            await ctx.reply(':white_check_mark: | Sucessfully disabled rooms!')
            
        except Exception as e:
            await ctx.reply(f':x: | An error occured: {e}')

    @bot.command()
    async def rooms(ctx):
        try:
            with open('config.json', 'r') as file:
                data = json.load(file)
            data['rooms']['enabled'] = True
            with open('config.json', 'w') as file:
                json.dump(data, file, indent=4)
            time.sleep(.5)
            current_pid = os.getpid()
            processes = subprocess.run(['tasklist'], capture_output=True, text=True).stdout.split('\n')
            programs_to_kill = ['python.exe', 'cmd.exe']

            for process in processes:
                for program in programs_to_kill:
                    if program in process:
                        pid = int(process.split()[1])
                        if pid != current_pid:
                            os.system(f'taskkill /PID {pid} /F')
            time.sleep(.5)
            os.system(r"start cmd")
            time.sleep(0.1)
            pyautogui.write(fr'python "{sniper_path}\main.py"')
            pyautogui.press('Enter')
            if press_f11:
                pyautogui.press('f11')
            await ctx.reply(':white_check_mark: | Sucessfully enabled rooms!')
            
        except Exception as e:
            await ctx.reply(f':x: | An error occured: {e}')

    @bot.command()
    async def kill(ctx):
        try:
            current_pid = os.getpid()
            processes = subprocess.run(['tasklist'], capture_output=True, text=True).stdout.split('\n')
            programs_to_kill = ['python.exe', 'cmd.exe']

            for process in processes:
                for program in programs_to_kill:
                    if program in process:
                        pid = int(process.split()[1])
                        if pid != current_pid:
                            os.system(f'taskkill /PID {pid} /F')
            await ctx.reply(':white_check_mark: | Sucessfully ended Sniper process!')
            
        except Exception as e:
            await ctx.reply(f':x: | An error occured: {e}')

    @bot.command()
    async def run(ctx):
        try:
            os.system(r"start cmd")
            time.sleep(0.1)
            pyautogui.write(fr'python "{sniper_path}\main.py"')
            pyautogui.press('Enter')
            if press_f11:
                pyautogui.press('f11')
            await ctx.reply(':white_check_mark: | Succesfully started Sniper process!')
            
        except Exception as e:
            await ctx.reply(f':x: | An error occured: {e}')

    with open('config.json', 'r') as file:
        data = json.load(file)

    if data['discord']['enabled'] == True:
        bot.run(data['discord']["token"])
    else:
        print("You have not enabled discord on config.json file!")
        os.system('pause')
        exit
except Exception as e:
    print(f'An error occured: {e}')
    os.system('pause')
