import numpy as np

print("nhap so dinh:")
numberOfVertex = int(input())
print("nhap so canh:")
numberOfEdge = int(input())
# input
# edge=[]
# for i in range(numberOfEdge):
#     tmp=[]
#     print("nhap canh " + str(i+1) + " :")
#     for x in range(2):
#         tmp.append(int(input()))
#     edge.append(tmp)
# print(edge)
edge = []
while (len(edge)<numberOfEdge):
    tmp = [np.random.randint(0,numberOfVertex) for i in range(2)]
    tmp.sort()
    if ((tmp not in edge) & (tmp[0] != tmp[1])):
        edge.append(tmp)
# print(edge)

degree = [0] * numberOfVertex
nearList = []
for i in range(numberOfEdge):
    nearList.append([])

for i in range(numberOfEdge):
    for j in range(2):
        degree[edge[i][j]] += 1
        nearList[edge[i][j]].append(edge[i][j-1])

# visited[degree.index(max(degree))]=1

def maxE(lis,degree):
    a=[]
    sortedList=[]
    for i in range(len(lis)):
        a.append([])
        a[i].append(lis[i])
        a[i].append(degree[lis[i]])
    def sortSecond(val):
        return val[1]
    a.sort(key = sortSecond,reverse = True)
    for i in range(len(lis)):
        sortedList.append(a[i][0])
    return sortedList

color = [0] * numberOfVertex
color[degree.index(max(degree))]=1
def explore(nearList,color,s):
    sortList = maxE(nearList[s],degree)
    for i in sortList:
        if (color[i]==0):
            nearColor=[]
            for c in nearList[i]:
                nearColor.append(color[c])
            for j in range(1,numberOfVertex + 1):
                if (j not in nearColor):
                    color[i] = j
                    break
            explore(nearList,color,i)

explore(nearList,color,degree.index(max(degree)))
print(color)

def coloring(n):
    broad = {
        0  :    "black",
        1  :	"yellow",
        2  :	"red",
        3  :	"purple",
        4  :	"green",
        5  :	"violet",
        6  :	"brown",
        7  :	"#9b9b00",
        8  :	"#5d9b00",
        9  :	"#4b0d84",
        10 :	"gray",
        11 :	"orange",
        12 :	"#5d9faf",
        13 :	"#5dcbf2",
        14 :	"#bf0d84",
        15 :	"#827bb0",
        16 :	"LemonChiffon",
        17 :	"#82d9b0",
        18 : 	"#865e15",
        19 :	"#feceff",
        20 :	"#8ffa35",
    }
    return broad.get(n)

file = open("colorGraph.dot","w")
file.write("Graph Color{\n")
for i in range(numberOfEdge):
    file.write(str(edge[i][0]) + " -- " + str(edge[i][1]) + "\n")
for i in range(numberOfVertex):
    file.write(str(i) +" [fillcolor = \""+ coloring(color[i]) +"\", style=filled];" + "\n")

file.write("}")
file.close()
print(max(color))
print("done")