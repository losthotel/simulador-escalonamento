class Process:
    def __init__(self, pid, arrival_time, burst_time, queue_level):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.queue_level = queue_level
        self.completion_time = 0

def fcfs_scheduling(processes):
    processes.sort(key=lambda p: p.arrival_time)
    time = 0
    result = []
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time
        time += process.burst_time
        process.completion_time = time
        result.append(process)
    return result

def round_robin_scheduling(processes, quantum):
    queue = sorted(processes, key=lambda p: p.arrival_time)
    time = 0
    result = []
    ready_queue = []
    index = 0

    while queue or ready_queue:
        while index < len(queue) and queue[index].arrival_time <= time:
            ready_queue.append(queue[index])
            index += 1

        if not ready_queue:
            if index < len(queue):
                time = queue[index].arrival_time
            else:
                break  # ← Correção aqui
            continue

        current = ready_queue.pop(0)
        exec_time = min(current.remaining_time, quantum)
        current.remaining_time -= exec_time
        time += exec_time

        while index < len(queue) and queue[index].arrival_time <= time:
            ready_queue.append(queue[index])
            index += 1

        if current.remaining_time > 0:
            ready_queue.append(current)
        else:
            current.completion_time = time
            result.append(current)
    return result

def multilevel_queue_scheduler(all_processes, queues_config):
    scheduled_processes = []
    
    for level, config in enumerate(queues_config):
        level_processes = [p for p in all_processes if p.queue_level == level]
        if config['policy'] == 'FCFS':
            result = fcfs_scheduling(level_processes)
        elif config['policy'] == 'RR':
            result = round_robin_scheduling(level_processes, config['quantum'])
        else:
            raise ValueError(f"Política desconhecida: {config['policy']}")
        scheduled_processes.extend(result)

    scheduled_processes.sort(key=lambda p: p.completion_time)
    return scheduled_processes

if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5, 0),
        Process("P2", 1, 3, 1),
        Process("P3", 2, 8, 0),
        Process("P4", 3, 6, 1)
    ]

    queues = [
        {"policy": "FCFS"},
        {"policy": "RR", "quantum": 2}
    ]

    result = multilevel_queue_scheduler(processes, queues)

    print("Processo | Fila | Tempo de Chegada | Tempo de Execução | Tempo de Conclusão")
    for p in result:
        print(f"{p.pid}\t\t{p.queue_level}\t\t{p.arrival_time}\t\t{p.burst_time}\t\t{p.completion_time}")