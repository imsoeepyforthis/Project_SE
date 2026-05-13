from collections import deque

# ================== CLASS PROCESS ==================
class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.completion = 0



# ================== ROUND ROBIN ==================
def round_robin(processes, quantum):
    time = 0
    queue = deque()
    gantt = []
    completed = []

    processes.sort(key=lambda p: p.arrival)
    i = 0

    while queue or i < len(processes):

        # Ajouter les processus arrivés
        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        # CPU idle
        if not queue:
            time += 1
            continue

        current = queue.popleft()

        start_time = time

        execution_time = min(quantum, current.remaining)

        time += execution_time
        current.remaining -= execution_time

        gantt.append((current.pid, start_time, time))

        # Ajouter nouveaux processus
        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        # Replacer dans queue ou terminer
        if current.remaining > 0:
            queue.append(current)
        else:
            current.completion = time
            completed.append(current)

    return gantt, completed


# ================== SRTF ==================
def srtf(processes):

    time = 0
    gantt = []
    completed = []

    n = len(processes)
    finished_count = 0

    while finished_count < n:

        available = [
            p for p in processes
            if p.arrival <= time and p.remaining > 0
        ]

        # CPU idle
        if not available:
            time += 1
            continue

        # plus petit remaining time
        current = min(available, key=lambda p: p.remaining)

        start_time = time

        # Exécution 1 unité
        time += 1
        current.remaining -= 1

        gantt.append((current.pid, start_time, time))

        # Vérifier fin
        if current.remaining == 0:
            current.completion = time
            completed.append(current)
            finished_count += 1

    return gantt, completed


# ================== METRICS ==================
def calculate_metrics(processes):

    total_waiting = 0

    print("\nWaiting Times:")

    for p in processes:

        turnaround = p.completion - p.arrival

        waiting = turnaround - p.burst

        total_waiting += waiting

        print(f"{p.pid} -> Waiting Time = {waiting}")

    avg_waiting = total_waiting / len(processes)

    print(f"\nAverage Waiting Time = {avg_waiting}")

    return avg_waiting


# ================== GANTT DIAGRAM ==================
def compress_gantt(gantt):

    compressed = []

    for p in gantt:

        if not compressed:
            compressed.append(list(p))

        elif compressed[-1][0] == p[0]:
            compressed[-1][2] = p[2]

        else:
            compressed.append(list(p))

    return compressed


def print_gantt(gantt):

    gantt = compress_gantt(gantt)

    print("\nGantt Diagram:\n")

    # Ligne des processus
    for p in gantt:
        print(f"|  {p[0]}  ", end="")

    print("|")

    # Ligne des temps
    print(gantt[0][1], end="")

    for p in gantt:
        print(f"      {p[2]}", end="")

    print("\n")


# ================== COMPARISON ==================
def compare_algorithms(rr_avg, srtf_avg):

    print("\n================ COMPARISON ================\n")

    print(f"Round Robin Average Waiting Time : {rr_avg}")

    print(f"SRTF Average Waiting Time        : {srtf_avg}")

    print()

    if rr_avg < srtf_avg:
        print("Round Robin is better for this dataset.")

    elif srtf_avg < rr_avg:
        print("SRTF is better for this dataset.")

    else:
        print("Both algorithms have same performance.")


# ================== MAIN ==================
def main():

    # RR processes
    processes1 = [
        Process("P1", 0, 7),
        Process("P2", 2, 4),
        Process("P3", 4, 1),
        Process("P4", 5, 4),
    ]

    # SRTF processes
    processes2 = [
        Process("P1", 0, 7),
        Process("P2", 2, 4),
        Process("P3", 4, 1),
        Process("P4", 5, 4),
    ]

    # ================= RR =================
    print("\n========== ROUND ROBIN ==========")

    gantt_rr, completed_rr = round_robin(processes1, quantum=2)

    print_gantt(gantt_rr)

    rr_avg = calculate_metrics(completed_rr)

    # ================= SRTF =================
    print("\n========== SRTF ==========")

    gantt_srtf, completed_srtf = srtf(processes2)

    print_gantt(gantt_srtf)

    srtf_avg = calculate_metrics(completed_srtf)

    # ================= COMPARISON =================
    compare_algorithms(rr_avg, srtf_avg)


if __name__ == "__main__":
    main()