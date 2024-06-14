import json
import os

# Directory containing your JSON files
json_dir = 'json/'

# List to store all records
records = []
set_total = set()

# Iterate through each JSON file in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        filepath = os.path.join(json_dir, filename)
        
        # Open each JSON file and load its contents
        with open(filepath, 'r') as f:
            data = json.load(f)
            # Assuming each JSON file contains a list of records under a key 'records'
            for item in data:
                product_id = item['allMeta']['tile']['product']['productId']
                # Check if the product_id is not already in the set
                if product_id not in set_total:
                    # Add product_id to the set
                    set_total.add(product_id)
                    # Add the item to the records list
                    records.append(item)

# Print the number of unique product IDs found
print(f"Number of unique product IDs: {len(set_total)}")

# Write the records to a JSON file
output_file = 'combined_records.json'
with open(output_file, 'w') as f:
    json.dump(records, f, indent=4)

print(f"Records have been written to '{output_file}'")
