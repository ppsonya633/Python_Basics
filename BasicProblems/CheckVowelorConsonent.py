
# This function will take a character as input and check if it is a vowel or a consonant

def check_vowelorconsonent(character):
    if character in ['a','e','i','o','u','A','E','I','O','U']:
        print("Vowel")
    else:
        print("Consonant")

# Main function
def main():
    character=input("Enter the character:")
    check_vowelorconsonent(character)

main()