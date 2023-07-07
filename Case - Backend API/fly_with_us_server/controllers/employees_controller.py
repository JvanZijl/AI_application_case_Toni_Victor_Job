import connexion
import six
import json

from fly_with_us_server.models.employee import Employee  # noqa: E501
from fly_with_us_server import util


def employees_get():  # noqa: E501
    """Returns a list of employees with their details

    Provides list of all employees, containing their id, name, availability and average handling times. # noqa: E501


    :rtype: List[Employee]
    """
    with open('./fly_with_us_server/data/employees.json') as employees_json_file:
        employees = json.load(employees_json_file)
    return employees
