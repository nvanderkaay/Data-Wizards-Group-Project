import pandas as pd

df = pd.read_csv('/Users/Candie/Desktop/Online_Cars_Sale_Marketplace.csv')


print("Preview of Original Data:")
print(df.head())



df_clean = df[~df.apply(lambda row: row.astype(str).str.contains("NA")).any(axis=1)]


print("\nPreview of Cleaned Data:")
print(df_clean.head())

print(df_clean.head())


print("\nOriginal shape:", df.shape)
print("Cleaned shape:", df_clean.shape)


luxury_brands = ['BMW', 'Mercedes', 'Audi', 'Lexus']

df_clean['VehicleType'] = df_clean['Make'].apply(
    lambda make: 'Luxury' if make in luxury_brands else 'Budget'
)


dealer_focus = df_clean.groupby(['SellerName', 'VehicleType']).size().unstack(fill_value=0)


dealer_focus['Luxury%'] = dealer_focus['Luxury'] / (dealer_focus['Luxury'] + dealer_focus['Budget'])
print(dealer_focus.sort_values('Luxury%', ascending=False).head(10))

