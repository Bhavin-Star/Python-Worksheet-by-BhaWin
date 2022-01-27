basicSalary = float(input('Enter the basic salary: '))
hra = 15/100 * basicSalary
da = 23/100 * basicSalary
totalSalry = hra + da + basicSalary
tax = totalSalry * 19/100

if(totalSalry > 70000):
    print('Eligilble to pay tax')
    print('Total Salary =', totalSalry - tax)

elif(totalSalry <= 70000 and totalSalry > 0):
    print('Not Eligible to pay tax')
    print('Total Salary =', totalSalry)

else:
    print('Invalid salary entered')
