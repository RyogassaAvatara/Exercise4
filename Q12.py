# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def make_forms(verb):
    characters = ('o', 'ch', 's', 'x', 'z')
    if verb.endswith('y'):
        if True:
            verb = verb[:-1]
            x = verb + 'ies'
            return x
    elif verb.endswith(characters):
        if True:
            y = verb + 'es'
            return y
    else:
        verb += 's'
        return verb


def main():
    user_input = input("Enter a word: ")
    print(make_forms(user_input))


main()
