import datetime

class Person():    # Creating base class Person
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self):
        return f"Person class object with first_name = <{self.first_name}>, last_name = <{self.last_name}>"
        
    def __repr__(self):
        return f"Person class object <{self.first_name} {self.last_name}>"
        
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

   
class Child(Person):    # Creating Child class inherited from Person class

    def __init__(self, id, first_name, last_name, gender, birthdate, address, trustee_list=[]):
        super().__init__(first_name, last_name)
        self.id = id
        self.gender = gender
        self.birthdate = birthdate
        self.address = address
        self.trustee_list = trustee_list
        
    def __str__(self):
        return f"Child class object with first_name = <{self.first_name}>, last_name = <{self.last_name}>"
        
    def __repr__(self):
        return f"Child class object <{self.first_name} {self.last_name}>"
        
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    @classmethod
    def header(cls):
        print(f"ID        Last Name       First Name      Age   Trustee Last and First name      Type  Phone number")
        print("=" * 100)

    @classmethod
    def printChildren(cls, children):
        Child.header()
        for i in children:
            trustee_all = ""
            for n in i.trustee_list:
                trustee = n
                trustee_all = trustee_all + f"{trustee.last_name.ljust(15)} {trustee.first_name.ljust(15)} {trustee.type} 0{str(trustee.phone)}"
            print(f"{str(i.id).ljust(9)} {i.last_name.ljust(15)} {i.first_name.ljust(15)} {str(i.age()).ljust(5)} {trustee_all}")
        print("_" * 100)


class Trustee(Person):    # Creating Trustee class inherited from Person class

    def __init__(self, first_name, last_name, type, phone):
        super().__init__(first_name, last_name)
        self.type = type
        self.phone = phone
        
    def __str__(self):
        return f"Trustee class object with first_name = <{self.first_name}>, last_name = <{self.last_name}>"
        
    def __repr__(self):
        return f"Trustee class object <{self.first_name} {self.last_name}>"


class Teacher(Person):    # Creating Teacher class inherited from Person class

    def __init__(self, first_name, last_name, phone):
        super().__init__(first_name, last_name)
        self.phone = phone
        
    def __str__(self):
        return f"Teacher class object with first_name = <{self.first_name}>, last_name = <{self.last_name}>"
        
    def __repr__(self):
        return f"Teacher class object <{self.first_name} {self.last_name}>"
   
def header():    #  Function for nicer printing output
    print(f"ID        Last Name       First Name      Age   Trustee Last and First name      Type  Phone number")
    print("=" * 100)
         
def printChildrenOut(children):    #  Function for printing list of children
    header()
    for i in children:
        trustee_all = ""
        for n in i.trustee_list:
            trustee = n
            trustee_all = trustee_all + f"{trustee.last_name.ljust(15)} {trustee.first_name.ljust(15)} {trustee.type} 0{str(trustee.phone)}"
        print(f"{str(i.id).ljust(9)} {i.last_name.ljust(15)} {i.first_name.ljust(15)} {str(i.age()).ljust(5)} {trustee_all}")
    print("_" * 100)
    
def header_teacher():    #  Function for nicer printing output
    print(f"ID        Child Last and First Name       Teacher Last and First name     Phone ")
    print("=" * 100)
    
def printChildrenTeacher(dictionary):    #  Function for printing list of connection children - teacher
    header_teacher()
    for k, v in dictionary.items():
        print(f"{str(k.id).ljust(9)} {k.last_name.ljust(15)} {k.first_name.ljust(15)} {v.last_name.ljust(15)} {v.first_name.ljust(15)} 0{v.phone}")