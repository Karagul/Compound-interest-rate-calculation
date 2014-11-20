balance = 320000
annualInterestRate = 0.2


def checkpayment(balance,payment):
    for i in range(12):
        unpaidbalance = balance - payment
        balance = unpaidbalance * (1+annualInterestRate/12)
    return balance

high = (balance * (1 + annualInterestRate/12)**12) / 12.0 
low = balance / 12.0

payment = (high + low) /2 

while abs(checkpayment(balance, payment)) >= 0.01:
    if checkpayment(balance, payment) > 0:
        low = payment
        payment = (high + low) /2 
    else:
        high = payment
        payment = (low + high)/2

    
    
        
print 'Lowest Payment: ' + str(round(payment,2))
