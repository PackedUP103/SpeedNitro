# Module Library #
print("\033[1;35;40m Loading modules  \n")
print("\033[1;36;40m Importing time  \n")
import time
time.sleep(0.0)
print("\033[1;36;40m Importing OS  \n")
import os
import ctypes
time.sleep(0.4)
print("\033[1;36;40m Importing Requests  \n")
import requests
time.sleep(0.4)
print("\033[1;36;40m Importing sys  \n")
import sys
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
import colorama
from colorama import Fore, Back, Style
import subprocess
from subprocess import call
from subprocess import *
time.sleep(0.4)
print("\033[1;36;40m Modules Loaded...  \n")
time.sleep(1)
os.system("cls")
print("\033[1;36;40m Loading Definers...  \n")

# Definer #
def gen(): # Gen
    # Stage 1
    os.system("cls")
    print("generating 16Byte nitro codes")
    codelen = 16
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    print("How many 16byte codes to generate (To not max out CPU/RAM Usage")
    print("This program will need to generate 16 byte codes, 4 byte codes , 20 byte codes")
    print("This is to make sure you are getting a higher ammount of getting a code then chancing it on 16 letters")
    lp = int(input(""))
    print("\033[1;32;40m Generating Codes (Press CTRL+C to end)  \n")
    k = open('16bytecodes.txt', 'w')
    for i in range(lp):
        k.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + '\n')
    k.close()
    # Stage 2
    os.system("cls")
    codelen = 4
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    print("generating 4Byte nitro codes")
    print("How many 4byte codes to generate (To not max out CPU/RAM Usage")
    lp = int(input(""))
    print("\033[1;32;40m Generating Codes (Press CTRL+C to end)  \n")
    k = open('4bytecodes.txt', 'w')
    for i in range(lp):
        k.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + '\n')
    k.close()
    print("generating 20Byte nitro codes")
    # Stage 3
    os.system("cls")
    codelen = 20
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    print("How many 20byte codes to generate (To not max out CPU/RAM Usage")
    lp = int(input(""))
    print("\033[1;32;40m Generating Codes (Press CTRL+C to end)  \n")
    k = open('20bytecodes.txt', 'w')
    for i in range(lp):
        k.write("discord.gift/" + ''.join(random.choice(letters) for i in range(codelen)) + '\n')
    k.close()
    boot()

def clearfile(): # Clear file
    os.system("cls")
    print("clearing file")
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
    # Run check 1 #
def stage1():
    with open("16bytecodes.txt") as f:
        for line in f:
            nitro = line.strip("\n")
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
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
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
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
            url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"
            r = requests.get(url)
            if r.status_code == 200:
                print("\033[1;31;40m Valid | {} \n".format(line.strip("\n")))
                break
            else:
                print("\033[1;31;40m Invalid | {} \n".format(line.strip("\n")))            
def menu(): # Logo
    os.system("cls")
    ctypes.windll.user32.MessageBoxW(0, "Thank you for using NitroBoost!", "Enjoy!", 0)
    print("\033[1;36;40m  \n")
    print("""
   _______  ___________  _  _______________  ____ 
  / __/ _ \/ __/ __/ _ \/ |/ /  _/_  __/ _ \/ __ |
 _\ \/ ___/ _// _// // /    // /  / / / , _/ /_/ /
/___/_/  /___/___/____/_/|_/___/ /_/ /_/|_|\____/ 
Premium NitroGenerator
By : PackedUP32
Version 1.5
Mode - RELEASE (SOURCE)
    """)

def don():
    os.system("cls")
    print("Buy me a coffee?")
    print("Bitcoin = bc1qj4q6352ypmusyghyyp68q02l8hxvhvnyjnj39j")
    print("Bitcoin Cash = bitcoincash:qq0344acxvjl9xy0vlftl38awjmg3mhz5qcwsgfsd5")
    print("Xrdp = rBSPTqYrsSkjCwk8AUfpa3eVYczX4GDGmN")
    print("Dodge Coin = DDZBYK8JdTA2umQnmpSH7n89pfqujdfXg1")
    print("Ethereum = 0xE343279109A1Bf25f1A888E5B45c55EeD7245174")
    print("Thank you")
    input("Press enter to continue")
    boot()

def options(): # Options
    print("\033[1;35;40m [1] Nitro Generator \n")
    print("\033[1;35;40m [2] Nitro Checker \n")
    print("\033[1;35;40m [3] Donate (Please donate so i can do more work like this) \n")
    print("\033[1;35;40m [4] Clear codes.txt file \n")
    print("\033[1;35;40m [5] Help Document \n")
    time.sleep(1)
    print("===================================")
    time.sleep(0.1)
    print("Status > [ WORKING ]")
    time.sleep(0.1)
    print("\033[1;35;40m Searching for proxies > [ FOUND ] \n")
    time.sleep(0.2)
    print("\033[1;35;40m Select your options \n")
    user_name = input()
    if user_name == "1":
        gen()

    elif user_name == "2":
        chk()

    elif user_name == "3":
        don()

    elif user_name == "4":
        clearfile()

    elif user_name == "5":
        os.system("cls")
        with open("20bytecodes.txt") as f:
            lines = f.readlines()
        input()
        menu()
        options()

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