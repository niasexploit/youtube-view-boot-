## Uthor @hidayatacode.com
import webbrowser
import time 
import os 

banner = """
██╗   ██╗ ██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗██╗   ██╗██╗███████╗██╗    ██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝██║   ██║██║██╔════╝██║    ██║
 ╚████╔╝ ██║   ██║██║   ██║   ██║   ██║   ██║██████╔╝█████╗  ██║   ██║██║█████╗  ██║ █╗ ██║
  ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║
   ██║   ╚██████╔╝╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗ ╚████╔╝ ██║███████╗╚███╔███╔╝
   ╚═╝    ╚═════╝  ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝                                                                              
     
     Github : github.com/hidayat-code
     Blog : www.hidayatcode.com
"""
print(banner)

 
url = input("Enter the youtube URL:")
refresh = input("Enter the refresh time in seconds:")
count = input("How many views do you want? ")
 
def openURL():
    webbrowser.open(url)
    time.sleep(int(refresh))
    
    for i in range(int(count)):
        print("Webpage has been viewed")
        openURL()
 
openURL()
