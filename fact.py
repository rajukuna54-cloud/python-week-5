#with recursion
x = int(input("enter a value:"))
def fact(x):
  
    if x == 0 or x == 1:
        return 1
    else:
        return x*fact(x-1)
print("the value of with recursion:",fact(x))

#without recursion
'''x=int(input("enter a value:"))'''
fact=1
for i in range(1,x+1):
    fact=fact*i
print("the value without recursion:",fact)
