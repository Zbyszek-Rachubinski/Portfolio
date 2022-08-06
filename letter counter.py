import time

text = input("Please provide a text: ")
dict = {}

for sign in text:

    if sign not in dict:
        dict[sign] = 1
    else:
        dict[sign] +=1

print("Here is the letter count of the provided text:")
time.sleep(0.5)
print(dict)
