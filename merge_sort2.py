import numpy as np

def merge_sort(values):
    if len(values) <= 1:
        return values
    
    middle_idx = len(values) // 2
    
    left_values = merge_sort(values[:middle_idx])
    right_values = merge_sort(values[middle_idx:])
    
    #print("%15s %-15s" % (left_values, right_values))
    sorted_values = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left_values) and right_index < len(right_values):
        if left_values[left_index] < right_values[right_index]:
            sorted_values.append(left_values[left_index])
            left_index += 1
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    
    sorted_values.extend(left_values[left_index:])
    sorted_values.extend(right_values[right_index:])
    
    return sorted_values


numbers = np.random.randint(0,50, size=10000)
#print(numbers)
sorted_nb = merge_sort(numbers)
print(sorted_nb)