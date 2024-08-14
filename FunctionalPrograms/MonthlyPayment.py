
def Monthly_pay(principle_amount,year,interest_rate):
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