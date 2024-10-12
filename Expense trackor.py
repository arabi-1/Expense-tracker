def income():
    try:
        income_input = input("What is your monthly income: ")
        income_value = float(income_input)
        income_pkr = f"PKR {income_value:,.2f}"
        return income_pkr
    except ValueError:
        print("Invalid input. Please enter a numerical value for income.")
        return income()


def Dairy():
    dairy = {}
    add_dairy = input("Did you buy any dairy today? (yes/no): ").strip().lower()
    if add_dairy == 'yes':
        try:
            dairy['Eggs'] = int(input("Total eggs bought today: "))
            dairy['Milk'] = float(input("Litres of milk bought today: "))
            yogurt_amount = float(input("Amount of Yogurt bought today (in PKR): "))
            dairy['Yogurt_PKR'] = f"PKR {yogurt_amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter numerical values where required.")
    return dairy


def Vegetables():
    vegetables = {}
    add_veg = input("Do you want to add a vegetable? (yes/no): ").strip().lower()
    while add_veg == 'yes':
        name = input("Enter the name of the vegetable: ")
        try:
            quantity = float(input(f"Enter the quantity (in kg) of {name}: "))
            price = float(input(f"Enter the price (in PKR) of {name} per kg: "))
            vegetables[name] = {
                'Quantity (kg)': quantity,
                'Price (PKR)': f"PKR {price:,.2f}"
            }
        except ValueError:
            print("Invalid input. Please enter numerical values for quantity and price.")
        add_veg = input("Do you want to add another vegetable? (yes/no): ").strip().lower()
    return vegetables


def Bakery():
    bakery = {}
    add_bakery = input("Did you buy a bakery item today? (yes/no): ").strip().lower()
    while add_bakery == 'yes':
        item = input("What did you buy: ")
        try:
            amount = float(input(f"Enter the amount spent on {item} (in PKR): "))
            bakery[item] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_bakery = input("Did you buy another bakery item? (yes/no): ").strip().lower()
    return bakery


def Condiments():
    condiments = {}
    add_condiments = input("Did you buy any condiments today? (yes/no): ").strip().lower()
    while add_condiments == 'yes':
        item = input("What did you buy: ")
        try:
            amount = float(input(f"Enter the amount spent on {item} (in PKR): "))
            condiments[item] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_condiments = input("Did you buy another condiment? (yes/no): ").strip().lower()
    return condiments


def Fruit():
    fruit = {}
    add_fruit = input("Did you buy any fruit today? (yes/no): ").strip().lower()
    while add_fruit == 'yes':
        item = input("What did you buy: ")
        try:
            amount = float(input(f"Enter the amount spent on {item} (in PKR): "))
            fruit[item] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_fruit = input("Did you buy another fruit? (yes/no): ").strip().lower()
    return fruit


def Meat():
    meat = {}
    add_meat = input("Did you buy any meat today? (yes/no): ").strip().lower()
    while add_meat == 'yes':
        item = input("What did you buy: ")
        try:
            amount = float(input(f"Enter the amount spent on {item} (in PKR): "))
            meat[item] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_meat = input("Did you buy another meat item? (yes/no): ").strip().lower()
    return meat


def Lentils():
    lentils = {}
    add_lentils = input("Did you buy any lentils today? (yes/no): ").strip().lower()
    while add_lentils == 'yes':
        item = input("What did you buy: ")
        try:
            amount = float(input(f"Enter the amount spent on {item} (in PKR): "))
            lentils[item] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_lentils = input("Did you buy another lentil item? (yes/no): ").strip().lower()
    return lentils


def Roti():
    roti = {}
    add_roti = input("Did you buy any roti today? (yes/no): ").strip().lower()
    while add_roti == 'yes':
        item = input("What did you buy: ")
        try:
            amount = float(input(f"Enter the amount spent on {item} (in PKR): "))
            roti[item] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_roti = input("Did you buy another roti item? (yes/no): ").strip().lower()
    return roti


def Internet():
    internet = {}
    try:
        expense = float(input("Enter your monthly internet expense (in PKR): "))
        internet['Expense_PKR'] = f"PKR {expense:,.2f}"
    except ValueError:
        print("Invalid input. Please enter a numerical value for the expense.")
        internet['Expense_PKR'] = "PKR 0.00"
    return internet


def Electricity():
    electricity = {}
    try:
        expense = float(input("Enter your monthly electricity expense (in PKR): "))
        electricity['Expense_PKR'] = f"PKR {expense:,.2f}"
    except ValueError:
        print("Invalid input. Please enter a numerical value for the expense.")
        electricity['Expense_PKR'] = "PKR 0.00"
    return electricity


def Gas():
    gas = {}
    try:
        expense = float(input("Enter your monthly gas expense (in PKR): "))
        gas['Expense_PKR'] = f"PKR {expense:,.2f}"
    except ValueError:
        print("Invalid input. Please enter a numerical value for the expense.")
        gas['Expense_PKR'] = "PKR 0.00"
    return gas


