class PhoneDirectory:
    phone_book = {}   # Class variable to store all contacts

    def __init__(self, name, number):
        self.name = name
        self.number = number
        PhoneDirectory.phone_book[name] = number  # Add contact to class dictionary

    @classmethod
    def display_contacts(cls):
        """Displays all saved contacts"""
        print("\n--- Phone Directory ---")
        if not cls.phone_book:
            print("No contacts found.")
        else:
            for name, number in cls.phone_book.items():
                print(f"{name}: {number}")

    @staticmethod
    def validate_number(number):
        """Check if phone number is valid (only digits & 10 characters)"""
        return number.isdigit() and len(number) == 10


# ---- Example Usage ----
while True:
    print("\n1. Add Contact\n2. View All Contacts\n3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")
        if PhoneDirectory.validate_number(number):
            PhoneDirectory(name, number)
            print("Contact added successfully!")
        else:
            print("Invalid number! Must contain 10 digits.")
    elif choice == '2':
        PhoneDirectory.display_contacts()
    elif choice == '3':
        print("Exiting Phone Directory. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
