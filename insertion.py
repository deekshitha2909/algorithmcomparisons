import time
def insertion(integers):
    output=[]
    comparisons=0
    allcomp=0
    start=time.time()
    for j in range(1,len(integers)):
        i=j-1
        temp=integers[j]
        allcomp=allcomp+1
        while(i>=0 and temp<integers[i]):
            comparisons=comparisons+1
            integers[i+1]=integers[i]
            i=i-1
        integers[i+1]=temp
    end=time.time()
    output.append(len(integers))
    output.append(allcomp+comparisons)
    output.append(int((end-start)*1000))
    print(','.join(str(x) for x in output))


