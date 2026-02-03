fruits = {"apple":130, "avocado":50, "sweet cherries":100}

item = input("item: ").lower().strip()

if item in fruits:
    print(f"calories: {fruits[item]}")
