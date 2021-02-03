from random import randrange, uniform, choice
from time import sleep
from datetime import datetime
import sys, configparser
import tweepy, requests, ferunDB

# Config file setup
config = configparser.ConfigParser()
configFile = ('config.cfg')
config.read(configFile)

# Key variables setup
TimeToCount = int(config['Count']['Time'])
CurrentTry = int(config['Tries']['CurrentTry'])
MaximumTries = int(config['Tries']['MaximumTries'])
LastID = int(config['IDs']['LastID'])

## ---------- Misc ---------- ##

class c:
    success = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    olors = '\033[0m'

def getTime():
    now = datetime.now()
    return now.strftime("%d/%m/%y %H:%M:%S")

def sumCount(c, a, b):
    c += 1
    config[a][b] = str(c)
    with open(configFile, 'w') as configfile:
        config.write(configfile)
    # Sums the current tries if an error occurrs.

def resetCount(a, b):
    c = 1
    config[a][b] = str(c)
    with open(configFile, 'w') as configfile:
        config.write(configfile)
    # Resets the tries if no error is found

## ---------- Misc ---------- ##

def tweet(tweetContent):   
    twtAPI.update_status(status = tweetContent)

def getUsername(i):  
    getAPIrequest = requests.get("https://api.roblox.com/users/%i" % (i)).json()
    try:
        user = getAPIrequest['Username']
        return user
    except KeyError:
        return 'Invalid_ID'

def resetLastID():
    config['IDs']['LastID'] = str(1390874933)
    with open(configFile, 'w') as configfile:
        config.write(configfile)

def getID():
    config.read(configFile)
    LastID = int(config['IDs']['LastID'])
    if LastID < 1390874933:
        resetLastID()
        config.read(configFile) 
        # resets the last id to the default one if the default one is changed in config.cfg to a lower one

    era = ['2004-2007', '2008-2009', '2010-2012', '2013-2015', '2016-2020'] # Eras
    eraLen = randrange(len(era)) # Picks era
    ID = [[1, 141923], [141924, 5881980], [5881981, 36349001], [36349002, 103536228], [103536229, LastID]] # IDs per Era
    ID = ID[eraLen] # Picks Era with ID
    return [randrange(ID[0], ID[1]), era[eraLen]]
    # ID[0] = randomly picked ID

if ferunDB.AlreadyExists:
    print(f"{c.warning}Database already exists, moving on...{c.olors}")
else:
    print(f"{c.warning}Username Database does not exist{c.olors}; {c.success}database has been created{c.olors}")
# Checks if the tweeted usernames file already exists

print("%s - Authenticating..." % (getTime()))
API_KEY, API_SECRET = config['Twitter API Keys']['API_KEY'], config['Twitter API Keys']['API_SECRET']
TOKEN_ACCESS, SECRET_TOKEN = config['Twitter API Keys']['TOKEN_ACCESS'], config['Twitter API Keys']['SECRET_TOKEN']

twtAuth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twtAuth.set_access_token(TOKEN_ACCESS, SECRET_TOKEN)
twtAPI = tweepy.API(twtAuth)

if twtAPI.verify_credentials():
    print(f"{c.success}%s - Authentication successful!{c.olors}" % (getTime()))
else:
    print(f"{c.fail}%s - Couldn't authenticate. Please check your keys and try again.{c.olors}" % (getTime()))
    sys.exit()

print("%s - Starting... now!" % (getTime()))

while True:
    while True:
        try:
            ID = getID()
            username = getUsername(ID[0])
            break
        except ValueError: # JSONDecodeError belongs to ValueError
            print(f"{c.fail}%s - Error in decoding username; trying again...{c.olors}" % (getTime()))
        
        # ID[0] = generated id; ID[1] = id's era

    if username == 'Invalid_ID': # checks if username is invalid
        print(f"{c.fail}%s - Invalid User ID (%i); will not be tweeted. continuing with the next ID...{c.olors}" % (getTime(), ID[0]))
        continue
    else:
        if ferunDB.isAlreadyTweeted(username):
            print(f"{c.warning}%s - Username (%s) already tweeted. Repeating...{c.olors}" % (getTime(), username))
            continue

    while True:
        try:
            tweet("fuck %s (ID: %i; era = %s)" % (username, ID[0], ID[1])) 
            print(f"{c.success}%s - Tweeted: Username = %s, ID = %i, Count = %i, Era = %s{c.olors}" % (getTime(), username, ID[0], ferunDB.getLastCount(), ID[1]))
            resetCount('Tries', 'CurrentTry') # resets the tries count to avoid problems
            ferunDB.createRow(username, ID[0])
            break
        except tweepy.TweepError as TweepError:    
            if CurrentTry > MaximumTries or CurrentTry == MaximumTries:
                print(f"{c.fail}%s - Cannot tweet anymore. Trying again in 15 minutes{c.olors}" % (getTime()))
                sleep(60 * 15) 
                break
            else:
                sumCount(CurrentTry, 'Tries', 'CurrentTry')
                CurrentTry = int(config['Tries']['CurrentTry'])
                print(f"{c.fail}%s - Could not tweet. Trying again...{c.olors}" % (getTime()))
                print(f"{c.fail}%s{c.olors}" % (TweepError))

    sleep(TimeToCount)

print(f"{c.success}%s - lol rip{c.olors}" % (getTime()))