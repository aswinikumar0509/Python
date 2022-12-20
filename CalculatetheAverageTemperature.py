# Calculate the Average Temperature
numDays = int(input("How many day's Temperature"))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day "+str(i+1)+"s high temp : "))
    temp.append(nextDay)
    total+=nextDay

avg = round(total/numDays)
print("\nAverage="+str(avg))

above = 0
for i in temp :
    if i > avg:
        above +=1
print(str(above)+"day's above average")
