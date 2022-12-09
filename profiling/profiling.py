#
# Automatic dataset reporting using Pandas profiling library
#
# Source: https://github.com/ydataai/pandas-profiling
# Dataset: https://github.com/allisonhorst/palmerpenguins

#%%
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

#%%
df = pd.read_csv("penguins.csv")
df.head(10)

#%%
profile = ProfileReport(df, title="Pandas Profiling Report")

# %%
# There are many more ways to use a report, here we export it to html
profile.to_file("pandas_profiling_report.html")
