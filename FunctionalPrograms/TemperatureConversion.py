
def convert_to_celsius(fahrenheit):
    celcius=(fahrenheit-32)*5/9
    return celcius

def convert_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit


def main():
    temperature=float(input("Enter the temperature: "))
    unit=input("Enter the unit (C/F): ")
    if unit=="C":
        print("The temperature in Fahrenheit is: ",convert_to_fahrenheit(temperature))
    elif unit=="F":
        print("The temperature in celcius is: ",convert_to_celsius(temperature))
    else:
        print("Invalid unoit")

main()