def Fuel():
    fuel = {}
    try:
        expense = float(input("Enter your monthly fuel expense (in PKR): "))
        fuel['Expense_PKR'] = f"PKR {expense:,.2f}"
    except ValueError:
        print("Invalid input. Please enter a numerical value for the expense.")
        fuel['Expense_PKR'] = "PKR 0.00"
    return fuel


def ChildFees():
    child_fees = {}
    add_child = input("Do you want to add a child? (yes/no): ").strip().lower()
    while add_child == 'yes':
        name = input("Enter the child's name: ")
        try:
            fee = float(input(f"Enter the school fee for {name} (in PKR): "))
            child_fees[name] = f"PKR {fee:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the fee.")
        add_child = input("Do you want to add another child? (yes/no): ").strip().lower()
    return child_fees


def PocketMoney():
    pocket_money = {}
    add_person = input("Did you give money to your child today? (yes/no): ").strip().lower()
    while add_person == 'yes':
        name = input("Which child was it?: ")
        try:
            amount = float(input(f"Enter the pocket money for {name} (in PKR): "))
            pocket_money[name] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_person = input("Did you give money to another child? (yes/no): ").strip().lower()
    return pocket_money


def EatingOut():
    eating_out = {}
    add_place = input("Did you eat out today? (yes/no): ").strip().lower()
    while add_place == 'yes':
        place = input("What and where did you eat?: ")
        try:
            amount = float(input(f"Enter the amount spent at {place} (in PKR): "))
            eating_out[place] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_place = input("Did you eat out anywhere else? (yes/no): ").strip().lower()
    return eating_out


def Shopping():
    shopping = {}
    add_item = input("Did you do any shopping today? (yes/no): ").strip().lower()
    while add_item == 'yes':
        item = input("What did you buy?: ")
        try:
            amount = float(input(f"Enter the amount spent on {item} (in PKR): "))
            shopping[item] = f"PKR {amount:,.2f}"
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")
        add_item = input("Did you buy anything else? (yes/no): ").strip().lower()
    return shopping


def Emergency():
    try:
        expense = float(input("Enter the amount spent on emergency (in PKR): "))
        return {'Emergency_Expense_PKR': f"PKR {expense:,.2f}"}
    except ValueError:
        print("Invalid input. Please enter a numerical value for the expense.")
        return {'Emergency_Expense_PKR': "PKR 0.00"}


def Expenses():
    expenses = {}

    expenses['Dairy'] = Dairy()
    print(f"You bought {expenses['Dairy'].get('Eggs', 0)} Eggs today")
    print(f"You bought {expenses['Dairy'].get('Milk', 0)} litres of Milk today")
    print(f"You bought {expenses['Dairy'].get('Yogurt_PKR', 'PKR 0.00')} worth of Yogurt today")

    expenses['Vegetables'] = Vegetables()
    for veg, details in expenses['Vegetables'].items():
        print(f"You bought {details['Quantity (kg)']} kg of {veg} for {details['Price (PKR)']}")

    expenses['Bakery'] = Bakery()
    for item, amount in expenses['Bakery'].items():
        print(f"Amount spent on {item}: {amount}")

    expenses['Condiments'] = Condiments()
    for item, amount in expenses['Condiments'].items():
        print(f"Amount spent on {item}: {amount}")

    expenses['Fruit'] = Fruit()
    for item, amount in expenses['Fruit'].items():
        print(f"Amount spent on {item}: {amount}")

    expenses['Meat'] = Meat()
    for item, amount in expenses['Meat'].items():
        print(f"Amount spent on {item}: {amount}")

    expenses['Lentils'] = Lentils()
    for item, amount in expenses['Lentils'].items():
        print(f"Amount spent on {item}: {amount}")

    expenses['Roti'] = Roti()
    for item, amount in expenses['Roti'].items():
        print(f"Amount spent on {item}: {amount}")

    expenses['Internet'] = Internet()
    print(f"Monthly internet expense: {expenses['Internet']['Expense_PKR']}")

    expenses['Electricity'] = Electricity()
    print(f"Monthly electricity expense: {expenses['Electricity']['Expense_PKR']}")

    expenses['Gas'] = Gas()
    print(f"Monthly gas expense: {expenses['Gas']['Expense_PKR']}")

    expenses['Fuel'] = Fuel()
    print(f"Monthly fuel expense: {expenses['Fuel']['Expense_PKR']}")

    expenses['ChildFees'] = ChildFees()
    for name, fee in expenses['ChildFees'].items():
        print(f"School fee for {name}: {fee}")

    expenses['PocketMoney'] = PocketMoney()
    for name, amount in expenses['PocketMoney'].items():
        print(f"Pocket money for {name}: {amount}")

    expenses['EatingOut'] = EatingOut()
    for place, amount in expenses['EatingOut'].items():
        print(f"Amount spent at {place}: {amount}")

    expenses['Shopping'] = Shopping()
    for item, amount in expenses['Shopping'].items():
        print(f"Amount spent on {item}: {amount}")

    expenses['Emergency'] = Emergency()
    print(f"Amount spent on emergency: {expenses['Emergency']['Emergency_Expense_PKR']}")

    return expenses


# Main Program
income_amount = income()
print(f"Your monthly income is: {income_amount}")

all_expenses = Expenses()
