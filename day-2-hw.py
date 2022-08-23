# exercise 1

l_1 = [1,11,14,5,8,9]
numbers = []

def num(number):
    for digit in number:
        if digit < 10:
            numbers.append(digit)
    return numbers

print(num(l_1))

# exercise 2

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def new_list(list_a, list_b):
    comb = list_a +list_b
    comb.sort()
    return comb
print(new_list(l_1,l_2))
