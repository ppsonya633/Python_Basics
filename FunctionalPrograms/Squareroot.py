
def sqrt(c):
    """This function calculates the square root of a number using Newton's method
    Args:
        c (float): The number for which the square root is to be calculated.
        Returns:
        float: The square root of the number."""
    

    if c < 0:
        return float('nan')
    t = c
    epsilon = 1e-15
    while abs(t - c/t) > epsilon*t:
        t = (c/t + t) / 2.0
    return t

def main():
    c = float(input("Enter the number: "))
    print("The square root of the number is: ",sqrt(c))

main()

