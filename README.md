# Python-project
This is an Python project during learning Python

This is simple explanation of this small project.
As my wife works as an kindergarten teacher I thought how nice it could
be to have an Python example of children and teachers register.
In this project I used object oriented classes.

In person.py file I created the following classes: Person, Child, Trustee(as parents) and Teacher.

In main.py file I used this classes to create objects of children, trustees and teachers.
This main.py file acts as my simple database of persons that I want to register in my file.
So main.py file uses objects created from object oriented classes.

File original.py is used to create and prints original children list connected with trustees.

File sort.py is used to create and prints children lists sorted by last name, first name,
sorted by age in descending order and sorted by children older than 2 years.

File sort_by_age.py is used to create and prints children list sorted by
age in descending order.

File teacher.py is used to create and prints list of teachers.

File original_csv.py is used as a command prompt program for creating csv file
of original children list connected with trustees.
On Windows command prompt in project folder with this files when you write:
>python original_csv.py children.csv
you will make file named children.csv with original children list in csv file format.

File age_sort_csv.py is used as a command prompt program for creating csv file
of children list sorted by age from sort_by_age.py
On Windows command prompt in project folder with this files when you write:
>python age_sort_csv.py children_sorted.csv
you will make file named children_sorted.csv with sorted children list in csv file format.

File teacher_csv.py is used as a command prompt program for creating csv file
of teachers list from teachers.py
On Windows command prompt in project folder with this files when you write:
>python teacher_csv.py children.csv
you will make file named teachers.csv with original teachers list in csv file format.

I also included this example files children.csv, children_sorted.csv and teacher.csv
This files can be used for communication with other programs.
