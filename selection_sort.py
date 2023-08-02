import numpy as np

numbers = np.random(10000)

def selection_sort(values):
    sorted_list = []
    
    for i in range(len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

#print(numbers)
print(selection_sort(numbers))