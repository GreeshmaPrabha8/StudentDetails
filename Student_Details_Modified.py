import json

# Definig a class student
class Student:

    
    # method is defined to add student details
    def add(self):
        
        print("-----------------------------")
        print("-----------------------------")
        print("Enter the Details:")
        print("-----------------------------")
        print("-----------------------------")
        self.name = input("Name:")
        self.standard = int(input("Class:"))
        self.division = input("Division:")
        self.rollno = int(input("Roll No:"))
        self.passedtest = int(input("Passed test details:"))
        self.failedtest = int(input("Failed test details:"))
        self.missedtest = int(input("Missed test details:"))
        aDict = {"Name:":self.name,"Class:":self.standard ,"Division:": self.division,"Roll No:":self.rollno,"Passed test details :":self.passedtest,"Failed test details:":self.failedtest, "Missed test details":self.missedtest}  
        jsonString = json.dumps(aDict)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()

 # method is defined to display student details
    def display(self):
        print("-----------------------------")
        print("-----------------------------")
        print("Details are:")
        print("-----------------------------")
        print("-----------------------------")
        print("Name is : ", self.name)
        print("Class :", self.standard)
        print("Division:", self.division)
        print("Roll No:", self.rollno)
        print("No: of Passed Test:", self.passedtest)
        print("No: of Missed Test:", self.failedtest)
        print("No: of Failed Test:", self.missedtest)
        
        
 # method is defined to check whether the student failed or missed more than 3 subjects

    def search(self):
        print("-----------------------------")
        print("-----------------------------")
        print("Search Result is:")
        print("-----------------------------")
        print("-----------------------------")
        if(self.missedtest>=4 or self.failedtest>=4):
            print("Need Instructor")
        else:
            print("Study well!")
            

# Main Code

# a list ls is created
ls =[]

#object obj for student class is created
obj = Student()

# displaying the opertions to be performed
print("\nOperations used:")
print("\n1.Add Student details\n2. Display Student details\n3.Check Student Pass or Fail details\n4.Exit")    


x = 'y'
while x == 'y':
    
    # it will check whether the option selected is not wrong
    try:
        enter = int(input("Please Select an Option: "))
    except ValueError:
        exit("\n Wrong Entry. Enter Again")
    else:
        print("\n") 
    
 # for each option given by user, it will perform the action.
    if (enter == 1):
        obj.add()
    elif (enter == 2):
        obj.display()
    elif (enter == 3):
        obj.search()
    elif (enter == 4):
        print("Thank You!")
    elif(enter < 1 or enter > 4):
        print("Please Enter Correctly") 
    x = input("\nDo you want to continue? y/n: ")
    
# Printing the list of student
n = 1
for el in ls:
    print(n,'. ', el)
    n = n + 1
