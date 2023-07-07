# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from fly_with_us_server.models.base_model_ import Model
from fly_with_us_server import util


class CallDemand(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, mon: List[int]=None, tue: List[int]=None, wed: List[int]=None, thu: List[int]=None, fri: List[int]=None, sat: List[int]=None, sun: List[int]=None):  # noqa: E501
        """CallDemand - a model defined in Swagger

        :param mon: The mon of this CallDemand.  # noqa: E501
        :type mon: List[int]
        :param tue: The tue of this CallDemand.  # noqa: E501
        :type tue: List[int]
        :param wed: The wed of this CallDemand.  # noqa: E501
        :type wed: List[int]
        :param thu: The thu of this CallDemand.  # noqa: E501
        :type thu: List[int]
        :param fri: The fri of this CallDemand.  # noqa: E501
        :type fri: List[int]
        :param sat: The sat of this CallDemand.  # noqa: E501
        :type sat: List[int]
        :param sun: The sun of this CallDemand.  # noqa: E501
        :type sun: List[int]
        """
        self.swagger_types = {
            'mon': List[int],
            'tue': List[int],
            'wed': List[int],
            'thu': List[int],
            'fri': List[int],
            'sat': List[int],
            'sun': List[int]
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
    def from_dict(cls, dikt) -> 'CallDemand':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CallDemand of this CallDemand.  # noqa: E501
        :rtype: CallDemand
        """
        return util.deserialize_model(dikt, cls)

    @property
    def mon(self) -> List[int]:
        """Gets the mon of this CallDemand.


        :return: The mon of this CallDemand.
        :rtype: List[int]
        """
        return self._mon

    @mon.setter
    def mon(self, mon: List[int]):
        """Sets the mon of this CallDemand.


        :param mon: The mon of this CallDemand.
        :type mon: List[int]
        """

        self._mon = mon

    @property
    def tue(self) -> List[int]:
        """Gets the tue of this CallDemand.


        :return: The tue of this CallDemand.
        :rtype: List[int]
        """
        return self._tue

    @tue.setter
    def tue(self, tue: List[int]):
        """Sets the tue of this CallDemand.


        :param tue: The tue of this CallDemand.
        :type tue: List[int]
        """

        self._tue = tue

    @property
    def wed(self) -> List[int]:
        """Gets the wed of this CallDemand.


        :return: The wed of this CallDemand.
        :rtype: List[int]
        """
        return self._wed

    @wed.setter
    def wed(self, wed: List[int]):
        """Sets the wed of this CallDemand.


        :param wed: The wed of this CallDemand.
        :type wed: List[int]
        """

        self._wed = wed

    @property
    def thu(self) -> List[int]:
        """Gets the thu of this CallDemand.


        :return: The thu of this CallDemand.
        :rtype: List[int]
        """
        return self._thu

    @thu.setter
    def thu(self, thu: List[int]):
        """Sets the thu of this CallDemand.


        :param thu: The thu of this CallDemand.
        :type thu: List[int]
        """

        self._thu = thu

    @property
    def fri(self) -> List[int]:
        """Gets the fri of this CallDemand.


        :return: The fri of this CallDemand.
        :rtype: List[int]
        """
        return self._fri

    @fri.setter
    def fri(self, fri: List[int]):
        """Sets the fri of this CallDemand.


        :param fri: The fri of this CallDemand.
        :type fri: List[int]
        """

        self._fri = fri

    @property
    def sat(self) -> List[int]:
        """Gets the sat of this CallDemand.


        :return: The sat of this CallDemand.
        :rtype: List[int]
        """
        return self._sat

    @sat.setter
    def sat(self, sat: List[int]):
        """Sets the sat of this CallDemand.


        :param sat: The sat of this CallDemand.
        :type sat: List[int]
        """

        self._sat = sat

    @property
    def sun(self) -> List[int]:
        """Gets the sun of this CallDemand.


        :return: The sun of this CallDemand.
        :rtype: List[int]
        """
        return self._sun

    @sun.setter
    def sun(self, sun: List[int]):
        """Sets the sun of this CallDemand.


        :param sun: The sun of this CallDemand.
        :type sun: List[int]
        """

        self._sun = sun
