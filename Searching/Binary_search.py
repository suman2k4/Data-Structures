def Binary_search(arr,low,high,key):
    if high >= low:
        mid=(low+high)//2

        if arr[mid]==key:
            return mid
        
        elif arr[mid]>key:
            return Binary_search(arr,low,mid-1,key)
        
        else:
            return Binary_search(arr,mid+1,high,key)
        
    else:
        return -1
    
arr=[12,24,36,48,60,72,84] #elements in the array shoulod be sorted

key=int(input("Enter the number you want to search:"))

result=Binary_search(arr,0,len(arr)-1,key)

if result==-1:
    print("The element {} not found in the array".format(key))

else:
    print("The element {} was found in the index {}".format(key,result))