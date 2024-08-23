# 1.Bank Account Create a class representing a bank account with attributes like account number, account holder name, and balance. Implement methods to deposit and withdraw money from the account.
class bankAccount:
    
    def __init__(self,accountNum,holderName,balance):
        self.accountNum=accountNum
        self.holderName = holderName
        self.balance=balance
        
    def deposite(self,amount):
        self.amount=amount
        print("User successfully deposite amount")
        return self.amount
    
    def withdraw(self):
        print("User successfully withdraw amount")
        return 0
    
harshada=bankAccount(234242,"harshada",23000)

print(harshada.deposite(230000))  #output-->User successfully deposite amount 230000
harshada.withdraw()  #output-->User successfully withdraw amount


#2.Employee Management Create a class representing an employee with attributes like employee ID, name, and salary. Implement methods to calculate the yearly bonus and display employee details.
class Employee:
    
    def __init__(self,EmpId,Name,Salary):
        self.EmpID=EmpId
        self.Name=Name
        self.Salary=Salary
        
    def bouns(self):
        if self.Salary>=55000:
            print(self.Salary*0.05)
        else:
            print(self.Salary*0.10)
            
    def EmpDetails(self): 
        print(self.EmpID, " ",self.Name," ",self.Salary)           
 
soni=Employee("A001","Alice",23000)  #output-->2300.0
soni.bouns()
soni.EmpDetails()         #output-->A001   Alice   23000


# 3..Library Catalog Create classes representing a library and a book. Implement methods to add books to the library, borrow books, and display available books.
class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.isBorrow=False
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
class library:
    
    def __init__(self):
        self.books=[]
        
    def addBook(self,title,author):
        book = Book(title, author) 
        self.books.append(book)
        print(f"Added : {book}")
        
    def borrowedBook(self,title):
        for book in self.books:
            if book.title==title and not book.isBorrow:
                book.isBorrow=True
                print("Borrowed")
                return
        print("Sorry book not avaiable")
        
    def displayBook(self):
        if not self.books:
            print("No such book is avaiable")
        else:
            for book in self.books:
                print(book)                 
                
libraryInstance = library()
libraryInstance.addBook("Atomic", "Author a")               
libraryInstance.addBook("Big Data", "Author b")               
libraryInstance.addBook("Python", "Author c")               
                
# Call the method on the instance
libraryInstance.displayBook()             
                    

# 4.. Vehicle Rental Create a class representing a vehicle rental system. Implement methods to rent a vehicle, return a vehicle, and display available vehicles.
class Vehicle:
    
    def __init__(self,VehName):
        self.vehname=VehName
        self.isRent=False
        
    def __str__(self):
        return f"{self.vehname}"
    
class RentVehicle:   
    
    def __init__(self):
        self.vehicle=[]
     
    def addVehicle(self,VehName):
        vehic=Vehicle(VehName)
        self.vehicle.append(vehic)
        
    def rentVehicle(self, Vehname):
        for vehicle in self.vehicle:
            if vehicle.vehname == Vehname:
                if not vehicle.isRent:
                    vehicle.isRent = True
                    print(f"{Vehname} is now on rent.")
                    return
                else:
                    print(f"{Vehname} is already rented.")
                    return
    print("Sorry, there is no vehicle available with that name.")
        
    def availVehicle(self):
        if not self.vehicle:
            print("no vehcile available")
        else:
            for vehicle in self.vehicle:
                print(vehicle) 

v=RentVehicle()
v.addVehicle("BMW")
v.addVehicle("Thar")
v.addVehicle("Honda")
v.rentVehicle("Honda")  #output-->Honda is now on rent.
                       

# 5.Product Inventory Create classes representing a product and an inventory system. Implement methods to add products to the inventory, update product quantity, and display available products
    
class Product:
    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity= quantity
        self.price = price
        
    def __str__(self):
        return f"{self.name} : {self.quantity} : {self.price}"    

class Inventory:
    
    def __init__(self):
        self.products= []
        
    def addProduct(self, name,quantity,price):
        prod = Product(name,quantity,price)    
        self.products.append(prod)
        
    def updateProductQuantity(self,productName, newQuantity):
        for product in self.products:
            if product.name == productName:
                product.quantity= newQuantity
                break
            
    def displayAvailable(self):
        if not self.products:
            print("product not avilable")
        else:
            for product in self.products:
                print(product) 
                
