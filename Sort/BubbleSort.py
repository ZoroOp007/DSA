"""
Bubble sort is sorting technique with n^2 time complexity
here we compare each element with its adjacent element and swap if a condition is not this
condition may change according to the sort we are for ex for ascending order we will compare if a[i] < a[i+
1] or not
"""
from typing import List
def BubbleSort(l : List) -> List:

    for i in range(1,len(l),1):
        for j in range(0, len(l)-i, 1):

            if l[j] > l[j+1]:
                temp  = l[j]
                l[j]  = l[j+1]
                l[j+1] =  temp



    return l

if __name__ == "__main__":
    a = [2,1,5,3,2,6,4,8,7]

    ans = BubbleSort(a)

    print(ans)
