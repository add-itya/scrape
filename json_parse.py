import json
import pandas as pd

# Load JSON data from file
with open('combined_records.json') as f:
    data = json.load(f)

# Flatten JSON data into a DataFrame
df = pd.json_normalize(data)

# Reorder columns
ordered_columns = [
    'allMeta.tile.product.displayName',
    'allMeta.tile.product.brand',
    'allMeta.tile.reviews.count',
    'allMeta.tile.reviews.averageRating',
    'allMeta.tile.product.productId',
    # Add other columns here if needed
]

# Ensure all columns are included, then reorder
df = df[ordered_columns + [col for col in df.columns if col not in ordered_columns]]

# Save DataFrame to CSV
df.to_csv('final_output.csv', index=False)
