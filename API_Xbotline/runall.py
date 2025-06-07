import subprocess

def run_multiple_scripts():
    scripts = ["menu.py","menulotto.py","pp.py","ambg.py","amp.py","kagm.py","k9.py","ns.py","spg.py","ry.py","dgg.py","hk.py","op.py","go.py","r88.py","pg.py","nl.py","ne.py","mc.py","jl.py","jk.py","amb.py","ambs.py","cq9.py","evo.py","fkg.py","hbe.py","rtg.py","smp.py","sxo.py","ygg.py","ag.py","sa.py","ae.py","wm.py","bg.py","ab.py","xpg.py","wr.py","mt.py","sn.py","main.py"]
    for script in scripts:
        subprocess.Popen(["python", script])

if __name__ == "__main__":
    run_multiple_scripts()