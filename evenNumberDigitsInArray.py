import numbers
from unittest import result


def findNumbers( nums):
        count = 0
        for num in nums:
            if len(str(num)) % 2 ==0:
                count += 1
        return count

numbers = [12,345,2,6,7896]
result = findNumbers(numbers)
print(result)