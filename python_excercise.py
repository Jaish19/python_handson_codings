# 1.	Consider a list whose elements are 1..10, iterate this list and display the output as follows, 
# (' 1', '  1', '  1')
# (' 2', '  4', '  8')
# (' 3', '  9', ' 27')
# (' 4', ' 16', ' 64')
# (' 5', ' 25', '125')
# (' 6', ' 36', '216')
# (' 7', ' 49', '343')
# (' 8', ' 64', '512')
# (' 9', ' 81', '729')
# ('10', '100', '1000')

def task_one(i):
    for i in l1:
        yield (i,i**2,i**3)
    
 
l1=range(10)
nok=task_one(l1)

for i in nok:
    print(i)

# 2.	Create a pyramid with stars. Get the input number from user. Say user enters “9”. Then It must display like below..
#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************

def pyramid(rows):
    for i in range(rows):
        yield ' '*(rows-i-1) + '*'*(2*i+1)
        

star=pyramid(10)
for i in star:
    print(i)


   # 3.	Write a Python program which accepts the radius of a circle from the user and compute the area. (think what is the Area of the circle formula)

   def area(pi, radius):
    print(pi, radius)
    return pi*(radius**2)

val=area(float(raw_input()),int(raw_input()))
print(val)

# 4.	Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. 
# a.	Example: if user enters “Sanjay” as First name and “Pradeep” as Last name, the output should be  “Pradeep Sanjay”

i=map(str, raw_input().split())
print(" ".join(i[::-1]))

# 5.	Write a Python program to display the first and last colors from the following list. Go to the editor color_list = ["Red","Green","White" ,"Black"] 

k=map(str, raw_input().split())
c=[0,-1]
for i in c:
    print(k[i])

#  6.	Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn+nnnn..
# a.	Sample value of n is 5 
# b.	Expected Result : 615


class formula(object):
    
    def __init__(self,a):
        self.a=a
        
    def calc(self):
         return (self.a+self.a*self.a+self.a*self.a*self.a)
        
        
        
class inpt(formula):
    def __init__(self):
        pass
    
    def user(self):
        user_input=int(raw_input())
        obj=formula(user_input)
        print(obj.calc())
    
new=inpt()
new.user()


# 7.	Write a Python program to get the volume of a sphere with radius 6. 

def volume(radius):
    return (1.33*3.14*radius)

def output(c):
    print("output is:",c)


output(volume(int(raw_input("please enter the value:"))))

# 8.	Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference
# Best example program for creating object for another from base class constructor:
class case(object):
    def __init__(self,b):
        
        pass
        
    def condition_two(self,i):
        return 17-i
    def condition_three(self,j):
        return j-17

class difference(object):
    def __init__(self,a,pm):
        self.a=a
        self.pm=pm # case class object as assigned
        
    def condition_one(self):
        
        if self.a<17:
            
            print("Returned condition two is:",self.pm.condition_two(self.a))
        else:
            print("returned condition three output is:",self.pm.condition_three(self.a))
            
       
# Get the input from user
userInput=int(raw_input("enter the value:"))
# Creating object for Case class
pm=case(userInput)
# passing a case object as parameter of difference class
obj=difference(userInput,pm)
obj.condition_one()



# 9.	Write a Python program to test whether a number is within 100 of 1000 or 2000.
def find_number():
    if int(raw_input("Enter the value:")) in range(100,1000,100):
        print("yes..")
    else:
        print("No..")
        
        
find_number()

# 10.	Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.


class equal(object):
    def __init__(self,a):
        self.a=a
        print(self.a)
    def check(self):
        count=0
        for i in range(len(self.a)-1):
            if self.a[i]==self.a[i+1]:
                count=count+1
            else:
                pass
        if len(self.a)-1==count:
             yield sum(self.a)
        else:
            for i in range(3):
                yield sum(self.a)
        
