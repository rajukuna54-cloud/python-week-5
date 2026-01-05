#without recursion
print("without recursion")
n = int(input("Enter a number: "))
if n <= 1:
    print(n, "is not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
#with recursion
print("with recursion")
def prime(n, i=2):
    if n <= 1:
        return 0
    if i == n:
        return 1
    if n % i == 0:
        return 0
    return prime(n, i + 1)
if prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
