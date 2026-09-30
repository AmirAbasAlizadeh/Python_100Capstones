def fibbu(num) :
    a = 1
    b = 0
    for x in range(num) :
        a , b = a + b, a
        
        print (a , b)

print(fibbu(10))