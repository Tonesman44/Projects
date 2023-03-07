#round function rounds to nearest whole number so I convert the decimal to an int
initial_balance = float(input("How much change is owed: "))
temp_balance = round(initial_balance*100)
num_coins = 0

#Determine which coin to use and return the coins value
def determine_coin(amount_remaining):
    amount_used = 0
    if(amount_remaining - 25 >= 0):
        return 25
    elif(amount_remaining - 10 >= 0):
        return 10
    elif(amount_remaining - 5 >= 0):
        return 5
    else:
        return 1
#Loop through balance subtracting each coins value and counting number of coins used
while(temp_balance > 0):
    temp_balance = temp_balance - determine_coin(temp_balance)
    num_coins = num_coins + 1
    
print ("Change owed: ", initial_balance)
print(num_coins)

