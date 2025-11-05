x="srinivas"
def myfun():
    x="sagar"
    print("My name is "+x)

myfun()
print("My name is "+x)
age=(input("age : "))
# eligible="Yes" if age>="18" else "No"
# print(eligible)
print("teen") if age>="18" or age<="13" else print("adult")
# vote=("no","yes")[age>=18]
# print(vote)
# FOR LOOPS
def q1():
    # display odd numbers from 0 to 20
    for x in range(0, 20, 2):
        print(x)

# q1()


def q2():
    # display numbers from 10 to 1 descending order
    for x in range(10, 0, -1):
        print(x)
# q2()


def q3():
    # to print character present ingiven string
    str = input("enter string:")
    for ch in str:
        print(ch)

# q3()
# WHILE LOOPS


def q4():
    # write a python to print nnumbers from 1 to 10 using while loop
    x = 1
    while x <= 10:
        print(x)
        x += 1


def q5():
    # python program to display sum of first n digits using while loop
    i = 1
    while i <= 10:
        i += i
    print(i)


q5()
q4()


def square(a):
    return a*a

a = int(input())
print(square(a))
# cook your dish here
class A:
    def methodA(self):
        print("Method A")
class B:
    def methodB(self):
        print("Method B")
class C(A,B):
    pass

c=C()
c.methodA()
c.methodB()