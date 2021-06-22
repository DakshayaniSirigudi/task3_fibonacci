def fibonacci(x):
    if x<0:
        print("invalid input")
    elif x==0:
        return 0
    elif x==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

print("Fabonacci series is as follows: ")
i=0
while i<10:
    print(int(fibonacci(i)))
    i=i+1
print("done")
