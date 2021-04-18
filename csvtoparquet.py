import pandas as pd
import sys

for item in sys.stdin:
    if item.endswith(".csv"):
        df = pd.read_csv("./" + item)
        df.to_parquet("./" + item.split(".")[0] + ".parquet", engine="auto", compression=None)
        break
