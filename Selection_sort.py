def ssort(arr):
    for i in range(len(arr)):
        minn = i
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                minn = j
        arr[i],arr[minn] = arr[minn],arr[i]
    return arr

print(ssort([9,4,2,11,2,1]))
