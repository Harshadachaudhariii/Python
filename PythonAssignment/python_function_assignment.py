import math
from functools import reduce
# Basics of Functions:
# 1.Write a Python program that defines a function to calculate the sum of two numbers and then calls the function.
def calculateSum(num1,num2):
    return num1+num2
print("The sum of the two number ",calculateSum(2,5))  #output-->7

# 2. Create a Python function that takes two arguments and returns their product.
def productOfTwoNum(num1,num2):
    return num1*num2
print(productOfTwoNum(2,4))   #output-->8


# Function Parameters and Arguments:
# 1.Write a Python program that defines a function with default argument values.
def sums(a=9,b=10):
    return a+b
print(sums())   #output-->19

# 2.Create a Python function that accepts a variable number of arguments and calculates their sum.
def variableNoArgumentSum(*arg):
    sums=0
    for i in arg:
        sums+=i    
    return sums
print(variableNoArgumentSum(1,2,3,4,5,6))     #output-->21



# Return Values and Scoping:
# 1.Write a Python program that demonstrates the use of global variables within functions.
counter=0
def increment():
    global counter
    counter+=1
    print("The increment value of the counter is ",counter)
 
def decrement():
    global counter
    counter-=1
    print("The decrement value of the counter is ",counter) 

increment()   #output-->1
decrement()   ##output-->0

#2.Create a Python function that calculates the factorial of a number and returns it.
def calculFact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(calculFact(6))  #output-->720     

#3.How can you access variables defined outside a function from within the function?
number=2
def accessVariable():
    # accessing global varibale
    print("Variable inside the function ",number)   #output-->2
accessVariable()   
def modifyVariable():
    global number
    number+=1
    print("The modifying value of global variable is ",number)  #output-->3
modifyVariable()
print("Value of x outside the function after modification:", number)  #output-->3      




# Lambda Functions and Higher-Order Functions:
# 1.Write a Python program that uses lambda functions to sort a list of tuples based on the second element.
tupleList=[(3,2),(2,1),(1,5),(4,3),(2,6),(6,4)]
sortListOfTuples=sorted(tupleList,key=lambda x:x[1])
print(sortListOfTuples)  #output-->[(2, 1), (3, 2), (4, 3), (6, 4), (1, 5), (2, 6)]

# 2.Explain the concept of higher-order functions in Python, and provide an example.
def operations(operation,x,y):   #taking argument three parameter
    return operation(x,y)     #first parameter is use to function
def add(x,y):
    return x+y
def mul(x,y):
    return x*y

result1=operations(add,2,4)
result2=operations(mul,2,4)
print("The sums is ",result1)   #output-->The sums is  6
print("The product is ",result2)   #output-->The product is 8

# 3.Create a Python function that takes a list of numbers and a function as arguments, applying the function to each element in the list.

def applyEach(elements, func):
    return [func(element) for element in elements]

numbers = [1, 2, 3, 4, 5]

# Define a function to be applied
def square(x):
    return x ** 2

# Apply the function to each element in the list
squared_numbers = applyEach(numbers, square)

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# map
#1. Write a Python program that uses the `map()` function to square each element of a list of numbers.
def squareListElement(listElement):
    return list(map(lambda sqrts:sqrts**2,listElement))

listElement=[1,2,3,4,5,6,7]
print(squareListElement(listElement))   #output-->[1, 4, 9, 16, 25, 36, 49]

# 2.Create a Python program that uses the `map()` function to convert a list of names to uppercase.
def listNameUpper(listName):
    return list(map(lambda u:u.upper(),listName))

listName=['alice','bob','tony','charlie']
print(listNameUpper(listName))   #output-->['ALICE', 'BOB', 'TONY', 'CHARLIE']

# 3.Write a Python program that uses the `map()` function to calculate the length of each word in a list of strings.
def calculaLengthList(listString):
    return list(map(lambda s : len(s),listString))

listString=['alice','bob','tony','charlie']
print(calculaLengthList(listString))  #output-->[5, 3, 4, 7]

# 4.Create a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.
def convertFahren(listCelsius):
    return list(map(lambda c : (c * 9 /5 ) + 32, listCelsius))

listCelsius=[22,24,25,26,28]
print(convertFahren(listCelsius))  #output-->[71.6, 75.2, 77.0, 78.8, 82.4]

