class Employee:
    def __init__(self, name, number):
        self.set_Name(name)
        self.set_Number(number)

    def set_Name(self, name):
        self.name = name

    def set_Number(self, number):
        self.number = number

    def get_Name(self):
        return self.name

    def get_Number(self):
        return self.number

    class ProductionWorker():
        def __init__(self, name, number, shift, hourlyPayRate):
            super().__init__(name, number)
            self.set_Shift(shift)
            self.set_Hourly_Pay_Rate(hourlyPayRate)

        def set_Shift(self, shift):
            self.shift=shift

        def set_Hourly_Pay_Rate(self, hourly_Pay_Rate):
            self.hourly_Pay_Rate = hourly_Pay_Rate

        def get_Shift(self):
            return self.shift

        def get_Hourly_Pay_Rate(self):
            return self.hourly_Pay_Rate

    pe = ProductionWorker('', 0, 0, 0.0)

    print('Enter details of Production Worker:')
    name = input('Name: ')
    number = int(input('Employee Number: '))
    shift = int(input('Shift: '))
    hourlyPayRate = float(input('Hourly Pay Rate: '))
   
    print('\nDetails of Production Worker:')
    print('Employee Name:', pe.getName())
    print('Employee Number:', pe.getNumber())
    print('Shift:', pe.getShift())
    print('Hourly Pay Rate:', pe.getHourlyPayRate())
