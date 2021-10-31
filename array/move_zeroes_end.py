## move all zeros of array to the end 

def pushZerosToEnd(arr, n):
    count = 0 # Count of non-zero elements

    for i in range(n):
        if arr[i] != 0:
             
            # here count is incremented
            arr[count] = arr[i]
            count+=1
    while count < n:
        arr[count] = 0
        count += 1
         
# Driver code
arr = [0,7,0,3,0,3,2,0,6,7,0,4,0,5]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)