inventory= Inventory()
inventory.addProduct("laptop",2,34000)  #output-->laptop : 2 : 34000
inventory.displayAvailable()        
inventory.updateProductQuantity("laptop",1)   #output-->laptop : 1 : 34000
inventory.displayAvailable()        


# 6.Shape Calculation Create a class representing a shape with attributes like length, width, and height. Implement methods to calculate the area and perimeter of the shape.
class shape :
    
    def __init__(self,lengths,width,height):
        self.lengths= lengths
        self.width= width
        self.height= height
        
    def areaShape(self):
        rectangularPrism = 2* (self.lengths * self.width + self.width * self.height +self.height* self.lengths)
        return f" The shape of surface area is {rectangularPrism}"
    
    def perimeterShape(self):
        rectangle = 2 * (self.lengths + self.width)
        return f"The shape of the perimeter of rectangle is {rectangle}"
    
s=shape(2,4,6)
print(s.areaShape())    #output-->The shape of surface area is 88

print(s.perimeterShape())   #output-->The shape of the perimeter of rectangle is

# 7.Student Management Create a class representing a student with attributes like student ID, name, and grades. Implement methods to calculate the average grade and display student details.
class student:
    
    def __init__(self,stuId,name,grades):
        self.Id= stuId
        self.name= name
        self. grades= grades  #list of grade
        
    def average(self):
        if not self.grades:
            return 0  
        
        else:
            return sum(self.grades)/ len(self.grades)
        
    def getGrade(self):
        avgs=self.average()
        
        if avgs>=90:
            return "A"
        elif avgs >=80:
            return "B"
        elif avgs >=60:
            return "C"
        elif avgs >=40:
            return "D"
        else:
            return "F"    
        
    def displayDetails(self):
        
        print(f"Student ID {self.Id}")    
        print(f"Student name {self.name}")    
        print(f"Student grade {self.getGrade()}")    
                                                        #output--> Student ID 13
students1= student(13,"Harshada",[90,89,99,67])         #output--> Student name Harshada
students1.displayDetails()                              #output--> Student grade B

# 8.# 8.Email Management Create a class representing an email with attributes like sender, recipient, and subject. Implement methods to send an email and display email details.

class email:
    
    def __init__(self,sender,recipient,subject):
        self.sender= sender
        self.recipient = recipient
        self.subject=  subject
        self.sent= False
        
    def sendEmail(self):
        if not self.sent:
            self.sent = True
            print("Email sent")
            
    def displayEmailDetails(self):
        print(self.sender," ",self.recipient," ", self.subject )   
        
Email= email("alice@gmail.com","bob@gmail.com","Remainder meeting")
Email.sendEmail()            #output-->Email sent
Email.displayEmailDetails()  #output-->alice@gmail.com   bob@gmail.com   Remainder meeting

# 9.Social Media Profile Create a class representing a social media profile with attributes like username and posts. Implement methods to add posts, display posts, and search for posts by keyword
class socialMedia:
    def __init__(self,username):
        self.username= username
        self.posts = []
        
    def addpost(self,posts):
        self.posts.append(posts) 
        
    def displayPosts(self):
        for post in self.posts:
            print(post)
            
    def searchPosts(self,keyword):
        result= [post for post in self.posts if keyword in post]     
        return result   
        
post= socialMedia("Hardh34")
post.addpost("This is post1 about Python.")
post.addpost("Another post related to social media.")
post.addpost("Python programming is fun!")

post.displayPosts()
            
serachResult=post.searchPosts("Python")
print(serachResult)

# 10.ToDo List Create a class representing a ToDo list with attributes like tasks and due dates. Implement methods to add tasks, mark tasks as completed, and display pending tasks.  
class Task:
    def __init__(self,taskDescribtion):
        self.Describtion= taskDescribtion
        self.complete= False
        
    def markComplete(self):
        self.complete = True
        
    def __str__(self):
        status =  "Complete" if self.complete else "Pending"
        return f"{self.Describtion} - {status}"

class ToDoList:
    
    def __init__(self,date):
        self.date=date
        self.task=[]
        
    def addTask(self,task):
        addTasks= Task(task)  
        self.task.append(addTasks) 
        
    def markTask(self,task):
        for task in self.task:
            if task.Describtion== task:
                task.markCompete()
                break
            
    def displayPending(self):
        for task in self.task:
            if not task.complete:
                print(task)        
        
todo = ToDoList("23-3-2004")
todo.addTask("Complete practice1")                            
todo.addTask("Complete practice2")                            
todo.addTask("Complete practice3")      

todo.markTask("Complete practice1")   
todo.displayPending()  # This will display the pending tasks


