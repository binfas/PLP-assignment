#list mainipulation program

#step 1 : Create an empty list
my_list = []

#step 2 Append element to my list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#step 3 : Insert the value at the second position
my_list.insert(1, 15)

#step 4: Extend my_list with another list
my_list.extend([50, 60, 70])

#step 5 : Remove the last element
my_list.pop()

#step 6 : Sort my_list in ascendind order
my_list.sort()

#step 7 : Find and print the index of the value 30
Index_of_30 = my_list.index(30)
print("Index of 30", Index_of_30)

#step 8 : Print the final list
print("Final list", my_list)
