def sumint(num):
    total = 0
    if type(num) != int:
        print("Wrong input... BYE!")
    else:
        for i in range(num + 1):
            total = total + i 
    print(f"Total is {total}")

sumint(3)

""" Professor Answer
def sumint(number):
    num = 1
    sum = 0
    while num < number + 1:
        sum = sum + num
        num = num + 1
    return sum
"""