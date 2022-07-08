def dot(a, b):
    # got info about how to use all() from https://www.geeksforgeeks.org/python-check-if-all-elements-in-list-follow-a-condition/
    if not (type(a) == type (b) == list and all(type(n) == list for n in a) and all(type(n) == list for n in b)\
        and all(type(n) == int for m in a for n in m) and all(type(n) == int for m in a for n in m)):# check if a, b are 2D arrays
        raise TypeError("Please enter two 2D arrays full of integers")
    if not (all(len(n) == len(a[0]) for n in a) and all(len(n) == len(b[0]) for n in b)):
        raise ValueError("Please ensure that each 2D array has a consistent amount of columns per row")
    elif len(a[0]) != len(b):# check if a, b is has the right dimensions
        raise ValueError("Please ensure that the matrices are of the correct dimensions to be multiplied")
    else:
        new_row = len(a)
        mid = len(b)
        new_col = len(b[0])
        new = [[0] * new_col for i in range(new_row)] 
        for n in range(new_row):
            for m in range (new_col):
                new[n][m] = sum(a[n][i] * b[i][m] for i in range(mid))
        return new

if __name__ == "__main__":
    a, b = [[1, 2, 3], [7, 8, 9]], [[1], [1], [1]]
    print(a, b, dot(a, b))