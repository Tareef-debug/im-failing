#Program to check if the nth bit is set or not 
def setornot(number,n):
    if number & (1<<(n-1)):
        print("Set")
    else:
        print("Not set")
number = int(input("Enter the number"))
n = int(input("Enter bit number"))
setornot(number,n)