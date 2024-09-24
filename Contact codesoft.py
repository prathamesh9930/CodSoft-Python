contacts = {}

while True:
    print('\nContacts Book App')
    print('1. Create Contact')
    print('2. View Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Search Contacts')
    print('6. Count Contacts')
    print('7. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input('Enter the person name: ')
        if name in contacts:
            print(f'Contact name {name} already exists.')
        else:
            # Validate age
            while True:
                age = input('Enter the person age: ')
                if age.isdigit() and 1 <= int(age) <= 150:
                    break
                else:
                    print('Invalid age. Please enter a valid age between 1 and 150.')

            # Validate phone number
            while True:
                phone = input('Enter the person phone no. (10 digits): ')
                if phone.isdigit() and len(phone) == 10:
                    break
                else:
                    print('Invalid phone number. Please enter a 10-digit phone number.')

            # Validate email
            while True:
                email = input('Enter the person email: ')
                if '@' in email and '.' in email:
                    break
                else:
                    print('Invalid email. Please enter a valid email address.')

            # Add the contact
            contacts[name] = {'age': age, 'phone no.': phone, 'email': email}
            print(f'Contact name {name} created successfully.')

    elif choice == '2':
        name = input('Enter the person name to view: ')
        if name in contacts:
            print(f"Name: {name}, Age: {contacts[name]['age']}, Phone: {contacts[name]['phone no.']}, Email: {contacts[name]['email']}")
        else:
            print(f'Contact name {name} does not exist.')

    elif choice == '3':
        name = input('Enter the person name to update: ')
        if name in contacts:
            # Validate new age
            age = input('Update the person age: ')
            while not age.isdigit() or not (1 <= int(age) <= 150):
                age = input('Invalid age. Please enter a valid age: ')

            # Validate new phone number
            phone = input('Update the person phone no.: ')
            while not (phone.isdigit() and len(phone) == 10):
                phone = input('Invalid phone number. Please enter a 10-digit phone number: ')

            # Validate new email
            email = input('Update the person email: ')
            while '@' not in email or '.' not in email:
                email = input('Invalid email. Please enter a valid email address: ')

            # Update the contact
            contacts[name] = {'phone no.': phone, 'email': email, 'age': age}
            print(f'Contact {name} updated successfully.')
        else:
            print('Contact not found.')

    elif choice == '4':
        name = input('Enter the person name to delete: ')
        if name in contacts:
            del contacts[name]
            print(f'Contact name {name} deleted successfully.')
        else:
            print(f'Contact name {name} does not exist.')

    elif choice == '5':
        search = input('Enter the person name to search: ')
        if search in contacts:
            print(f"Name: {search}, Age: {contacts[search]['age']}, Phone: {contacts[search]['phone no.']}, Email: {contacts[search]['email']}")
        else:
            print(f'Contact name {search} does not exist.')

    elif choice == '6':
        print(f'Total contacts in Contact Book: {len(contacts)}')

    elif choice == '7':
        print('Exiting the Contacts Book App')
        break

    else:
        print('Invalid choice. Please enter a valid choice.')