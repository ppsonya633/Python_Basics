
# This function will take number as a input and it will print the number is prime or not

def check_prime(number):

    """
    This function will take number as a input and it will print the number is prime or not
    Args:
         number(int)
    Returns:
            None"""
    for i in range(2,(number//2)+1):
        if number%i==0:
            print("The number is not prime")
            break
        else:
            print("The number is prime")
            break

def main():
    number=int(input("Enter the number:"))
    check_prime(number)

main()
