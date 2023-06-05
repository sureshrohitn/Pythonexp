def fib():
    a,b=0,1
    while(a<10):
        yield b
        a,b=a,a+b
    return a
        
x=fib()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
for i in fib():
    print(i)
