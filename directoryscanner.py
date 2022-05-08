"""
       .---.
      /     \
      \.@-@./
      /`\_/`\
     //  _  \\
    | \     )|_
   /`\_`>  <_/ \
gsp\__/'---'\__/

"""
import requests
from colorama import Fore, Back, Style

print(Fore.BLUE+"Website Directory Scanner")
print("Enter the url \nPlease use HTTPS or HTTP")
url = input("> "+Fore.GREEN+"")

wordlist = open('wordlist.txt')

directory = wordlist.readlines()

for directory in directory:
    
    dir = directory

    response = requests.get(url+dir)

    if response.status_code != 404:
        print(Fore.GREEN+"\n+ "  + str(url+dir)+"\nstatus code: "+str(response.status_code))