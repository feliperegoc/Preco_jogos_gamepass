import json

# Load the data from the JSON file
with open('produtos_xbox.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

# Initialize a variable to hold the total price
total_price = 0

# Loop through each product and add the price to the total
for product in products:
    # Check if the product has a price and add it to the total
    if 'Preço' in product and product['Preço'].isdigit():
        total_price += float(product['Preço'])

print(f"O Preço total dos produtos é: {total_price}")
