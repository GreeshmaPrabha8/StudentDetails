class Student:

    def __init__(self,name,standard,division,rollno,passeddata,faileddata,misseddata):
        self.name = input("Enter your name:")
        self.standard = int(input("Enter your class:"))
        self.division = input("Enter your division:")
        self.rollno = int(input("Enter your roll number:"))
        self.passedtest = int(input("Enter passed test details:"))
        self.failedtest = int(input("Enter failed test details:"))
        self.missedtest = int(input("Enter missed test details:"))

class Test(Student):
    
    def menu(self):
	    print("\n1. Add Details and Display")
	    #  print("\n2. Display")
	    print("\n2. Checking")
	    print("\n3.Exit")
	    try:
	        enter = int(input("Please Select an Option: "))
	    except ValueError:
	        exit("\nHy! That's Not A Number")
	    else:
	        print("\n")
	    if (enter == 1):
	        display()
	    elif (enter == 2):
	        search()
	    elif (enter == 3):
	        print("Thank You!")
	    elif(enter < 1 or enter > 3):
	        print("Please Enter Valid Option")
    
    

    def display(self):
        print("Details are:")
        print("Name is : ", self.name)
        print("Class :", self.standard)
        print("Division:", self.division)
        print("Roll No:", self.rollno)
        print("No: of Passed Test:", self.passedtest)
        print("No: of Missed Test:", self.failedtest)
        print("No: of Failed Test:", self.missedtest)


    def search(self):
        if(self.missedtest>=4 or self.failedtest>=4):
            print("Need Instructor")
        else:
	        print("Study well!")
	        
ls =[]
obj = Test('', 0,'', 0, 0, 0, 0)
print("\nOperations used, ")
print("\n1.Add and Display Student details\n2.Check Student Pass or Fail details\n3.Exit")    
 
try:
    enter = int(input("Please Select an Option: "))
except ValueError:
    exit("\n Wrong Entry. Enter Again")
else:
    print("\n")    
    
if (enter == 1):
    obj.display()
elif (enter == 2):
	obj.search()
elif (enter == 3):
	print("Thank You!")
elif(enter < 1 or enter > 3):
	print("Please Enter Correctly")   
    
    
    

