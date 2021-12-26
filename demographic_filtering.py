import numpy as np
import pandas as pd

df = pd.read_csv('articles.csv')
df = df.sort_values(['total_events'], ascending=[True])
output=df.head(20)
print(output)