# -*- coding: utf-8 -*-
import os
import sys
import time
import random
import string
from multiprocessing import Pool, cpu_count, Manager

# =========================
# 🎨 ANSI COLORS CYBER UI
# =========================
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
M = "\033[95m"
C = "\033[96m"
W = "\033[0m"
BL = "\033[1m"

# =========================
# 💀 CYBER BANNER
# =========================
def banner():
    os.system("clear")
    print(R + BL + r"""
███╗   ███╗ █████╗ ███╗   ██╗██╗   ██╗███████╗██╗      █████╗ 
████╗ ████║██╔══██╗████╗  ██║██║   ██║██╔════╝██║     ██╔══██╗
██╔████╔██║███████║██╔██╗ ██║██║   ██║█████╗  ██║     ███████║
██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║     ██╔══██║
██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
        CYBER OS PRO UI EDITION - QPYTHON3
""" + W)

# =========================
# 📂 INPUT FILE USERS
# =========================
def load_users(path):
    users = []
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if line:
                users.append(line)
    return users

# =========================
# 🔐 PASSWORD MODES
# =========================
def gen_random():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(random.randint(6,10)))

def gen_pattern():
    # A1b2C3 style
    out = []
    for i in range(3):
        out.append(random.choice(string.ascii_uppercase))
        out.append(str(random.randint(0,9)))
    return ''.join(out)

def gen_dictionary(user):
    base = user.split("@")[0] if "@" in user else user
    words = ["admin", "123", "2024", "pro", "vip", "x", "hack", "sys"]
    return base + random.choice(words)

def gen_hybrid(user):
    return user.split("@")[0] + "_" + gen_pattern() + str(random.randint(10,99))

# =========================
# ⚙️ PROCESSOR
# =========================
def process_line(data):
    index, user, mode = data

    if mode == "1":
        pwd = gen_random()
    elif mode == "2":
        pwd = gen_pattern()
    elif mode == "3":
        pwd = gen_dictionary(user)
    else:
        pwd = gen_hybrid(user)

    return index, f"{user}:{pwd}"

# =========================
# 📊 DASHBOARD
# =========================
def dashboard(done, total):
    percent = int((done / total) * 100)
    bar = "█" * (percent // 5) + "-" * (20 - percent // 5)
    sys.stdout.write(f"\r{C}[{bar}] {percent}% | {done}/{total} combos")
    sys.stdout.flush()

# =========================
# 💾 SAVE OUTPUT
# =========================
def save_output(data, filename):
    folder = "/sdcard/Combo/"
    if not os.path.exists(folder):
        os.makedirs(folder)

    path = folder + filename

    with open(path, "w", encoding="utf-8") as f:
        for item in sorted(data, key=lambda x: x[0]):
            f.write(item[1] + "\n")

    return path

# =========================
# 🚀 MAIN ENGINE
# =========================
def main():
    banner()

    print(G + "[1] RANDOM MODE")
    print(Y + "[2] PATTERN A1b2C3")
    print(C + "[3] DICTIONARY MODE")
    print(M + "[4] HYBRID PRO MODE" + W)

    mode = input("\n➤ Selecciona modo: ")

    path = input("\n📂 Ruta archivo usuarios: ")
    output_name = input("💾 Nombre archivo salida (.txt): ")

    users = load_users(path)
    total = len(users)

    print(G + f"\n⚡ Usuarios cargados: {total}" + W)
    print(B + f"🧠 CPU CORES: {cpu_count()}" + W)
    print(Y + "🚀 Iniciando procesamiento...\n" + W)

    pool = Pool(cpu_count())

    tasks = [(i, users[i], mode) for i in range(total)]

    results = []
    done = 0

    for res in pool.imap(process_line, tasks):
        results.append(res)
        done += 1
        dashboard(done, total)

    pool.close()
    pool.join()

    print("\n\n💾 Guardando archivo...")
    path_out = save_output(results, output_name)

    print(G + f"\n✔ COMPLETADO: {path_out}" + W)
    print(R + "💀 MANUELA CYBER OS TERMINADO 💀" + W)

# =========================
# ▶️ RUN
# =========================
if __name__ == "__main__":
    main()