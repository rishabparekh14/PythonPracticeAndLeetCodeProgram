def validMountainArray(arr):
    length = len(arr)
    i =0

    while i+1 < length and arr[i] < arr[i+1]:
           i += 1
        
    if i == 0 or i == length-1:
        return False
    
    while i+1 < length and arr[i+1] < arr[i]:
        i += 1

    return i == length-1





numbers = [3,5,5]
#[7,1,14,11]
#[-20,8,-6,-14,0,-19,14,4]
result = validMountainArray(numbers)
print(result)
        