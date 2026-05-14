from collections import deque

#CLASSE PROCESSUS
class Processus:
    def __init__(self, pid, arrivee, burst):
        self.pid = pid
        self.arrivee = arrivee
        self.burst = burst
        self.restant = burst
        self.fin = 0

#ROUND ROBIN
def round_robin(processus, quantum):

    temps = 0
    file = deque()
    gantt = []
    termines = []

    # Trier selon le temps d’arrivée
    processus.sort(key=lambda p: p.arrivee)

    i = 0

    while file or i < len(processus):

        # Ajouter les processus arrivés
        while i < len(processus) and processus[i].arrivee <= temps:
            file.append(processus[i])
            i += 1

        # CPU libre
        if not file:
            temps += 1
            continue

        # Retirer le premier processus
        courant = file.popleft()

        debut = temps

        # Temps d’exécution
        temps_execution = min(quantum, courant.restant)

        # Mise à jour du temps
        temps += temps_execution

        # Diminuer le temps restant
        courant.restant -= temps_execution

        # Ajouter au diagramme de Gantt
        gantt.append((courant.pid, debut, temps))

        # Ajouter nouveaux processus arrivés
        while i < len(processus) and processus[i].arrivee <= temps:
            file.append(processus[i])
            i += 1

        # Vérifier si terminé
        if courant.restant > 0:
            file.append(courant)

        else:
            courant.fin = temps
            termines.append(courant)

    return gantt, termines

#SRTF
def srtf(processus):

    temps = 0
    gantt = []
    termines = []

    n = len(processus)

    nombre_termines = 0

    while nombre_termines < n:

        # Processus disponibles
        disponibles = [
            p for p in processus
            if p.arrivee <= temps and p.restant > 0
        ]

        # CPU libre
        if not disponibles:
            temps += 1
            continue

        # Processus avec plus petit temps restant
        courant = min(disponibles, key=lambda p: p.restant)

        debut = temps

        # Exécution d’une unité
        temps += 1

        courant.restant -= 1

        gantt.append((courant.pid, debut, temps))

        # Vérifier fin
        if courant.restant == 0:
            courant.fin = temps
            termines.append(courant)
            nombre_termines += 1

    return gantt, termines

#CALCUL DES METRIQUES
def calculer_metriques(processus):

    total_attente = 0

    print("\nTemps d’attente :")

    for p in processus:

        # Temps de retour
        turnaround = p.fin - p.arrivee

        # Temps d’attente
        attente = turnaround - p.burst

        total_attente += attente

        print(f"{p.pid} -> Temps d’attente = {attente}")

    moyenne = total_attente / len(processus)

    print(f"\nTemps d’attente moyen = {moyenne}")

    return moyenne

#COMPRESSER LE GANTT
def compresser_gantt(gantt):

    compresse = []

    for p in gantt:

        if not compresse:
            compresse.append(list(p))

        elif compresse[-1][0] == p[0]:
            compresse[-1][2] = p[2]

        else:
            compresse.append(list(p))

    return compresse

#AFFICHAGE GANTT
def afficher_gantt(gantt):

    gantt = compresser_gantt(gantt)

    print("\nDiagramme de Gantt :\n")

    # Ligne processus
    for p in gantt:
        print(f"|  {p[0]}  ", end="")

    print("|")

    # Ligne temps
    print(gantt[0][1], end="")

    for p in gantt:
        print(f"      {p[2]}", end="")

    print("\n")

#COMPARAISON
def comparer_algorithmes(rr_moyenne, srtf_moyenne):

    print("\n================ COMPARAISON ================\n")

    print(f"Temps moyen Round Robin : {rr_moyenne}")

    print(f"Temps moyen SRTF        : {srtf_moyenne}")

    print()

    if rr_moyenne < srtf_moyenne:
        print("Round Robin est meilleur pour ces données.")

    elif srtf_moyenne < rr_moyenne:
        print("SRTF est meilleur pour ces données.")

    else:
        print("Les deux algorithmes ont la même performance.")

#MAIN
def main():

    # Processus RR
    processus1 = [
        Processus("P1", 0, 7),
        Processus("P2", 2, 4),
        Processus("P3", 4, 1),
        Processus("P4", 5, 4),
    ]

    # Processus SRTF
    processus2 = [
        Processus("P1", 0, 7),
        Processus("P2", 2, 4),
        Processus("P3", 4, 1),
        Processus("P4", 5, 4),
    ]

    #ROUND ROBIN
    print("\n========== ROUND ROBIN ==========")

    gantt_rr, termines_rr = round_robin(processus1, quantum=2)

    afficher_gantt(gantt_rr)

    rr_moyenne = calculer_metriques(termines_rr)

    #SRTF
    print("\n========== SRTF ==========")

    gantt_srtf, termines_srtf = srtf(processus2)

    afficher_gantt(gantt_srtf)

    srtf_moyenne = calculer_metriques(termines_srtf)

    #COMPARAISON
    comparer_algorithmes(rr_moyenne, srtf_moyenne)

if __name__ == "__main__":
    main()