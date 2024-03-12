def cube(x):
    return x*x*x


l = [1,2,3,4,5,6,7]
#in this program it is too hectic to create new list, then for loop to itterate , hence MAP
new_l = []

for items in l:
    new_l.append(cube(items))
#print(new_l)

print(map(cube,l))#returns map object

print((tuple(map(cube,l))))
print((list(map(cube,l))))
print((set(map(cube,l))))