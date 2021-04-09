#!/usr/bin/env python

import pandas as pd
import os
import sys

for item in sys.stdin:
   if item.endswith(".csv"):
        df = pd.read_csv(f"/user/hadoop/HW1/{item}")
        df.to_parquet("/user/hadoop/HW1/" + item.split(".")[0] + ".parquet", engine="auto", compression=None)
    
