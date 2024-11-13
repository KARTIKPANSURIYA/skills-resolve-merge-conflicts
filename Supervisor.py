# Author: Kartik Pansuriya
# Date: November 10, 2024
# Description: This file describes a supervisor class in which it inherits from employee and stores level information.

from Employee import Employee

class Supervisor(Employee):
    def __init__(self, name: str, emp_id: int, pay_rate: float, level: int):
        """
        Initializing a Supervisor with a name, ID, pay rate, and level.
        """
        super().__init__(name, emp_id, pay_rate)
        self.__level = level

    def calcPay(self, hours_worked: int) -> float:
        """
        Calculating pay with an additional bonus based on supervisor level.
        :return: Total pay + bonus
        """
        return super().calcPay(hours_worked) + (1000.0 * self.__level)

    def getLevel(self) -> int:
        return self.__level

    def setLevel(self, level: int):
        self.__level = level
