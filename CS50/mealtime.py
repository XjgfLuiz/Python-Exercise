def main():
    time = input("what time is it? ")
    meal = convert(time)
    if meal > 6 and meal < 10:
        print("breakfast")
    elif meal > 11 and meal < 14:
        print("lunch")
    elif meal > 17 and meal < 21:
        print("dinner")
    else:
        ...

def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    result = hour+(minute/60)
    return result


if __name__ == '__main__':
    main()