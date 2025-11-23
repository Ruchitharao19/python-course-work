products=['laptop','mouse','phone','keyword','charger','speaker']
stocks=[100,20,500,0,200,6]
print('*'*30)
print(products)
print('*',30)
network=True
if network:
    product=input("Enter the product: ").strip()
    if product in products:
        index=products.index(product)
        if stocks[index]==0:
            print(f"{product}-out of stock")
        elif 1<=stocks[index]<=10:
            print(f"{product}-only few items left.hurry up")
        else:
            print(f"{product}")
    else:
        print("product not found")
else:
    print("check your internet")
