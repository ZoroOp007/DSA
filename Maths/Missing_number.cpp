#include<iostream>

using namespace std;

void missing_number( int *a, int l)
{
    int min=a[0],max=a[0];
    int sum=0;

    for(int i=0; i<l; i++)
    {
        if(min > a[i])
            min = a[i];
        if(max < a[i])
            max = a[i];
        
        sum += a[i];
    }

    int s = (l+1)*( min + max)/2 ;

    cout << "min : " << min << " max : " << max <<endl;

    cout << "sum : " << sum << " s : " << s << endl;
    cout << "Missing Number : " << abs(sum - s);
}

int main()
{
    int arr[] = {2,3,4,5,6,7,8};

    missing_number(arr,7);
    return 0;
}