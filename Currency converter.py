# Code to convert currencies 
# You can use it to realtime convert between dollars, rupees and yen

initial = int(input("Which currency will you use?:\n 1. Rupees 2.Dollars 3.Yen: "))
final = int(input("Which currency do you want?:\n 1. Rupees 2.Dollars 3.Yen: "))
cash = float(input("Enter the amount: "))
ex_rate = 1.00


def to_dollars(initial,cash):
    global ex_rate
    if initial == 1:
        ex_rate = 83.17

    elif initial == 3:
        ex_rate = 142.41 

    else:
        ex_rate == 1

    money = ex_rate * cash

    print("The amount in dollars is: ", money)

def to_rupees(initial,cash):
    global ex_rate

    if initial == 2:
        ex_rate = 1/83.17

    elif initial == 3:
        ex_rate = 1.71 

    else:
        ex_rate == 1

    money = ex_rate * cash

    print("The amount in dollars is: ", money)

def to_yen(initial,cash):
    global ex_rate

    if initial == 2:
        ex_rate = 1/1.71

    elif initial == 1:
        ex_rate = 1/142.41 

    else:
        ex_rate == 1

    money = ex_rate * cash

    print("The amount in dollars is: ", money)

if final == 2:
    to_dollars(initial,cash)

elif final == 1:
    to_rupees(initial,cash)

elif final == 3:
    to_yen(initial,cash)

else:
    print("Invalid currency")



    


