# Question 3: Customer Management System
# Project Description: This project involves you creating a customer management system that you can use to manage your customers and perform basic transactions. This system will have basic functions such as storing customer information, adding new customers, updating customer information, deleting customers and viewing the customer list. Here are the basic steps of the project:

# 1-Use a dictionary structure to store customer information. Assign a unique customer identification (ID) for each customer and associate customer information with this ID. You can use a dictionary containing information such as name, surname, e-mail, phone number for each customer.

# 2-Provide a menu where the user can choose the following actions:

# Add new customers
# Updating customer information
# Delete customer
# List all customers
# Check out
# 3-Perform the relevant action according to the user's choice. For example, when adding a new customer, get the required information from the user and add a new customer to the dictionary.

# 4-When updating customer information, view the current information using the customer ID and save the updated information.

# 5-In the customer deletion process, get the customer ID from the user and delete this customer from the dictionary.

# 6-In the process of listing all customers, view the list of existing customers.

# 7-Repeat the process until the user logs out.
#1
from ast import main


customers={}
next_id=1
def add_customer():
{ global next_id
    name=input("enter name's customer")
    surname=input("enter surname's customer")
    email=input("enter email's customer")
    phone=input("enter phone's customer")
    customers(next_id)={
        "name":name,
        "surname":surname,
        "email":email,
        "phone":phone
    }
    print("f customer was added{next_id}")
    next_id+=1
}
def update_customer():
    {
        
        customer_id=int(input("enter id's customer"))
    if customer_id in customers:
          print("enter your updates")
          customers[customer_id]['name']
          customers[customer_id]['surname']
          customers[customer_id]['email']
          customers[customer_id]['phone']
          customers[customer_id]={
              "name"=name,
              "surname"=surname,
              "email"=email,
              "phone"=phone
          }
          print("data's customer updated")
    else:
          print("there isn't customer for this id" )
    }
    def delete_customer():
    {
            
           customer_id =int(input("enter your id that you want to delete"))
            if customer_id in customers :   
                 del customers[customer_id]
            print("customer deleted")
            else:  
                print("customer not found")
    }
def list_customers():
    if not customers:
        print("there are no customer")
        return
    print("customer list")
for cid,info in customers.items():
    print(f"id:{cid}|{info['name']}|{info['surname']}|{info['email']}|{info['phone']}")
#main list
def main:
while True:
    print("customer management system")
    print("1. add new customer")
    print("2.update data's customer")
    print("3.delete customer")
    print("4.view customer list")
    print("5.existing")
    choice=input("select process")
    if choice == "1":
            add_customer()
    elif choice == "2":
            update_customer()
    elif choice == "3":
            delete_customer()
    elif choice == "4":
            list_customers()
    elif choice == "5":
            print("program end")
            break
    else:
            print("choice not correct try again")
main()
