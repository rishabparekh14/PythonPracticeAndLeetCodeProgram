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

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included  
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i] 


numbers = [1,0,2,3,0,4,5,0]
result = duplicateZeros(numbers)
print(result)
               
                    
     
            
                
                
                
                
        