import subprocess
def run_multiple_scripts():
    scripts = ["ambs.py","cq9.py","evo.py","fkg.py","hbe.py","rtg.py","smp.py","sxo.py","ygg.py"]
    for script in scripts:
        subprocess.Popen(["python", script])

if __name__ == "__main__":
    run_multiple_scripts()