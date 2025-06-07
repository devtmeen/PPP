import configparser
import json
from time import sleep
import os
from subprocess import Popen, CREATE_NEW_CONSOLE

configDefault = configparser.ConfigParser()
configDefault.read(['config.ini'])
patch = configDefault.get("Config", "patch")
folder_list = json.loads(configDefault.get("Config", "folder_list"))

if __name__ == "__main__":
    for folder in folder_list:
        print(patch + folder + "/main.py")
        os.chdir(patch + folder)
        Popen(["python", patch + folder + "/main.py"], creationflags=CREATE_NEW_CONSOLE)
        #Popen(["python", patch + folder + "/main.py"])
        sleep(0.5)
