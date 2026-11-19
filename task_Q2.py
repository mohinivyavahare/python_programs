name = input("enter your name: ")
count = 0

for char in name.lower():
    if char in 'aeiou':
        count += 1

print("total vowels:", count)