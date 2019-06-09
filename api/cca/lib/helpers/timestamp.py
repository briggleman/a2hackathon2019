from datetime import datetime


def isotimestamp():
    """
    Gets the current time and casts to iso format (ie, 2019-04-20T16:36:00+00:00)
    :return: str: current time formatted to an iso string
    """
    return datetime.isoformat(datetime.utcnow())
