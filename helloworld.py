print("Hello World")
def ps(x,y):
    z=2x+3y
    a=0
    
    for i in range(1,100):
        if i%3==0:
            continue
        else:
            a=a+i
    return a*z

ps(3,7)
