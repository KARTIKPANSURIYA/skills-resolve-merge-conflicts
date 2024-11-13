# Author: Kartik Pansuriya
# Date: November 10, 2024
# Description: This file describes  a base class Employee to store general employee information.

class Employee:
    def __init__(self, name: str, emp_id: int, pay_rate: float):
        """
        Initialize the  class Employee with a name, ID, and pay rate.
        :param name: Name of the employee
        :param emp_id: Employee ID number
        :param pay_rate: Hourly pay rate
        """
        self._name = name
        self._emp_id = emp_id
        self._pay_rate = pay_rate

    def calcPay(self, hours_worked: int) -> float:
        """
        Calculating pay based on hours worked.
        :param hours_worked: Number of hours worked
        :return: Total pay
        """
        return hours_worked * self._pay_rate

    def getName(self) -> str:
        return self._name

    def getID(self) -> int:
        return self._emp_id

    def getPayRate(self) -> float:
        return self._pay_rate

    def setName(self, name: str):
        self._name = name

    def setID(self, emp_id: int):
        self._emp_id = emp_id

    def setPayRate(self, pay_rate: float):
        self._pay_rate = pay_rate
