a = int(input('Enter the 1st no: '))
b = int(input('Enter the 2nd no: '))
c = int(input('Enter the 3rd no: '))
print()

# If a is the greatest
if(a > b > c):
   print(a, 'is the greatest')
   print(b, 'is lower than', a, 'and greater than', c)
   print(c, 'is the lowest')

elif(a > c > b):
   print(a, 'is the greatest')
   print(c, 'is lower than', a, 'and greater than', b)
   print(b, 'is the lowest')

# If b is the greatest
elif(b > a > c):
   print(b, 'is the greatest')
   print(a, 'is lower than', b, 'and greater than', c)
   print(c, 'is the lowest')

elif(b > c > a):
   print(b, 'is the greatest')
   print(c, 'is lower than', b, 'and greater than', a)
   print(a, 'is the lowest')

# If c is the greatest
elif(c > a > b):
   print(c, 'is the greatest')
   print(a, 'is lower than', c, 'and greater than', b)
   print(b, 'is the lowest')

elif(c > b > a):
   print(c, 'is the greatest')
   print(b, 'is lower than', c, 'and greater than', a)
   print(a, 'is the lowest')

# Equality 1
elif(a > b or a > c and b == c):
    print(a, 'is the greatest')
    print(b, 'is equal to', c, 'and is lower than', a) 

elif(a < b or a < c and b == c):
    print(a, 'is the lowest')
    print(b, 'is equal to', c, 'and is greater than', a) 

# Equality 2
elif(b > a or b > c and a == c):
    print(b, 'is the greatest')
    print(a, 'is equal to', c, 'and is lower than', b) 

elif(b < a or b < c and a == c):
    print(b, 'is the lowest')
    print(a, 'is equal to', c, 'and is greater than', b) 

# Equality 3
elif(c > a or c > b and a == b):
    print(c, 'is the greatest')
    print(a, 'is equal to', b, 'and is lower than', c) 

elif(c < a or c < b and a == b):
    print(c, 'is the lowest')
    print(a, 'is equal to', b, 'and is greater than', c) 

# Equality 4
elif(a == b == c):
    print('All numbers are equal')

else:
    print('Error')
   
   