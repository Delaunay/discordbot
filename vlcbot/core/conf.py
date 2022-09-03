import os
import json
import importlib_resources
import pkgutil
import importlib

from appdirs import user_config_dir

NAME = "vlcbot"
AUTHOR = "vlcbot"
CONFIG = user_config_dir(NAME, AUTHOR)

CONFIGNAME = "config.json"
LATEST_CONF = None


def load_conf():
    """Loads the configuration from the config file"""
    # pylint: disable=global-statement
    global LATEST_CONF

    config = os.path.join(CONFIG, CONFIGNAME)
    os.makedirs(CONFIG, exist_ok=True)

    if not os.path.exists(config):
        return {}

    with open(config, "r", encoding="utf-8") as conffile:
        conf = json.load(conffile)

    LATEST_CONF = conf
    return conf


def save_conf(conf):
    """Saves the given configuration to the config file"""
    config = os.path.join(CONFIG, CONFIGNAME)
    os.makedirs(CONFIG, exist_ok=True)

    with open(config, "w", encoding="utf-8") as conffile:
        json.dump(conf, conffile)


def ffmpeg():
    path = importlib_resources.files('vlcbot.binaries.ffmpeg.win64')
    return str(path / 'bin' / 'ffmpeg.exe')


def discover_plugins(module):
    """Discover plugins"""
    path = module.__path__
    name = module.__name__

    plugins = {}

    for _, name, _ in pkgutil.iter_modules(path, name + "."):
        plugins[name] = importlib.import_module(name)
        print(f" - Found plugin: {name}")

    return plugins


# # PERMISSIONS = 3145728

# client_id = 1015663761169850418
# scope = 'bot'
# permissions = 3145728
# guild_id = 256839590764085250
# disable_guild_select = False


# # https://discord.com/oauth2/authorize?client_id=1015663761169850418&scope=bot&permissions=3145728