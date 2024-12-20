def display_menu():
    menu = {
        "Burger": 5.99,
        "Pizza": 8.99,
        "Salad": 4.99,
        "Soda": 1.99
    }
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    return menu

def select_item(menu):
    while True:
        choice = input("Enter the name of the item you want to order: ")
        if choice in menu:
            return choice, menu[choice]
        print("Invalid selection. Please choose an item from the menu.")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input("Enter cash amount: "))
            if cash >= total_cost:
                return cash
            print(f"Insufficient funds. Please provide at least ${total_cost:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def calculate_change(cash, total_cost):
    return cash - total_cost

def main():
    menu = display_menu()
    item, price = select_item(menu)
    print(f"You selected {item}, which costs ${price:.2f}.")
    cash = process_payment(price)
    change = calculate_change(cash, price)
    print(f"Payment accepted. Your change is ${change:.2f}. Thank you for your order!")

if __name__ == "__main__":
    main()
