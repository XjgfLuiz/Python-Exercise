def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 1 < len(s) < 7:
        return False
    if not s[:2].isalpha():
        return False

    number_started = False

    for i in s:
        if not i.isalnum():
            return False

        if i.isdigit():
            if not number_started:
                number_started = True
                if i == "0":
                    return False

        if number_started==True and i.isdigit()!=True:
            return False

    return True

main()