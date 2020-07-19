Pan=input("please enter pan card number :")

acn=range(10,99)

adhar=int(input("please enter adhar card number :"))


if (adhar==112233445566 and Pan =='ABC1122') or (adhar in acn) :
    print("you are valid user"+" and your card number is :",adhar)

else :
        print("you are not valid user")
