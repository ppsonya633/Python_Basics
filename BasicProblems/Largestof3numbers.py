
# author: Pratik Patil
# date: 12-08-2024
# title: Finding the largest of 3 numbers


# This function will take 3 numbers as input and print the largest of them
def largestof_3(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>c:
        print(b)
    else:
        print(c)

def main():
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c=int(input("Enter the third number:"))
    largestof_3(a,b,c)

main()
