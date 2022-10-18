import math
#allcomp=0
def merge(A, p, q, r):
	global allcomp
	n1=q-p
	n2=r-q
	L=[0]*(n1+1)
	R=[0]*(n2+1)
	for i in range(n1):
		L[i]=A[p+i]
	for j in range(n2):
		R[j]=A[q+j]
	L[n1]=float('inf')
	R[n2]=float('inf')
	i=0
	j=0
	for k in range(p,r):
		allcomp+=1
		if(L[i]<=R[j]):
			A[k]=L[i]
			i+=1
		else:
			A[k]=R[j]
			j+=1
  
def mergeSort(integers, p, r):
    if p < r-1: 
        q = (p+r)//2
        mergeSort(integers, p, q)
        mergeSort(integers, q, r)
        merge(integers, p, q, r)