class three_num(equal):
    def __init__(self):
        pass
    def add(self):
        userInput=map(int,raw_input("Enter your inputs:").split())
        super(three_num,self).__init__(userInput)
               
        
        
obj=three_num()
obj.add()
c=obj.check()
for i in c:
    print("Values are:",i)



# 11.	Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

userInput=str(raw_input("Enter the value:"))
val=list(str(userInput))
print(val)
if val[0]=='l'and val[1]=='s':
    print("No need of any change")
else:
    val.insert(0,'Mr.')
    
print("".join(val))
    
  # 12.	Write a Python program to get a string which is n (non-negative integer) copies of a given string 
class state_three(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def operation(self):
        for i in range(self.y):
            print(self.x)
            
        
        
class state_two(state_three):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        super(state_two,self).__init__(a,b)
    
    def measure(self):
        print("Enter input string:",self.a)
        print("enter the clock cycle count:",self.b)


class state_one(state_two,state_three):
    def __init__(self,ip,length):
        self.ip=ip
        self.length=length
        super(state_one,self).__init__(ip,length)
        
    
    
obj=state_one(str(raw_input('Enter the string here:')), int(raw_input("Enter the clock cycles:")))
obj.measure()
obj.operation()

print(state_one.mro())


# 13. Write a Python program to test whether a passed letter is a vowel or not.

val=raw_input("Enter a letter:")
vowels=['a','e','i','o','u']
if val in vowels:
    print("yess")
else:
    print("no")


# 14. Write a Python program to concatenate all elements in a list into a string and return it. 


class concatination(object):
    def __init__(self,c):
        self.c=c
        
    def first_half(self,cur,km):
        l=''
        for i in self.c[km:]:
            l=l+i
            
        pur="".join(l)
        
        return cur + pur

    
    def second_half(self):
        km=len(self.c)/2
        k=''
        for i in self.c[:km]:
            k=k+i
        cur="".join(k)   
        print(obj.first_half(cur,km))


obj=concatination(['a','b','c','d'])
obj.second_half()


# 15. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence


k=[]

def deliever(func):
    def jost(i):
        func(i)
    return jost
        
def operation(func):
    def wrapper(value):
        for i in value:
            if i%2==0 and i<237:
                func(i)
            else:
                pass
    return wrapper


@operation
@deliever
def final(value):
    k.append(value)
    
    
final(range(300))
print(k)


----------------------------------------------------------------------------------------------------------------
# 17. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2
# a.  Test Data : 
# color_list_1 = set(["White", "Black", "Red"]) 
# color_list_2 = set(["Red", "Green"])
# Expected Output : 
# {'Black', 'White'} 

def func_base(func):
    def root(j,u):
        if j in u:
            func(j)
        else:
            pass

    return root
def func_one(func):
  
    def chast(l,k):
        print(l,k)
        for i in l:
            func(i,k)
        
    return chast


@func_one
@func_base
def func_two(l):
    s.append(l)
    
  
s=[]    
inp_one=set(map(str,raw_input("Enter one value:").split()))
inp_two=set(map(str,raw_input("Enter two value:").split()))
func_two(inp_one,inp_two)
# func_two(inp_one,inp_two)
print(s)

-------------------------------------------------------------------------------------------------
 # 18.    Write a Python program that will accept the base and height of a triangle and compute the area. 

def decorate(func):
    def charge(self,a,b,c):
        func(self)
    return charge
    
class triangle(object):
    b=5
    _b=8
    __b=27
    def __init__(self,x,y,z):
        self.x=x
        self._y=y
        self.__z=z
    @decorate    
    def operation(self):
        print("Operation is:",self.x,self._y,self.__z)
        
    def __moreSecured(self):
        val=self.x+self._y+self.__z
        solution=val+obj.__b
        return solution

l,b,h=map(int,raw_input('Enter your Length,Breath and Height values:').split(" "))  

obj=triangle((l),(b),(h))  
obj.operation(l,b,h)
# obj._triangle__moreSecured()
print("Triangle operation value is:",obj._triangle__moreSecured())


----------------------------------------------------------------------------------

# 21. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 

def decorate(func):
    def change(self,a,b):
        func(self,a,b)
    return change
class simple(object):
    b=10
    _b=25
    __b=2
    
    def __init__(self,x,y):
        self.x=x
        self.__y=y
    @decorate   
    def orderOne(self,a,b):
        n=self.x+obj.b
        print(n)
        return n
    
    
a=5
b=5
obj=simple(a,b)
c=obj.orderOne(5,2)
print("Inside class b values,",obj.b)
print("Inside class b values,",obj._simple__b)
print("am returned value",c)
if c>=15 and c<=20:
    print("Value is 20")
else:
    print("value is",c)        
            
        
    
    ---------------------------------------------------------------------

# 24.  Write a Python program to check whether a file exists

import os
open('general.txt')
print(os.path.isfile('general.txt'))

-------------------------------------------------------------------------------

# 25. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import struct
print(struct.calcsize("P") * 8)

----------------------------------------------------------------------------------------------

# 26. Write a Python program to get OS name, platform and release information. 

import platform
import os
print(os.name)
print(platform.system())
print(platform.release())
-------------------------------------------------------------
# 27. Write a Python program to check if a string is numeric.

class check_input(object):
    def __init__(self,a,b):
        self.a=a
        self._b=b
    def type_input_three(self,x,y):
        print("type of new and text is",x,y)
        
        
    def type_input_two(self,a,b):
        new=type(a)
        next=type(b)
        obj.type_input_three(new,next)
        
        
obj=check_input('suresh',5)
obj.type_input_two('suresh',7)

-----------------------------------------------------------------------------------

# 28. Write a Python program to check if a number is positive, negative or zero.

class check_one(object):
    def __init__(self):
#         self.c=c
        pass
    def status(self,n):
        print("its proved",n)
        
    def not_status(self,m):
        print("its negative",m)
        
    def zero_status(self,j):
        print("Its zero value",j)
    
    
        
        
class check_two(check_one):
    def __init__(self,k):
        self.k=k
        
    def choke(self):
        if self.k>0:
            super(check_two,self).status(self.k)
        elif self.k<0:
            super(check_two,self).not_status(self.k)
        else:
            super(check_two,self).zero_status(self.k)



class check_three(check_two):
    def __init__(self,val):
        self.val=val
        super(check_three,self).__init__(val)
        
        
obj=check_three(0)
obj.choke()
        
 
---------------------------------------------------------------------------------------
# 29. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.


METHOD 1:

def divisible_by_fifteen(n):
     
     for i in n:
        if i%5==0:
            yield i 
        else:
            pass

    
l1=[5,15,20,14,7,84,95,7,4,2,25]

cnts=divisible_by_fifteen(l1)
for c in cnts:
    print("its divisible",c)

------------------------------------------------------------------------------------------

METHOD 2:

def divisible(val):
    if val%15==0:
        return val
    else:
        pass


l1=[25,5,45,55,85,44,77,66,25,95,60,90]
# coll=divisible(l1)
coll=list(map(divisible,[25,5,45,55,85,44,77,66,25,95,60,90]))
print("Divisible by 15 is:",coll)

METHOD 3:

coll=list(filter(lambda x: (x%15==0),[25,45,90,55,60]))
print(coll)

METHOD 4:

l1=[1,2,3,4,5,10,15,85]

print(filter(lambda x: x==3 or x==5, l1))

Method 4:

def mul(x):
    return (x*x)

def add(x):
    return (x+x)


func=[mul,add]
for i in range(5):
    value=map(lambda x:x(i),func)
    print(value)

METHOD 5:

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

--------------------------------------------------------------------

# 31. Write a Python program to compute the product of a list of integers (without using for loop)

l1=[1,2,3,4,5]
coll=(reduce(lambda x,y:x*y,l1))
print("product of a list",coll)



==============================================================================================================================
------------------------------------------DICTIONARY EXCERCIZE-----------------------------------------------------------
==============================================================================================================================

# GENERIC EXAMPLE:
---------------------

d1={'name':'jai','Age':24,'Gender':'M'}
for k,v in d1.items():
    print(k,v)

---------------------------------------

# 1.	Write a Python script to sort (ascending and descending) a dictionary by value.


# EXACT ANSWER:

import operator
jai={'A':85,'C':98,'D':68,'B':74,'E':21}

print("original order",jai)
sorted_one=sorted(jai.items(),key=operator.itemgetter(1))  # if (1)---Value, (0)---Key
print("Ascending order",sorted_one)
sorted_two=sorted(jai.items(),key=operator.itemgetter(1),reverse=True)
print("decending order",sorted_two)
------------------------------------------------------------------------------
# FOR ASCENDING
mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
    print (key +":"+str(value))

# FOR DECENDING

mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (-v,k)):
    print (key +":"+str(value))
