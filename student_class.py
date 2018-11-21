# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 19:38:34 2018

@author: tancr
"""

#%%
"White Belt"
# =============================================================================
# 
# Create a Student class that has the following attributes:
# 
# name
# last name
# age
# master (either MCSBT or MDBI)
#  Make sure you parametrize all those fields in the constructor.
# 
# =============================================================================

class student:
    
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
#        
#    def info(self, student):
#        if self.name == student:
#            print(self.name + self.last_name + self.age + self.master)
#            
        
    
student1 = student("Javier","Fernandez", 24, "A soon to be proud MCSBT")

#%%

'Blue Belt'

# =============================================================================
# Add a print_student method in the Student class that prints a line like follows for the object
# 
# 
# Pepe García is a 55 year old student of the MCSDBI masters programme
# 
#  
# 
# Create a list of all 28 Students representing all students in this class.  Then iterate over all of them and call print_student on each one to print its description.
# 
# =============================================================================

class student:
    
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
#        
#    def info(self, student):
#        if self.name == student:
#            print(self.name + self.last_name + self.age + self.master)

 
class Master:
    
    master_students = []
    
    def __init__(self, name):
        self.name = name
                
    def add_master_students_list(self, master_students_list):
        self.master_students += master_students_list
        
    def print_student(self):
        for student in self.master_students:      
            print(student.name + " is a "+ student.age + " years old student of the " + student.master + " masters program")      
         
mcsbt = Master("mcsbt")

master_students_list = [
    student("Alejandro", "Meneses", "27", "MCSBT"),
    student("Agata", "Kaczmarek", "31","MDBI"),
    student("Anastasia", "Lasunina", "25", "MDBI"),
    student("Anikken", "Barstad","27", "MDBI"),
    student("Candela", "Noya", "24", "MDBI"),
    student("Daniil", "Osipov", "21", "MDBI"),
    student("David", "Barrero Gonzalez", "31", "MCSBT"),
    student("Edem", "Francois", "28", "MCSBT"),
    student("Eduardo", "Paraja", "23", "MDBI"),
    student("Florian", "Diegruber", "25", "MCSBT"),
    student("Hannah", "Oldorf", "23", "MCBT"),
    student("Isabella", "Rosenthal", "27", "MDBI"),
    student("Javier", "Fernandez", "24", "MCSBT"),
    student("Lukas", "Hauser", "28","MDBI"),
    student("Leila", "Tazi", "27", "MCSBT"),
    student("Laura", "Kageneck", "23", "MCSBT"),
    student("Monica", "Alvarenga","28", "MDBI"),
    student("Natalie", "Cedeno", "26", "MDBI"),
    student("Octavio", "Ramírez", "28", "MDBI"),
    student("Tancredi", "Bernard", "21", "MCSBT"),
    student("Yasmine", "Lyagoubi", "23", "MDBI"),
    ]

mcsbt.add_master_students_list(master_students_list)

mcsbt.print_student()

#class student_list:
#    
#    lst = []
#        
#    def __init__(self, name):
#        self.name = name
#        
#    def add_member(self, member):
#        self.lst.append(member)
#        
#    def add_member_list(self, member_list):
#        self.lst += member_list
#
#mcsbt = student_list("master")
#lst = [Member("Fernandez","Javier"),
#Member("","bass"),
#Member("John","sings"),
#Member("George", "guitar")]
#
#beatles.add_member_list(members)
#



































