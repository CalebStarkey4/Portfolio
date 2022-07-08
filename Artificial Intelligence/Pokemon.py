# Loosely based on ex9.16
import pandas as pd
import matplotlib.pyplot as plt

# Download the Pokémon dataset from kaggle.com (Links to an external site.) (you'll need to create a free account).

data = pd.read_csv('pokemon.csv')

# You may need to research some of these DataFrame manipulations. Number the output to match the questions.

# Sample output
#   1: There are 41 columns in the dataset.

# 1: how many columns are there?
columns = len(data.columns)
print(f"1: There are {columns} columns.")

# 2: how many rows are there?
rows = len(data.index)
print(f"2: There are {rows} rows.")

# 3: print top 5 rows (there will be an ellipse showing some middle columns are not being displayed)
top_five = data.head()
print(f"3: The top five rows are as follows:\n{top_five}")

# 4: print a list of all the column names
column_names = ", ".join(data.columns[0:columns - 2]) + ", and " + data.columns[-1]
print(f"4: The column names are {column_names}.")

# 5: are there any duplicate values in the name column? hint: true if count for that field > unique value 
duplicates = True if data.name.count() != len(data.name.unique()) else False
string1 = "" if duplicates else "no "
print(f"5: There are {string1}duplicate values.")

# 6: modify your DataFrame so the name column becomes the index, sorted alphabetically; show bottom 5
data.sort_values("name", inplace = True)
data.set_index("name", inplace = True)
bottom_five = data.tail()
print(f"6: The bottom five rows are as folows:\n{bottom_five}")

# 7: print the row for record 100
record_100 = data.iloc[[100]]
print(f"7: The 100th record is as follows:\n{record_100}.")

# 8: print the row with index Magikarp
Magikarp_row = data.loc[["Magikarp"]]
print(f"8: Magikarp is in row {Magikarp_row}.")

# 9: how many Pokémons have the Fish Pokémon classfication?
fish_count = data["classfication"].value_counts()["Fish Pokémon"]
print(f"9: {fish_count} Pokémon are classified as Fish Pokémon.")

# 10: what is the Japanese name of Machamp?
machamp_name = data["japanese_name"]["Machamp"]
print(f"10: Machamp's Japanese name is {machamp_name}.")

# 11: what is the highest height (height_m) of any Pokémon?
max_height = max(data["height_m"])
tallest_Pokémon = data.loc[data["height_m"] == max_height].index
print(f"11: The tallest Pokémon is {max_height} meters.")

# 12: what is the pokedex_number of the Pokémon with this max height?
max_height_pokedex = data[data["height_m"] == max_height].iloc[0]["pokedex_number"]
print(f"12: The pokedex number is {max_height_pokedex}.")

# 13: how many Pokémon don't have a type2? hint: NaNs are ignored in the statistics, so compute inverse first
single_type_count = rows - data['type2'].count()
print(f"13: {single_type_count} Pokémon only have one type.")

# 14: how many abilities does the first Pokémon have? hint: convert the string it returns to a list with split()
ability_count = len(data['abilities'][data.index[0]].split(","))
string2 = "ies" if ability_count > 1 else "y"
print(f"14: The first Pokémon has {ability_count} abilit{string2}.")

# 15: create a histogram for the speed column
speed_histogram = data.hist("speed")
plt.show()

input("This has been a brief analysis of Pokemon")