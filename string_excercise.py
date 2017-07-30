# 1. Write a Python program to calculate the length of a string. 

l1='jai'
print(len(l1))

# 2. Write a Python program to count the number of characters (character frequency) in a string.  
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

from collections import Counter
l1='jai'
print(list(str(l1)))
count=Counter(list(str(l1)))
print(count)

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.  
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String 


# l1='w3resource'
l1='w2'
if len(l1)>=2:
    print(l1[0:2]+l1[len(l1)-2:])
else:
    print("its empty string")
   
    
#  4. Write a Python program to get a string from a user,  where all occurrences of its first char have been changed to '$', except the first char itself.  
# Sample String : 'restart'
# Expected Result : 'resta$t'

# Trying code:

l1='jaiganesh'

spt=list(str(l1))
c=''
for i in spt:
    c=c+i
print(c) 

# Trying code 2:
from collections import Counter
l1='jaishjs'

c=''
join_list=[]
for i in l1:
    if i not in join_list:
        join_list.append(i)
    else:
        join_list.append('@')
        
for i in join_list:
    c=c+i
    
print(c)
    
     
 OUTPUT:jaish@@

 # exact code 

 from collections import Counter
l1='jaishjs'

spt=[]
c=''
spt.append(l1[0])

for i in l1[1:]:
    if l1[0]==i:
        spt.append('@')
    else:
        spt.append(i)
        
for i in spt:
    c=c+i
print(c) 

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.  
# Sample String : ‘Sanjay’, 'Surya' 
# Expected Result : 'Sunjay Sarya'

l1=raw_input("Enter the string 1:")

l2=raw_input("Enter the string 2:")

print(l2[0:2]+l1[2:]+','+l1[0:2]+l2[2:])
#             
# INPUT:
# Enter the string 1:jai
# Enter the string 2:vijay
# OUTPUT:
# vii,jajay
#         
        
     
#  6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.  
# Sample String : 'abc'
# Expected Result : 'abcing' 
# Sample String : 'string'
# Expected Result : 'stringly'
    
l1='ft'
if len(l1)>=3:
    if(l1[-3:]=='ing'):
        print(l1[:]+'ly')
    else:
        print(l1[:]+'ing')
else:
    print("just printing  "+l1)


#  7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.  
# Sample String : 'The lyrics is not that poor!'
# Expected Result : 'The lyrics is good!'

# l1=['not','bad','poor']
# l3=['fuck','bullshit']
# l2=list((raw_input("enter the text:")).split())
# c=''
# for n,i in enumerate(l2):
#     if i in l1:
#         l2.remove(i)
#         l2.insert(n,'good')
#     elif i in l3:
#         l2.remove(i)
#         l2.insert(n,len(i)*'*')
        
# print(" ".join(l2))



# 8. Write a Python function that takes a list of words and returns the length of the longest one.  

def long(l1):
    l2=[]
    for i in l1:
        l2.append(len(i))
        
    
    return l1[l2.index(max(l2))]
   

l1=['jai','suresh','saraswathi','raji','vijay']
output=long(l1)
print(output)


# 9. Write a Python program to remove the nth index character from a nonempty string. 


l1='jai'
l2=list(str(l1))
val=int(raw_input("enter the value wanna remove:"))
l2.remove(l2[val])

print("".join(l2))

# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged. 

l1=list(str('jai'))
l3=list(str('jai'))
l2=list(str('vijay'))
print(len(l2))
for n,i in enumerate(l1):
    if n==0:
        l1.remove(i)
        l1.insert(n, l2[0])
    elif n==len(l1)-1:
        l1.remove(i)
        l1.insert(n,l2[-1])
        
for n,i in enumerate(l2):
    if n==0:
        l2.remove(i)
        l2.insert(n,l3[0])
        
    elif n==len(l2)-1:
        l2.remove(i)
        l2.insert(n,l3[-1])
        
print("".join(l1)+'  '+"".join(l2))
    
    
# INPUT:jai, vijay
# OUTPUT:vay, jijai

# 11. Write a Python program to remove the characters which have odd index values of a given string. 

l1=['jai','suresh','saraswathi','raji','vijay']

for n,i in enumerate(l1):
    if n%2==0:
        pass
    else:
        l1.remove(i)
        
