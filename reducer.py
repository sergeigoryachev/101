#!/usr/bin/env python

import pandas as pd
import sys

for item in sys.stdin.split():
   if item.endswith(".csv"):
        df = pd.read_csv(f"/user/hadoop/HW1/{item}")
        df.to_parquet("/user/hadoop/HW1/" + item.split(".")[0] + ".parquet", engine="auto", compression=None)
        break
    
