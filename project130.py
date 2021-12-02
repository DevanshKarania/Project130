from os import access
import pandas as pd
import csv

df = pd.read_csv("class129/final.csv")

del df["Star_name1"]
del df["Distance1"]
del df["Mass1"]
del df["Radius1"]

df.to_csv("Final_Deleted.csv")