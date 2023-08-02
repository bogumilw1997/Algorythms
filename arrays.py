new_list = [1, 2, 3]
result = new_list[0]

if 1 in new_list:
    print (True)
    
for n in new_list:
    if n ==1:
        print(True)
        break
    
numbers = []

numbers.append(2)
print(len(numbers))

numbers.append(20)
print(len(numbers))

numbers.extend([1,5,100])
print(numbers)