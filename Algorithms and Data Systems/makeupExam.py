stack = [None] * 5
top = 0
# "Assumed" initialization. I included it for testing purposes;
# if I wasn't supposed to include it in my final code submision,
# please ignore both of these.
# The instructions weren't super clear on whether to actually include these in the code or not. 

def push(i):          # Pushes things to the stack
    global top          # allows for changes to top
    global stack          # allows for changes to stack
    if top == len(stack):          # If the stack is full
        stack += [None] * len(stack)          # Double the size of the stack
    stack[top] = i          # adds i to stack
    top += 1          # increases top

def pop():          # Pops things from the stack
    global top          # allows for changes to top
    result = stack[top - 1]          # stores value to be returned
    top -= 1          # decreases top
    return result          # returns value

def evaluate(postfix):          # Function that actually evaluates the postfix
    digits = '123456789'          # declares string to use later to check for digits
    operators = '+-/*'          # declares string to use later to check for operators
    for i in postfix:          # loops through all characters in postfix
        if i in digits:          # if i is a digit
            push(int(i))          # Convert it to an int and push it to the stack
        elif i in operators:          # else if i is an operator
            a = pop()          # pop top value and store it for future use; this is to ensure that we don't assume commutative property of addition and subtraction
            if i == '+':          # if addition
                push(pop() + a)          # pop another one and add the stored value to it
            elif i == '-':          # if subtraction
                push(pop() - a)          # pop another one and subtract the stored value from it
            elif i == '/':          # if division
                push(pop() // a)          # pop another one and divide it by the stored value using integer division
            else:          # if multiplication
                push(pop() * a)          # pop another one and multiply it by the stored value
        else:          # if i is neither an operator or a digit
            return "Invalid input"          # return an error message
    return (pop()) if top == 1 else "Invalid input"          # if after popping the answer the stack will be empty, return the answer; otherwise return an error message

print(evaluate(input('Please enter a postfix expression: ')))          # prompt the person running the code for a postfix expression, evaluate it, and then print it