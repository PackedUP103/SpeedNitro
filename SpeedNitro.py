# MIT License
#
# Copyright (c) 2021 Zak Koyer
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Load First #
import sys
from sys import platform

# Load Library #
def clear():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "darwin" or platform == "darwin2":
        os.system('clear')
    elif platform == "win32" or platform == "win64":
        os.system('cls')


# Module Library #
import os
import colorama
from colorama import Fore, Back, Style
clear()
print("\033[1;35;40m RESET  \n")
clear()
print("\033[1;36;40m Loading modules  \n")
print("\033[1;36;40m Importing OS  \n")
print("\033[1;36;40m Importing time  \n")
import time
time.sleep(0.0)
import ctypes
time.sleep(0.4)
print("\033[1;36;40m Importing Requests  \n")
import requests
time.sleep(0.4)
print("\033[1;36;40m Importing sys  \n")
import sys
from sys import platform
time.sleep(0.4)
print("\033[1;36;40m Importing Discord  \n")
time.sleep(0.4)
print("\033[1;36;40m Importing String  \n")
import string
time.sleep(0.4)
print("\033[1;36;40m Importing Random  \n")
import random
print("\033[1;36;40m Importing Rest of modules  \n")
import webbrowser
import json
import discord
import urllib3
import threading
from threading import Thread
import subprocess
from subprocess import call
from subprocess import *
time.sleep(0.4)
print("\033[1;36;40m Modules Loaded...  \n")
time.sleep(1)
clear()
print("\033[1;36;40m Loading Definers...  \n")


# Definer #
def gen(): # Gen
    # Stage 1
    clear()
    codelen = 16
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    lp = int(input("How many 16 Character codes do you want to generate >> "))
    print("\033[1;32;40m Generating Codes (Press CTRL+C to end)  \n")
    k = open('16bytecodes.txt', 'w')
    for i in range(lp):
        k.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + '\n')
    k.close()
    # Stage 2
    clear()
    codelen = 4
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    lp = int(input("How many 4 Character codes do you want to generate >> "))
    print("\033[1;32;40m Generating Codes (Press CTRL+C to end)  \n")
    k = open('4bytecodes.txt', 'w')
    for i in range(lp):
        k.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + '\n')
    k.close()
    # Stage 3
    clear()
    codelen = 20
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    lp = int(input("How many 20 Character codes do you want to generate >> "))
    print("\033[1;32;40m Generating Codes (Press CTRL+C to end)  \n")
    k = open('20bytecodes.txt', 'w')
    for i in range(lp):
        k.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + '\n')
    k.close()
    boot()
def clearfile(): # Clear file
    clear()
    print("Deleting Files:")
    if os.path.exists("16bytecodes.txt"):
        os.remove("16bytecodes.txt")
        os.remove("4bytecodes.txt")
        os.remove("20bytecodes.txt")
        print("Cleared files")
    else:
        print("Codes are already cleared")
    time.sleep(1)
    input("press enter to continue")
    boot()

def chk(): # Check Codes #
    print("\033[1;35;40m Connecting to proxies \n")
    time.sleep(1)
    print("\033[1;35;40m Connected \n")
    print("checking nitro codes")
    threading.Thread(target=stage1).start()
    threading.Thread(target=stage2).start()
    threading.Thread(target=stage3).start()

#.old (  url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"  )

# Stage 1 #
def stage1():
    with open("16bytecodes.txt") as f:
        for line in f:
            nitro = line.strip("\n")
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            if r.status_code == 200:
                print("\033[1;31;40m Valid | {} \n".format(line.strip("\n")))
                break
            else:
                print("\033[1;31;40m Invalid | {} \n".format(line.strip("\n")))

# Stage 2 #
def stage2():
    with open("4bytecodes.txt") as f:
        for line in f:
            nitro = line.strip("\n")
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            if r.status_code == 200:
                print("\033[1;31;40m Valid | {} \n".format(line.strip("\n")))
                break
            else:
                print("\033[1;31;40m Invalid | {} \n".format(line.strip("\n")))

# Stage 3 #
def stage3():
    with open("20bytecodes.txt") as f:
        for line in f:
            nitro = line.strip("\n")
            url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            if r.status_code == 200:
                print("\033[1;31;40m Valid | {} \n".format(line.strip("\n")))
                break
            else:
                print("\033[1;31;40m Invalid | {} \n".format(line.strip("\n")))
                
def menu(): # Logo
    clear()
    if platform == "win32" or platform == "win64":
        ctypes.windll.user32.MessageBoxW(0, "Thank you for using NitroBoost!", "Enjoy!", 0)
    print("\033[1;36;40m  \n")
    print("""
   _______  ___________  _  _______________  ____ 
  / __/ _ \/ __/ __/ _ \/ |/ /  _/_  __/ _ \/ __ |
 _\ \/ ___/ _// _// // /    // /  / / / , _/ /_/ /
/___/_/  /___/___/____/_/|_/___/ /_/ /_/|_|\____/ 
Premium NitroGenerator
By : PackedUP32
Version 2.0
Mode - RELEASE (SOURCE)
    """)

def don():
    clear()
    print("Donation links & addresses are on main github")
    input("Press enter to continue")
    boot()

def system_check():
    if platform == "linux" or platform == "linux2":
        print("\033[1;33;40mOS=> Linux: Testing")
    elif platform == "darwin" or platform == "darwin2":
        print("\033[1;33;40mOS=> MacOS: Testing")
    elif platform == "win32" or platform == "win64":
        print("\033[1;32;40mOS=> Windows: Supported")

def options(): # Options
    print("\033[1;35;40m [1] Nitro Generator \n")
    print("\033[1;35;40m [2] Nitro Checker \n")
    print("\033[1;35;40m [3] Donate (Please donate so i can do more work like this) \n")
    print("\033[1;35;40m [4] Delete Codes \n")
    print("\033[1;35;40m [5] Updates & Changes \n")
    time.sleep(0.1)
    print("===================================")
    time.sleep(0.1)
    print("\033[1;36;40m System Information: ")
    system_check()
    print("Status > [ WORKING ]")
    print("")
    print("\033[1;35;40m Select your options \n")
    user_name = input("\033[1;33;40m >> \033[1;32;40m")
    if user_name == "1":
        gen()

    elif user_name == "2":
        chk()

    elif user_name == "3":
        don()

    elif user_name == "4":
        clearfile()

    elif user_name == "5":
        clear()
        f = open("update_log.txt")
        print(f.read())
        print("")
        print("")
        print("Press ENTER to go back.")
        input()
        boot()

def status():
    print("Status:")
    time.sleep(0.2)
    print("\033[1;32;40m ↳[ WORKING ] \n")
    time.sleep(0.2)
    print("\033[1;35;40m Searching for tokens \n")
    time.sleep(0.2)
    print("\033[1;32;40m ↳[ FOUND ] \n")
def boot():
    menu()
    options()
boot()
print("Press enter to continue")
