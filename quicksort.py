import numpy as np

def quicksort(values):
    if len(values) <= 1:
        return values
    
    less_than_pivot = []
    greater_than_pivot = []
    
    pivot = values[0]
    
    for value in values[1:]:
        if value <=pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    #print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))        
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
numbers = np.random.randint(0,50, size=1000000)

sorted_nb = quicksort(numbers)
print(sorted_nb)