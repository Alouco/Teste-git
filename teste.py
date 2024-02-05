def fun():
    global y
    y= int(y)
    x = 100 * y
    print(x)
    
y = 2

fun()