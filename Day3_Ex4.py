"""Example 4: Python program to calculate the sum of all the odd numbers within the given range.
5--> 1+3+5=9
"""
x=1
res=0
num=int(input("Enter a range of odd number you want to calculate"))
for add in range(x,num+1):
    if add%2!=0:
        res=res+add
print(res)
