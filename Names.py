import time
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def mergeSort(x):
    result = []
    if len(x) < 20:
        return sorted(x)
    mid = int(len(x) / 2)
    y = mergeSort(x[:mid])
    z = mergeSort(x[mid:])
    i = 0
    j = 0
    while i < len(y) and j < len(z):
        if y[i] > z[j]:
            result.append(z[j])
            j += 1
        else:
            result.append(y[i])
            i += 1
    result += y[i:]
    result += z[j:]
    return result

def quicksort(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0]
        i = 0
        for j in range(len(x)-1):
            if x[j+1] < pivot:
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksort(x[:i])
        second_part = quicksort(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

def sortList(alist,sortMethod):
    if sortMethod == "BUBLE":
        return bubbleSort(alist)
    if sortMethod == "QUICK":
        return quicksort(alist)
    if sortMethod == "MERGE":
        return mergeSort(alist)
    if sortMethod == "PYTHON":
        return sorted(alist,key=str)

def sortAndSum(sortMethod):
    f=open("names.txt")
    char_num_dict = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    names = sortList(f.read().replace('"','').split(','),sortMethod)
    sum=0
    for ind,val in enumerate(names):
	    temp=0
	    for x in val:
		    temp+=char_num_dict[x]
	    sum+=temp*(ind+1)
    return sum

start = time.time()
result = sortAndSum("BUBLE")
elapsed = time.time() - start
print("BUBLE METHOD %s, seconds: %s " % (result ,elapsed))

start = time.time()
result = sortAndSum("QUICK")
elapsed = time.time() - start
print("QUICKSORT METHOD %s, seconds: %s " % (result ,elapsed))

start = time.time()
result = sortAndSum("MERGE")
elapsed = time.time() - start
print("MERGE METHOD %s, seconds: %s " % (result ,elapsed))

start = time.time()
result = sortAndSum("PYTHON")
elapsed = time.time() - start
print("PYTHON METHOD %s, seconds: %s " % (result ,elapsed))