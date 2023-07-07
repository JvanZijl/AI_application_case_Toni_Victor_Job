import connexion
import six
import json

from fly_with_us_server.models.call_demand import CallDemand  # noqa: E501
from fly_with_us_server.models.call_demand_overwrite import CallDemandOverwrite  # noqa: E501
from fly_with_us_server import util


def call_demand_week_number_day_hour_post(body, week_number, day, hour):  # noqa: E501
    """Overwrite the model predicted call demand.

    Manually change the predicted call-demand for a specific hour. # noqa: E501

    :param body: Overwrite call demand value &amp; reason.
    :type body: dict | bytes
    :param week_number: The week number for which the call demand prediction should be overwritten.
    :type week_number: int
    :param day: The day of the week for which the call demand predicition should be overwritten.
    :type day: str
    :param hour: The hour of the day for which the call demand prediction should be overwritten.
    :type hour: int

    :rtype: None
    """
    if connexion.request.is_json:
        body = CallDemandOverwrite.from_dict(connexion.request.get_json())  # noqa: E501

    week_index = week_number - 1

    with open('./fly_with_us_server/data/call-demand.json', 'r') as call_demand_json_file:
        call_demand = json.load(call_demand_json_file)

    call_demand[week_index][day][hour] = body.value

    with open('./fly_with_us_server/data/call-demand.json', 'w') as call_demand_outfile:
        json.dump(call_demand, call_demand_outfile)

    return "OK"


def call_demand_week_number_get(week_number):  # noqa: E501
    """Returns the predicted number of calls for the provided weeknumber

    Provides an object with as items the days of the week, and as their value an array of predicted call demand per hour. # noqa: E501

    :param week_number: The week number for which the call demand prediction should be returned
    :type week_number: int

    :rtype: CallDemand
    """
    week_index = week_number - 1

    with open('./fly_with_us_server/data/call-demand.json', 'r') as call_demand_json_file:
        call_demand = json.load(call_demand_json_file)

    return call_demand[week_index]