------------------------------------------------------------------

 # 1.1 Write a Python script to sort (ascending and descending) a dictionary by key.

 mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (k,v)):
    print (key +":"+str(value))

-------------------------------------------------------------


# 2.	Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x) 
# 3.	Sample Dictionary ( n = 5) : Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 

print({x: x*x for x in range(5)})

# TYPE 2:

c={x*x: x for x in range(6) if x%2==1}
print(c)


# 4.	Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 
# Sample Dictionary 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

print({x: x*x for x in range(16)})


# 5.	Write a Python program to sum all the VALUES in a dictionary


jai={'A':8,'B':98,'C':85,'D':55}
print(sum(jai.values()))


# SAMPLE CODE:

l1=[1,1,1,5,2,5,8,4,5,3,3]
d1={}
for i in l1:
    d1[i]=l1.count(i)
    
print(d1)

----------------------------------------------------------------
# 6.	Write a Python program to multiply all the items in a dictionary 


jai={'A':8,'B':98,'C':85,'D':55}
cet=jai.values()
c=1
for i in cet:
    c=c*i
    						
print("Multiplication value of dictionary items:",c)

---------------------------------------------------------------------
# 7.	Write a Python program to remove a key from a dictionary.

jai={'A':8,'B':98,'C':85,'D':55}
for k,v in jai.items():
    del jai[k]
    
