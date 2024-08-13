# author: Pratik Patil
# date: 12-08-2024
# title: Power of 2

# This function will take a number as input and print the power of 2 till that number and return the 
def powerof_2(n):
    value=1
    while(n>=0):
        value*=2
        n=n-1
        print(value,end=" ")
    return value





# Main function
def main():
   number=int(input("Enter the number:"))

   if(number>=0 and number<31):
     powerof_2(number)
   else:
    print("stack overflow")

main()