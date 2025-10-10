 #Mini Market Sepeti
 
products = {"apple":3, "banana":2, "bread":2, "milk":4}
print("Welcome to the Mini Market!")

print("Can you add 3 products to your basket?")

product1 = input("Enter the name of the first product:")
product2 = input("Enter the name of the second product:")
product3 = input("Enter the name of the third product:")

while True:
    if product1 in products and product2 in products and product3 in products:
        
        total_price = products[product1] + products[product2] + products[product3]
        print(f"The total price of {product1}, {product2}, and {product3} is: {total_price} TL")
        break
    else:
        print("One or more products are not available. Please try again.")
        product1 = input("Enter the name of the first product:")
        product2 = input("Enter the name of the second product:")
        product3 = input("Enter the name of the third product:")
        
    
        
        
    


 