import csv
import os
from os import read

def clear():
    _ = os.system('cls')
header_file = ['Name','Phone Number','E-Mail','Address']
if not os.path.exists("sample.csv"):
    with open('sample.csv', 'w') as file:
        make_file = csv.DictWriter(file, fieldnames= header_file)
        make_file.writeheader()
print("\n>>>PYTHON PHONE DIRECTORY<<<")
def welcome():
    while True:
        entry = input("\nPlease select your desired entry:\n1. Creat New Contact\n2. Remove Records\n3. Display Records\n4. Close\n")
        if entry == '1':
            phonebook()

        elif entry == '2':
            clear()
            _ = os.remove("sample.csv")
            with open('sample.csv', 'w') as file:
                make_file = csv.DictWriter(file, fieldnames= header_file)
                make_file.writeheader()

        elif entry == '3':
            display()
            

        elif entry == '4':
            clear()
            break        
def phonebook():
    clear()
    print("Creating New contact record")
    with open("sample.csv", "a") as adding_data:
        add_file = csv.DictWriter(adding_data, fieldnames= header_file)
        name = input("Name: ")
        phone_number = input("Phone #: ")
        email = input("E-Mail: ")
        address = input("Address: ")

        info = {
            'Name':name.title(),
            'Phone Number':phone_number,
            'E-Mail':email,
            'Address':address
        }
        add_file.writerow(info)       
def display():
    clear()
    with open("sample.csv", "r") as read_file:
        read = read_file.read()
        print(read)
if __name__=='__main__':
    welcome()
