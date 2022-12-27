# Run command: pip install pandas
# pip install lxml

import pandas as pd

df = pd.read_html("https://en.wikipedia.org/wiki/List_of_river_systems_by_length")

print(df[5].to_string())
