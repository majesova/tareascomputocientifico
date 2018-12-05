#created by:Manuel Soberanis
import time
def maxMin(values):
    results = {}
    numValues = len(values)
    if numValues== 0:
        results['max']=results['min']= 0
        return results
    
    if(numValues == 1):
        results['max'] = results['min'] = values[0]
        return results
    else: 
        results['max']=values[1]
        results['min']=values[0]
    
    for i in range(0, numValues):
        if values[i] > results['max']:
            results['max'] = values[i]
        elif  values[i] < results['min']:
            results['min'] = values[i]
                
    return results

values = [2,1,30,4,5,6,7]
start = time.time()
result = maxMin(values)
elapsed = time.time() - start
print("min: %s, max:%s, seconds: %s" % (result['min'], result['max'] ,elapsed))