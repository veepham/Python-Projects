
# Parent Class
class User:
    name = "Jane"
    email = "jane@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry.name))
        else:
            print("The password or email is incorrect.")

# Child clases 
class Employee(User):
    base_pay = 11.00
    department = 'General'
    pin_number = "3980"

    # Saame method as parent but will use entry_pin instead of password
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_pin = input("Enter your PIN: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print("Welcome back, {}!".format(entry.name))
        else:
            print("The PIN or email is incorrect.")

# Invoke the methods inside each cass for User and Employee

customer = User()
customer.getLoginInfo()

manager = Employee()
manager.getLoginInfo()
    
