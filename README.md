# Fuck Every ROBLOX Username
Python script where it tweets every minute fuck along with a random ROBLOX username between the IDs 10.000.000-1.000.000.000 obtained from ROBLOX's API for 2.000.160 times.
Started in November 14th, 2020 and ends in September 3rd, 2024.
 
## To set it up:
Before setting it up, you will need to have a Twitter Developer account. You can do it via https://developer.twitter.com/. If you plan to host the bot on a Twitter account that isn't yours, I'd recommend you to apply for a Developer account IN your main account, later in the guide I'll explain how to set up the bot in another account. 

Even if Python 2 is already depracated, you need to install Python 3. I'd recommend you to use the Python 3 version from https://www.python.org/ instead of the Windows Store one.

Also if you're an EXPERIENCED user, feel free to do it your way. This is the first time I'm documenting something like this so if you think something is wrongfully documentated, feel free to send a pull request!

**1.** Download the latest release by cloning it from Git, or just pressing the green button and clicking on Download ZIP; then extract it in a folder of your choice.

**2.** Open up a terminal, go to the folder where you extracted it in, then create a virtual environment in the same folder by typing in `python3 -m venv feru_env`; if you want to, you can change feru_env to the name of your choice.

**3.** Activate the virtual environment by typing in: `source feru_env/bin/activate`, or if you're using Windows: `feru_env/Scripts/activate.bat`. If your virtual environment's name isn't feru_env, change it to the name you put it in while typing the command. Remember to activate this IN the same folder where you extracted the latest release AND where you created the virtual environment.

**4.** To install the required modules, type in: `python3 -m pip install -r requirements.txt`
If it gives you an error saying that Python wasn't found, replace "python3" with "python". If it gives you an error saying 'pip' wasn't found, you may want to reinstall pip.

**5.** Before executing the Python script, you need to put your Twitter API keys on it. To do so, open config_barebones.cfg, and put in your API keys. (Note: if you're going to host the bot on another Twitter account, leave the token_access and secret_token in blank and skip to the next section.). Feel free to tweak the configuration file to your likings. When you're done, change the file name to config.cfg.

**6.** You can now host the bot! To do it, run python3 main.py.

### For users who want to host the bot in another Twitter Account:
Before doing this I'd like to say that from my experience: **if you're doing this on Windows Subsystem for Linux, you should do this in Windows instead of WSL. I did this in WSL and it didn't release the .twurlrc file for some reason. I probably did something wrong but still, I'd recommend you to do it in Windows instead of WSL.**

**1.** Install Ruby: https://www.ruby-lang.org/

**2.** After installing it, open your terminal and type `gem install twurl`

**3.** When the installation is finished, type in `twurl authorize --consumer-key [API_KEY] --consumer-secret [API_SECRET]` (this is logical but replace api_key and api_secret with your twitter application's api key and api key secret). After that, follow the on-screen instructions.

**4.** After authenticating, a file called `.twurlrc` will appear; open it. Pay attention to both 'token' and 'secret' keys. Open the config.cfg file that you edited earlier, fill in respectively the 'token' code in 'token_access', and 'secret' code in 'secret_token'. (I know this is logical but some people may don't know about this so I had to mention this.)

**5.** You can now host the bot! To do it, run python3 main.py.

## FAQ

#### Why 2 million usernames and why tweet it every 60 seconds?
If i did it every 15 minutes, I would only have 100k users in 3/4 years. My goal is to do it with a high quantity of usernames possible that will finish in 3/4 years.

#### Why did you do this?
i was bored

#### your code is horrible lol
If you think it is feel free to send a pull request then, I'll see if I'll accept it.
