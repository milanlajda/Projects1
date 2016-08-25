def quicksort(arr):
    pivot=len(arr)-1
    temp=0
    for t in range(0,len(arr)):
        for p in range(0, len(arr)):
            if arr[p]<arr[pivot]:
                temp=arr[p]
                arr[p]=arr[t]
                arr[t]=temp
                t=t+1
                if arr[p]==arr[pivot]:
                    t=arr[pivot]
            print arr
            print arr[t]







quicksort([4,6,2,1,5,7,9,5,4,3])
