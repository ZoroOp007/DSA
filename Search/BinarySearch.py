def BinarySearch(A,l,r,key,first=-1):
    if( r > l):

        mid = ( l+r )//2

        if(A[mid] == key):
            first = mid

        if( A[mid] >= key):
            return BinarySearch(A,l,mid-1,key,first) 
        else:
            return BinarySearch(A,mid+1,r,key,first)   
    
    else:
            return first
    

A = [1,2,4,5,6,7,7,7,7,8,9,12,34,14]

print(BinarySearch(A,0,len(A),3))