# 5.Write a Python program that uses the `map()` function to round each element of a list of floating-point numbers to the nearest integer.
def floatNumbersNearestInt(listElement):
    return list(map(round,listElement))

listElements=[2.3,4.5,8.7,0.8,9.4]
print(floatNumbersNearestInt(listElements))  #output-->[2, 4, 9, 1, 9]


# Reduce :-
# 1.Write a Python program that uses the `reduce()` function to find the product of all elements in a list.
def productAllElement(listElement):
    return reduce(lambda a,b:a*b,listElement)

listElement1=[1,2,3,4,5,6]
print(productAllElement(listElement1))  #output-->720

# 2.Create a Python program that uses `reduce()` to find the maximum element in a list of numbers.
def findMaximumListNO(listElement):
    return reduce(lambda maxi1,maxi2: max(maxi1,maxi2),listElement)

listElement2=[23,34,56,78,12,-89]
print(findMaximumListNO(listElement2))  #output-->78

# 3.How can you use the `reduce()` function to concatenate a list of strings into a single string?
def concatStringsSingle(listString):
    return reduce(lambda s1,s2 : s1+s2,listString)

listString1=['list','of' ,'strings' ,'into','single','string']
print(concatStringsSingle(listString1))  #output-->listofstringsintosinglestring

# 4.Write a Python program that calculates the factorial of a number using the `reduce()` function.
def calculFactorial(fact):
    if fact==0 or fact==1:
        return 1
    return reduce(lambda a,b:a*b,range(1, fact+1))

nums=7
print(calculFactorial(nums))  #output-->5040

# 5.Write a Python program that uses the `reduce()` function to find the sum of the digits of a given number.
def sumOfDigitGivenNum(number):
    digits=map(int,str(number))
    return reduce(lambda x,y : x+y,digits)

num1=1234567
print(sumOfDigitGivenNum(num1))  #output-->28


# Filter :-
# 1.Write a Python program that uses the `filter()` function to select even numbers from a list of integers.
def selectEvenNum(lists):
    return list(filter(lambda a: a%2==0,lists))

li=[1,2,3,4,5,6,7,8,9,0]
print(selectEvenNum(li))   #output-->[2, 4, 6, 8, 0]

# 2.Write a Python program that uses the `filter()` function to select prime numbers from a list of integers.
def selectPrimeNum(lists):
    return list(filter(lambda a: a%2!=0 ,lists))

lst=[12,34,5,67,8,65,33]  
print(selectPrimeNum(lst))   #output-->[5, 67, 65, 33]

# 3.Create a Python program that uses the `filter()` function to select names that start with a specific letter from a list of strings.
def selectNameStart(names,letter):
    return names.startswith(letter)

names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

letter='A'

filter_name=list(filter(lambda name: selectNameStart(name,letter),names))
print(filter_name)  #output-->['Alice']

# 4.Create a Python program that uses `filter()` to select words longer than a certain length from a list of strings.
def selectLongerLength(words):
    return list(filter(lambda word:len(word)>5,words ))
    
words = ["apple", "banana", "cherry", "date"]
print(selectLongerLength(words))  #output-->['banana', 'cherry']

# 5.Write a Python program that uses the `filter()` function to select elements greater than a specified threshold from a list of values.
def selectElementGreater(values):
    return list(filter(lambda value: value>20,values))

values=[10, 25, 30, 5, 60, 8]
print(selectElementGreater(values))  #output-->[25, 30, 60]

# 6.How can you use the `filter()` function to remove None values from a list in Python?
def removeNoneValues(noneValue):
    return list(filter(None,noneValue))

noneValue=[1, None, 2, None, 3, 4, None]
print(removeNoneValues(noneValue))  #output-->[1, 2, 3, 4]



#  function using if else 
# 1. Write a Python program to check if a number is positive, negative, or zero using an if-else statement
def checkNumber(n):
    if n<0:
        print("Number is negative")
    elif n>0:
        print("Number is positive")   #<--output
    else:
        print("Number is zero")
                
checkNumber(5)

# 2.Create a Python program that checks if a given number is even or odd using an if-else statement.
def checkEvenOdd(m):
    if m%2==0:
        print("Number is even ")   #<--output
    else:
        print("Number is odd")

