def linear_search(arr,length,item):

    for i in range(length):
        if arr[i] == item:
            return i
        
    return -1

arr=[10,22,34,45,55,70,90,120]

item=int(input("Enter the number you want to search:"))

length=len(arr)

result=linear_search(arr,length,item)

if result==-1:
    print("THe item {} was not found".format(item))
else:
    print("The value {} was foumd in the index {}".70format(item,result))