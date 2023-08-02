def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(sum([1, 4,8,2]))


def sum_rec(numbers):
    if not numbers:
        return 0
    #print("Calling sum(%s)" % numbers[1:])
    remaining_sum = sum_rec(numbers[1:])
    #print("Call to sum(%s) returning %d + %d" % (numbers, numbers[0], remaining_sum))
    return numbers[0] + remaining_sum

print(sum_rec([1, 4,8,2]))