checkEvenOdd(4)            

# 3.Write a Python program to determine the largest of three numbers using if-else.
def determineLargestNum(num1,num2,num3):
    if (num1>num2 and num1>num3) :
        print(f"The number {num1} is largest among three ")
    elif (num2>num3 and num2>num1):
        print(f"The number {num2} is largest among three ")
    else:
        print(f"The number {num3} is largest among three")   #<--output 
 
determineLargestNum(23,34,56)    

# 4.Write a Python program that calculates the absolute value of a number using if-else.
def absolute(n):
    if n > 0:
        return n
    else:
        return -n
print(absolute(-13))    #output-->13

# 5.Create a Python program that checks if a given character is a vowel or consonant using if-else.
def checkVowelConsonant(character):
    vowels='aeiou'
    if character in vowels:
        print("A given character is a vowel ")
    else:    
        print("A given character is a consonant ")  #<--output

checkVowelConsonant('y')        

# 6.Write a Python program to determine if a user is eligible to vote based on their age using if-else.
def checkEligible(age):
    if age >= 18:
        print("A user is eligible to vote")  #<--output
    else:
        print("A user is not eligible to vote")
  
checkEligible(34)
        
# 7. Create a Python program that calculates the discount amount based on the purchase amount using if-else.
def discountAmount(purchaseAmount):
    if purchaseAmount>=1000:
        discount=purchaseAmount*0.1   # 10% discount for purchases of $1000 or more
    elif purchaseAmount>=500:
        discount=purchaseAmount*0.05    # 5% discount for purchases of $500 or more
    else:
        discount=0   # No discount for purchases below $500
        
    return discount

print(discountAmount(400))  #output-->0

# 8.Write a Python program to check if a number is within a specified range using if-else.
def checkSpecifiedRange(number,start,end):
    if number>=start and number<=end:
        print("A number is within a specified range")  #<--output
        
    else:
        print("A number is not within a specified range")    
        
number=int(input("enter the number"))  #20
start=int(input("Enter the lower bound"))  #10
end=int(input("enter the upper bound"))    #30       
checkSpecifiedRange(number,start,end)        
       
# 9.Create a Python program that determines the grade of a student based on their score using if-else.
def determineGrade(score):
    if score >= 90:
        print("Grade is A")
    elif score >= 80:
        print("Grade is B")
    elif score >= 70:
        print("Grade is C")
    elif score >= 60:
        print("Grade is D")
    else:
        print("Grade is F")
score=int(input("enter the score"))      #output-->67                         
determineGrade(score)                       

# 10.Write a Python program to check if a string is empty or not using if-else.
def checkEmptyString(string):
    if string=="":
        print("String is empty")
    else:
        print("String is not empty")  #<--output
string="Hello"
checkEmptyString(string)          

# 11.Create a Python program that identifies the type of a triangle (e.g., equilateral, isosceles, or scalene) based on input values using if-else.
def checkTypeTriangle(side1,side2,side3):
    if side1==side2 and side2==side3 and side3==side1:
        print("Triangle is equilateral") 
    elif side1==side2 or side2==side3 or side3==side1:
        print("Triangle is isosceles ")  #<--output
    else:
        print("Triangle is scalene")   
checkTypeTriangle(12,12,10)  

