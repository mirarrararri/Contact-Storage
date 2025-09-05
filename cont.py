#Global list to store contacts
contact_storage = []

#Function to display menu
def display_menu():
    print("===== CONTACT STORAGE =====")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("=" * 25)
#Function to add contact
def add_contact():
    name = input("Enter name: ").strip()
    phone_num = input("Enter phone number: ").strip()
    email = input("Enter e-mail: ").strip()

    contact = {"name": name, "phone_num": phone_num, "email": email}
    contact_storage.append(contact)
    print(f"Contact '{name}' ADDED SUCCESSFULLY!")
#Function to view contact
def view_contact():
    if not contact_storage:
        print("No contact available!")
        return

    print("\n===== CONTACT LIST =====")
    for a, contact in enumerate(contact_storage, start=1):
        print(f"[{a}] {contact['name']} | {contact['phone_num']} | {contact['email']}")
    print("=" * 25)
#Function to search contact
def search_contact():
    name = input("Input name to search: ").strip().lower()
    found = False

    for contact in contact_storage:
        if contact["name"].lower() == name:
            print(f"Contact Found: {contact['name']} | {contact['phone_num']} | {contact['email']}")
            found = True
            break

    if not found:
        print("Contact not found.")
#Function to delete contact
def delete_contact():
    delete_name = input("Enter name to delete: ").strip().lower()
    global contact_storage
    new_contacts = [c for c in contact_storage if c["name"].lower() != delete_name]

    if len(new_contacts) < len(contact_storage):
        contact_storage = new_contacts
        print(f"Contact '{delete_name}' DELETED SUCCESSFULLY.")
    else:
        print("Contact not found.")
#Main function to start the program
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice: Please enter number 1 to 5 only.")

if __name__ == "__main__":
    main()


