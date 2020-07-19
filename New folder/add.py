def abc(a,b,c):
    add=0
    add=a+b+c
    if add<=21:
        return add

    elif add<31 and 11 in (a,b,c):
        add=add-10
        return add
    else :
        return 'bust'