#12.Write a Python program to determine the day of the week based on a user-provided number using if-else.
def determineDayWeek(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"   #<--output
    elif num== 4:
        return "Thursday"
    elif num ==5:
        return "Friday"
    elif num==6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    else:
        return "Invalid number! Please enter a number between 1 and 7."
num=int(input("Enter a number (1-7) to get the day of the week: "))   #input-->3
print(determineDayWeek(num))   

# 13.Create a Python program that checks if a given year is a leap year using both if-else and a function.
def checkLeapYear(years):
    if (years % 4 == 0 and years % 100 != 0) or (years % 400 == 0):
        print("A given year is a leap year")  #<--output
    else:
        print("A given year is not a leap year")    

year1=2024
checkLeapYear(year1) 

# 14.Write a Python program to categorize a given character as uppercase, lowercase, or neither using if-else.
def checkCharacterCase(characters):
    if characters.isupper():
        print("Given character is in upper case")
    elif characters.islower():
        print("Given character is in lower case")  #<--output
    else:
        print("Given character is neither lower case or upper case")        

charact="h"
checkCharacterCase(charact)

# 15.Write a Python program to determine if a given number is prime or not using if-else.
def checkPrime(n):
    if n <= 1:
        print("Given number is not a prime number")
    elif n == 2:
        print("Given number is a prime number")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:   
                print("Given number is not a prime number")
                return 
    print("Given number is a prime number")  #<==output

n = 29
checkPrime(n)


# 16.Create a Python program that checks if a given year is a century year or not using if-else
def checkCenturyYear(years):
    if years%100==0:
        print("A given year is a century year")
    else:    
        print("A given year is not a century year")  #<--output
year2=2001
checkCenturyYear(year2)

# 17.Create a Python program that determines the eligibility of a person for a senior citizen discount based on age using if-else.
def seniorCitizenDiscount(age):
    if age>=65:
        return "Eligible for senior citizen discount."  #<--output
    else:
        return "Not eligible for senior citizen discount."
    
age=int(input("enter the age"))  #89
print(seniorCitizenDiscount(age))

# 18.Write a Python program to determine if a given number is a perfect square using if-else.
def determinePerfectSquare(n):
    if n < 0:
        return "Negative numbers cannot be perfect squares."
    sqrt=math.isqrt(n)
    if sqrt*sqrt==n:
        return "The number is a perfect square." #<--output
    else:
        return "The number is not a perfect square."
n=25
print(determinePerfectSquare(n))

# 19.Create a Python program that calculates the BMI (Body Mass Index) of a person based on their weight and height using if-else.
def calculBMI(weight,height):
    
    height=height/ 100    ## Convert height from cm to meters
    bodyMassIndex= weight / (height*height)
    
    if bodyMassIndex <18.5:
        return "Underweight and possibly malnourished"
    elif 18.5 <= bodyMassIndex <=24.9:
        return "Health weight"   #<--output
    elif 25.0 <= bodyMassIndex <=29.9:
        return "Overweight"
    elif bodyMassIndex >=30:
        return "Obesity"
    else:
        return "Severe obesity" 
    
weight=int(input("Enter the weight"))        
height=int(input("Enter theheight"))       
print(calculBMI(weight,height))   # weight = 55 kg, height = 155 cm


#20.Write a Python program to determine the roots of a quadratic equation using if-else.
def deterQuadraticEqn(a,b,c):
    
    discriminant=b**2 - 4 * a *c
    
    if discriminant >0:
        root1 = (-b + math.sqrt(discriminant))/ (2 * a)
        root2 = (-b - math.sqrt(discriminant))/ (2 * a)
        return f"Two distinct real roots: {root1} and {root2}"
    
    elif discriminant==0:
        root= -b /(2 * a)
        return f"One real root (repeated): {root}"
    
    else:
        # No real roots (complex roots)
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"Complex roots: {real_part} ± {imaginary_part}i"

a=float(input("enter the coefficient of a"))  #1
b=float(input("enter the coefficient of b"))   #-3
c=float(input("enter the coefficient of c"))  #2
print(deterQuadraticEqn(a,b,c))



# function using for loop
# 1.Write a Python program to print numbers from 1 to 10 using a for loop.
def num_print():
    for i in range(1,11):
        print(i,end=" ")
        
num_print()  #output--> 1 2 3 4 5 6 7 8 9 10 

# 2.Write a Python program to calculate the sum of all numbers from 1 to 100 using a for loop.
def sumOfAllNumbers():
    sums=0
    for j in range(1,101):
        sums+=j
    return sums
print(sumOfAllNumbers())  #output-->5050

# 3.How do you iterate through a list using a for loop in Python?
def iterateList(lst):
    for k in lst:
        print(k,end=" ")  #output-->a s d f g 
       
lst=['a','s','d','f','g'] 
iterateList(lst)  

# 4.Write a Python program to find the product of all elements in a list using a for loop.
def productOfAllElements(lists):
    product=1
    for i in lists:
        product*=i
        
    return product
lists=[1,2,3,4,5]            
print(productOfAllElements(lists))   #output-->120

# 5.Create a Python program that prints all even numbers from 1 to 20 using a for loop.
def printsAllEvenNumbers():
    for i in range(1,21):
        if i%2==0:
            print(i,end=" ")
                          
printsAllEvenNumbers()    #output-->2 4 6 8 10 12 14 16 18 20

# 6.Write a Python program that calculates the factorial of a number using a for loop.

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))  #output--->120