print(l1)


# 12. Write a Python program to count the occurrences of each word in a given sentence. 

from collections import Counter
l1=raw_input("please enter the sentence:")
count=Counter(l1)
print(count)



# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases. 
userInput = raw_input("Enter a sentence, with different lower and upper cases").swapcase()

print (userInput) 


# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). 
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

userInput = ['red','white','black', 'red', 'green', 'black']
userInput.sort()
print (userInput)


# 15. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 
# Sample function and result : 
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses

userInput = raw_input("Enter a sentence")
print(userInput[-2:]*4)


# 16. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string. 
# Sample function and result : 
# first_three('ipysanjay') -> ipy
# first_three('python') -> pyt


def stringExer(come):
    if len(come)>3:
        c=come[0:3]
    else:
        pass
    return c
    
userInput='california'
c=stringExer(userInput)
print(c)


# 17. Write a Python function to get the first half of a specified string of even length. 
# Sample function and result : 
# string_first_half('Python') -> Pyt


def stringExer(come):
    count=len(come)//2
    c=come[0:count]
    return c
   
    
userInput='californiaa'
c=stringExer(userInput)
print(c)

# 18. Write a Python function to reverses a string if it's length is a multiple of 4. 


def stringExer(come):
    if len(come)%4==0:
        
        return come[::-1]
    else:
        print("its not divisible by 4")
    

userInput='californ'
c=stringExer(userInput)
print(c)


# 19. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 

def stringExer(come):
    secInput=come[0:5]
#     print(userInput.isupper())
    if sum(map(str.isupper,secInput))>=2:
        return come.upper()
    else:
        print("condition not satisfied")

userInput='CaLiforn'
c=stringExer(userInput)
print(c)

#SAMPLE 2

def stringExer(come):
    if come[0].isupper() and come[1:].islower():
        print("It's in a format")
    else:
        print("its not in format")
   

userInput='Californ'
c=stringExer(userInput)
print(c)

# 21. Write a Python program to remove a newline in Python. 

x='a\n\n\n'
print(x.strip())

print('hi')

# 22. Write a Python program to check whether a string starts with specified characters. 

def stringExer(come):
    if come[0].isalnum() == True:
        return "there no special character"
    else:
        return "there's special character"
   

userInput='@orn'
c=stringExer(userInput)
print(c)

# 24. Write a Python program to print the following floating numbers upto 2 decimal places. 

x=3.14558
x=-4.5895

print("original number:",x)
print("original number:"+"{:.3f}".format(x)) 


# 25. Write a Python program to print the following floating numbers upto 2 decimal places with a sign. 
x=3.14558
x=-4.5895

print("original number:",x)
print("original number:"+"{:+.3f}".format(x))


# 26. Write a Python program to print the following floating numbers with no decimal places. 

# SAMPLE 1

x=3.14558
# x=-4.5895
c=list(str(x))
# print(c)
if '.'in c:
    c.remove('.')
print("".join(c))
        
# SAMPLE 2

# x=3.14558
x=4.5895

print("original number:",x)
print(abs(x))
print("original number:"+"{:+.0f}".format(x))

# 27. Write a Python program to display a number in left, right and center aligned of width 10. 


x='123456'
print("From left alignment:",x[0:len(x)])
print("From right alignment:", x[len(x):])
print("From center alignment:", x[len(x)//2:])

# 28. Write a Python program to count occurrences of a substring in a string. 

from collections import Counter
x='jaivijay'
count=Counter(x)
print(count)

# 29. Write a Python program to reverse a string. 

x='jai'
print(x[::-1])

# 30. Write a Python program to reverse words in a sentence. 

x=raw_input().split()
print(x[::-1])

# 31. Write a Python program to strip a set of characters from a string. 

# SAMPLE 1

x='00000000 is not a number'
print(x.strip('0'))

# SAMPLE 2

def strip_character(str, chars):
    return "".join(i for i in str if i not in chars)

  
print("\nOriginal String")
print("Johny johny yes papa eating sugar no papa")
print("\nAfter striping string:")
print(strip_character("Johny johny yes papa eating sugar no papa", 'aeiou'))



# 23. Write a Python program to create a Caesar encryption. 

# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

  