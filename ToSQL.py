import pandas as pd
import sqlite3
df =pd.read_csv('titanic.csv')
titanic = df.to_sql(name='titanic', con=sqlite3)