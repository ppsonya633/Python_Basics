# author: Pratik Patil
# date: 12-08-2024
# title: Flip a coin


import random
# random_value=random.random()
# rounded_value=round(random_value,1)
# print(rounded_value)


# This function will return a random number between 0 and 1
def getrandom_number():
    random_value=random.random()
    rounded_value=round(random_value,1)
    return rounded_value

# This function will take the total number of flips as input and return the percentage of heads and tails
def flip_coin(total_flips):
    noof_heads=0
    noof_tails=0
    for i in range(total_flips):
     result=getrandom_number()
     if result<0.5:
        noof_tails+=1  
     else:
        noof_heads+=1
    
    percentage_heads=(noof_heads/total_flips)*100
    percentage_tails=(noof_tails/total_flips)*100
    print("Percentage of Heads:",percentage_heads)
    print("Percentage of Tails:",percentage_tails)

total_flips=int(input("Enter the number of flips:"))



# Main function
def main():
   if(total_flips>0):
    flip_coin(total_flips)
   else:
    "Invalid Input"

main()
