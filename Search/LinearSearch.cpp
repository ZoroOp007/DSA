#include<iostream>

using namespace std;

void linear_search( int *arr, int key, int size)
{
    for (int x=0; x<size; x++)
    {
        if(arr[x] == key)
        {
            cout << "Element found at position : " << x << endl;
        }
    }
}
int main()
{
    int arr[10] = {2,1,3,4,2,3,1,42,3};

    int key = 1;
    linear_search(arr,10,key);
    
    return 0;
}