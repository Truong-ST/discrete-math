#print F5 or find Run to run code
import numpy as np

print("nhap so canh:")
numberOfEdge = input()
numberOfEdge=int(numberOfEdge)

# input
edge=[]
for i in range(numberOfEdge):
    tmp=[]
    print("nhap canh " + str(i+1) + " :")
    for x in range(2):
        tmp.append(int(input()))
    edge.append(tmp)

# run
pruferCode = [0 for i in range(numberOfEdge - 1)]

for i in range(len(edge)-1):
    level = [0 for l in range(numberOfEdge + 1)]	# bậc của các đỉnh (thứ tự)
    index = [0 for i in range(numberOfEdge + 1)]	# vị trí của đỉnh trong edge

    for x in range(len(edge)):
        for y in range(2):
            level[edge[x][y]] += 1
            index[edge[x][y]] = x
            
    minLevel = numberOfEdge + 2						# đỉnh nhỏ nhất
    count = 0
    for n in level:
        if ((n == 1)&(count != 0)):
            minLevel = count
            break
        count += 1

    if (edge[index[minLevel]][0] == minLevel):
        pruferCode[i] = edge[index[minLevel]][1]
    else :
        pruferCode[i] = edge[index[minLevel]][0]

    edge.remove(edge[index[minLevel]])


print(pruferCode)

