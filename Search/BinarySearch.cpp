// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int BinarySearch(int *arr, int key, int size)
{
    int beg = 0;
    int end = size -1;
    
    while( beg <= end)
    {
        int mid = (beg + end)/2;
        
        if(arr[mid] == key)
            return mid;
        else if(arr[mid] > key)
            end = mid -1;
        else
            beg = mid+1;
    }
    return -1;
}

int BS(int* arr,int key, int beg, int end)
{
    int mid = (beg + end)/2;
    
    if( arr[mid] == key )
        return mid;
    else
    {
        if( arr[mid] < key)
            return BS(arr,key,mid+1,end);
        else
            return BS(arr,key,beg,mid+1);
    }
    
    return -1;
}

//Return first occurence using binary search
int BinaryS(int * arr, int key, int beg, int end)
{
    int ptr = -1;
    
    while( beg <= end)
    {
        int mid = (beg + end)/2;
        
        if(arr[mid] == key)
        {
            ptr = mid;
            end = mid-1;
        }
        else if(arr[mid] > key)
        {
            end = mid - 1;
        }
        else
        {
            beg = mid + 1;
        }
    }
    return ptr;
}


int main() {
    
    int arr[20] = {2,12,34,121,121,121,321,324,432,543,654};
    
    // int idx = BinarySearch(arr,121,20);
    
    // cout << "Element found at index : "<< idx <<"\nValue : " << arr[idx];
    
    int idx = BinaryS(arr,121,0,19);
    
    cout << idx;
    
    return 0;
}