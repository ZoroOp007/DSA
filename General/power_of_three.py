## Binary Search : check if element exists or not if yes then return its index otherwise -1

def BinarySearch(arr,l,r,key):

    if(l<=r):
        mid = (l+r)/2

        if(arr[mid] == key):
            return mid
        
        if(arr[mid]>key):
            BinarySearch(arr,l,mid-1,key)
        else:
            BinarySearch(arr,r,mid+1,key)
        


## Binary Search : return the first occurence of a element in given list 



## Binary Search : return the last occurence of a element in given list 

## Binary Search : return the both first and last occurence of the given list

## I think this is all variations of question in soving any binary search question 

