import sys
import os
import time
import insertion
import merge
import heap
import merge3way

  
files=['random20000.txt','number20000.txt','sorted20000.txt','rsorted20000.txt','random40000.txt','number40000.txt','sorted40000.txt','rsorted40000.txt','random80000.txt','number80000.txt','sorted80000.txt','rsorted80000.txt','random160000.txt','number160000.txt','sorted160000.txt','rsorted160000.txt','random320000.txt','number320000.txt','sorted320000.txt','rsorted320000.txt']

print("MERGE SORT")
for i in range(len(files)):
	with open(files[i]) as f:
		integers=f.readlines()
		integers=[i.rstrip('\n') for i in integers]
		integers=[eval(i) for i in integers]
		merge.allcomp=0
		start=time.time()
		merge.mergeSort(integers,0,len(integers))
		end=time.time()
		print(str(len(integers))+","+str(merge.allcomp)+","+str(int((end-start)*1000)))

print("=====================================================================")
print("HEAP SORT")		
for i in range(len(files)):
	with open(files[i]) as f:
		integers=f.readlines()
		integers=[i.rstrip('\n') for i in integers]
		integers=[eval(i) for i in integers]
		heap.allcomp=0
		start=time.time()
		heap.heapSort(integers)
		end=time.time()
		print(str(len(integers))+","+str(heap.allcomp)+","+str(int((end-start)*1000)))

print("=========================================================================")
print("3 WAY MERGE SORT")
for i in range(len(files)):
	with open(files[i]) as f:
		integers=f.readlines()
		integers=[i.rstrip('\n') for i in integers]
		integers=[eval(i) for i in integers]
		merge3way.allcomp=0
		start=time.time()
		l=merge3way.merge_sort_3way(integers,1,len(integers))
		end=time.time()
		print(str(len(integers))+","+str(merge3way.allcomp)+","+str(int((end-start)*1000)))
		
		
print("==========================================================================")
print("INSERTION SORT")
for i in range(len(files)):
	with open(files[i]) as f:
		integers=f.readlines()
		integers=[i.rstrip('\n') for i in integers]
		integers=[eval(i) for i in integers]
		insertion.insertion(integers)
		
		

		
