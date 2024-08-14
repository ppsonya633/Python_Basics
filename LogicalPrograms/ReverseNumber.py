
#This function will get the int number as a parameter and it will return the reverse of the number

def reverse_number(number):
    """
    This function will take number as a input and it will return the reverse of the number
    Args:
         number(int)
    Returns:
            reversenumber(int)
    """
    tnumber=number
    reversenumber=0
    while number>0:
        remainder=number%10
        reversenumber=(reversenumber*10)+remainder
        number=number//10

    return reversenumber

def main():
    number=int(input("Enter the number:"))
    result=reverse_number(number)
    print(result)

main()