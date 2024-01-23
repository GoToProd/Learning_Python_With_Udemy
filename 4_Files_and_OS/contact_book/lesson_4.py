import pickle
import os


class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    def __str__(self):
        return "Name: {0}, \nEmail: {1}, \nPhone: {2}".format(self.name, self.email, self.phone)
    
    def change_name(self, name):
        self.name = name
        
    def change_email(self, email):
        self.email = email
        
    def change_phone(self, phone):
        self.phone = phone

def create_address_book():
    os.chdir('./contact_book')
    file = os.path.isfile('address.txt') == 1
    if file == 0:
        text_file = open("address.txt", "w")
        text_file.write("")
        text_file.close()
    else:
        print('Address book founded. \n')

    

def add_contact():
    address_book_file = open('address.txt', 'rb')
    is_file_empty = os.path.getsize('address.txt') == 0
    if not is_file_empty:
        list_contact = pickle.load('address.txt')
    else:
        list_contact = []
    try:
        contact = get_contact_info_from_user()
        address_book_file=open('address.txt', 'wb')
        list_contact.append(contact)
        pickle.dump(list_contact, address_book_file)
        print('Contact added to address book')
    except KeyboardInterrupt:
        print('Contact not added')
    except EOFError:
        print('Contact not added, problem with file')
    finally:
        address_book_file.close()


def get_contact_info_from_user():
    try:
        contact_name = input('Enter contact name: \n')
        contact_email = input('Enter contact email: \n')
        contact_phone = input('Enter contact phone: \n')
        contact = Contact(contact_name, contact_email, contact_phone)
        return contact
    except EOFError as e:
        raise e 
    except KeyboardInterrupt as e:
        raise e


def display_contact():
    address_book_file = open('address.txt', 'rb')
    is_file_empty = os.path.getsize('address.txt') == 0
    if not is_file_empty:
        list_contact = pickle.load(address_book_file)
        for each_contact in list_contact:
            print(each_contact)
    else:
        print('No contact in address book.')
        return 
    address_book_file.close()


def search_contact():
    address_book_file = open('address.txt', 'rb')
    is_file_empty = os.path.getsize('address.txt') == 0
    if not is_file_empty:
        search_name = input('Enter name: \n')
        is_contact_found = False
        list_contact = pickle.load(address_book_file)
        for each_contact in list_contact:
            contact_name = each_contact.name
            search_name = search_name.lower()
            contact_name = contact_name.lower()
            if (search_name == contact_name):
                print(each_contact)
                is_contact_found = True
                break
        if not is_contact_found:
            print('No contact name {search_name} with the provided search name.')
        else:
            print('Address book is empty. No contact to search.')
        address_book_file.close()


def delete_contact():
    address_book_file = open('address.txt', 'rb')
    is_file_empty = os.path.getsize('address.txt') == 0
    if not is_file_empty:
        name = input('Enter the contact name you want to delete: \n')
        list_contact = pickle.load(address_book_file)
        is_contact_deleted = False
        for i in range(0,len(list_contact)):
            each_contact = list_contact[i]
            if each_contact.name == name:
                del list_contact[i]
                is_contact_deleted = True
                print('Contact deleted')
                address_book_file=open('address.txt', 'wb')
                if (len(list_contact)) == 0:
                    address_book_file.write(b'')
                else:
                    pickle.dump(list_contact, address_book_file)
                    break
        if not is_contact_deleted:
            print('No contact with this name.')
    else:
        print('Address book is empty. No contact delete.')
    address_book_file.close()


def modify_contact():
    address_book_file = open('address.txt', 'rb')
    is_file_empty = os.path.getsize('address.txt') == 0
    if not is_file_empty:
        name = input('Enter the contact name you want to modify: \n')
        list_contact = pickle.load(address_book_file)
        is_contact_modified = False
        for each_contact in list_contact:
            if each_contact.name == name:
                do_modification(each_contact)
                address_book_file = open('address.txt', 'wb')
                pickle.dump(list_contact, address_book_file)
                is_contact_modified = True
                print('Contact been modified.')
                break
        if not is_contact_modified:
            print('No contact with this name.')
    else:
        print('Address book empty. No contact to modify.')


def do_modification(contact):
    try:
        while True:
            print('Enter 1 to modify email \n 2 to modify address \n 3 to modify name \n 4 to quit')
            choise = input()
            if(choise == '1'):
                new_email = input('Please enter a new email: \n')
                contact.change_email(new_email)
                break
            elif(choise == '2'):
                new_address = input('Please enter a new address: \n')
                contact.change_address(new_address)
                break
            elif(choise == '3'):
                new_name = input('Please enter a new name: \n')
                contact.change_name(new_name)
                break
            elif(choise == '4'):
                print('Modify benn cancelled. \n')
                break
            else:
                print('Incorrect choise')
    except EOFError:
        print('Error by EOFError')
    except KeyboardInterrupt:
        print('KeyboardInterrupt error')


create_address_book()

print("Enter 'a' to add a contact \n Enter 'b' to browse through contacts \n Enter 'd' to delete contact \n Enter 'm' to modify contact \n Enter 's' to search contact \n Enter 'q' to quit \n")
while True:
    choise = input('Enter your choise: \n')
    if (choise.lower() == 'q'):
        print('Thanks for using our application.')
        break
    elif(choise.lower() == 'b'):
        display_contact()
    elif(choise.lower() == 'd'):
        delete_contact()
    elif(choise.lower() == 'm'):
        modify_contact()
    elif(choise.lower() == 's'):
        search_contact()
    elif(choise.lower() == 'a'):
        add_contact()
    else:
        print('Incorrect choise, need to enter choise again.')