# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fly_with_us_server.models.base_model_ import Model
from fly_with_us_server.models.employee_availability_mon import EmployeeAvailabilityMon  # noqa: F401,E501
from fly_with_us_server import util


class EmployeeAvailability(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, mon: EmployeeAvailabilityMon=None, tue: EmployeeAvailabilityMon=None, wed: EmployeeAvailabilityMon=None, thu: EmployeeAvailabilityMon=None, fri: EmployeeAvailabilityMon=None, sat: EmployeeAvailabilityMon=None, sun: EmployeeAvailabilityMon=None):  # noqa: E501
        """EmployeeAvailability - a model defined in Swagger

        :param mon: The mon of this EmployeeAvailability.  # noqa: E501
        :type mon: EmployeeAvailabilityMon
        :param tue: The tue of this EmployeeAvailability.  # noqa: E501
        :type tue: EmployeeAvailabilityMon
        :param wed: The wed of this EmployeeAvailability.  # noqa: E501
        :type wed: EmployeeAvailabilityMon
        :param thu: The thu of this EmployeeAvailability.  # noqa: E501
        :type thu: EmployeeAvailabilityMon
        :param fri: The fri of this EmployeeAvailability.  # noqa: E501
        :type fri: EmployeeAvailabilityMon
        :param sat: The sat of this EmployeeAvailability.  # noqa: E501
        :type sat: EmployeeAvailabilityMon
        :param sun: The sun of this EmployeeAvailability.  # noqa: E501
        :type sun: EmployeeAvailabilityMon
        """
        self.swagger_types = {
            'mon': EmployeeAvailabilityMon,
            'tue': EmployeeAvailabilityMon,
            'wed': EmployeeAvailabilityMon,
            'thu': EmployeeAvailabilityMon,
            'fri': EmployeeAvailabilityMon,
            'sat': EmployeeAvailabilityMon,
            'sun': EmployeeAvailabilityMon
        }

        self.attribute_map = {
            'mon': 'mon',
            'tue': 'tue',
            'wed': 'wed',
            'thu': 'thu',
            'fri': 'fri',
            'sat': 'sat',
            'sun': 'sun'
        }
        self._mon = mon
        self._tue = tue
        self._wed = wed
        self._thu = thu
        self._fri = fri
        self._sat = sat
        self._sun = sun

    @classmethod
    def from_dict(cls, dikt) -> 'EmployeeAvailability':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Employee_availability of this EmployeeAvailability.  # noqa: E501
        :rtype: EmployeeAvailability
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mon(self) -> EmployeeAvailabilityMon:
        """Gets the mon of this EmployeeAvailability.


        :return: The mon of this EmployeeAvailability.
        :rtype: EmployeeAvailabilityMon
        """
        return self._mon

    @mon.setter
    def mon(self, mon: EmployeeAvailabilityMon):
        """Sets the mon of this EmployeeAvailability.


        :param mon: The mon of this EmployeeAvailability.
        :type mon: EmployeeAvailabilityMon
        """

        self._mon = mon

    @property
    def tue(self) -> EmployeeAvailabilityMon:
        """Gets the tue of this EmployeeAvailability.


        :return: The tue of this EmployeeAvailability.
        :rtype: EmployeeAvailabilityMon
        """
        return self._tue

    @tue.setter
    def tue(self, tue: EmployeeAvailabilityMon):
        """Sets the tue of this EmployeeAvailability.


        :param tue: The tue of this EmployeeAvailability.
        :type tue: EmployeeAvailabilityMon
        """

        self._tue = tue

    @property
    def wed(self) -> EmployeeAvailabilityMon:
        """Gets the wed of this EmployeeAvailability.


        :return: The wed of this EmployeeAvailability.
        :rtype: EmployeeAvailabilityMon
        """
        return self._wed

    @wed.setter
    def wed(self, wed: EmployeeAvailabilityMon):
        """Sets the wed of this EmployeeAvailability.


        :param wed: The wed of this EmployeeAvailability.
        :type wed: EmployeeAvailabilityMon
        """

        self._wed = wed

    @property
    def thu(self) -> EmployeeAvailabilityMon:
        """Gets the thu of this EmployeeAvailability.


        :return: The thu of this EmployeeAvailability.
        :rtype: EmployeeAvailabilityMon
        """
        return self._thu

    @thu.setter
    def thu(self, thu: EmployeeAvailabilityMon):
        """Sets the thu of this EmployeeAvailability.


        :param thu: The thu of this EmployeeAvailability.
        :type thu: EmployeeAvailabilityMon
        """

        self._thu = thu

    @property
    def fri(self) -> EmployeeAvailabilityMon:
        """Gets the fri of this EmployeeAvailability.


        :return: The fri of this EmployeeAvailability.
        :rtype: EmployeeAvailabilityMon
        """
        return self._fri

    @fri.setter
    def fri(self, fri: EmployeeAvailabilityMon):
        """Sets the fri of this EmployeeAvailability.


        :param fri: The fri of this EmployeeAvailability.
        :type fri: EmployeeAvailabilityMon
        """

        self._fri = fri

    @property
    def sat(self) -> EmployeeAvailabilityMon:
        """Gets the sat of this EmployeeAvailability.


        :return: The sat of this EmployeeAvailability.
        :rtype: EmployeeAvailabilityMon
        """
        return self._sat

    @sat.setter
    def sat(self, sat: EmployeeAvailabilityMon):
        """Sets the sat of this EmployeeAvailability.


        :param sat: The sat of this EmployeeAvailability.
        :type sat: EmployeeAvailabilityMon
        """

        self._sat = sat

    @property
    def sun(self) -> EmployeeAvailabilityMon:
        """Gets the sun of this EmployeeAvailability.


        :return: The sun of this EmployeeAvailability.
        :rtype: EmployeeAvailabilityMon
        """
        return self._sun

    @sun.setter
    def sun(self, sun: EmployeeAvailabilityMon):
        """Sets the sun of this EmployeeAvailability.


        :param sun: The sun of this EmployeeAvailability.
        :type sun: EmployeeAvailabilityMon
        """

        self._sun = sun
