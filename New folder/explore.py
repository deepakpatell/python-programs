a=[1,2,3,3]
def fun(a):
    for i in range(0,len(a)-1):
        if a[i]==3 and a[i+1]==3:
            return True
        else :
            return False
