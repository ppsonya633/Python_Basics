# author: Pratik Patil
# date: 12-08-2024
# title: Check if the year is a leap year or not


# This function will take a year as input and print if the year is a leap year or not
def leap_year(year):
  if(len(str(year))==4):  
    if(year%4==0 and year%400==0):
       print("Leap Year")
    elif(year%4==0 and year%100!=0):
         print("Leap Year")
    elif(year%400==0):
            print("Leap Year")
    else:
        print("Not a Leap Year")
  else:
        print("Invalid Input")
    



def main():
    year=int(input("Enter the year:"))
    leap_year(year)

main()