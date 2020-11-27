import subprocess, sys
import configparser
import requests, time, math
from time import sleep
from datetime import datetime

config = configparser.ConfigParser()
configFile = ('config.cfg')
config.read(configFile)

def getTime():
    now = datetime.now()
    return now.strftime("%d/%m/%y %H:%M:%S")

def sumLastID(c):
     config['IDs']['LastID'] = str(c)
     with open(configFile, 'w') as configfile:
        config.write(configfile)

def apiRequest(i):  
    y = r = requests.get("https://api.roblox.com/users/%i" % (i))
    if '404' in y and r:
        None
    if y:
        return r

def getUsername(i):
    getAPIrequest = requests.get("https://api.roblox.com/users/%i" % (i)).json()
    try:
        user = getAPIrequest['Username']
        return user
    except KeyError:
        return 'Invalid_ID'


def getLastID():
    x = 0
    for i in range(30, 0, -1):
        n = x + pow(2, i)
        if apiRequest(n) or apiRequest(n+1) or apiRequest(n+2):
            x = int(n)

    timeout = 0

    while True:
            found = False
            for i in range(0, math.floor(timeout/10)):
                q = apiRequest(x + i)
                if q:
                    for j in range (0, i-1):
                        Q = apiRequest(x + j)
                        if Q:
                            q = Q
                            break
                    found = True
                    break
            if found: 
                break
            timeout += 1
    
    timeout = 0
    x += 1

    sumLastID(x)
    print("%s - New ID: %i" % (getTime(), x))

while True:
    getLastID()
    sleep(60 * 1440)