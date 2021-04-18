import pandas as pd
import sys
import os

def convert_to_parquet():
    for item in os.listdir(os.getcwd()):
        if item.endswith(".csv"):
            df = pd.read_csv("./" + item)
            df.to_parquet("./output/" + item.split(".")[0] + ".parquet", engine="auto", compression=None)

    return os.listdir(os.path.join(os.getcwd(), "output")) 

if __name__ == "__main__":
    convert_to_parquet()