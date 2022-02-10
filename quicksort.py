import numbers


def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot)) 
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

numbers = [4, 7, 1, 9, 3, 2, 6,7]
print(numbers)
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
        
