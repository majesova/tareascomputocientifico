import time
def getMax(values):
    greater = values[0] #todas las filas tienen al menos un elemento
    numValues = len(values)

    if(numValues == 1):
        greater =  values[0]
        return greater
    
    for i in range(0, numValues):
        if values[i] > greater:
            greater = values[i]
    return greater

def maxByMethod(values, method):
    if method == "CUSTOM":
        return getMax(values)
    if method == "PYTHON":
        return max(values)

def sumInRow(rowValue, rowNum, method):
    numElements = len(rowValue[rowNum])
    for i in range(numElements):
        rowValue[rowNum][i] += maxByMethod([rowValue[rowNum+1][i], rowValue[rowNum+1][i+1]],method)
    if len(rowValue[rowNum])==1: return rowValue[rowNum][0]
    else: return sumInRow(rowValue, rowNum-1, method)

rows = []
with open('triangle.txt') as file:
    for line in file:
        rows.append([int(i) for i in line.rstrip('\n').split(" ")])
 
start = time.time()
result = sumInRow(rows, len(rows)-2, "CUSTOM") # start at second to last row
elapsed = time.time() - start
print("CUSTOM METHOD: %s, seconds: %s " % (result ,elapsed))

start = time.time()
result = sumInRow(rows, len(rows)-2, "PYTHON") # start at second to last row
elapsed = time.time() - start
print("PYTHON METHOD: %s, seconds: %s " % (result ,elapsed))

#usando getMax: 1074, seconds: 0.0007290840148925781
#usando max: 1074, seconds: 0.00014901161193847656
        