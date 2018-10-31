A1=[12,4,65,3,12,5,43,34,6,3,343,43,4]
A=[10,1,25,51,2,3]
def bubbleSort(A):
	for i in range(0,len(A)-1):
		for j in range(0,len(A)-1-i):
			if A[j]>A[j+1]:
				A[j],A[j+1]=A[j+1],A[j]
		print("i->",i,A)
	return A
print(bubbleSort(A))
