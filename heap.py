allcomp=0
def heapify(integers,n,i):
	global allcomp
	k=i
	p=2*i+1
	r=2*i+2
	
	if p<n:
		allcomp+=1
		if integers[i]<integers[p]:
			k=p
	
	if r<n:
		allcomp+=1
		if integers[k]<integers[r]:
			k=r
	
	if k!=i:
		allcomp+=1
		(integers[i],integers[k])=(integers[k],integers[i])
		heapify(integers,n,k)

 
def heapSort(integers):
    for i in range(len(integers) // 2 - 1, -1, -1):
        heapify(integers,len(integers), i)
 
    for i in range(len(integers) - 1, 0, -1):
        (integers[i],integers[0]) = (integers[0],integers[i])  
        heapify(integers,i,0)
