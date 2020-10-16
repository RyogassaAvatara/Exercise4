# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def words_to_ints(lst):
    numbers = []
    for i in lst:
        numbers.append(len(i))
    return numbers


if __name__ == "__main__":
    user_input = list(input("Enter words >> ").split(","))
    print(words_to_ints(user_input))

