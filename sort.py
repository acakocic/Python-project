from main import children_list, printChildrenOut
from person import *

# Sorting the list by lastName, firstName in ascending order.
print("\n\nSorting the list by lastName, firstName in ascending order.\n")
for i in range(len(children_list)):
    for j in range(i + 1, len(children_list)):
        name_i = children_list[i].last_name + children_list[i].first_name
        name_j = children_list[j].last_name + children_list[j].first_name
        if name_i > name_j:
           children_list[i], children_list[j] = children_list[j], children_list[i]
printChildrenOut(children_list)

# Sorting the list by age in descending order
print("\n\nSorting the list by age in descending order.\n")
for i in range(len(children_list)):
    for j in range(i + 1, len(children_list)):
        if children_list[i].age() < children_list[j].age():
           children_list[i], children_list[j] = children_list[j], children_list[i]  
printChildrenOut(children_list)

# Getting a list of children older than 2 years
print('\n\nGetting a list of children older than 2 years.\n')
new_list = [i for i in children_list if i.age() > 2]
printChildrenOut(new_list)

