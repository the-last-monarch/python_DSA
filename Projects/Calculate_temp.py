numDays = int(input("How many days tempature you want? "))
total = 0
temp = []
for i in range(numDays):
    newDays = int(input("Day " + str(i+1) + "'s of tempature: "))
    temp.append(newDays)
    total += temp[i]

avg = round(total/numDays,2)
print("\nAverage is " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1
print(str(above) + " Day(s) are above tempature.")



