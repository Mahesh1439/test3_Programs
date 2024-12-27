"""Example 2: Python program to print all the even numbers within the given range."""
x=1
y=int(input("Enter a range of even numbers do you want to print"))
for num in range(x,y+1):
    if num%2==0:
        print(num)