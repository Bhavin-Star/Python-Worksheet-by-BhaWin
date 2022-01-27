n = int(input('Enter the level till where you want to print the fibonacci series: '))

a = 0
b = 1
print(a)
print(b)

# n - 1 bec 2 Nos are printed before also
for i in range(1, n-1):
    c = a + b
    print(c)
    a = b
    b = c