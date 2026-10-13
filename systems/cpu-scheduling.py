# Recovered student coursework; see README.md and PROVENANCE.json for attribution and status.
processes = []

while True:
    process_names = input("Enter process names one at a time (when finished type 'DONE')")
    if process_names.strip().upper() == 'DONE':
        break

    arrival_time = int(input(f"Enter arrival time for {process_names}: "))
    process_time = int(input(f"Enter process time for {process_names}: "))

    remaining_time = process_time
    waiting_time = 0

    processes.append({
        "name": process_names,
        "arrival_time": arrival_time,
        "process_time": process_time,
        "remaining_time": remaining_time,
        "waiting_time": waiting_time
    })

print("Processes you entered: ", process_names)
for process in processes:
        print(f"Process Name: {process['name']}, Arrival Time: {process['arrival_time']}, Processing Time: {process['process_time']}")




user_input_algorithm = input("Enter a algorithm: ('RR', 'SPN', 'SRT', 'HRRN', 'FEEDBACK')")
user_input_algorithm = user_input_algorithm.strip().upper()
print("You entered:", user_input_algorithm)


    

def sortProcessesbyArrivalTime(processes):
    processes.sort(key=lambda x: x["arrival_time"])
    for process in processes:
        print(f"Process: {process['name']}, Arrival Time: {process['arrival_time']}, Process Time: {process['process_time']}")


def round_robin(processes, timeQuantum):
    print("rr")
    timeline = []
    time = 0

    sortProcessesbyArrivalTime(processes)
    
    while any(p["remaining_time"] > 0 for p in processes):
        for process in processes:
            if process["arrival_time"] <= time and process["remaining_time"] > 0:
                run_time = min(timeQuantum, process["remaining_time"])
                
                
                for _ in range(run_time):
                   
                    timeline.append((time, process["name"]))
                    time += 1
                    process["remaining_time"] -= 1

            elif not any(p["arrival_time"] <= time and p["remaining_time"] > 0 for p in processes):
                time += 1

    print("\nRR timeline of execution (time: process):")
    for t, pname in timeline:
        print(f" {t}: {pname}")


if user_input_algorithm == "RR":
    # Code for RR scheduling
    print("Round Robin selected (enter time quantum):")
    timeQuantum = int(input())
    round_robin(processes, timeQuantum)
    # timeline = []a

    # time = 0


    # sortProcessesbyArrivalTime(processes)
    
    # while any(p["remaining_time"] > 0 for p in processes):
    #     for process in processes:
    #         if process["arrival_time"] <= time and process["remaining_time"] > 0:
    #             run_time = min(timeQuantum, process["remaining_time"])
                
                
    #             for _ in range(run_time):
                   
    #                 timeline.append((time, process["name"]))
    #                 time += 1
    #                 process["remaining_time"] -= 1

    #         elif not any(p["arrival_time"] <= time and p["remaining_time"] > 0 for p in processes):
    #             time += 1

    # print("\nRR timeline of execution (time: process):")
    # for t, pname in timeline:
    #     print(f" {t}: {pname}")


elif user_input_algorithm == "SPN":
    # Code for SPN scheduling
    print("Shortest Process Next selected")
    sortProcessesbyArrivalTime(processes)
    time = 0
    timeline = []
    queue = []
    process_complete = []


    while len(process_complete) < len(processes):
        for process in processes:
            if process["arrival_time"] <= time and process not in queue and process not in process_complete:
                queue.append(process)
        if queue:
            queue.sort(key=lambda x: x["process_time"])  
            current_process = queue.pop(0) 

        
            for _ in range(current_process["process_time"]):
                timeline.append((time, current_process["name"]))
                time += 1

            process_complete.append(current_process)
        else:
            time += 1

    print("\nSPN timeline of execution (time: process):")
    for t, pname in timeline:
        print(f" {t}: {pname}")



elif user_input_algorithm == "SRT":
    # Code for SRT scheduling
    print("Shortest Remaining Time selected")
    sortProcessesbyArrivalTime(processes)
    time = 0
    timeline = []
    queue = []
    process_complete = []


    while len(process_complete) < len(processes):
        for process in processes:
            if process["arrival_time"] <= time and process not in queue and process not in process_complete:
                queue.append(process)
        if queue:
            queue.sort(key=lambda x: x["remaining_time"])  
            current_process = queue[0]
            timeline.append((time, current_process["name"]))
            current_process["remaining_time"] -= 1
            time += 1

            if current_process["remaining_time"] == 0:
                queue.remove(current_process)
                process_complete.append(current_process)
        else:
            time += 1

    print("\nSRT timeline of execution (time: process):")
    for t, pname in timeline:
        print(f" {t}: {pname}")



elif user_input_algorithm == "HRRN":
    # Code for HRRN scheduling
    print("Highest Response Ratio Next selected")
    sortProcessesbyArrivalTime(processes)
    time = 0
    timeline = []
    queue = []
    process_complete = []

    while len(process_complete) < len(processes):
        for process in processes:
            if process["arrival_time"] <= time and process not in queue and process not in process_complete:
                queue.append(process)
        if queue:
            for process in queue:
                waiting_time = time - process["arrival_time"]
                process["response_ratio"] = (waiting_time + process["process_time"]) / process["process_time"]


            queue.sort(key=lambda x: x["response_ratio"], reverse=True)
            current_process = queue.pop(0)  
            for _ in range(current_process["process_time"]):
                timeline.append((time, current_process["name"]))
                time += 1
            process_complete.append(current_process)
        else:
            time += 1

    print("\nHRRN timeline of execution (time: process):")
    for t, pname in timeline:
        print(f" {t}: {pname}")



elif user_input_algorithm == "FEEDBACK":
    # Code for Feedback scheduling
    print("Feedback scheduling selected (enter time quantum):")
    timeQuantum = int(input())
    queue1 = []
    queue2 = []
    queue3 = []
    timeline = []
    time = 0

    sortProcessesbyArrivalTime(processes) 
    for process in processes:
        process["remaining_time"] = process["process_time"]
        queue1.append(process)

    while queue1 or queue2 or queue3:
        if queue1:
            #print("q1")
            current_process = queue1.pop(0)
            run_time = min(timeQuantum, current_process["remaining_time"])
        elif queue2:
            #print("q2")
            current_process = queue2.pop(0)
            run_time = min(timeQuantum, current_process["remaining_time"])
        elif queue3:
            #print("q3")
            current_process = queue3.pop(0) 
            run_time = min(timeQuantum, current_process["remaining_time"])




        for _ in range(run_time):
            timeline.append((time, current_process["name"]))
            time += 1
            current_process["remaining_time"] -= 1

        if current_process["remaining_time"] > 0:
            if current_process in queue1:
                queue2.append(current_process) 
            elif current_process in queue2:
                queue3.append(current_process) 
            else:
                queue3.append(current_process)


    print("\nFeedback timeline of execution (time: process):")
    for t, pname in timeline:
        print(f" {t}: {pname}")


else:

    print("Incorrect input")
