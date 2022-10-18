def merge(arr, start, m1, m2, end):
	global allcomp
	larr= arr[start -1 : m1]
	marr = arr[m1: m2 + 1]
	rarr = arr[m2 + 1 : end]
	larr.append(float('inf'))
	marr.append(float('inf'))
	rarr.append(float('inf'))
	
	il = 0
	im = 0
	ir = 0
	for i in range(start-1, end):
		flag=0
		least = min([larr[il], marr[im], rarr[ir]])
		allcomp+=1
		if least == larr[il]:
			arr[i] = larr[il]
			il += 1
			flag=1
		elif least == marr[im]:
			arr[i] = marr[im]
			im += 1
		else:
			arr[i] = rarr[ir]
			ir += 1
		if(flag==0):
			allcomp+=1
    
def merge_sort_3way(arr, start, end):

    if len(arr[start -1: end]) < 2:
        return arr
    else: 
        m1 = start + ((end - start) // 3)
        m2 = start + 2 * ((end-start) // 3)

        merge_sort_3way(arr, start, m1)
        merge_sort_3way(arr, m1+1, m2 + 1)
        merge_sort_3way(arr, m2+2, end)
        merge(arr, start, m1, m2, end)
        return arr
    

