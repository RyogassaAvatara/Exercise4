# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def translate(text):
    word = ""
    for i in range(len(text)):
        if text[i] == "a":
            word = word + text[i]
        elif text[i] == "i":
            word = word + text[i]
        elif text[i] == "e":
            word = word + text[i]
        elif text[i] == "u":
            word = word + text[i]
        elif text[i] == "o":
            word = word + text[i]
        elif text[i] == " ":
            word = word + text[i]
        else:
            word = word + text[i] + "o" + text[i]
    return word


def main():
    user_input = input("Type a text you want to be translated: ")
    print("Translation:", translate(user_input))


main()
