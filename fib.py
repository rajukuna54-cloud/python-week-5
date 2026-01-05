#with recursion
x = int(input("enter a value:"))
def fib(x):
    if x==1:
        return 0
    elif x==2:
        return 1
    else:
        return fib(x-2)+fib(x-1)
print("fibonacci series with recursion:")
for i in range(1,x+1):
    print(fib(i),end=" ")

#without recursion

fib1=0
fib2=1
print("\nfibonacci series without recursion:")
for i in range(1,x+1):
    print(fib1,end=" ")
    temp = fib1
    fib1=fib2
    fib2=temp+fib2
