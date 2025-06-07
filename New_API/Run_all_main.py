import configparser
import json
import subprocess
import sys
from pathlib import Path
from time import sleep

CONFIG_PATH = Path(__file__).resolve().parent / "config.ini"

config_default = configparser.ConfigParser()
config_default.read([CONFIG_PATH])
patch = Path(config_default.get("Config", "patch"))
folder_list = json.loads(config_default.get("Config", "folder_list"))

if __name__ == "__main__":
    for folder in folder_list:
        main_path = patch / folder / "main.py"
        print(main_path)
        subprocess.Popen([sys.executable, str(main_path)])
        sleep(0.5)
