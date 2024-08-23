# Basic Level
# 1. Write a Python program to print the numbers from 1 to 10 using a `for` loop.
for i in range(1,11):
    print(i,end=" ")  #output-->1 2 3 4 5 6 7 8 9 10
    
#2. Create a program that calculates the sum of all numbers in a list using a `for` loop.
lists=[1,2,3,4,5,6,7,8,9]
sums=0
for i in lists:
    sums+=i
print(sums)     #output-->45

# 3. Write a program to print the characters of a string in reverse order using a `for` loop.
# Input string
input_string = "Hello, World!"

# Loop through the string in reverse order
for i in range(len(input_string) - 1, -1, -1):
    print(input_string[i], end="")
#   output-->!dlroW ,olleH

# 4. Develop a program that finds the factorial of a given number using a `for` loop
fact=1
for i in range(1,6):
    fact*=i    
print(fact)  #output-->120

# 5. Create a program to print the multiplication table of a given number using a `for` loop
number=5
for i in range(1,11):
    print(i*number, end=" ")  #output-->5 10 15 20 25 30 35 40 45 50
 
# 6. Write a program that counts the number of even and odd numbers in a list using a `for` loop
list1=[1,2,3,4,5,6,7,8,9,10]
count_even=0
count_odd=0
for i in list1:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1

print("Counts of the even number is ",count_even)     #output-->5        
print("Counts of the odd number is ",count_odd)        #output-->5  

# 7. Develop a program that prints the squares of numbers from 1 to 5 using a `for` loop
for j in range(1,6):
    print(j*j,end=" ")  #output--> 1 4 9 16 25 
    
# 8. Create a program to find the length of a string without using the `len()` function
length=0
string1="hello, world"
for i in string1:
    length+=1
print(length)     #output--> 12

# 9. Write a program that calculates the average of a list of numbers using a `for` loop.
list2=[1,2,3,4,5]
total=0
counts=0
for i in list2:
    total+=i
    counts+=1
average=total/counts
print(average)    #output-->3.0

# 10. Develop a program that prints the first `n` Fibonacci numbers using a `for` loop
n=int(input("enter the number"))  #input-->8
a,b=0,1
for _ in range(n):
    print(a,end=" ")
    a,b=b,a+b
#output--> 0 1 1 2 3 5 8 13 

# Intermediate Level
 # 11. Write a program to check if a given list contains any duplicates using a `for` loop.
def isDuplicate(lst):
    dupli=set()
    
    for i in lst:
        if i in dupli:
            return True    
        dupli.add(i)
        
    return False
lst=[1,2,3,4,5]
if isDuplicate(lst):
    print("The list contains duplicates.")  
    
else:
    print("The list not contains duplicates.")  #output    
    
# 12. Create a program that prints the prime numbers in a given range using a `for` loop
num=10
for i in range(num):
    if i %2!=0:
        print(i,end=" ") 
        
        
        
# 13. Develop a program that counts the number of vowels in a string using a `for` loop.
strings="duplicates" 
count1=0
vowels='aeiou'
for k in strings:
    if k in vowels:
        count1+=1
        
print(count1)        #output-->4

# 