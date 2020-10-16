# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def filter_long_words(lwords, n):
    lst = []
    for i in lwords:
        if len(i) > n:
            lst.append(i)
        else:
            pass
    return lst


if __name__ == "__main__":
    user_input = list(input("Enter list of long words: ").split(","))
    length = int(input("Minumum Length: "))
    print("Words with more than", length, "letters are ", filter_long_words(user_input, length))
