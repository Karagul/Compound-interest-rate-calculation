balance = 3329
annualInterestRate = 0.2

keepbalance = balance
payment = 0

while balance >= 0:
    balance = keepbalance
    payment += 10
    for i in range(0, 12):
        monthlyunpaidbalance = balance - payment
        balance = monthlyunpaidbalance * (1 + annualInterestRate/12.0)

    
print 'Lowest Payment: ' + str(payment)