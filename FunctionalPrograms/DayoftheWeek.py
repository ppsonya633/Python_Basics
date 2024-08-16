
'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Get Monthly Payments

'''
def Monthly_pay(principle_amount,year,interest_rate):
    """
    Discription:
        This function calculates the monthly payment for a loan based on the principle amount, number of years, and interest rate.
    Args:
        principle_amount (float): The principle amount of the loan.
        year (int): The number of years for the loan.
        interest_rate (float): The interest rate for the loan.
    Returns:
        float: The monthly payment for the loan."""
    n = 12*year
    interest_rate = interest_rate/(12*100)
    payment = (principle_amount*interest_rate)/(1-(1+interest_rate)**(-n))
    return payment

def main():
    p = float(input("Enter the principal amount: "))
    y = int(input("Enter the number of years: "))
    r = float(input("Enter the rate of interest: "))
    payment = Monthly_pay(p,y,r)
    print("The monthly payment is: ",payment)

main()