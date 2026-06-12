import pandas as pd

df = pd.read_csv("dataset/phishing_email.csv")

print(df.head())
print("\nColumns:")
print(df.columns)

print("\nShape:")
print(df.shape)