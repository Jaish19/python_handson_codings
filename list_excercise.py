# ques 1  1. Write a Python program to sum all the items in a list.

l1=[1,2,3,4,5]
sum(l1)

# ques 2 . Write a Python program to multiplies all the items in a list

j=1
l1=[1,2,3,4,5]
for i in l1:
    j=j*i
    
print(j)
    

# 3. Write a Python program to get the largest number from a list.
l1=[1,5,4,7,8,9]
print(max(l1))

# 4. Write a Python program to get the smallest number from a list.
l1=[1,5,4,7,8,9]
print(min(l1))

# own task

l1= ['abc', 'xyz', 'aba', '1221']
check=[]
for i in l1:
    print(len(str(i)))
    check.append(len(str(i)))
   
print(check)
          
# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

l1= ['abc', 'xyz', 'aba', '1221','515','jaish']

count=0
for i in l1:
    
    c=list(str(i))
    
    if c[0]==c[len(c)-1]:
        count=count+1
    
print("Total Number of repetition:",count)
    
          
# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# METHOD 1
l1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l2=[]
for n in l1:
    i=list(n)
    if i[0]>i[1]:
        temp=i[0]
        i[0]=i[1]
        i[1]=temp
        l2.append(tuple(i))
    else:
        l2.append(tuple(i))
        
print(l2)

# METHOD 2

l1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
l2=[]
for n in l1:
    i=list(n)
    i.sort()
    l2.append(tuple(i))
        
print(l2)
        
        
    
# 7. Write a Python program to remove duplicates from a list.

# method 1
l2=[2,2,8,8,5,4,5]
c=set(l2)
print(c)

# method 2 using counter

from collections import Counter
l2=[5,5,8,6,6,8,8,1,2,3,9]
counts=Counter(l2)
l3=[]
print(counts)
for k,v in counts.items():
    l3.append(k)
  
print(l3)


# 8. Write a Python program to check a list is empty or not.

l2=[5]
print(len(l2))
if len(l2)==0:
    print("its empty")

 # 9. Write a Python program to clone or copy a list.

 l1=[1,2,3,4,5]
 l2=[]
 l2=l1

 # 10. Write a Python program to find the list of words that are longer than n from a given list of words.

 l1=['abc','jaiganesh','suresh']
l2=raw_input("user!!enter the input:").split()

for i in range(len(l1)):
    if len(str(l1[i]))<len(str(l2[i])):
        print("In the above list",str(l1[i]),"is greater than ",str(l2[i]))
    else:
        pass

# sample ip and op:
# user!!enter the input:jai suresh vijayakumar
# ('In the above list', 'suresh', 'is greater than ', 'vijayakumar')


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
# method 1
l1=set(raw_input("enter l1:").split())
l2=set(raw_input("enter l2:").split())
found=False
print(l1.symmetric_difference(l2), len(l1.symmetric_difference(l2)))
if len(l1.symmetric_difference(l2))>0:
    print("TRUE")

 # method 2

 l1=[1,2,3,4,5]
l2=[2,8,9,6,7] 
for i in range(len(l1)):
    if l1[i] in l2:
        print("yes")
        break
    else:
        pass
  
    
# 12. Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

l1=['jai','idiid','green','black','oragne','pink']
l2=[0,1,3]
for i in l2:
    l1.remove(l1[i])
    
print(l1)
    

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

l1=[1,2,3,4,5,6,7,8,9]
for i in l1:
    if i%2==0:
        l1.remove(i)
        
print(l1)

# Write a Python program to shuffle and print a specified list.**********************

# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def square(a):
    return a**2


l1=[]
count=0
for i in range(1,31):
    count=count+1
    if count<=5 or count>=25:
        l1.append(square(count))
    else:
        l1.append(count)
        
print(l1)


# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

def square(a):
    return a**2


l1=[]
count=0
for i in range(1,31):
    count=count+1
    if count<=5 or count>=25:
        l1.append(count)
    else:
        l1.append(square(count))
        
print(l1)


# 18. Write a Python program to generate all permutations of a list in Python.

from itertools import *
l1=[1,2,3,4,5]
l2=[7,8,9,4,5]
c=product(l1,l2)
for i in c:
    print(i)


 # 19.Write a Python program to get the difference between the two lists.

# method 1
 l1=set([1,2,3,4,5])
l2=set([7,8,9,4,5])

print(l1.symmetric_difference(l2))

# method 2

l1=[1,2,3,4,5]
l2=[7,8,9,4,5]
l3=[]
for i in range(len(l1)):
    if l1[i]!=l2[i]:
        l3.extend([l1[i],l2[i]])
l3.sort()
print(l3)


# 20. Write a Python program access the index of a list.

l1=[1,2,6,5,9,70]
for i in l1:
    print(l1.index(i),'=',i)


 # 21. Write a Python program to convert a list of characters into a string.

 l1=map(int, raw_input("user enter the values:").split())
print(l1)
l2=[]
for i in l1:
    l2.append(str(i))
    
print(l2)

# 22. Write a Python program to find the index of an item in a specified list.

l1=map(int, raw_input("user enter the values:").split())
find=raw_input("user enter the value to find:")

for i in l1:
    if i==int(find):
        print("user the index of your entered value is", l1.index(i))
    else:
        pass

# 23. Write a Python program to flatten a shallow list.*************************


# 24. Write a Python program to append a list to the second list.

l1=[1,2,3,5,4]
l2=[]
for i in l1:
	l2.append(i)
print(l2)

# 25. Write a Python program to select an item randomly from a list.*****************

# 26. Write a python program to check whether two lists are circularly identical.

l1=[1,2,3,5,4]
l2=[1,2,3,5]
if l1==l2:
    print("true") 

# 27. Write a Python program to find the second smallest number in a list.

l1=[1,2,3,5,4]
l1.remove(min(l1))
print("Second smallest number in the list",min(l1))   

# 28. Write a Python program to find the second largest number in a list.

l1=[1,2,3,5,4]
l1.remove(max(l1))
print("Second largest number in the list",max(l1))   

# 29. Write a Python program to get unique values from a list.*********************

# 30. Write a Python program to get the frequency of the elements in a list.

l1=[1,2,3,5,4,1,1,13,3,5]
for i in l1:
    print("count of",i,"is",l1.count(i))

# 31. Write a Python program to count the number of elements in a list within a specified range.

l1=[1,2,3,5,4,1,1,13,3,5]
for i in l1:
    print("count of",i,"is",l1.count(i))

# 32. Write a Python program to check whether a list contains a sublist.

 l1=[1,2,3,5,4]
l1.append([2,3])
for i in range(len(l1)):
    if type(l1[i])==int:
        pass
    else:
        print("Above list contains list inside")

# 33. Write a Python program to generate all sublists of a list.

# method 1
l1=[1,2,3,5,4]
l1.append([2,3])
for i in l1:
    if type(i) is int:
        print(i)
    else:
        for j in i:
            print(j) 

# method 2
 
l1=[1,2,3,5,4]
l1.append([2,3])
for i in l1:
	print(i)


# 34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
# Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any given limit.

def steve_parenthesis(n):
    prime_list=[]
    for i in range(2,n+1):
        if i not in prime_list:
            print(i)
            for j in range(i*i, n+1,i):
                prime_list.append(j)
            
            
            
print(steve_parenthesis(100))
    




    
    

