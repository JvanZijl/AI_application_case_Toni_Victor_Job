# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fly_with_us_server.models.base_model_ import Model
from fly_with_us_server.models.employee_availability import EmployeeAvailability  # noqa: F401,E501
from fly_with_us_server import util


class Employee(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None, avg_handling_time: int=None, availability: EmployeeAvailability=None):  # noqa: E501
        """Employee - a model defined in Swagger

        :param id: The id of this Employee.  # noqa: E501
        :type id: int
        :param name: The name of this Employee.  # noqa: E501
        :type name: str
        :param avg_handling_time: The avg_handling_time of this Employee.  # noqa: E501
        :type avg_handling_time: int
        :param availability: The availability of this Employee.  # noqa: E501
        :type availability: EmployeeAvailability
        """
        self.swagger_types = {
            'id': int,
            'name': str,
            'avg_handling_time': int,
            'availability': EmployeeAvailability
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'avg_handling_time': 'avg_handling_time',
            'availability': 'availability'
        }
        self._id = id
        self._name = name
        self._avg_handling_time = avg_handling_time
        self._availability = availability

    @classmethod
    def from_dict(cls, dikt) -> 'Employee':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee of this Employee.  # noqa: E501
        :rtype: Employee
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Employee.


        :return: The id of this Employee.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Employee.


        :param id: The id of this Employee.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this Employee.


        :return: The name of this Employee.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Employee.


        :param name: The name of this Employee.
        :type name: str
        """

        self._name = name

    @property
    def avg_handling_time(self) -> int:
        """Gets the avg_handling_time of this Employee.


        :return: The avg_handling_time of this Employee.
        :rtype: int
        """
        return self._avg_handling_time

    @avg_handling_time.setter
    def avg_handling_time(self, avg_handling_time: int):
        """Sets the avg_handling_time of this Employee.


        :param avg_handling_time: The avg_handling_time of this Employee.
        :type avg_handling_time: int
        """

        self._avg_handling_time = avg_handling_time

    @property
    def availability(self) -> EmployeeAvailability:
        """Gets the availability of this Employee.


        :return: The availability of this Employee.
        :rtype: EmployeeAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability: EmployeeAvailability):
        """Sets the availability of this Employee.


        :param availability: The availability of this Employee.
        :type availability: EmployeeAvailability
        """

        self._availability = availability