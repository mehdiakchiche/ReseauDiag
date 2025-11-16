# ReseauDiag

import tkinter as tk
from tkinter import ttk, messagebox
import socket
import subprocess
import platform

# -----------------------------
# Fonction : Ping
# -----------------------------
def faire_ping(cible):
    systeme = platform.system().lower()
    commande = ["ping", "-n" if systeme == "windows" else "-c", "4", cible]

    try:
        resultat = subprocess.run(commande, capture_output=True, text=True)
        return resultat.stdout
    except:
        return "Erreur lors du ping."

# -----------------------------
# Fonction : Traceroute
# -----------------------------
def faire_traceroute(cible):
    systeme = platform.system().lower()
    commande = ["tracert" if systeme == "windows" else "traceroute", cible]

    try:
        resultat = subprocess.run(commande, capture_output=True, text=True)
        return resultat.stdout
    except:
        return "Erreur lors du traceroute."

# -----------------------------
# Fonction : Scan ports
# -----------------------------
def scan_ports(cible):
    ports_test = [21, 22, 80, 443]
    resultat = ""

    for port in ports_test:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        code = sock.connect_ex((cible, port))
        if code == 0:
            resultat += f"Port {port} : OUVERT\n"
        else:
            resultat += f"Port {port} : fermé\n"
        sock.close()

    return resultat

# -----------------------------
# Fonction : Infos locales
# -----------------------------
def infos_locales():
    try:
        nom_pc = socket.gethostname()
        ip_locale = socket.gethostbyname(nom_pc)
        return f"Nom de la machine : {nom_pc}\nAdresse IP locale : {ip_locale}"
    except:
        return "Impossible de récupérer les informations locales."

# -----------------------------
# Interface graphique
# -----------------------------
fenetre = tk.Tk()
fenetre.title("NetworkDiag - BTS CIEL")
fenetre.geometry("600x500")

onglets = ttk.Notebook(fenetre)
page_diag = ttk.Frame(onglets)
page_avance = ttk.Frame(onglets)
page_infos = ttk.Frame(onglets)

onglets.add(page_diag, text="Diagnostic rapide")
onglets.add(page_avance, text="Outils avancés")
onglets.add(page_infos, text="Infos PC")
onglets.pack(expand=True, fill="both")

# -----------------------------
# Page Diagnostic rapide
# -----------------------------
label_cible = ttk.Label(page_diag, text="Adresse ou domaine :")
label_cible.pack(pady=5)

entree_cible = ttk.Entry(page_diag, width=40)
entree_cible.pack(pady=5)

zone_resultat = tk.Text(page_diag, height=20)
zone_resultat.pack(pady=10)

# ---- Bouton exécuter ----
def lancer_diag():
    cible = entree_cible.get().strip()
    if not cible:
        messagebox.showerror("Erreur", "Veuillez entrer une cible.")
        return

    zone_resultat.delete("1.0", tk.END)
    zone_resultat.insert(tk.END, "--- Ping ---\n")
    zone_resultat.insert(tk.END, faire_ping(cible) + "\n")

    zone_resultat.insert(tk.END, "--- Scan de ports ---\n")
    zone_resultat.insert(tk.END, scan_ports(cible) + "\n")

bouton_diag = ttk.Button(page_diag, text="Lancer diagnostic", command=lancer_diag)
bouton_diag.pack(pady=5)

# -----------------------------
# Page Outils avancés
# -----------------------------
label_cible2 = ttk.Label(page_avance, text="Traceroute vers :")
label_cible2.pack(pady=5)

entree_trace = ttk.Entry(page_avance, width=40)
entree_trace.pack(pady=5)

zone_trace = tk.Text(page_avance, height=20)
zone_trace.pack(pady=10)

# ---- Bouton traceroute ----
def lancer_trace():
    cible = entree_trace.get().strip()
    if not cible:
        messagebox.showerror("Erreur", "Veuillez entrer une cible.")
        return

    zone_trace.delete("1.0", tk.END)
    zone_trace.insert(tk.END, faire_traceroute(cible))

bouton_trace = ttk.Button(page_avance, text="Lancer traceroute", command=lancer_trace)
bouton_trace.pack(pady=5)

# -----------------------------
# Page Infos PC
# -----------------------------
zone_infos = tk.Text(page_infos, height=20)
zone_infos.pack(pady=10)

zone_infos.insert(tk.END, infos_locales())

# -----------------------------
fenetre.mainloop()
