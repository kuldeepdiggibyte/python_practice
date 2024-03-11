subject = ["History","Science","Mathematics","English"]
print(subject)
print(subject[0:3])
subject.append("Physics") #append used to insert at last, only 1 arg it takes
print(subject)
subject.insert(5,"chemistry") # insert takes 2 arg, index number and insert item
print(subject)
subject1 = ["Biology","geography"]
#subject.insert(1,subject1)
#print(subject)
subject.extend(subject1) #extend add individual subjects not entire list
print(subject)