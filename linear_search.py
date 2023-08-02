def linear_search(lst, target):
    """Returns the index position of the target if found, else returns -1"""
    for index, value in enumerate(lst):
        if value == target:
            return index
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [i for i in range(11)]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)