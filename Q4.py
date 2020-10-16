# Name : Ida Bagus Ryogassa Avatara
# ID   : 2440100323


def is_member(val, a):
    if a.count(val) >= 1:
        return True
    else:
        return False


if __name__ == "__main__":
    x = eval(input("Enter Value: "))
    a = eval(input("Enter a List: "))
    print(is_member(x, a))


