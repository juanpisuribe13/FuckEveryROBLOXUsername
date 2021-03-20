# FERUN (Fuck Every Roblox Username)

Archived this repository because I am moving away from Twitter for the sakes of my mental health. It was a fun ride.
Also to be fair I never liked this bot anyways because I found it childish so... yeah.

Tweets f--k alongside with a random ROBLOX username obtained from their API. Username is picked in eras; if the latest era is picked, it will pick an ID between 2016 and the latest ID registered which is obtained via the RecentRobloxUsers.py script (last ID is obtained every 24 hours to avoid sending a high amount of requests to ROBLOX).

## Before you begin...

- You need a Twitter Developer Account; apply for access [here](https://developer.twitter.com/en/apply-for-access).

- Python **3**;  NOT 2, **but 3**. If you're on Windows, I recommend you to get it [on Python's official website](https://www.python.org/downloads/) instead of downloading it on the Microsoft Store.

## Setup

**1.** Clone the repository via git clone

```git
git clone https://github.com/juanpisuribe13/FuckEveryROBLOXUsername.git
```

**2.** Add your Twitter API keys to the `config_barebones.cfg` file, then rename the file to `config.cfg`.

**3.** To avoid cluttering your Python installation, create a virtual environment by typing:
```bash
python3 -m venv env

# if above command opens windows store, try this one
python -m venv env
 ``` 

**3.1** After creating the virtual environment, access it.
```bash
# For UNIX users:
source env/bin/activate

# For Windows users:
.\env\Scripts\activate.bat
```

**4.** Install the required libraries found in the `requirements.txt` file.
```bash
pip install -r requirements.txt

# if above command doesn't work, try this
python3 -m pip install -r requirements.txt

## if above command STILL doesn't work because it 
## opened a windows store tab, try this one
python3 -m pip install -r requirements.txt
```

**5.** Done! To run the bot, do `python3 main.py`.

## FAQ

### Can I use your recent registered IDs/users script?
Yeah! You can, though you should **definitely use [this version](https://gist.github.com/juanpisuribe13/3972f188cbabed60c32e2b55c115397f)** instead of the one in the repository.

### What are the eras exactly and what's up with it?
The eras are 2004-2007, 2008-2009, 2010-2012, 2013-2015, and 2016-2021 (latest 2021 IDs are obtained via the RecentRobloxUsers.py script).

Eras are used for relevancy. Think about a bot that picks an username between the first ID and the last ID; sadly, it will only focus on the highest IDs. That's where the eras come in, giving both older and newer IDs a chance.

### Why not pick it in order?
Sounds good in paper, but it'll take millions of years to finish its goal.

## Contributing
If you have an idea for the bot (and know Python obviously) or feel like the code's off, feel free to send a Pull request!

## License
[MIT](https://raw.githubusercontent.com/juanpisuribe13/FuckEveryROBLOXUsername/main/LICENSE)

#

~~also i beg you to not look at the old readme.md file~~
