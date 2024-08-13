# author: Pratik Patil
# date: 12-08-2024
# title: Finding the Nth Harmonic number


# This function will take a number as input and return the Nth Harmonic number
def Nth_Harmonicnumber(n):
    harmonic=1
    for i in range(2,n+1):
        harmonic+=1/i
    return harmonic



# Main function
def main():
 n=int(input("Enter the value of n:"))

 if(n!=0):
   print(round(Nth_Harmonicnumber(n),1))

main()
