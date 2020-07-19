
text=input('enter animal name :')

def Animal_Name(text):
    t1=text.split()
    return t1[0][0] == t1[1][0]


Animal_Name(text)
