print "\t\t\t\t\t\t\t\t\t\t\t\tShortest job first\t\t\t\t\t\t\t\t\t\t\t\t"
name =[]
burst_time = []
arrival_time = []
finish_time =[]
waiting_time =[]
print "Enter the number of processes"
n = int(input())
print "Enter the Name of the processes"
name = [str(raw_input()) for i in range(n)]
print "Arrival time is set at 0 for every process"
arrival_time = [int(0) for i in range(n)]
print "Enter the burst time of the processes"
burst_time = [int(input()) for i in range(n)]
for i in range(n):
    for j in range(n-i-1):
        if(burst_time[j]>burst_time[j+1]):
            temp2=burst_time[j]
            burst_time[j]=burst_time[j+1]
            burst_time[j]=temp2
            temp3=name[j]
            name[j]=name[j+1]
            name[j]=temp3
print "Process Name"+"\t"+"Arrival time"+"\t"+"Burst time"
for i in range(n):
    print name[i],"\t\t\t",arrival_time[i],"\t\t\t\t",burst_time[i]
for i in range(n):
    finish_time[i] = arrival_time[i] + burst_time[i]
    print "waiting time",waiting_time
    sum+=waiting_time[i]
print "Average waiting time ",sum/n








