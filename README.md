# DiscoBot

A simple plugin-based bot for Discord using [discord.py](https://github.com/Rapptz/discord.py). https://discordapp.com/

## Features
--------
- Plugin system
- It says `AYYLMAO` when you type `!sup` in a discord channel

## Plugins
-------

Plugins are added in the file `disco/plugins/__init__.py` like this:

We want to add our plugin with classname `HelloWorld` in file `helloworld.py` as a plugin:

```
[...]

# Custom plugins
from .helloworld import HelloWorld

```

A template plugin can be found in `dicso/plugins/template.py`

An example plugin can be found in `dicso/plugins/helloworld.py` and `dicso/plugins/greetings.py`

Configure
---------

First set an environment variable containing the login credentials for the bot as such

#### Linux/Unix
```
export DISCOBOT_EMAIL=<email>
export DISCOBOT_PASS=<passwd>
```

#### Windows

In the windows environment variable editor:
- add two variables `DISCOBOT_EMAIL` and `DISCOBOT_PASS`
- give them the appropriate values

**If you are on windows, make sure to run the program as admin**, or else python
can't retrieve the variable.

---

If you want to use the `meme.py` plugin you will also have to fill in the these variables.
```
IMGFLIP_USER=<imgflip_username>
IMGFLIP_PASS=<imgflip_password>
```

## Installation

##### Option one (recommended)
If you have `pip` and `git` installed and working, it's pretty straight forward.

```
pip install git+https://github.com/Syntox32/DiscoBot
```

##### Option two

Download the project in some way (.zip or git), `cd` to the directory and run.

```
python setup.py install
```
---

You can now run the script by typing this in the console of your choice.
```
disco.py
```

Development
-----------
Make sure you have `Python 2.7.x` installed.

Run `pip install -r requirements.txt` in the top-directory.

Start the bot with `python main.py`

Requirements
------------
The project requires *Python 2.7.x* to be installed

You will also have intall [discord.py](https://github.com/Rapptz/discord.py) by Rapptz. This can be done by doing `pip install discord.py`

License
-------
The whole project is licensed under an MIT license.
