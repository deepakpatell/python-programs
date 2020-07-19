model  = input("Enter mobile model name : ")
ram    = input("Enter mobile ram size : ")
rom    = input("Enter mobile rom size : ")
camera = input("Enter mobile camera mp : ")
price  = int(input("Enter mobile pricr : "))

print("Mobile model : ",model)
print("Mobile ram : ",ram)
print("Mobile rom : ",rom)
print("Mobile camera : ",camera)
print("Mobile price : ",price)

price = price - 5000

print("Mobile model  after discount :",price)

price = price + (price*(18/100))


print ("price after gst :", price)


print("the price of ",model + " is ",price)
