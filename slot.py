def deposit():
    while True:
        amount = input("Amount you want to bet")
        if amount.isdigit(): ## ensures input is a number
            amount = int(amount)
            if amount > 0 : ## check if number is bigger than zero
                break
            else :
                print ("Amount must be greater than 0")
        else :
            print("please enter a number")
            
    return amount


deposit()
        