import math
A=[1,2,2,7,7,9]
# A=[1,1,2,2,5]
# B=[3,1,4,1,5]
B = [2,6,7,4,8]
def BinarySearch(Arr,key):
    l = 0
    r= len(Arr) - 1
    if Arr[r] == key:
        return r+1
    while(l<=r):
        mid = math.floor((l+r)/2)
        if Arr[mid]>key and Arr[mid-1]<=key:
            return mid
        else:
            if Arr[mid]<=key:
                l=mid+1
            elif Arr[mid]>key:
                r = mid-1
                
                
    
for i in B:
    #print(i)
    print(BinarySearch(A,i),end=" ")