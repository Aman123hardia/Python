import pandas as pd
df = pd.DataFrame({
    "State": ['Andhra Pradesh', 'Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu'],
    "Capital": ['Hyderabad', 'Mumbai', 'Bengaluru', 'Trivandrum', 'Chennai'],
    "Literacy %": [89, 77, 82, 97,85],
    "Avg High Temp(c)": [33, 30, 29, 31, 32 ]
})
# print(df)


print(df.loc[[0,1,2,3,4]])