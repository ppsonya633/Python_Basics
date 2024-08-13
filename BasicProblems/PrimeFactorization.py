# author: Pratik Patil
# date: 12-08-2024
# title: Prime Factorization

# This function will take a number as input and will chek if the number is prime or not if number is prime it will return true else false

def isprime(n):
    for i in range(2,(n//2)+1):
        if(n%i==0):
            return False
    return True


factor=[]

# This function will take a number as input and will return the prime factors of the number
def prime_factors(number):
    i=2
    while(i*i<=number):
        if(number%i==0):
            if(isprime(i)):
                factor.append(i)
        i+=1

    return factor

# Main function
def main():
    number=int(input("Enter the number:"))
    print(list(prime_factors(number)))

main()