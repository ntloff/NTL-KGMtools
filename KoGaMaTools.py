from kogama import Kogama
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore, Back, Style
import json
import re
import threading
import string
import random
import os
import pyfiglet
# +config
username = "153513agthawe"
password = "7aghgfaset"
server = "www"
# -config
k = Kogama.Kogama(server)
k.Auth().login(username=username, password=password)
os.system("cls")
os.system("pyfiglet ADV KoGaMa Spammer by ntloff")
sleep(2)
os.system("cls")
os.system("title ntloff: NTL-KGMspammer")
print(Fore.WHITE + "1) " + Fore.LIGHTMAGENTA_EX + "Game comment spammer;" + Fore.RESET)
print(Fore.WHITE + "2) " + Fore.LIGHTMAGENTA_EX + "Get all valid coupons;" + Fore.RESET)
choice = input(">>> ")
if(choice == "1"):
    os.system("cls")
    print("Enter game ID")
    gameid = input(Fore.LIGHTMAGENTA_EX + ">>> " + Fore.LIGHTYELLOW_EX)
    print("Enter message to spam")
    content = input(Fore.LIGHTMAGENTA_EX + ">>> " + Fore.LIGHTYELLOW_EX)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    k.Game().add_comment(gameid, content)
    os.system("cls")
if(choice == "2"):
    os.system("cls")
    print( Fore.LIGHTYELLOW_EX + "Activating Monkey code...")
    k.User().redeem_coupon("monkey")
    print( Fore.LIGHTYELLOW_EX + "Activating Fish code...")
    k.User().redeem_coupon("fish")
    print( Fore.LIGHTYELLOW_EX + "Activating Xmas2020 code...")
    k.User().redeem_coupon("Xmas2020")
    print( Fore.LIGHTYELLOW_EX + "Activating Michal code...")
    k.User().redeem_coupon("michal")
    print( Fore.LIGHTYELLOW_EX + "Activating Bonny code...")
    k.User().redeem_coupon("bonny")
    print( Fore.LIGHTYELLOW_EX + "Activating CreyCrey50 code...")
    k.User().redeem_coupon("creycrey50")
    input()