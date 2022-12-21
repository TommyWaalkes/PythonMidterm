# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import product

def keepGoing(message):
    answer = input(message)

    if answer == "y" or answer == "Y":
        return True
    elif answer =="n"or answer=="N":
        return False
    else:
        return keepGoing()

def findProduct(name, products):
    for pro in products :
        if pro.name == name :
            return pro

def payment(total):
    print("The grand total is: $" + str(total))
    pay_method = input("How would you like to pay? cash credit or check")

    if pay_method == "cash":
       PayByCash(total)
    elif pay_method == "check":
        PayByCheck(total)
    elif pay_method == "credit":
       PayByCard(total)
    else:
        print("That input was neither cash, credit, nor check")
        print("lets try that again champ!")
        payment(total)

def PayByCard(total):
    print("Please input your 4 digit card number")
    try:
        cc_no = int(input())
        if len(str(cc_no))==4:
            print("Valid Credit card no.")
            date = input("Please input your expiration date")
            try:
                cvv = int(input("Lastly please input the 3 digit cvv on the back of your card"))
                length = len(str(cvv))
                if length == 3:
                    print("Valid Credit card")
                    print("Info: ")
                    print("Credit Card Number: " + str(cc_no))
                    print("Date: " + date)
                    print("CVV: "+ str(cvv))
                    print("")
                    print("$"+str(total) + " charged to your card")
                else:
                    print("Incorrect length for CVV, must be three digits long")
                    print("lets try again")
                    PayByCard(total)
            except:
                print("Input CVV was not a valid number")
                print("Lets try that again")
                PayByCard(total)
        else:
            print("Credit card no was an incorrect length")
            print("lets try that again! ")
            PayByCard(total)

    except:
        print("Input was not a valid number")
        print("let's try that again")
        PayByCard(total)

def PayByCash(total):
    cash = int(input("How much cash would you like to input?"))

    if cash == total:
        print("Exact change, so no change due!")
    elif cash > total:
        diff = cash - total
        print("here is $" + str(diff) + " in change")
    elif cash < total:
        print("Sorry that is not enough cash let's try again")
        payment(total)

def PayByCheck(total):
    print("Please input your check number. It must be four digits")
    try:
        check_no = int(input())
        check_no_s = str(check_no)
        if len(check_no_s) == 4:
            print("Valid Check no")
            print("You have paid $" + str(total))
        else:
            print("Check number was " + len(check_no_s) + " digits")
            print("Invalid length, lets try that again")
            PayByCheck(total)
    except:
        print("input was not a number ")
        print("Lets try that again")
        PayByCheck(total)


def PrintReciept(products, nameToQuan ):
    total = 0
    for name in nameToQuan:
        item = findProduct(name, products)
        quantity = nameToQuan[name]
        subtotal = item.price * quantity

        print(item.name +" $"+str(subtotal) +" = $" + str(item.price) + "*" + str(quantity ))
    grandTotal = GetTotal(products, nameToQuan)
    print("Grand Total: $" + str(grandTotal))

def GetTotal(products, nameToQuan ):
    total = 0
    for name in nameToQuan:
        item = findProduct(name, products)
        quantity = nameToQuan[name]
        subtotal = item.price * quantity
        total += subtotal;
    return total

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    p =  product.Product("Fish", 2, "food", "2 dollar fish, do you want it or nah?")
    print(p)
    p2 = product.Product("Apple", 1, "food", "a red apple")
    p3 = product.Product("Knife", 9, "kitchenware", "a sharp knife")
    nameToQuan = dict()
    products = ((p,p2,p3))

    goOn = True

    while(goOn):
        i = 1
      #  print("Please select a product")
        for pro in products:
            print(str(i)+ ": "+ str(pro))
            i += 1

        answer = int(input("Select an item from the list: 1 to " + str(len(products)))) -1
        if answer < 0 or answer > len(products):
            print("I'm sorry that is not a number between 1 and " + str(len(products)))
            print("lets try that again!")
            continue
        selected = products[answer];
        print(products[answer])
        amount = int(input("How many do you want?"))
        price = selected.price * amount
        print(price)
        nameToQuan[selected.name] = amount
        goOn = keepGoing("Would you like to purchase another item? y/n")

    total = GetTotal(products, nameToQuan)
    payment(total)
    PrintReciept(products, nameToQuan)

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
