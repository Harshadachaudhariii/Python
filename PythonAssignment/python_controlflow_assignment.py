# Basic If-Else Statements:
# 1. Write a Python program to check if a given number is positive or negative.
num=12
if num>0:
    print("Given number is positive")  #<--output
else:
    print("Given number is negative")

# 2. Create a program that determines if a person is eligible to vote based on their age
# age=int(input("enter the value"))   #input-->45
age=8
if age>=18:
    print("Person is eligible to vote")   #<--output
else:    
    print("Person is not eligible to vote")

# 3. Develop a program to find the maximum of two numbers using if-else statements
# num1=int(input("enter the number"))   #input-->2
# num2=int(input("enter the number"))   #input-->4
num1,num2=2,4
if num1>num2:
    print(f"The maximum number is {num1}")
else:    
    print(f"The maximum number is {num2}")  #<--output
    
# 4. Write a Python script to classify a given year as a leap year or not.
year=2024
if year%4==0:
    print("Given year is a leap year")  #<---output
else:
    print("Given year is not a leap year")   
    
#5. Create a program that checks whether a character is a vowel or a consonant.
char='b'
vowel='aeiou'
if char in vowel:
    print("A character is a vowel")  
else:
    print("A character is a consonant")   #<--output
    
#6. Implement a program to determine whether a given number is even or odd.
num3=7
if num3%2==0:
    print("Given number is even") 
else:    
    print("Given number is odd") #<--output
    
#7. Write a Python function to calculate the absolute value of a number without using the `abs()` function
def absolute(n):
    if n>0:
        return n
    else:
        return -n
n=-5
print(absolute(n))    #output-->5

# 8. Develop a program that determines the largest of three given numbers using if-else statements

number=23
number1=50
number2=13
if number>number1 and number>number2:
    print(f"The largest number {number} is among three")
    if number1>number and number1>number2:
        print(f"The largest number {number1} is among three")
    # output-->The largest number 50 is among three
else:
    print(f"The largest number {number2} is among three")
        
#9. Create a program that checks if a given string is a palindrome.
def checkPalindrome(string):
    return string==string[::-1]
string="racecar"
if checkPalindrome(string):
    print("Given string is a palindrome")
else:    
    print("Given string is not a palindrome")
  
# 10. Write a Python program to calculate the grade based on a student's score.
# score=int(input("enter the score"))
score=45
if score >= 90:
    grade = 'A'
else:
    if score >= 80:
        grade = 'B'
    else:
        if score >= 70:
            grade = 'C'
        else:
            if score >= 60:
                grade = 'D'
            else:
                grade = 'F'

print(f"The student's grade is: {grade}")
           
# Nested If-Else Statements
#  11. Write a program to find the largest among three numbers using nested if-else statements
number3=23
number4=50
number5=13
if number>number1 and number>number2:
    print(f"The largest number {number} is among three")
else:
    if number1>number and number1>number2:
        print(f"The largest number {number1} is among three")
    # output-->The largest number 50 is among three
    else:
        print(f"The largest number {number2} is among three")
        
# 12. Implement a program to determine if a triangle is equilateral, isosceles, or scalene.
side1=7
side2=10
side3=5
if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    if side1 == side2 == side3:
        print("A triangle is equilateral")
    else:
        if side1 == side2 or side2 == side3 or side3 == side1:
            print("A triangle is isosceles")
        else:
            print("A triangle is scalene")
            # ouput-->A triangle is scalene
else:
    print("The sides do not form a valid triangle")     
    
# 13. Develop a program that checks if a year is a leap year and also if it is a century year
# year1 = int(input("Enter a year: "))
year1=1994

# Check if it's a century year
if year1 % 100 == 0:
    is_century = True
else:
    is_century = False

# Check if it's a leap year
if (year1 % 4 == 0 and year1 % 100 != 0) or (year1 % 400 == 0):
    is_leap = True
else:
    is_leap = False

# Output results
if is_leap and is_century:
    print(f"{year1} is a leap year and also a century year.")
else:
    if is_leap:
        print(f"{year1} is a leap year but not a century year.")
    else:
        if is_century:
            print(f"{year1} is not a leap year but it is a century year.")
        else:
            print(f"{year1} is neither a leap year nor a century year.")


# 14. Write a Python script to determine if a number is positive, negative, or zero.

numbers=-8
if numbers<0:
    print("A number is negative")   #<--output
else:
    if numbers >0:
        print("A number is positive")
    else:
        print("A number is zero")    

#  15. Create a program to check if a person is a teenager (between 13 and 19 years old)

teenagerAge=34
if teenagerAge<13:
    print("A person is child")
else:
    if teenagerAge>=13 and teenagerAge<=19:
        print("A person is teenager")
    else:
        print("A person is adult") #<--output
        
# 16. Develop a program that determines the type of angle based on its measure (acute, obtuse, or right)                   
    
angle1 = 60
angle2 = 60
angle3 = 60
 

if angle1 + angle2 + angle3 == 180:
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        print("It is a right angle")
    elif angle1 > 90 or angle2 > 90 or angle3 > 90:
        print("It is an obtuse angle")
    else:
        print("It is an acute angle")   #<--output
else:
    print("It is not a valid triangle")
    
    

