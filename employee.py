class Employee:
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number

    def __str__(self):
        return "\nEmployee name: " + self.__employee_name + "\nEmployee number: " + self.__employee_number


class ProductionWorker(Employee):
    def __init__(self, employee_name, employee_number, shift, pay_rate):
        Employee.__init__(self, employee_name, employee_number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    def get_shift(self):
        return self.__shift

    def get_pay_rate(self):
        return self.__pay_rate

    def __str__(self):
        return "\nEmployee name: " + self.get_employee_name() + "\nEmployee number" + self.get_employee_number() + \
            "\nShift: " + self.__shift + "\nPay rate: " + self.__pay_rate
