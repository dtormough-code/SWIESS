contact = {}
def add_contact(name, phone):
   name=input("Enter contact name: ")
   phone=input("Enter contact phone number: ")  
   email=input("Enter contact email: ")
   contact[name] = {'phone': phone, 'email': email}
print("Contact added successfully!")
def view_contacts():
    if not contact:
        print("No contacts found.")
    else:
        for name, details in contact.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}")
def delete_contact(name):
    if name in contact:
        del contact[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"Contact '{name}' not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            delete_contact(name)
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()