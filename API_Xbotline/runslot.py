import subprocess
def run_multiple_scripts():
    scripts = ["main.py","menu.py","pp.py","pg.py","nl.py","ne.py","mc.py","jl.py","jk.py","amb.py"]
    for script in scripts:
        subprocess.Popen(["python", script])

if __name__ == "__main__":
    run_multiple_scripts()