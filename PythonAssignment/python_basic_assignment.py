# 1.Declare two variables, x and y, and assign them integer values. Swap the values of these variables without using any temporary variable
x=10
y=20
x,y=y,x
print(x,y)
# 2.Create a program that calculates the area of a rectangle. Take the length and width as inputs from the user and store them in variables. Calculate and display the area.

length=float(input())
width=float(input())
area_of_rect=length*width
print(area_of_rect)

# 3.Write a Python program that converts temperatures from Celsius to Fahrenheit. Take the temperature in Celsius as input, store it in a variable, convert it to Fahrenheit, and display the result.

celsius=int(input())   #input -->25
# (0°C × 9/5) + 32 
result=(celsius*9/5)+32
print(result)   #output-->77

# 4. Write a Python program that takes a string as input and prints the length of the string.
str1=input()    #input-->Hello
result=len(str1)   #len() calculate length of the string
print(result)   #output -->5

# 5. Given a string, reverse the order of characters using string slicing and print the reversed string.
str2="Hello world!"
reverse=str2[::-1]   #[::-1] reverse string
print(reverse)   #output -->!dlrow olleH

# 6. Create a program that takes a string as input and removes all the spaces from it. Print the modified string without spaces.
str3="   Hello World!  "
result=str3.replace(" ","")
print(result)   # output-->HelloWorld!

# 7. Write a program that takes a string as input and checks if it is a palindrome (reads the same forwards and backwards).
str4=input()  #input --> madam
result=str4[::-1]
if(str4==result):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")   # output -->The string is a palindrome.

# 8. Create a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u) in the string.
sentence=input()   #input -->Educated owls avoid unique areas.
vowel="aeiouAEIOU"
count=0
for char in sentence:   # this for loop iterate sentence with variable name as char
    if char in vowel:   #checking if the char present in vowel then it count
        count+=1
print(" the number of vowels in the string are : ",count)      #output -->  the number of vowels in the string are :  15