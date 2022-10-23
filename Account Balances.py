#===================================================================================
# Program Name: Account Balances
# Author Name: Keegan Bramlet
# Date: 10/23
# Purpose of the program: Calculate Yearly Bank Balances with a fixed interest rate
#===================================================================================
balance = 1000
rate = 0.05

y0 = balance
y1 = balance * rate + balance
y2 = y1 * rate + y1
y3 = y2 * rate + y2

print(y1)
print(y2)
print(y3)
