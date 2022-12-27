# Run command: pip install pandas
# pip install lxml

import pandas as pd

# for print formatting
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)

### The longest river in the world ###
df = pd.read_html("https://en.wikipedia.org/wiki/List_of_river_systems_by_length")
print(df[5].info())
# print(df[5].to_string())


### List of dog breeds recognized by the FCI ###
# https://github.com/paiv/fci-breeds/blob/main/fci-breeds.csv
df2 = pd.read_csv(
    "https://raw.githubusercontent.com/paiv/fci-breeds/main/fci-breeds.csv"
)

print(df2.info())
# print(df2.head())
# print(df2.to_string())


# Python Module Index
# https://docs.python.org/3/py-modindex.html

# Python Package Index
# https://pypi.org/
