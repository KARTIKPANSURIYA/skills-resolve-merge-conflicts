# Author: Kartik Pansuriya
# Date: November 10, 2024
# Description: This is main file it manages employees, calculates total payroll, and displays employee information.

from Worker import Worker
from Supervisor import Supervisor


def calc(employee_list):
    """
    Calculating the total pay for all employees.
    :param employee_list: List of Worker and Supervisor objects
    :return: Total payroll cost
    """
    total_pay = 0
    for employee in employee_list:
        total_pay += employee.calcPay(40)
    return total_pay


def listEmployees(employee_list):
    """
    Lists all employees with their details.
    :param employee_list: List of Worker and Supervisor objects
    """
    for employee in employee_list:
        print(f"Name: {employee.getName()}")
        print(f"ID: {employee.getID()}")
        print(f"Pay Rate: ${employee.getPayRate():.2f}")

        if isinstance(employee, Worker):
            print(f"Shift: {employee.shiftType()}")
        elif isinstance(employee, Supervisor):
            print(f"Level: {employee.getLevel()}")
        print("-" * 30)


def main():
    employee_list = []
    num_employees = int(input("How many employees would you like to add: "))

    i = 0  # Start as an 0 for the number of successfully added employees
    while i < num_employees:
        emp_type = input("\nWould you like to add a worker or a supervisor: ").strip().lower()

        if emp_type == "worker":
            name = input("Please enter the name of the worker: ")
            emp_id = int(input("Please enter the id of the worker: "))
            pay_rate = float(input("Please enter the pay rate of the worker: "))
            shift = int(input("Please enter the shift of the worker (1 for day, 2 for night): "))
            employee = Worker(name, emp_id, pay_rate, shift)
            employee_list.append(employee)
            i += 1  # Incrementing  after a successful entry

        elif emp_type == "supervisor":
            name = input("Please enter the name of the supervisor: ")
            emp_id = int(input("Please enter the id of the supervisor: "))
            pay_rate = float(input("Please enter the pay rate of the supervisor: "))
            level = int(input("Please enter the level of the supervisor: "))
            employee = Supervisor(name, emp_id, pay_rate, level)
            employee_list.append(employee)
            i += 1  # Incrementing after a successful entry

        else:
            print(f"{emp_type} is not a valid option. Try again!")

    print("\nEmployee List:")
    listEmployees(employee_list)

    total_pay = calc(employee_list)
    print(f"\nThe total cost of all of the workers' pay is ${total_pay:.2f}")


if __name__ == "__main__":
    main()
