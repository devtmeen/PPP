import subprocess
def run_multiple_scripts():
    scripts = ["menu.py","ag.py","sa.py","ae.py","wm.py","bg.py","ab.py","xpg.py","wr.py","mt.py"]
    for script in scripts:
        subprocess.Popen(["python", script])

if __name__ == "__main__":
    run_multiple_scripts()