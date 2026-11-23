num = int(input("enter a number: "))


def check_odd_even(num):
    if num % 2 == 0:
        return '"even"'
    else:
        return '"odd"'


result = check_odd_even(num)
print(result)