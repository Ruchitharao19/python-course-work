print("Welcome! to NYKAA")
print("---------------------------")
Product_brand = input("Enter Nykaa product brand: ")
Product_name = input("Enter Nykaa product name: ")
Product_price = float(input("Enter Nykaa product price: "))
Product_quantity = int(input("Enter Nykaa product quantity: "))
Product_discount_percentage = float(input("Enter Nykaa product discount percentage: "))
Product_description = input("Enter Nykaa product description: ")

# Calculate discounted price
discounted_price = Product_price - (Product_price * Product_discount_percentage / 100)

# Display Nykaa product information using different string formatting methods
print("\nNykaa Product Information:")
print("---------------------------")

# Using comma separation
print("Product Name:", Product_name, "\tPrice:", Product_price, "\tQuantity:", Product_quantity)

# Using percentage formatting
print("Discount: %.2f" % Product_discount_percentage)

# Using f-strings (Python 3.6+)
print(f"Discounted Price: ₹{discounted_price:.2f}")

# Using .format() method
print("Description: {}".format(Product_description))

# Using f-strings with multiple values
print(f"Product: {Product_name}, Price: ₹{Product_price:.2f}, Quantity: {Product_quantity}, Discounted Price: ₹{discounted_price:.2f}")

print("Your order is confirmed")

