print("Welcome to Nykaa!")
print("--------------------")
product_id = int(input("Enter Product ID: "))
product_name = input("Enter Product Name: ")
product_price = float(input("Enter Price: "))
stock_details = tuple(input("Enter Stock Details (available,sold): ").split(","))
discount_percentage = float(input("Enter Discount Percentage: "))
product_features = set(input("Enter Product Features: ").split(","))
supplier_name = input("Enter Supplier Name: ")
supplier_contact = input("Enter Supplier Contact Number: ")
supplier_location = input("Enter Supplier Location: ")

# Create supplier details dictionary
supplier_details = {
    "Name": supplier_name,
    "Contact": supplier_contact,
    "Location": supplier_location
}

# Calculate available stock
available_stock = int(stock_details[0])

# Calculate discounted price
discounted_price = product_price - (product_price * discount_percentage / 100)

# Display product details using different formatting methods
print("\nProduct Information:")
print("--------------------")

# Using Comma Separation (sep=',')
print("Product ID:",product_id , "\tName:",product_name,"\tPrice:",product_price, sep=',')
print(f"Stock Available: {available_stock} units")
print("Product Features:", product_features)
# Using Percentage Formatting (% operator)
print("Product Discount: %.2f%%" % discount_percentage)

# Using f-strings (f"")
print(f"discounted_price:{discounted_price}")

# Using .format() method
print("Supplier Details - Name : {}, Contact : {}, Location : {}".format(supplier_details["Name"], supplier_details["Contact"], supplier_details["Location"]))
print("product delivered")
print("--------------------------")
