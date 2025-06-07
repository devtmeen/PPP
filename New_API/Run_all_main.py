import configparser
import json
import os
import subprocess
import sys
from pathlib import Path
from time import sleep

CONFIG_PATH = Path(__file__).resolve().parent / "config.ini"

config_default = configparser.ConfigParser()
config_default.read([CONFIG_PATH])
patch = Path(os.getenv("PATCH_DIR", config_default.get("Config", "patch")))
folder_list = json.loads(config_default.get("Config", "folder_list"))

# Base port used when calculating per-API ports
base_port = 8080

if __name__ == "__main__":
    for index, folder in enumerate(folder_list):
        # Compute a unique port number for this API
        port = base_port + index

        # Update the folder's config.ini with the computed port
        config_path = patch / folder / "config.ini"
        cfg = configparser.ConfigParser()
        cfg.read([config_path])
        if not cfg.has_section("Config"):
            cfg.add_section("Config")
        cfg.set("Config", "port", str(port))
        with open(config_path, "w") as config_file:
            cfg.write(config_file)

        # Launch the API using the current Python executable
        main_path = patch / folder / "main.py"
        print(f"Starting {main_path} on port {port}")
        subprocess.Popen([sys.executable, str(main_path)])
        sleep(0.5)
