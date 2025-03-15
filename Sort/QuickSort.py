def partition(A,low,high):

    pivot = A[high]
    i = low-1

    for j in range(low,high):
        if( A[j] <= pivot ):
            i = i+1

            A[i],A[j] = A[j],A[i]
    
    A[i+1],A[high] = A[high],A[i+1]

    return i+1

def Quicksort(A,low,high):
    if(high >= low):
        pivot_idx = partition(A,low,high)

        #Quick sort on the left part
        Quicksort(A,low,pivot_idx-1)

        #Quick sort on the right part
        Quicksort(A,pivot_idx+1,high)

A = [1,3,2,4]

Quicksort(A,0,3)

print(A)