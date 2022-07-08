# stack implementation
def palindrome2():
    old = n = int(input("Please enter a positive integer: "))
    stack = []
    reverse = 0
    i = 1
    while(n != 0):
        stack.append(n % 10)
        n = n // 10
    while(len(stack) > 0):
        reverse = stack.pop() * i + reverse
        i *= 10

# recursive implementation
def recursive_reverse(n, r):
    if n != 0:
        return recursive_reverse(n // 10, r * 10 + (n % 10))
    else:
        return r

def palindrome1():
    nr = int(input("Please enter a positive integer: "))
    print("Palindrome" if nr == recursive_reverse(nr, 0) else "Not a Palindrome")

# for loop implementation
def palindrome0():
    nums = list(input("Please input a positive integer: "))
    palindrome = True
    for i in range(len(nums)//2):
        if nums[i] != nums [-i - 1]:
            palindrome = False
            break
        print("Palindrome" if palindrome else "Not a Palindrome")

