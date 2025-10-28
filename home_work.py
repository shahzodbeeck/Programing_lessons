#-----------------------Task 1 -------------------#

my_tup =4,6,2,8,3,1
print(my_tup)
my_tup=list(my_tup)
my_tup.append(9)
print(tuple(my_tup))
list(my_tup)
my_tup[4:4]=[15,20,25]
print(list(my_tup))
my_tup.append(30)
print(tuple(my_tup))

#-------------------------------------Task 2---------------------------------#
print("Task 2")
tup_2=10,4,7,2,9,1,5
tup_2=list(tup_2)
tup_2.append(12)
print(tuple(tup_2))
tup_2=list(tup_2)
tup_2[2:2]=[20,25]
print(tuple(tup_2))
tup_2=list(tup_2)
tup_2.remove(min(tup_2))
tup_2.sort()
tup_2.insert(0,100)
print(tuple(tup_2))
