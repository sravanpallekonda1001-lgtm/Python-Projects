products={"Shoes":2500,"Jacker":3000,"Tshirt":600,"Watch":5000,"Saree":5000}
print(products)
print("="*100)
print("----Available products----\n Shoes=2500,\n Jacket = 3000, \n Tshirt=600,\n Watch=500,\n Saree=5000")
product_name=input("enter the input:")
if product_name in products.keys():
    quantity=int(input("how many you want:"))
    total = products[product_name]*quantity+50
    print("your total bill is",total,"+ 50 rs for gst")
else:
    print("product not available")
    