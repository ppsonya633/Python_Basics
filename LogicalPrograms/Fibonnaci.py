
# This function will take a n as a parameter and it will print the fibonnaci series upto n terms.
def fibonnaci_series(n):
    """
    This function will take a n as a parameter and it will print the fibonnaci series upto n terms.
    Args:
         n(int)
    Returns:
            None"""
    previous=0
    next=1
    for i in range(n):
        sum=previous+next
        print(sum,end=" ")
        previous=next
        next=sum


def main():
    n=int(input("Enter the number of terms: "))
    fibonnaci_series(n)

main()