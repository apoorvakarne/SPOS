class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.service_time = 0 
        self.waiting_time = 0  

    def set_service_time(self, service_time):
        self.service_time = service_time

    def calculate_waiting_time(self):
        self.waiting_time = self.service_time - self.arrival_time

def fcfs(processes):
    current_time = 0
    gantt_chart = []  

    for process in processes:
        # Service time for the current process is the max of current_time or arrival_time
        service_time = max(current_time, process.arrival_time)
        process.set_service_time(service_time)
        
 
        gantt_chart.append((service_time, service_time + process.burst_time, process.pid))
        
        current_time = service_time + process.burst_time

    # waiting times 
    for process in processes:
        process.calculate_waiting_time()

    return gantt_chart

def print_processes(processes):
    print("PID\tAT\tBT\tST\tWT")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.service_time}\t{process.waiting_time}")

def calculate_average_waiting_time(processes):
    total_waiting_time = sum(process.waiting_time for process in processes)
    return total_waiting_time / len(processes)

def print_gantt_chart(gantt_chart):
    print("\nGantt Chart:")
    print("--------------------------------------------------------")
    print("|", end="")
    for entry in gantt_chart:
        print(f"  P{entry[2]}  |", end="")
    print()
    print("--------------------------------------------------------")
    print(f"{gantt_chart[0][0]}", end="")
    for entry in gantt_chart:
        print(f"       {entry[1]}", end="")
    print()

def main():
    num_processes = int(input("Enter the number of processes: "))
    processes = []

    for i in range(num_processes):
        print(f"Process {i + 1}")
        arrival_time = int(input("Enter Arrival Time: "))
        burst_time = int(input("Enter Burst Time: "))
        processes.append(Process(i + 1, arrival_time, burst_time))

    processes.sort(key=lambda x: x.arrival_time)

    gantt_chart = fcfs(processes)

    print("\nFCFS Scheduling Results:")
    print_processes(processes)

    avg_waiting_time = calculate_average_waiting_time(processes)
    print(f"\nAverage Waiting Time: {avg_waiting_time}")

    print_gantt_chart(gantt_chart)

if __name__ == "__main__":
    main()
