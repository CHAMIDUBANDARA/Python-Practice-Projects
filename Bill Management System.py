
# This whole code display about billing system.
# We use to create this code python basic.
# To start the billing, enter number "1".
# To remove a product from the bill, enter number "2".
# To calculate total from the bill, enter number "3".
# To print bill, enter number "4".
# To exit the current bill and print new bill, enter number "5".
# To run this code we have to enter product name firstly.
# Then we have to enter product price.
# After that we need to enter quantity of the products.
# Finally need to enter discount to find available discount for each products.
# Then we have two main options. Either add more products to the cart or finish select products and print the bill.
# Finally we can see the total by reducing discount from each products.
# So after that we have to give cash to the cashier.
# Then the bill is printed by the cashier and display the balance in the bill.
# Finally we can close the bill.


from datetime import datetime

class ISCItem:# create a Class
    def __init__(self, name, price, quantity, discount=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount

class ISCBill:# create a Class
    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.items = []
        self.datetime = datetime.now()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self.items:
            item_total = (item.price * item.quantity) - (item.price * item.quantity * item.discount / 100)
            total += item_total
        return total

    def print_bill(self, cash):
        for item in self.items:
            print(f"{item.name:12} {item.price:8.2f} {item.quantity:8} {item.discount:8}%")
        print("\n\n")
        total = self.calculate_total()
        print(f"Sub Total: {total:.2f}\nCash: {cash:.2f}")
        print("\tITUM SHOPPING COMPLEX\n\t#120,Diyagama Homagama.\n\tTel : 051-7995675\n\tE-mail:ISC@Diyagama.lk\n")
        print(f"Date: {self.datetime.strftime('%Y-%m-%d')}\nTime:{self.datetime.strftime('%I:%M:%S%p')}")
        print(f"Cashier: {self.cashier_name}\n")
        print("Item Name     Price     Quantity   Discount ")
        for item in self.items:
            print(f"{item.name:12} {item.price:8.2f} {item.quantity:8} {item.discount:8}%")
        print("\n")
        total = self.calculate_total()
        print(f"Sub Total: {total:.2f}\nCash: {cash:.2f}\n")
        balance = cash - total
        print(f"Balance: {balance:.2f}\nNumber of items: {len(self.items)}\n\n")
        print("WE STRIVE TO PROVIDE  EXCELLENT SERVICE\n\tAND QUALITY PRODUCTS.\nTHANK YOU FOR SHOPPING WITH US.\n\tHAVE A GREAT DAY! ")
        


def main():
    cashier_name = input("Enter cashier name: ")
    bill = ISCBill(cashier_name)
    choice = ""
    while choice != "5":
        print("\nWelcome to ITUM SHOPPING COMPLEX\n1. Add item\n2. Remove item\n3. Calculate total\n4. Print bill\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            discount = float(input("Enter item discount percentage: "))
            item = ISCItem(name, price, quantity, discount)
            bill.add_item(item)
            print("Item added successfully.")

        elif choice == "2":
            if len(bill.items) == 0:
                print("No items in the bill.")
                continue
            print("Items in the bill:")
            for i, item in enumerate(bill.items):
                print(f"{i+1}. {item.name} ({item.quantity})")
            index = int(input("Enter the index of the item to remove: "))
            if index < 1 or index > len(bill.items):
                print("Invalid index.")
                continue
            item = bill.items[index - 1]
            bill.remove_item(item)
            print("Item removed successfully!")

        elif choice == "3":
            total = bill.calculate_total()
            print(f"Total: {total}")

        elif choice == "4":
            cash = float(input("Enter cash payment: "))
            bill.print_bill(cash)

        elif choice == "5":
            print("Exiting...")

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
