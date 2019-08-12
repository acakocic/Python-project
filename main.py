import datetime
from person import *

trustee1 = Trustee("Aleksandar", "Kovacevic", "father", 642414441)
trustee2 = Trustee("Maja", "Petrovic", "mother", 623456789)
trustee3 = Trustee("Marija", "Markovic", "mother", 634567892)
trustee4 = Trustee("Zoran", "Zdravkovic", "father", 63425789)
trustee5 = Trustee("Tamara", "Miletic", "mother", 63233556)
trustee6 = Trustee("Petar", "Markovic", "father", 645671123)
trustee7 = Trustee("Zoran", "Aleksic", "father", 641112223)

teacher1 = Teacher("Milena", "Ilic", 642556161)
teacher2 = Teacher("Irena", "Malinic", 63455425)
teacher3 = Teacher("Milan", "Kovacevic", 622125587)

list1 = []
list1.append(trustee1)
list4 = []
list4.append(trustee2)
list5 = []
list5.append(trustee3)
list6 = []
list6.append(trustee4)
list8 = []
list8.append(trustee5)
list9 = []
list9.append(trustee6)
list10 = []
list10.append(trustee7)

child1 = Child(123456789, "Ana", "Kovacevic", "female", datetime.date(2012, 1, 30), "Radanska 18", list1)
child2 = Child(122334455, "Marta", "Kovacevic", "female", datetime.date(2014, 6, 15), "Radanska 18", list1)
child3 = Child(133564898, "Lazar", "Kovacevic", "male", datetime.date(2016, 7, 15), "Radanska 18", list1)
child4 = Child(324566789, "Ilija", "Petrovic", "male", datetime.date(2013, 7, 25), "Visegradska 45", list4)
child5 = Child(322115674, "Lana", "Markovic", "female", datetime.date(2014, 11, 12), "Petra Dobrnjca 23", list5)
child6 = Child(432156789, "Andjela", "Zdravkovic", "female", datetime.date(2017, 9, 13), "Knjazevacka 101/34", list6)
child7 = Child(432445566, "Nikola", "Zdravkovic", "male", datetime.date(2015, 1, 23), "Knjazevacka 101/34", list6)
child8 = Child(543276886, "Petar", "Miletic", "male", datetime.date(2014, 3, 24), "G.B.Jankovica 34", list8)
child9 = Child(232422211, "Irena", "Markovic", "female", datetime.date(2018, 3, 21), "Durmitorska 32", list9)
child10 = Child(657893847, "Ivona", "Aleksic", "female", datetime.date(2014, 7, 19), "Durmitorska 32", list10)

children_list = [child1, child2, child3, child4, child5, child6, child7, child8, child9, child10]

child_teacher = {child1:teacher1, child2:teacher1, child3:teacher2, child4:teacher1, child5:teacher2,\
    child6:teacher3, child7:teacher2, child8:teacher1, child9:teacher3, child10:teacher2}
    
teacher_list = [teacher1, teacher2, teacher3]

