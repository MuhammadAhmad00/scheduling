print "\t\t\t\t\t\t\t\t\t\t\t\t\tVirtual Round Robin\t\t\t\t\t\t\t\t\t\t\t\t"
print "\t\t\t\t\t\t\t\t\t\tThe Input wait is for Even processses\t\t\t\t\t\t\t\t\t\t"
burst_time = []
process_name = []
order = []
wait = []
remaining_bt = []
wait_input = []
turn_around = []
print "\t\t\t\t\t\t\t\t\t\t\t processes will wait for input for 15 sec"
input_wait = int(15)
print "Enter the number of processes"
n = input()
wait = [int(0) for i in range(n)]
print "Enter the name of the processes"
process_name = [str(raw_input()) for i in range(n)]
print "Enter  Quantum time for the processes "
quantum = input()
print "Enter the order of the processes in which u want to run"
order = [int(input()) for i in range(n)]
print "Arrival time for the processes is set 0"
arrival_time = [int(0) for i in range(n)]
print "Enter the burst time for the processes"
burst_time = [int(input()) for i in range(n)]
for i in range(n):
    for j in range(n - i - 1):
        if order[i] > order[i + 1]:
            temp = order[i]
            order[i] = order[i + 1]
            order[i + 1] = order[i]
            temp2 = process_name[i]
            process_name[i] = process_name[i + 1]
            process_name[i + 1] = temp2
            temp3 = burst_time[i]
            burst_time[i] = burst_time[i + 1]
            burst_time[i + 1] = temp3
print "Process Name" + "\t\t" + "Process Order" + "\t\t" + "Burst Time" + "\t\t" + "Arrival Time"
for i in range(n):
    print process_name[i] + "\t\t\t\t\t", order[1], "\t\t\t\t\t\t", burst_time[i], "\t\t\t\t\t", arrival_time[i]
print "\t\t\t\t\t\t\t\t\t\tNow we find the waiting time for the processes\t\t\t\t\t\t\t\t\t"
remaining_bt = [int(burst_time[i]) for i in range(n)]
for i in range(n):
    if i%2 == 0:
        wait_input=[int(burst_time[i]+input_wait)]
t = int(0)
done = int(0)
while done == int(1):
    done = int(1)
for i in range(n):
    if remaining_bt[i] > 0:
        done = int(0)
        if remaining_bt[i]>quantum:
            t+=quantum
            remaining_bt[i] -= quantum
        else :
            t = t + remaining_bt[i]
            wait[i] = t - burst_time[i]
            if done == 1:
                break
sum = int(0)
print "Waiting time for the processes"
for i in range(n):
    print wait[i]
    sum += wait[i]
print "Average waiting time"
print sum/n
print "\t\t\t\t\t\t\t\t\t\t\t\tNow find the final turn round time"
turn_around=[int(burst_time[i]+wait[i]) for i in range(n)]
print"Turn round time of the processes"
turn = int(0)
for i in range(n):
    print turn_around[i]
    turn += int(turn_around[i])
print "Average turn around time"
print turn/n




