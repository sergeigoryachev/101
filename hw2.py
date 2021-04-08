import pandas as pd
import os

element_list = os.listdir()
#print("List of files in current dir:", element_list)

for i in range(len(element_list)):
    if element_list[i].endswith(".csv"):
        df = pd.read_csv(f".\Documents\expedia-hotel-recommendations\{element_list[i]}")
        df.to_parquet("/user/hadoop/HW1/" + element_list[i] + ".parquet", engine="auto", compression=None)
    #df_parquet = pd.read_parquet(".\\Documents\\" + element_list[i] + ".parquet")
