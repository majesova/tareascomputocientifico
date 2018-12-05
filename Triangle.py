import time

def sumInRow(rowValue, rowNum):
    numElements = len(rowValue[rowNum])
    for i in range(numElements):
        rowValue[rowNum][i] += max([rowValue[rowNum+1][i], rowValue[rowNum+1][i+1]])
    if len(rowValue[rowNum])==1: return rowValue[rowNum][0]
    else: return sumInRow(rowValue, rowNum-1)

rows = []
with open('triangle.txt') as file:
    for line in file:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
 
start = time.time()
result = sumInRow(rows, len(rows)-2) # start at second to last row
elapsed = time.time() - start
 
print("%s, seconds: %s " % (result ,elapsed))

#def sumInRow(data, rowNumber):


#triangle = open("triangle.txt")
#lineIde = 0
#for line in triangle:
#    print(len(line))
#    for i in range(0, len(line)):

        