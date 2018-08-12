import sqlite3
import pandas as pd

from helper import get_firefox_path

path = get_firefox_path()

conn = sqlite3.connect(path)
df = pd.read_sql("SELECT * FROM moz_bookmarks", conn)

print(df)







