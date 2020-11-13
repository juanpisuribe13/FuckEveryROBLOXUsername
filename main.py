from random import randrange
import configparser
import tweepy
import requests, json
from time import sleep
from datetime import datetime

config = configparser.ConfigParser()
configFile = ('config.cfg')
config.read(configFile)

TimeToCount = int(config['Count']['Time'])
CurrentCount = int(config['Count']['CurrentCount'])
MaximumCount = int(config['Count']['MaximumCount'])
CurrentTry = int(config['Tries']['CurrentTry'])
MaximumTries = int(config['Tries']['MaximumTries'])
ID = randrange(1, 1000000000)

usernamesFileName = ("TweetedUsernames.txt")

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

def getTime():
    time = datetime.now()
    return time.strftime("%D %T")

print("%s - Logging in on Twitter..." % (getTime()))
API_KEY = config['Twitter API Keys']['API_KEY']
API_SECRET = config['Twitter API Keys']['API_SECRET']
TOKEN_ACCESS = config['Twitter API Keys']['TOKEN_ACCESS']
SECRET_TOKEN = config['Twitter API Keys']['SECRET_TOKEN']

twtAuth = tweepy.OAuthHandler(API_KEY, API_SECRET)
twtAuth.set_access_token(TOKEN_ACCESS, SECRET_TOKEN)
twtAPI = tweepy.API(twtAuth)
print(f"{bColors.okGreen}%s - Logged in!{bColors.ENDC}" % (getTime()))

def tweet(tweetContent):   
    twtAPI.update_status(tweetContent)

def getUsername(i):  
    getAPIrequest = requests.get("https://api.roblox.com/users/%i" % (i))
    try:
        user = getAPIrequest.json()['Username']
        return user
    except KeyError:
        return 'Invalid_ID'

def sumCount(c, a, b):
    c += 1
    config[a][b] = str(c)
    with open(configFile, 'w') as configfile:
        config.write(configfile)

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

print("%s Starting... now!" % (getTime()))

while CurrentCount < MaximumCount:
    ID = randrange(1, 1000000000)
    username = getUsername(ID)

    print("%s Checking if tweet can be sent..." % (getTime()))
    if username == 'Invalid_ID':
        print(f"{bColors.fail} %s - Invalid User ID (%i), will not be tweeted; continuing with the next one...{bColors.ENDC}" % (getTime(), ID))
        continue
    else:
        if isAlreadyTweeted(username):
            print(f"{bColors.warning}%s - Username (%s) already tweeted. Repeating...{bColors.ENDC}" % (getTime(), username))

    while CurrentTry < MaximumTries:
        try:
            tweet("fuck %s" % (username)) 
            sumCount(CurrentCount, 'Count', 'CurrentCount')
            CurrentCount = int(config['Count']['CurrentCount'])
            print(f"{bColors.okGreen}%s - Tweeted: Username = %s, ID = %i, Count = %i{bColors.ENDC}" % (getTime(), username, ID, CurrentCount))
            saveUsername(username)
        except tweepy.TweepError as TweepError:     
            TweepError = str(TweepError)
            if '187' in TweepError:
                break
            else:
                sumCount(CurrentTry, 'Tries', 'CurrentTry')
                CurrentTry = int(config['Tries']['CurrentTry'])
                print(f"{bColors.fail}%s - Could not tweet. Trying again in 15 minutes...{bColors.ENDC}" % (getTime()))
                print(f"{bColors.fail}%s{bColors.ENDC}" % (TweepError))
                sleep(60 * 15)
        if CurrentTry > MaximumCount or CurrentTry == MaximumCount:
            print(f"{bColors.fail}%s - Cannot tweet anymore. Switching off...{bColors.ENDC}" % (getTime))
            raise KeyboardInterrupt

    if CurrentCount < MaximumCount:
        sleep(TimeToCount)
    else:
        continue # just so it can leave the loop if it hasnt reached its maximum

print(f"{bColors.okGreen}%s - lol rip{bColors.ENDC}" % (getTime()))