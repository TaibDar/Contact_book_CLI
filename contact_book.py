"""
contact_book.py
---------------
A simple command-line Contact Book project in Python.

Features:
- Add, view, search, update, and delete contacts.
- Stores all contacts in a text file (`contacts.txt`).
- Handles missing files and invalid entries gracefully.
- Supports multiple matches when updating or deleting contacts.
"""

def add_contact():
    """
    Add a new contact to the contact book.
    Prompts the user for name, phone number, and email.
    Saves the details into `contacts.txt`.
    """
    with open("contacts.txt", "a+") as file:
        print("\n--- Add New Contact ---")
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        file.write(f"{name},{phone},{email}\n")
    print(" Contact added successfully!\n")


def view_contacts():
    """
    View all saved contacts from `contacts.txt`.
    Displays each contact with an index number.
    If the file doesn't exist or is empty, shows a friendly message.
    """
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        if not contacts:
            print("\n No contacts found.\n")
        else:
            print("\n--- Contacts List ---")
            for idx, contact in enumerate(contacts, start=1):
                try:
                    name, phone, email = contact.strip().split(",")
                    print(f"{idx}. Name: {name}\n   Phone: {phone}\n   Email: {email}\n")
                except ValueError:
                    print(f"Invalid contact entry: {contact.strip()}")
            print("----------------------\n")
    except FileNotFoundError:
        print("\n No contacts file found.\n")


def search_contact():
    """
    Search for a contact by name.
    Prompts the user for the name and checks each contact in `contacts.txt`.
    Case-insensitive comparison is used.
    """
    print("\n--- Search Contact ---")
    search_name = input("Enter name to search: ")
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()
        found = False
        for contact in contacts:
            try:
                name, phone, email = contact.strip().split(",")
                if name.lower() == search_name.lower():
                    print(f"\n Contact Found:\n   Name: {name}\n   Phone: {phone}\n   Email: {email}\n")
                    found = True
            except ValueError:
                continue
        if not found:
            print("\n Contact not found.\n")
    except FileNotFoundError:
        print("\n No contacts file found.\n")


def update_contact():
    """
    Update an existing contact by name.
    - If multiple contacts match, the user can select which one to update.
    - Prompts for new name, phone, and email.
    - Saves updated contact back into `contacts.txt`.
    """
    print("\n--- Update Contact ---")
    update_name = input("Enter name to update: ")
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        matches = []
        for idx, contact in enumerate(contacts):
            try:
                name, phone, email = contact.strip().split(",")
                if name.lower() == update_name.lower():
                    matches.append((idx, name, phone, email))
            except ValueError:
                continue

        if not matches:
            print("\n Contact not found.\n")
            return

        # If multiple matches found
        if len(matches) > 1:
            print("\nMultiple contacts found:")
            for i, (_, name, phone, email) in enumerate(matches, start=1):
                print(f"{i}. {name}, {phone}, {email}")
            try:
                choice = int(input("\nSelect contact number to update: "))
                if choice < 1 or choice > len(matches):
                    print("\n Invalid choice.\n")
                    return
                match_idx = matches[choice - 1][0]
            except ValueError:
                print("\n Invalid input.\n")
                return
        else:
            match_idx = matches[0][0]

        # Get new values
        print("\nEnter new details:")
        new_name = input("New name: ")
        new_phone = input("New phone number: ")
        new_email = input("New email: ")

        contacts[match_idx] = f"{new_name},{new_phone},{new_email}\n"

        with open("contacts.txt", "w") as file:
            file.writelines(contacts)

        print("\n Contact updated successfully!\n")
    except FileNotFoundError:
        print("\n No contacts file found.\n")


def delete_contact():
    """
    Delete a contact by name.
    - If multiple contacts match, the user can select which one to delete.
    - Removes the chosen entry from `contacts.txt`.
    """
    print("\n--- Delete Contact ---")
    delete_name = input("Enter name to delete: ")
    try:
        with open("contacts.txt", "r") as file:
            contacts = file.readlines()

        matches = []
        for idx, contact in enumerate(contacts):
            try:
                name, phone, email = contact.strip().split(",")
                if name.lower() == delete_name.lower():
                    matches.append((idx, name, phone, email))
            except ValueError:
                continue

        if not matches:
            print("\n Contact not found.\n")
            return

        # If multiple matches found
        if len(matches) > 1:
            print("\nMultiple contacts found:")
            for i, (_, name, phone, email) in enumerate(matches, start=1):
                print(f"{i}. {name}, {phone}, {email}")
            try:
                choice = int(input("\nSelect contact number to delete: "))
                if choice < 1 or choice > len(matches):
                    print("\n Invalid choice.\n")
                    return
                match_idx = matches[choice - 1][0]
            except ValueError:
                print("\n Invalid input.\n")
                return
        else:
            match_idx = matches[0][0]

        # Delete contact
        del contacts[match_idx]
        with open("contacts.txt", "w") as file:
            file.writelines(contacts)

        print("\n Contact deleted successfully!\n")
    except FileNotFoundError:
        print("\n No contacts file found.\n")


# ------------------- MAIN MENU -------------------
if __name__ == "__main__":
    """
    Main menu loop for the Contact Book.
    Continuously displays options until the user chooses to exit.
    """
    while True:
        print("\n========== Contact Book ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("==================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\n Exiting program... Goodbye!\n")
            break
        else:
            print("\n Invalid choice. Please try again.\n")