print(jai)

-------------------------------------------------------------------

# 8. Write a Python program to map two lists into a dictionary

l1=['a','b','c']
l2=[1,2,3]
print(dict(zip(l1,l2)))



-----------------------------------------------------------------------
# 9.	Write a Python program to sort a dictionary by key. 

# METHOD ONE:

import operator
jai={'A':8,'B':98,'C':85,'D':55}

sorted_key=sorted(jai.iteritems(), key=operator.itemgetter(0))
print("Ascending order:",sorted_key)
sorted_ano=sorted(jai.iteritems(),key=operator.itemgetter(0),reverse=True)
print("Decending Order:",sorted_ano)

# METHOD TWO:

import operator
jai={'A':8,'C':85,'D':55,'B':98}

for key,value in sorted(jai.iteritems(),key=lambda(k,v):(k,v)):
    print(key,value)

# METHOD THREE:

import operator
jai={'A':8,'B':98,'C':85,'D':55}

for key,value in sorted(jai.iteritems(),key=lambda(k,v):(v,k)):#(-v,k)----->for decending order
    print(key,value)

-------------------------------------------------------------------------------------------

# 10.	Write a Python program to get the maximum and minimum value in a dictionary 

#SAMPLE 1
stats={'A':8,'B':98,'C':85,'D':55}
chance=[(value,key) for key,value in stats.items()]
print("Maximum values are:",max(chance))
print("Minimum values are:",min(chance)) 


#SAMPLE 2
my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])


------------------------------------------------------------------





