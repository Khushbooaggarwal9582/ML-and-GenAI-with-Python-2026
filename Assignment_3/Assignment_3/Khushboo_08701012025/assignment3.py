#Q1
def func():
    i=1
    while(i<=10):
        print(i)
        i+=1
func()

#Q2
def sum(n):
    sum=0
    while(n>0):
        sum+=n
        n-=1
    return sum
n=int(input("enter number"))
print(sum(n))

#Q3
def reverse(n):
    rev=0
    while(n>0):
        lastdig=n%10
        rev=rev*10+lastdig
        n//=10
    return rev
n=int(input("enter number"))
print(reverse(n))

#Q4
def count(n):
    cnt=0
    while(n>0):
        cnt+=1
        n//=10
    return cnt
n=int(input("enter number"))
print(count(n))

#Q5
def palindrome(n):
    temp=n
    rev=0
    while(n>0):
        lastdig=n%10
        rev=rev*10+lastdig
        n//=10
    return temp==rev
n=int(input("enter number"))
if(palindrome(n)):
    print("palindrome")
else:
    print("not palindrome")

#Q6
def fibonacci(n):
     a,b=0,1
     for i in range(n):
          print(a,end=" ")
          a,b=b,a+b
n=int(input("Enter number of terms:"))
fibonacci(n)

#Q7
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Division by zero not allowed"
    return a/b
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=int(input("Enter choice(1-4):"))
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
if choice==1:
    print("Result:",add(a,b))
elif choice==2:
    print("Result:",subtract(a,b))
elif choice==3:
    print("Result:",multiply(a,b))
elif choice==4:
    print("Result:",divide(a,b))
else:
    print("Invalid Choice")

#Q8
name=input("Enter name:")
roll=input("Enter roll no:")
marks=input("Enter marks:")
with open("student.txt","w")as f:
    f.write("Name:"+name+"\n")
    f.write("Roll No:"+roll+"\n")
    f.write("Marks:"+marks)
    f.close()
print("Data stored successfully")

#Q9
with open("student.txt","w")as file:
    content=file.read()
print(content)

#Q10
try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("Result:",a/b)
except ZeroDivisionError:
    print("Division by zero is not allowed")

#Q11
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
name=input("Enter name:")
marks=int(input("Enter marks:"))
s=Student(name,marks)
s.display()

