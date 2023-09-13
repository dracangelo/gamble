MAX_LINES = 3


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

def get_number_of_lines():
    while True:
        lines = input("enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): ## ensures input is a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else :
                print ("enter a valid line number")
        else :
            print("please enter a number")
            
    return lines
    


def main():
    balance = deposit()
    
main()
        