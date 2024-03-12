def sum_func(func, l):
    result = 0
    for i in l:
        if func(i):
            result = result + i
    return result



L = [34,23,65,12,87,45,73]

even = lambda x : x%2==0
odd = lambda x: x%2!=0
division = lambda x: x%3==0

print(sum_func(even,L))
print(sum_func(odd,L))
print(sum_func(division,L))


