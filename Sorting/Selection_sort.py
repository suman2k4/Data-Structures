def selection_sort(arr,size):
    for i in range(size):
        min_idx = i
        for j in range(i+1,size):   
            if arr[j] < arr[min_idx]:
                min_idx = j
                arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr=[56,42,90,72,-12,-43,67,90]
size = len(arr)
selection_sort(arr,size)
print("The sorted array is: ",arr)