
#This function will take two parameters dividend and divisor and print the quotient and remainder
def quotient_and_remainder(dividend,divisor):

    tquotient=dividend//divisor
    reminder=dividend%divisor
    
    print("Quotient:",tquotient)
    print("Reminder:",reminder)

def main():
    dividend=int(input("Enter the dividend:"))
    divisor=int(input("Enter the divisor:"))
    quotient_and_remainder(dividend,divisor)

main()
