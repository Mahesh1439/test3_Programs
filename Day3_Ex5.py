"""Example 5: Python program to calculate the sum of all the even numbers within the given range..
5--> 2+4=6
"""
x=1
res=0
num=int(input("Enter a range of odd number you want to calculate"))
for add in range(x,num+1):
    if add%2==0:
        res=res+add
print("The sum of all the even numbers are: ",res)
