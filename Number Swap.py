number = int(input("Please input a 5-digit number"))
# print(swap(number))
if 10000 <= number < 100000:
    new = (number % 10) * 10000
    number // 10
    new += (number % 10) * 1000
    number // 10
    new += (number % 10) * 100
    number // 10
    new += (number % 10) * 10
    number // 10
    new += (number % 10)
    print(new)
else:
    print("number must be 5 digits")



#this is just for fun to see if I can optimize it since I'm done
def swap(number):
    new = 0
    for i in range():
        new += (number % 10) * (10000/(10**i))
        number // 10
    return new
