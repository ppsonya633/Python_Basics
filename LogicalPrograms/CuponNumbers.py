#imported the random module
import random
distinct_coupon=[]

#function to generate a random number
def generate_coupon():
    """
    This function generates a random number between 0 and 1
    Args:
        None
        Returns:random number between 0 and 1(float)"""
    coupon=random.random()
    return round(coupon,1)

def distinct_cupones(n):

    """
    This function generates n distinct coupon numbers
    Args:
        n: Number of distinct coupon numbers to generate
        Returns: List of distinct coupon numbers"""
    for i in range(n):
        coupon=generate_coupon()
        if coupon not in distinct_coupon:
            distinct_coupon.append(coupon)
    return distinct_coupon

def main():
    number=int(input("Enter the number "))
    result=distinct_cupones(number)
    print(result)


main()

