ages = {"Alex": 25, "Zbyszek": 27, "Nina": 14}
names = ["Alex", "Zbyszek", "Nina"]

name = input("Identify yourself, please.")

if name in names:

    print("Welcome ", name)
    print("You are ", ages[name])

else:
    raise ValueError ("Access denied!")
