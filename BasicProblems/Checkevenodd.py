
# author: Pratik Patil
# date: 12-08-2024
# title: Check if the number is even or odd


# This program will take a number as input and print if the number is even or odd
def check_evenodd(number):
    if(number%2==0):
        print("Even")
    else:
        print("Odd")


# Main function
def main():
    number=int(input("Enter the number:"))
    check_evenodd(number)

main()