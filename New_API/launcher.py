import subprocess
import sys
from pathlib import Path

API_DIR = Path(__file__).resolve().parent


def run_script(name: str) -> None:
    subprocess.Popen([sys.executable, str(API_DIR / name)])


if __name__ == "__main__":
    run_script("Update_BonusTime.py")
    run_script("Update_BonusTime_Baccarat.py")
    run_script("Run_all_main.py")
