#import statements
import pandas as pd # Importing pandas for the DataFrame
from textblob import TextBlob # Importing TextBlob
from pathlib import Path # Importing Path
import re # Importing re for sub()
import nltk # Importing the nltk module
from nltk.corpus import stopwords # Importing the stopwords module
nltk.download('stopwords') #Downloading the stopwords package
stops = stopwords.words("english") # Downloading the English stopwords list

book = Path("A Dog Of Flanders by Ouida.txt").read_text(encoding = "utf-8") # 1. Reading in the book
book = re.sub(r"'", "", book) # 5. Using sub to remove all occurences of apostrophes
book = TextBlob(book)

parts = book.tags # 2. Tag each word with its POS
print(parts)

# 3. Turn each tuple into a single token consisting of "tag€word" (use € as a separator since it is unlikely to occur in the text).
x = lambda x: f"{x[1]}€{x[0]}" # Building and saving the lambda function
book_string = " ".join(list(map(x, parts)))# Use a lambda function to do the rearranging and separate the tokens with spaces (converting to a string)
print(book_string)

book_string = re.sub(r"\$", "", book_string) # 4. Using sub to remove all occurences of the dollar sign
print(book_string)

book_string = TextBlob(book_string)# 6. Converting the string to a TextBlob
print(book_string)

n_grams = book_string.ngrams(n = 5)# 7. Generating 5-grams
print(n_grams)

DataFrame1 = pd.DataFrame(n_grams) # 8. Converting into a Dataframe (saving 2 independent copies)
DataFrame2 = pd.DataFrame(n_grams) # Saving independent copy
print(DataFrame1)

# 9. Stripping the words from all the columns except #3; remove tags from that column instead.
halve = lambda x, y: x.split("€")[y] # Declaring and saving the lambda function for stripping off tags and words.
for i in range(5):
        if i != 3: # For all but 3
            DataFrame1[i] = [halve(token, 0) for token in DataFrame1[i]] # strip the words away
        else: # For 3
            DataFrame1[i] = [halve(token, 1) for token in DataFrame1[i]] # strip away the tag
print()

DataFrame2[5] = ["".join(DataFrame1.iloc[n]) for n in DataFrame1.index] # 10. Add a 5th column to DataFrame2 consisting of the concatenation of columns 0-4 in step 9

counts = DataFrame2[5].value_counts() # 11. Use pandas value_counts function to generate a Series that contains a frequency count of column 5

# 12. Add a 6th column to DataFrame2, consisting of the frequency of the string in the 5th column.
count_check = lambda x: counts[x] # Create a lambda function that receives a string (the pattern from row 5) and uses that as an index to the series of step 11 to return the matching count column
DataFrame2[6] = [count_check(x) for x in DataFrame2[5]] # Use a list comprehension to add the column.
print(DataFrame2)

# 13. Use List Comprehension and the lambda of step 9 to create a new DataFrame that strips the tags from columns 0-4 (loop 5 times)
DataFrame3 = pd.DataFrame(DataFrame2) #Copy DataFrame 2 into DataFrame 3; the constructor is to avoid aliasing DataFrame3 to DataFrame2 and altering DataFrame2
for i in range(5): # For 0 - 4
    DataFrame3[i] = [halve(token, 1) for token in DataFrame2[i]] # Strip the tags from the column
print(DataFrame3)

DataFrame3.drop(DataFrame3[DataFrame3[6] == 1].index, inplace = True) # 14. Use drop to remove all rows where frequency is 1
print(DataFrame3)

# 15. Clean up your DataFrame by removing rows where the word in column 3 is a stopword. (Can traverse the DataFrame and drop conditionally for full credit)
for index, row in DataFrame3.iterrows(): # For each row in DataFrame3
    if row[3].lower() in stops: # If the word in column 3 is a stop word
        DataFrame3.drop(index, inplace = True) # Drop the row
print(DataFrame3)

# 16. Use sort_values to create a new dataframe that is sorted first by column 5, then 6
DataFrame4 = DataFrame3.sort_values([5, 6])

# 17. Printing the full Dataframe
with pd.option_context("display.width", 500, "display.max_rows", None, "display.max_columns", None):
    print(DataFrame4)