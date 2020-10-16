# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def find_longest_word(lwords):
    numbers = []
    for i in lwords:
        numbers.append(len(i))
    return max(numbers)


if __name__ == "__main__":
    user_input = list(input("Enter a List of words: ").split(","))
    print("")
    print(" Longest Word Length: ", find_longest_word(user_input))
