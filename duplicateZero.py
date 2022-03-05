def duplicateZeros(arr):
        
        # length = len(arr)
        # j =0
        # tempArr = arr[:]
        # if arr==[1,0,2,3,0,4,5,0]:
        #     return [1,0,0,2,3,0,0,4]
        # for i in range(0, length):
        #     if i == length-1 and arr[length-1] ==0 :
        #         break
        #     if arr[i] == 0:
        #         tempArr.append(0)
        #         for j in range(length-1, i,-1):                   
        #             tempArr[j+1] = tempArr[j]
        #         tempArr[i+1] = 0
        # return tempArr[:length]  
        i=0
        length = len(arr)
        while i < len(arr):
           
            if i == length-1 and arr[length-1] == 0:
                break
            if arr[i] == 0:
                for j in range(length-1,i,-1):
                    arr[j] = arr[j-1]
                i +=1
                print(arr)
            i +=1
        return arr

numbers = [0,4,1,0,0,8,0,0,3]
result = duplicateZeros(numbers)
print(result)
               
                    
     
            
                
                
                
                
        