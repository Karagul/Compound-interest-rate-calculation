balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

totalpaid = 0

for month in range(1, 13):
    monthpayment = balance * monthlyPaymentRate
    unpaidbalance = balance - monthpayment
    
    
    balance = unpaidbalance * (1 + annualInterestRate/12.0)
    
    totalpaid += monthpayment
    
    
    print 'Month: ' + str(month)
    print 'Minimum monthly payment: ' + str(round(monthpayment,2))
    print 'Remaining balance: ' + str(round(balance, 2))

print 'Total paid: ' + str(round(totalpaid, 2))
print 'Remaining balance: ' + str(round(balance, 2))
    