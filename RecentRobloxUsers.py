import subprocess, sys
import configparser
import requests, time, math
from time import sleep

config = configparser.ConfigParser()
configFile = ('config.cfg')
config.read(configFile)

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

x = 0
for i in range(30, 0, -1):
    n = x + pow(2, i)
    if apiRequest(n) or apiRequest(n+1) or apiRequest(n+2):
        x = int(n)

timeout = 0
newest = None
while True:
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
    print("New ID: %i" % (x))
    sleep(60 * 1440)