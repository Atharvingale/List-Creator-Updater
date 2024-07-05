from tabulate import tabulate
import os
command = "cls" if os.name == "nt" else "clear"
os.system(command)

def make_list():
    data = []
    headers = input("Enter the headers (comma-separated): ").split(",")
    data.append(headers)
    while True:
        row = input("Enter a row of data (comma-separated) or 'done' to finish: ")
        if row.lower() == "done":
            break
        data.append(row.split(",")) 
    
    with open(filename, 'a') as file:
        for row in data:
            file.write(','.join(row) + '\n')   
    return data

def view_data():
    try:
        with open(filename, 'r') as file:
            lines= file.readlines()
            data = [line.strip().split(",")for line in lines]
            return data
    except FileNotFoundError:
        print("The file does not exists !!")
        return []
def add_data():
    data = []
    while True:
       row = input("Enter a row of data (comma-separated) or 'done' to finish: ")
       if row.lower() == "done":
           break
       data.append(row.split(",")) 
   
    with open(filename, 'a') as file:
        for row in data:
            file.write(','.join(row) + '\n')   
    return data

while True:
    print("||| WELCOME TO LIST CREATOR / List Updater |||\n")    
    print("1. New List")
    print("2. Add data to the list")
    print("3. View the list")
    print("4. Exit")
    a = input("Enter the operation number to perform:-")
    if(a=="1"):
        filename = input("Enter the file name: ")
        data = make_list()
        print(tabulate(data, headers="firstrow", tablefmt="grid"))

    elif(a=="2"):
        filename = input("Enter the file name: ")
        data = add_data()
        print(tabulate(data, headers="firstrow", tablefmt="grid"))

    elif(a=="3"):
        filename = input("Enter the file name: ")
        data = view_data()
        print(tabulate(data, headers="firstrow", tablefmt="grid"))
    elif(a=="4"):
        command = "cls" if os.name == "nt" else "clear"
        os.system(command)
        break
    else:
        command = "cls" if os.name == "nt" else "clear"
        os.system(command)
        print("                           !!! ERROR INVALID OPTION TRY AGAIN !!!\n\n")

