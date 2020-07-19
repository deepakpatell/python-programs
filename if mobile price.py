mobileprice=int(input("please enter mobile price :"))


if mobileprice > 50000 :
    print("congratulation you will get 15 percent discount on purchasing Rs : ",mobileprice)
    mobileprice=mobileprice-(mobileprice*15/100)
    print("Mobile price after discount :",mobileprice)

else :
    print("sorry you will not get the discount your purchase is ",mobileprice)
    

#input()
input("press enter to exit :") #pls use "" to mention string
#raw_input() this was used in python 2
