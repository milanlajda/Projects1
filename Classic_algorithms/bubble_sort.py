def bubblesort(arr):
    temp=0
    for a in range(0, len(arr)):
        for b in range(0, len(arr)):
            if arr[b]>arr[a]:
                temp = arr[b]
                arr[b]=arr[a]
                arr[a]=temp
    print arr




bubblesort([8,4,9,2,9,1,4,7,2])