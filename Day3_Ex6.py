"""Example 6: Python program to print a multiplication table of a given number."""
table_num=int(input("Enter which table you want to print"))
for x in range(1,11):
    res=table_num*x
    print(f"{table_num} X {x} = ",res)
