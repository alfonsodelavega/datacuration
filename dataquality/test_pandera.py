#
# Pandera: data testing library
#
# Source: https://pandera.readthedocs.io/en/stable/index.html

# Alternatives:
#
# - Amazon Deequ: https://github.com/awslabs/deequ
# - Great Expectations: https://docs.greatexpectations.io/docs/tutorials/quickstart/
# - Soda Core: https://github.com/sodadata/soda-core

#%%
import pandas as pd
import pandera as pa
from pandera import Check

#%%
df = pd.read_csv("penguins.csv")
df.head(10)

#%%
'''
This schema passes for the dataset. Possible modifications to see errors:

- Remove one of the species of the Check.isin restriction
- Change the 60 bill length value with 50
- Remove the "nullable" parameter for the bill length
'''

schema = pa.DataFrameSchema({
    "species": pa.Column(object, Check.isin(["Adelie", "Chinstrap", "Gentoo"])),
    "bill_length_mm": pa.Column(float, Check(lambda length: length < 60), nullable=True)
})

validated_df = schema(df)
print(validated_df)
