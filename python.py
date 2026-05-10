from collections import deque

class Process:
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
        self.remaining = burst
        self.completion = 0


# ------------------ ROUND ROBIN ------------------
def round_robin(processes, quantum):
    time = 0
    queue = deque()
    gantt = []
    completed = []

    processes.sort(key=lambda p: p.arrival)
    i = 0

    while queue or i < len(processes):
        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        if not queue:
            time += 1
            continue

        current = queue.popleft()
        start_time = time
        execution_time = min(quantum, current.remaining)

        time += execution_time
        current.remaining -= execution_time

        gantt.append((current.pid, start_time, time))

        while i < len(processes) and processes[i].arrival <= time:
            queue.append(processes[i])
            i += 1

        if current.remaining > 0:
            queue.append(current)
        else:
            current.completion = time
            completed.append(current)

    return gantt, completed


# ------------------ SRTF ------------------
def srtf(processes):
    time = 0
    completed = []
    gantt = []
    n = len(processes)
    finished_count = 0

    while finished_count < n:
        available = [p for p in processes if p.arrival <= time and p.remaining > 0]

        if not available:
            time += 1
            continue

        current = min(available, key=lambda p: p.remaining)

        start_time = time
        time += 1
        current.remaining -= 1

        gantt.append((current.pid, start_time, time))

        if current.remaining == 0:
            current.completion = time
            completed.append(current)
            finished_count += 1

    return gantt, completed


# ------------------ METRICS ------------------
def calculate_metrics(processes):
    total_waiting = 0

    for p in processes:
        turnaround = p.completion - p.arrival
        waiting = turnaround - p.burst
        total_waiting += waiting
        print(f"{p.pid}: Waiting Time = {waiting}")

    avg = total_waiting / len(processes)
    print(f"\nAverage Waiting Time = {avg}")


# ------------------ MAIN TEST ------------------
def main():
    # IMPORTANT: create fresh copies for each algorithm
    processes1 = [
        Process("P1", 0, 7),
        Process("P2", 2, 4),
        Process("P3", 4, 1),
        Process("P4", 5, 4),
    ]

    processes2 = [
        Process("P1", 0, 7),
        Process("P2", 2, 4),
        Process("P3", 4, 1),
        Process("P4", 5, 4),
    ]

    print("=== ROUND ROBIN ===")
    gantt_rr, completed_rr = round_robin(processes1, quantum=2)

    for g in gantt_rr:
        print(g)

    calculate_metrics(completed_rr)

    print("\n=== SRTF ===")
    gantt_srtf, completed_srtf = srtf(processes2)

    for g in gantt_srtf:
        print(g)

    calculate_metrics(completed_srtf)


if __name__ == "__main__":
    main()