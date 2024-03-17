product_prices = {
    "Rice": [45, 42, 41, 40],
    "Salt": [34, 35, 36, 36],
    "Fish": [200, 202, 201, 205],
    "Orange": [100, 99, 101, 102]
}

def find_minimum_price(product_name):
    if product_name in product_prices:
        prices = product_prices[product_name]
        min_price = min(prices)
        min_index = prices.index(min_price) + 1  
        print(f"{product_name} -> market {min_index} value = {min_price}")
    else:
        print("Product not found in the data")

product_name = input("Input the product name: ")

find_minimum_price(product_name)
