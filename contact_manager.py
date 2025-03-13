# Contact manager application

contacts = []
def add_contact():
    name = input("Enter Name: ")
    for contact in contacts:
        if contact[0] == name:
            print("Contact with this name already exists!")
            return
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contacts.append((name, phone, email))
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("List of Contacts:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact[0]} - {contact[1]} - {contact[2]}")

def search_contact():
    name = input("Enter name to search: ")
    for contact in contacts:
        if contact[0] == name:
            print(f"Contact Found: {contact[0]} - {contact[1]} - {contact[2]}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            new_phone = input("Enter new phone number: ")
            contacts[i] = (contact[0], new_phone, contact[2])
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    for i, contact in enumerate(contacts):
        if contact[0] == name:
            contacts.pop(i)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nWelcome to Contact Manager Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

