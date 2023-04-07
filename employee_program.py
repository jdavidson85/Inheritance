

def main():
    name = input("Employees name: ")
    number = input("Employees number: ")
    shift = input("Employees shift: ")
    pay = input("Employees pay rate: ")

    new_employee = Employee.ProductionWorker(name, number, shift, pay)
    print("\nEmployee name: " + new_employee.get_employee_name() + "\nEmployee number: " +
          new_employee.get_employee_number() + "\nEmployee shift: " + new_employee.get_shift,
          "\nEmployee pay rate", + new_employee.get_employee_pay_rate)


main()