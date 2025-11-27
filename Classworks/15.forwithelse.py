#for with else
products=["laptop","screen","phone","speaker"]
search=input("enter the product:").strip()
for i in products:
    if i == search:
        print("product found")
        break
    print(i)
else:
    print("end of the products. the item you search for is not found")