# 7.How can you iterate through the characters of a string using a for loop in Python?

def iterateString(strings):
    for k in strings:
        print(k,end=" ")  
strings="helloworld"
iterateString(strings)  #output-->h e l l o w o r l d 

# 8.Write a Python program to find the largest number in a list using a for loop.
def largestNumber(lst):
    maxi=0
    for i in lst:
        if i>maxi:
            maxi=i
    return maxi  
lsts=[1,45,-67,0,34,90,78]
print(largestNumber(lsts))  #output-->90

# 9.Create a Python program that prints the Fibonacci sequence up to a specified limit using a for loop

def fibonacciSequence(n):
    a,b=0,1
    for _ in range(n):
        print(a,end=" ")
        a,b=b,a+b
specifiedLimit=8    
fibonacciSequence(specifiedLimit)     #output-->0 1 1 2 3 5 8 13

# 10. Write a Python program to count the number of vowels in a given string using a for loop.
def countNoVowels(strs):
    vowels='aeiou'
    counts=0
    for i in strs:
        if i in vowels:
            counts+=1
            
    return counts

strings1="duplicates"
print(countNoVowels(strings1))    #output-->4    

# 11.Create a Python program that generates a multiplication table for a given number using a for loop

def multiTable(num):
    for k in range(1,11):
        print(num*k,end=" ")
        
num=5
multiTable(num)  #output-->5 10 15 20 25 30 35 40 45 50 

# 12.Write a Python program to reverse a list using a for loop.
def reverseList(lst):
    reverseList=[]
    for i in range(len(lst)-1,-1,-1):
        reverseList.append(lst[i])
    return reverseList    
lst1=[10,20,30,40]
print(reverseList(lst1))  #output-->[40, 30, 20, 10]

# 13.Write a Python program to find the common elements between two lists using a for loop.
def commonElement(list1,list2):
    commonList=[]
    for i in list1:
        for j in list2:
            if i==j:
                commonList.append(j)
    return commonList
            
list1=[1,2,3,4,5,6]
list2=[7,8,3,9,5]
print(commonElement(list1,list2))  #output--> [3,5]

# 14.write a program for loop to iterate through the keys and values of a dictionary in Python.
def iterateKeysValues(dicts):
    for i in dicts:
        print(i,dicts[i])
        
dicts={"name":"Alice","age":23,"gender":"male","city":"Canda"}        

iterateKeysValues(dicts)
# name Alice
# age 23
# gender male
# city Canda

#15. Create a Python program that checks if a string is a palindrome using a for loop.
def is_palindrome(s):
    s = s.lower()  # Normalize the string to lowercase
    length = len(s)   #7
    
    # Compare characters from the start and end of the string
    for i in range(length):
        if s[i] != s[length - 1 - i]:    #1st iteration s[0] 'r' == s[7-1-0]==s[6] 'r'
            return False
        # Stop checking once we reach the middle
        if i >= length // 2:
            break
    
    return True

test_string = "Racecar"
print(f'"{test_string}" is a palindrome.' if is_palindrome(test_string) else f'"{test_string}" is not a palindrome.')

# 16.Write a Python program to find the sum of all odd numbers from 1 to 50 using a for loop.
def sumAllOddNumbers():
    sums=0
    for h in range(1,51):
        if h %2 !=0:
            sums+=h
    return sums

print(sumAllOddNumbers())     #output->>625   

# 17.Create a Python program that counts the number of words in a sentence using a for loop
def countWordsSentence(sentence):
    words=sentence.split()
    counts=0
    for i in words:
        counts+=1
    return counts
sentence="program that counts the number" 
print(countWordsSentence(sentence))    #output-->5

# 18.Write a Python program that checks if a given year is a leap year using a for loop.
def checkLeapYear(years):
    for k in range(years,years+1):
        if (k%4==0 and k%100!=0) or k%400==0:
            return True
        
    return False
years=2025  
print(checkLeapYear(years)) #output-->false


 
   
        
        