class Employee:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        return self.base_pay


class SalesEmployee(Employee):
    def __init__(self, name, base_pay, sales_incentive):
        super().__init__(name, base_pay)
        self.sales_incentive = sales_incentive

    def get_pay(self):
        return self.base_pay + self.sales_incentive
employee1 = Employee("John Doe", 5000)
print(f"Employee 1 Pay: Rs. {employee1.get_pay()}")

sales_employee = SalesEmployee("Jane Smith", 4000, 1000)
print(f"Sales Employee Pay: Rs. {sales_employee.get_pay()}")
