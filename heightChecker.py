def heightChecker( heights):
        expected = sorted(heights)
        counter =0
        
        for i in range(0, len(heights)):
            if heights[i] != expected[i]:
                counter +=1
        return counter

numbers = [5,1,2,3,4]
result = heightChecker(numbers)
print(result)