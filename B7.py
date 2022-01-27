t = float(input('Enter the temperature: '))

if(t >= 0 and t <= 25):
    print('Cold')

elif(t >= 26 and t <= 35):
    print('Moderate')

elif(t > 35):
    print('Hot')

elif(t<0):
    print('Freezing')

else:
    print('Error')