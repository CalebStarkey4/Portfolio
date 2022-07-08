# Import statements
import re
import pandas as pd
import numpy as np

# Building the dataframe
list = [["(000)000-0000", "0"] for i in range(14)]
for i in range(6):
    list[i][0] = f"({(i + 1) % 10}{(i + 2) % 10}{(i + 3) % 10}){(i + 4) % 10}{(i + 5) % 10}{(i + 6) % 10}-{(i + 7) % 10}{(i + 8) % 10}{(i + 9) % 10}{i}"
dates = ["022122", "02212022", "2/21/22", "02/1/22", "2-21-22",\
        "02-1-2022", "02-21-1922", "02211922", "02-32-22", "023222",\
        "13-21-22", "132122", "Feb 21 2022", "202212020"]
for i in range(14):
    list[i][1] = dates[i]
data = pd.DataFrame(list)
# found information on how to rename rows and columnts at 
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html
data.rename(index = {0:"abc", 1:"def", 2:"ghi", 3:"jkl", 4:"mno", 5:"pqr", 6:"er1", 7:"er2",\
                    8:"er3", 9:"er4", 10:"er5", 11:"er6", 12:"er7", 13:"er8"},\
                    columns = {0:"tel", 1:"date"}, inplace = True)

def date_linter(data): # Allows for the use of return in unpaid_intern to make things more efficient
    """Iterates through a DataFrame and runs the dates through """
    for n in range(len(data.date)):
        data.date[n] = unpaid_intern(data.date[n])
        
def unpaid_intern(date):
    """Converts dates from some variation of MM-DD-YYYY to YYYY-MM-DD format"""
    pattern = r"(\d{1,2})[-/]?(\d{1,2})[-/]?(\d{2,4})" # Single regular expression to find the month, day, and year from the date inputted; fulfills the second bonus requirement
    pattern_2 = r"(\d{2})(\d{2})(\d{4})"
    if not (re.fullmatch(pattern, date) or re.fullmatch(pattern_2, date)): # Checks to see if the date inputted followed a valid format
        return np.nan
    elif re.fullmatch(pattern, date):
        result = re.search(pattern, date) # Searches for the values in parentheses in the regular expression
    else:
        result = re.search(pattern_2, date)
    month, day, year = result.groups() # Unpacks result into month, day, and year
    if len(month) == 1: # Make the length of month uniform
        month = "0" + month
    if int(month) < 0 or int(month) > 12: # Checks to ensure that month has a possible value
        return np.nan
    if len(year) == 2 and 0 <= int(year) <= 22: # Checks to ensure that 2-digit year inputs are possible and then expands them to 4-digit year output
        year = "20" + year
    elif not (len(year) == 4 and 2000 <= int(year) <= 2022): # Checks to ensure all other year inputs are 4 digits and represent valid year inputs
        return np.nan
    if len(day) == 1: # Makes the length of day uniform
        day = "0" + day
    if int(month) in [range(1, 9, 2), range(8, 14, 2)]:
        max_days = 31
    elif int(month) in [4, 6, 9, 11]:
        max_days = 30
    elif is_leap(int(year)): # Check for leap year
        max_days = 29
    else:
        max_days = 28
    if int(day) < 0 or int(day) > max_days: # Checks to ensure day has a possible value (doesn't take the month into account when doing this)
        return np.nan
    return (f"{year}-{month}-{day}") # Returns the linted date in its new YYYY-MM-DD format

def is_leap(year):
    if year % 4: # If the year is divisible by 4
        return False
    if year % 100 == 0 and year % 400: # If the year is divisible by 100 but not by 400
        return False
    return True

if __name__ == "__main__":
    print("Before:")
    print(data)
    date_linter(data)
    print("After:")
    print(data)