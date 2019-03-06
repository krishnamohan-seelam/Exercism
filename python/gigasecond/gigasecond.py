from datetime import datetime, timedelta


def add_gigasecond(moment):
    if not isinstance(moment, datetime):
        raise ValueError(f'{moment} is not datetime object')
    return moment + timedelta(seconds=10 ** 9)
