products = {
    "product1": {"name": "Laptop", "price": 800, "quantity": 5},
    "product2": {"name": "Phone", "price": 500, "quantity": 10},
    "product3": {"name": "Tablet", "price": 300, "quantity": 8}
}

sorted_products = dict(sorted(products.items(), key=lambda x: x[1]["price"]))
print(products)
for product_id, product_info in sorted_products.items():
    print(f"Product ID: {product_id}, Name: {product_info['name']}, Price: {product_info['price']}, Quantity: {product_info['quantity']}")