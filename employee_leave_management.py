
class Employee:

    def __init__(self, employee_id, employee_name, department, leave_balance):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.leave_balance = leave_balance

   
    def apply_leave(self, days):

        if days <= 0:
            print("Invalid Leave Request")

        elif days <= self.leave_balance:
            self.leave_balance -= days
            print("Leave Approved")

        else:
            print("Insufficient Leave Balance")

    
    def cancel_leave(self, days):

        if days > 0:
            self.leave_balance += days
        else:
            print("Invalid Cancellation")

   
    def check_balance(self):
        print(f"Leave Balance: {self.leave_balance}")

   
    def display_employee(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Employee Name: {self.employee_name}")
        print(f"Department: {self.department}")
        print(f"Leave Balance: {self.leave_balance}")
    


employee_id = input("Employee Id: ")
employee_name=input("Name : ") 
department = input("Department : ")
leave_balance = int(input("Leave balance : "))
n = int(input("Enter number of operations: "))
print()
print("="*30)
emp = Employee(employee_id, employee_name, department, leave_balance)

print("Operations ")
print()
print("Apply\nBalance\nCancel\nDisplay\n")
for i in range(n):

    operation = input("Enter operation: ").lower()

    if operation == "apply":
        days = int(input("Enter days: "))
        emp.apply_leave(days)
        print("-"*20)
    elif operation == "cancel":
        days = int(input("Enter days: "))
        emp.cancel_leave(days)
        print("-"*20)
    elif operation == "balance":
        emp.check_balance()
        print("-"*20)
    elif operation == "display":
        emp.display_employee()
        print("-"*20)

