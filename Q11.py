# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def char_freq(string):
    freq = {}
    for i in range(len(string)):
        if string[i] in freq:
            freq[string[i]] = freq.get(string[i]) + 1
        else:
            freq[string[i]] = 1
    return freq

def main():
    user_input = input("Enter a Word >> ")
    print(char_freq(user_input))

main()