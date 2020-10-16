# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def make_forming(verb):
    new = ""
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    vowels = ['a', 'e', 'i', 'o', 'u']
    if verb == "be":
        new = verb + "ing"
    elif verb[-2::] == "ee":
        new = verb + "ing"
    elif verb[-2::] == "ie":
        new = verb[:-2].split()
        new = new[0] + "ying"
    elif verb[-1] == "e":
        new = verb[:-1].split()
        new = new[0] + "ing"
    elif verb[-1] in consonants:
        if verb[:-2] in consonants:
            if verb[-2:-1] in vowels:
                new = verb + str(verb[-1]) + "ing"
    else:
        new = new + "ing"
    return new


def main():
    user_input = input("Enter a Word: ")
    print(make_forming(user_input))



