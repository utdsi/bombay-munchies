class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability


class Canteen:
    def __init__(self):
        self.inventory = []
        self.sales_records = []

    def add_snack(self, snack_id, name, price, availability):
        snack = Snack(snack_id, name, price, availability)
        self.inventory.append(snack)
        print(f"Snack '{snack.name}' added to inventory.")

    def remove_snack(self, snack_id):
        snack = self.find_snack_by_id(snack_id)
        if snack:
            self.inventory.remove(snack)
            print(f"Snack '{snack.name}' removed from inventory.")
        else:
            print("Snack not found in inventory.")

    def update_availability(self, snack_id, availability):
        snack = self.find_snack_by_id(snack_id)
        if snack:
            snack.availability = availability
            print(f"Availability of snack '{snack.name}' updated to {availability}.")
        else:
            print("Snack not found in inventory.")

    def sell_snack(self, snack_id):
        snack = self.find_snack_by_id(snack_id)
        if snack:
            if snack.availability == "yes":
                self.sales_records.append(snack)
                snack.availability = "no"
                print(f"Snack '{snack.name}' sold.")
            else:
                print("Snack is currently unavailable.")
        else:
            print("Snack not found in inventory.")

    def find_snack_by_id(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                return snack
        return None


def display_menu():
    print("=== Mumbai Munchies Canteen ===")
    print("1. Add Snack to Inventory")
    print("2. Remove Snack from Inventory")
    print("3. Update Snack Availability")
    print("4. Sell Snack")
    print("5. Exit")


def get_user_choice():
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= 5:
            return int(choice)
        print("Invalid choice. Please try again.")


def main():
    canteen = Canteen()
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 1:
            snack_id = input("Enter Snack ID: ")
            name = input("Enter Snack Name: ")
            price = float(input("Enter Snack Price: "))
            availability = input("Is Snack Available? (yes/no): ")
            canteen.add_snack(snack_id, name, price, availability)
        elif choice == 2:
            snack_id = input("Enter Snack ID to remove: ")
            canteen.remove_snack(snack_id)
        elif choice == 3:
            snack_id = input("Enter Snack ID to update availability: ")
            availability = input("Is Snack Available? (yes/no): ")
            canteen.update_availability(snack_id, availability)
        elif choice == 4:
            snack_id = input("Enter Snack ID to sell: ")
            canteen.sell_snack(snack_id)
        elif choice == 5:
            print("Thank you for using Mumbai Munchies Canteen system. Goodbye!")
            break


if __name__ == "__main__":
    main()
