subject = ["History","Science","Mathematics","English"]
print(subject)
print(subject[0:3])
subject.append("Physics") #append used to insert at last, only 1 arg it takes
print(subject)
subject.insert(5,"chemistry") # insert takes 2 arg, index number and insert item
print(subject)
subject1 = ["Biology","geography","zoology"]
#subject.insert(1,subject1)
#print(subject)
subject.extend(subject1) #extend add individual subjects not entire list
print(subject)

#list sorting
subject.sort() #this method make changes in original file
print(subject)
num = [4,6,8,2,3]
print(sorted(num)) #this sorted method wont make change in original file
print(num)

name = ["kuldeep","Kartik","Saket","vipul"]
course_str = ", ".join(name) #converted in string
print(course_str)
new_list = course_str.split(',') #converted in list
print(new_list)


