# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def pangram_check(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in text.lower():
            return "Your sentence is NOT a Pangram"
    return "Your sentence is a Pangram"


def main():
    user_input = input("Enter a sentence to check if is a pangram: ")
    print(pangram_check(user_input))

main()
