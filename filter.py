L = [43,67,12,78,45,97,45,97,54]
# filters are used on specific condition and they apply condition while ittration
even = list(filter(lambda x : x % 2 == 0,L))
print(even)
odd = list(filter(lambda x : x % 2 != 0, L))
print(odd)
