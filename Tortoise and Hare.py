#Simulation: The Tortoise and the Hare (See page 152)

#Instead of 2 functions to generate the percentages in the table for the tortoise and the hare, 
# use a single move() function and distinguish between hare/tortoise using a parameter.  

#Create a second function print_positions() to display the dist-position line (see below). 
# The function should include an optional argument border which defaults to False.
# When the function is called with True, the output should be bracketed between [ and ]. 
# Be careful that an OUCH still aligns the closing bracket (see second sample below).

#Upload text of source code, and 2 sample runs (one with, one without a border; the second one should include at least one OUCH)

from random import randrange
from time import sleep

def move(hare, tortoise, dist):
    """Moves the tortoise and the hare"""
    t = randrange(1, 11)
    h = randrange(1, 11)
    new_t = tortoise
    # Tortoise:
    if t <= 5: # Fast plod (3 squares to the right): 50%
        new_t += 3
        if new_t > dist:
            new_t = dist
    elif t <= 7: # Slip (6 squares to the left): 20%
        new_t -= 6
        if new_t < 1:
            new_t = 1
    else: # Slow plod (1 square to the right): 30%
        new_t += 1
    # Hare:
    if h <= 2: # Sleep (no move): 20 %
        return new_t, hare
    if h <= 4: # Big hop (9 squares to the right): 20%
        if hare >= dist - 8:
            return new_t, dist
        return new_t, hare + 9
    if h <= 5: # Big slip (12 squares to the left): 10%
        if hare <= 12:
            return new_t, 1
        return new_t, hare - 12
    if h <= 8: # Small hop (1 square to the right): 30%
        return new_t, hare + 1
    # Small slip (2 squares to the left): 20%
    if hare <= 2:
        return new_t, 1
    return new_t, hare - 2

def ouch(p, border, dist):
    leeway = dist - p
    if leeway >= 4:
        ouch = "OUCH!"
    elif leeway == 3:
        ouch = "OOF!"
    elif leeway == 2:
        ouch = "OW!"
    else:
        ouch = "OW"
    print(("[" if border else ""), \
        " " * (p - 1), \
        ouch, \
        sep = "", end = ((" " * (leeway - len(ouch) + 1) + "]\n") if border else "\n"))

def print_positions(border = False, dist = 70, doSleep = False):
    """Prints the race"""
    T = H = 1
    print("ON YOUR MARK...")
    if doSleep:
        sleep(1)
    print("GET SET...")
    if doSleep:
        sleep(1)
    print("BANG!")
    if doSleep:
        sleep(.5)
    print("AND THEY'RE OFF!")
    if doSleep:
        sleep(1)
    while T != dist and H != dist:
        T, H = move(H, T, dist)
        if H == T != dist:
            ouch(H, border, dist)
        elif H == T == dist:
            print(("[" if border else ""), \
            " " * (dist - 1), \
            "θ", \
            sep = "", end = ("]\n" if border else "\n"))
        else:
            first = (("T", T) if T > H else ("H", H))
            second = (("H", H) if T > H else ("T", T))
            print(("[" if border else ""), \
                " " * (second[1] - 1), \
                second [0], \
                " " * (first[1] - second[1] - 1), \
                first[0], \
                sep = "", end = (((" " * (dist - first[1])) + "]\n") if border else "\n"))
        if doSleep:
            sleep(.75)
    if H != T:
        print("And the winner is...")
        if doSleep:
            sleep(1)
        if H == dist != T:
            print("HARE!")
        else:
            print("TORTOISE!")
    else:
        print("It's a tie!")
    again = input("Would you like to watch another race (y/n)? ")
    if again == "y":
        Border = (True if input("Would you like to see the finish line (y/n)? ") == "y" else False)
        Dist = int(input("How long would you like the race to be (please enter a positive integer)? "))
        while Dist < 0:
            Dist = int(input("Please enter a positive integer: "))
        print_positions(Border, Dist, True)
    
if __name__ == "__main__":
    # print_positions(False, 70, False) # No border, no sleep
    # print_positions(True, 70, False) # Border, no sleep
    print_positions(True, 30, True) # Border and sleep