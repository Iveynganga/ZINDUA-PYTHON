
def find_highest_priced_product(products):
    if not products:
        return None

    # Use the max function with a lambda function as the key to find the dictionary with the highest price
    highest_priced_product = max(products, key=lambda x: x["price"])

    return highest_priced_product

# Example Usage:
products_list = [
    {"name": "Laptop", "price": 1200},
    {"name": "Smartphone", "price": 800},
    {"name": "Tablet", "price": 500},
    {"name": "Headphones", "price": 120},
]
result = find_highest_priced_product(products_list)
print(result)
 

 
