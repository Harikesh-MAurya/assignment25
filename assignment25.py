# 1. Write a python script to create a Profile class with 3 attributes (name, email, age).
# 2. Write a python script to update the above Profile class with encapsulation.
# 3. Write a python script to update 2nd Question, change email and age to __email and
# __age.
# 4. Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.
# 5. Write a python script to create a Calculator class with 2 methods for adding and
# subtracting 2 values.
# 6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
# and division of 2 values and inherit it from the Calculator class.
# 7. Write a python script to create a Phone class with 2 methods to print the features
# (calling and sms).
# 8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
# Phone Class.
# 9. Write a python script to create an application like Truecaller where names and
# numbers are stored. Truecaller class will have 2 methods (1st to fetch the name of a
# number and 2nd to add a new entry).
# 10. Write a python script to add the new method in SmartPhone class which accepts
# Truecaller object as a parameter and call the fetch method of Truecaller


# 1) .................................................
# class Profile:
#     def __init__(self,name,email,age) -> None:
#         self.name=name
#         self.email=email
#         self.age=age
        
#     def show(self):
#         return (self.name,self.email,self.age)
    
    
# p1=Profile('harikesh','xyz@gmail.com',18)
# print(p1.show())


# 2) .................................................
# class Profile:
#     def __init__(self,name,email,age) -> None:
#         self.name=name
#         self.email=email
#         self.age=age
        
#     def show(self):
#         return (self.name,self.email,self.age)
    
#     def input_profile(self):
#         self.name=input("Enter another name : ")
#         self.email=input("Enter new email : ")
#         self.age=int(input("Enter new age : "))
    
# p1=Profile('harikesh','xyz@gmail.com',18)
# print(p1.show())

# p1.input_profile()
# print(p1.show())


# 3)...............................................
# class Profile:
#     def __init__(self,name,__email,__age) -> None:
#         self.name=name
#         self.email=__email
#         self.age=__age
        
#     def show(self):
#         return (self.name,self.email,self.age)
    
#     def input_profile(self):
#         self.name=input("Enter another name : ")
#         self.email=input("Enter new email : ")
#         self.age=int(input("Enter new age : "))
#         return Profile(self.name,self.email,self.age)
    
# p1=Profile('harikesh','xyz@gmail.com',18)
# # print(p1.__age) # it show attribute error and not easily exicutable
# print(p1.show())

# p1.input_profile()
# print(p1.show())


# 4) ...................................................

# from platform import platform
# class Profile:
#     platform=10
#     def __init__(self,n,e,a) -> None:
#         self.n=n
#         self.e=e
#         self.a=a
        
#     def show_init(self):
#         return(self.n,self.e,self.a)
#     @classmethod
#     def func_access_class_variable(cls):
#         print(cls.platform)
        
# p1=Profile("harikesh",'xcv@gmail.com',20)
# print(p1.show_init())
# p1.func_access_class_variable()


# 5) ....................................................
# class calculator:
#     def __init__(self,num1,num2) -> None:
#         self.num1=num1
#         self.num2=num2
        
#     def __add__(self,other):
#         total_num1=self.num1 + other.num1
#         total_num2=self.num2 + other.num2
#         c3=calculator(total_num1,total_num2)       
#         return c3
            
#     def __sub__(self,other):
#         total_num1=self.num1 - other.num1
#         total_num2=self.num2 - other.num2
#         c4=calculator(total_num1,total_num2)       
#         return c4
    
#     def show_addition(self):
#         print(self.num1+self.num2)
        
#     def show_substraction(self):
#         print(self.num1-self.num2)

# print("Enter number for first : ")
# c1=calculator(int(input("Enter num1 : ")),int(input("Enter num2 : ")))
# print(c1.show_addition())
# print(c1.show_substraction())

# print("Enter number for second : ")
# c2=calculator(int(input("Enter num1 : ")),int(input("Enter num2 : ")))
# print(c2.show_addition())
# print(c2.show_substraction())


# 6) ..........................................................
# class calculator:
#     def __init__(self,num1,num2) -> None:
#         self.num1=num1
#         self.num2=num2
        
#     def __add__(self,other):
#         total_num1=self.num1 + other.num1
#         total_num2=self.num2 + other.num2
#         c3=calculator(total_num1,total_num2)       
#         return c3
            
#     def __sub__(self,other):
#         total_num1=self.num1 - other.num1
#         total_num2=self.num2 - other.num2
#         c4=calculator(total_num1,total_num2)       
#         return c4
    
#     def show_addition(self):
#         print(self.num1*self.num2)
        
#     def show_substraction(self):
#         print(self.num1/self.num2)

# print("Enter number for first : ")
# c1=calculator(int(input("Enter num1 : ")),int(input("Enter num2 : ")))
# print(c1.show_addition())
# print(c1.show_substraction())

# print("Enter number for second : ")
# c2=calculator(int(input("Enter num1 : ")),int(input("Enter num2 : ")))
# print(c2.show_addition())
# print(c2.show_substraction())


# 7) .......................................................
# class Phone:
#     def __init__(self) -> None:
#         self.str1=""
#         self.str2=""
        
#     def get_feature(self):
#         self.str1=input("Enter Calling feature : ")
#         self.str2=input("enter SMS feature : ")
        
        
#     def print_feature(self):
#         print(self.str1.upper())
#         print(self.str2.upper())
        
# p1=Phone()
# p1.get_feature()
# p1.print_feature()


# 8) ............................................................
# class Calculator:
#     def __init__(self,num1,num2) -> None:
#         self.num1=num1
#         self.num2=num2
        
#     def  multiply(self):
#         print(self.num1 * self.num2)
        
#     def division(self):
#         print(self.num1 / self.num2)
        
# class Phone:
#     def __init__(self) -> None:
#         self.str1=''
#         self.str1=''
        
#     def get_feature(self):
#         self.str1=input("Enter feature 1 : ")
#         self.str2=input("Enter feature 2 : ")
        
#     def print_fearture(self):
#         print(self.str1,self.str2)
        
# class SmartPhone:
#     c1=Calculator(int(input("Enter num1 : ")),int(input("Enter num2 : ")))
#     c1.multiply()
#     c1.division()
    
#     c2=Phone()
#     c2.get_feature()
#     c2.print_fearture()


# 9) .......................................................................
l1=[]
class Truecaller:
    def __init__(self,name,number) -> None:
        self.name=name
        self.number=number
        
    def print_detail(self):
        l1.append(self.name)
        l1.append(self.number)
        print(l1)
        
while True:  
    ans=input("enter for first name and number [y/n]: ")  
    if ans=='y':
        t1=Truecaller(input("Enter name : "),int(input("Enter number : "))) 
        t1.print_detail()
        while True:
            ans=input("Enter y for new entry and n for break the loop [y/n] : ")
            if ans=='y' or ans=='Y':
                t2=Truecaller(input("Enter new name : "),int(input("Enter new number : ")))
                t2.print_detail()
            else:
                break
    