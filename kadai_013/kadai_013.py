def calculate_total_price(price, tax_rate):
    total_price = price * 1.1
    return total_price
price = 1000 
tax_rate = 1.1
total_price = calculate_total_price(price, tax_rate)
print(f"{total_price}円")
