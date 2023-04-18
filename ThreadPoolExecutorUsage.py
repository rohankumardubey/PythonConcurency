from concurrent.futures import ThreadPoolExecutor , as_completed
import time

ConcurrentResultDict = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
NonConcurrentResultDict = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}


def appendConcurrentResult(a,b,c):
    result = (a**b)*c
    ConcurrentResultDict[result % 10].append(result)
    time.sleep(1)

def appendnonConcurrentResult(a,b,c):
    result = (a**b)*c
    NonConcurrentResultDict[result % 10].append(result)
    time.sleep(1)

startTime = time.time()
process=[]

with ThreadPoolExecutor(max_workers=10) as executor:
    for i in range(10):
        process.append(executor.submit(appendConcurrentResult,i,(i*i),(i*i*i)))
print("conurrent cost : "+str((time.time()-startTime)))


startTime = time.time()
for i in range(10):
    appendnonConcurrentResult(i,(i*i),(i*i*i))
print("non concurrent cost : "+str((time.time()-startTime)))

print("concurent result dictonary : "+str(ConcurrentResultDict))
print("non concureent result dictonary : "+str(NonConcurrentResultDict))