import configparser
import json
from time import sleep
from subprocess import Popen
import sys
from pathlib import Path

configDefault = configparser.ConfigParser()
configDefault.read(["config.ini"])
patch = configDefault.get("Config", "patch")
folder_list = json.loads(configDefault.get("Config", "folder_list"))

base_port = 8080

if __name__ == "__main__":
    for index, folder in enumerate(folder_list):
        folder_path = Path(patch) / folder
        port = base_port + index

        config_path = folder_path / "config.ini"
        config = configparser.ConfigParser()
        config.read(config_path)
        if not config.has_section("Config"):
            config.add_section("Config")
        config.set("Config", "port", str(port))
        with open(config_path, "w") as f:
            config.write(f)

        print(folder_path / "main.py")
        Popen([sys.executable, str(folder_path / "main.py")])
        sleep(0.5)
