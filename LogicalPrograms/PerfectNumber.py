

numberfactors=[]

def calculate_sum(numberfactors):
    """This function calculates the sum of the factors of the number
       Args:
         numberfactors: List of factors of the number
         Returns:
              sum: Sum of the factors of the number(int)
    """
    sum=0
    for i in numberfactors:
        sum+=i
    return sum
    

def check_perfect_number(number):
    """This function will take number as a parameter and it will calculate all the factor of the number 
       and then it will check whether the sum of the factors of the number is equal to the number or not
       Args:
         number: Number to check for perfect number
         Returns:
              None"""
    for i in range(1,(number//2)+1):
        if number%i==0:
            numberfactors.append(i)

    if calculate_sum(numberfactors)==number:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

def main():
    number=int(input("Enter the number to check for perfect number: "))
    check_perfect_number(number)
    print("Factors of the number are: ",numberfactors)

main()
