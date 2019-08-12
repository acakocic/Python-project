from main import children_list, printChildrenOut
from person import *

# Sorting the list by age in descending order
print("\n\nSorting the list by age in descending order.\n")
for i in range(len(children_list)):
    for j in range(i + 1, len(children_list)):
        if children_list[i].age() < children_list[j].age():
           children_list[i], children_list[j] = children_list[j], children_list[i]  
printChildrenOut(children_list)

