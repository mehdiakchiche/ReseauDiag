# NetworkDiag – Outil de diagnostic réseau (Projet BTS CIEL)

ReseauDiag est un outil simple de diagnostic réseau réalisé dans le cadre de mon BTS CIEL.  
Il permet d’effectuer rapidement les tests réseau les plus courants grâce à une interface graphique claire et accessible.

## Fonctionnalités

- **Ping** d’une adresse IP ou d’un domaine (4 paquets)
- **Scan rapide de ports** (21, 22, 80, 443)
- **Traceroute / Tracert** selon le système utilisé
- **Informations réseau locales**
  - Nom de la machine
  - Adresse IP locale

## Technologies utilisées
- **Python 3**
- Tkinter (interface graphique)
- Subprocess (ping / traceroute)
- Socket (scan de ports)

## Organisation du projet
Le projet est contenu dans un seul fichier Python afin de conserver un format simple et lisible.

## Comment exécuter le programme
1. Installer Python 3  
2. Lancer le script :
   ```bash
   python NetworkDiag.py
   ```

## Objectif pédagogique
Ce projet m’a permis de mettre en pratique :
- La manipulation de commandes réseau
- L’usage d’interfaces graphiques en Python
- La communication via sockets
- La structuration d’un petit outil fonctionnel et utile

## Améliorations possibles
- Scan de ports avancé
- Test de débit
- Sauvegarde d’historique

---

Merci d’avoir consulté ce projet !
