from random import randrange, uniform, choice
from time import sleep
from datetime import datetime
import configparser
import tweepy, requests

# Config file setup
config = configparser.ConfigParser()
configFile = ('config.cfg')
config.read(configFile)

# Key variables setup
TimeToCount = int(config['Count']['Time'])
CurrentCount = int(config['Count']['CurrentCount'])
CurrentTry = int(config['Tries']['CurrentTry'])
MaximumTries = int(config['Tries']['MaximumTries'])
LastID = int(config['IDs']['LastID'])
usernamesFileName = ("TweetedUsernames.txt")

# Misc
def getTime():
    now = datetime.now()
    return now.strftime("%d/%m/%y %H:%M:%S")

def tweet(tweetContent):   
    twtAPI.update_status(status = tweetContent)

def getUsername(i):  
    getAPIrequest = requests.get("https://api.roblox.com/users/%i" % (i)).json()
    try:
        user = getAPIrequest['Username']
        return user
    except KeyError:
        return 'Invalid_ID'

def sumCount(c, a, b):
    c += 1
    config[a][b] = str(c)
    with open(configFile, 'w') as configfile:
        config.write(configfile)
    # Used to sum the current tries if an error occurrs.

def resetCount(a, b):
    c = 1
    config[a][b] = str(c)
    with open(configFile, 'w') as configfile:
        config.write(configfile)
    # Used to reset the tries if no error is found

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

    a = ['2004-2007', '2008-2009', '2010-2012', '2013-2015', '2016-2020']
    e = randrange(len(a))
    b = [[1, 141923], [141924, 5881980], [5881981, 36349001], [36349002, 103536228], [103536229, LastID]]
    b = b[e]
    return [randrange(b[0], b[1]), a[e]]

def saveUsername(username):
    usernamesFile = open(usernamesFileName, "a")
    usernamesFile.write("%s\n" % (username))
    usernamesFile.close()

def isAlreadyTweeted(username):
    usernamesFile = open(usernamesFileName, "r")
    usernamesArray = usernamesFile.read()
    usernamesFile.close()
    usernamesArray = usernamesArray.split("\n")
    if username in usernamesArray:
        return True
    else:
        return False

class bColors:
    okGreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    ENDC = '\033[0m'

try:
    usernamesFile = open(usernamesFileName, "x")
    print(f"{bColors.warning}Username File does not exist{bColors.ENDC}; {bColors.okGreen}file has been created{bColors.ENDC}")
    usernamesFile.close()
except FileExistsError:
    print(f"{bColors.warning}Usernames File already exists, moving on{bColors.ENDC}")
# Checks if the tweeted usernames file already exists

print("%s - Logging in on Twitter..." % (getTime()))
API_KEY = config['Twitter API Keys']['API_KEY']
API_SECRET = config['Twitter API Keys']['API_SECRET']
TOKEN_ACCESS = config['Twitter API Keys']['TOKEN_ACCESS']
SECRET_TOKEN = config['Twitter API Keys']['SECRET_TOKEN']
twtAuth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twtAuth.set_access_token(TOKEN_ACCESS, SECRET_TOKEN)
twtAPI = tweepy.API(twtAuth)
print(f"{bColors.okGreen}%s - Logged in!{bColors.ENDC}" % (getTime()))

print("%s - Starting... now!" % (getTime()))

while True:
    ID = getID()
    username = getUsername(ID[0])
    # ID[0] = generated id; ID[1] = id's era

    if username == 'Invalid_ID': # checks if username is invalid
        print(f"{bColors.fail} %s - Invalid User ID (%i), will not be tweeted; continuing with the next one...{bColors.ENDC}" % (getTime(), ID[0]))
        continue
    else:
        if isAlreadyTweeted(username):
            print(f"{bColors.warning}%s - Username (%s) already tweeted. Repeating...{bColors.ENDC}" % (getTime(), username))

    while True:
        try:
            tweet("fuck %s (ID: %i)" % (username, ID[0])) 
            CurrentCount = int(config['Count']['CurrentCount'])
            print(f"{bColors.okGreen}%s - Tweeted: Username = %s, ID = %i, Count = %i, Era = %s{bColors.ENDC}" % (getTime(), username, ID[0], CurrentCount, ID[1]))
            resetCount('Tries', 'CurrentTry') # resets the tries count to avoid problems
            saveUsername(username)
            break
        except tweepy.TweepError as TweepError:    
            if CurrentTry > MaximumTries or CurrentTry == MaximumTries:
                print(f"{bColors.fail}%s - Cannot tweet anymore. Trying again in 15 minutes{bColors.ENDC}" % (getTime))
                sleep(60 * 15) 
                break
            else:
                sumCount(CurrentTry, 'Tries', 'CurrentTry')
                CurrentTry = int(config['Tries']['CurrentTry'])
                print(f"{bColors.fail}%s - Could not tweet. Trying again...{bColors.ENDC}" % (getTime()))
                print(f"{bColors.fail}%s{bColors.ENDC}" % (TweepError))

    sleep(TimeToCount)

print(f"{bColors.okGreen}%s - lol rip{bColors.ENDC}" % (getTime()))