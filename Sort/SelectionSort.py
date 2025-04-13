"""
Selection Sort : 
"""

def SelectionSort(l):

    for i in range(0,len(l)-1):
        for j in range(i+1,len(l)):

            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp

    return l

if __name__ == "__main__":
    l = [1,3,2,5,6,5,1]

    ans = SelectionSort(l)

    print(ans)