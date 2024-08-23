# 1. Create a list with integers from 1 to 10.
lists=[i for i in range(1,11)]
print(lists)  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Find the length of a list without using the `len()` function.
def length(lists):
    length=0
    for i in lists[0:]:
        length+=1
    return length

lists=[1,2,3,4,5,6,7,8,9,10]
print(length(lists))   #output-->10

# 3. Append an element to the end of a list.
def appendList(list1,Element):
    
    list1.append(Element)
    return list1
list1=[1,2,3,4,5]
element=6
print(appendList(list1,element))   #output-->[1,2,3,4,5,6]

# 4. Insert an element at a specific index in a list
def insertElement(list2,element2):
    list2.insert(4,element2)
    return list2
list2=[1,2,3,4,5,6]
element2=56
print(insertElement(list2,element2))   #output-->[1, 2, 3, 4, 56, 5, 6]

# 5. Remove an element from a list by its value.
def removeElement(list3,element3):
    list3.remove(element3)
    return list3
list3=[1,2,3,4,5]
element3=3
print(removeElement(list3,element3))  #output-->[1, 2, 4, 5]

# 6. Remove an element from a list by its index.

def removeIndexElement(lists):
    lists.pop(3)
    return lists
lists=[33,4,56,39,90]
print(removeIndexElement(lists))    #output-->[33, 4, 56, 90]


# 7. Check if an element exists in a list.
def checkElementExist(list4,element4):
    for i in list4[0:]:  #travser upto len of list
        if i==element4:
            return True
    return False    
list4=[1,2,34,6,73,22]   
element4=34
if checkElementExist(list4,element4):
    print("Element exists in lists")   #output-->Element exists in lists
else:    
    print("Element not exists in lists")   


#8. Find the index of the first occurrence of an element in a list.
def  indexFirstOccurrence(list5,element5):
    firstOccu=list5.index(element5)
    return firstOccu
    
myList = [10, 20, 30, 20, 10]
element = 20

index =indexFirstOccurrence(myList,element)

print("The index of the first occurrence of", element, "is", index)
# output-->The index of the first occurrence of 20 is 1

# 9. Count the occurrences of an element in a list
def  countOccurrences(list5,element5):
    firstOccu=list5.count(element5)
    return firstOccu
    
myList = [10, 20, 30, 20, 10,20,20]
element = 20

index =countOccurrences(myList,element)

print("The index of the first occurrence of", element, "is", index)
# output-->The index of the first occurrence of 20 is 4

# 10. Reverse the order of elements in a list
def reverseOrderElements(lists):
    reverse=sorted(lists,reverse=True)
    return reverse
myLists=[10,20,30,40,50]
print(reverseOrderElements(myLists))  #output-->[50, 40, 30, 20, 10]

# 11. Sort a list in ascending order.
def sortListAscending(lists):
    order= sorted(lists)
    return order
lit=[4,2,6,8,3,5]
print(sortListAscending(lit))  #output-->[2, 3, 4, 5, 6, 8]

# 12. Sort a list in descending order.
def sortListDescending(lists):
    desOrder=sorted(lists,reverse=True)
    return desOrder
myLists=[10,20,30,40,50]
print(sortListDescending(myLists))   #output-->[50, 40, 30, 20, 10]

# 13. Create a list of even numbers from 1 to 20.
def listEvenNumbers():
    list1=[i for i in range(1,21) if i%2==0]
    return list1
print(listEvenNumbers())  #output-->[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 14. Create a list of odd numbers from 1 to 20.
def listOddNumbers():
    list2=[i for i in range(1,21) if i%2!=0]
    return list2
print(listOddNumbers())   #output-->[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 15. Find the sum of all elements in a list.
def sumOfAllElements(lists):
    sums=sum(i for i in lists[0:] )
    return sums
lsit=[1,2,3,4,5]
print(sumOfAllElements(lsit))  #output->15

# 16. Find the maximum value in a list.
def maximumValue(lists):
    if not lists:
        return None
    maxi=lists[0]
    for i in lists[0:]:
        if i>maxi:
            maxi=i
    return maxi
myLits3=[1,34,67,4,90,56]
print(maximumValue(myLits3))   #output-->90

# 17. Find the minimum value in a list.
def minimumValue(lists):
    if not lists:   #handle empty case 
        return None
    mini=lists[0]
    for i in lists[0:]:
        if i<mini:
            mini=i
    return mini
myLits3=[34,6,78,-45,86]
print(minimumValue(myLits3))   #output-->-45

# 18. Create a list of squares of numbers from 1 to 10.
def listOfSquares():
    square=[i*i for i in range(1,11)]
    return square
print(listOfSquares())  #output-->[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 19. Create a list of random numbers.
import random 

def listOfRandomNumbers(start,end,size):
    return [random.randint(start,end) for _ in range(size)]

start=1
end=20
size=10
print(listOfRandomNumbers(start,end,size))     #output-->[8, 15, 3, 10, 11, 12, 15, 18, 7, 13]

# 20. Remove duplicates from a list.
def removeDuplicates(myList):
    removeDupli=list(set(myList))
    return removeDupli
list5=[1,4,4,2,3,5,1]
print(removeDuplicates(list5))   #output-->[1, 2, 3, 4, 5]

