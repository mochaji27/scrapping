from datetime import datetime


def get_datetime(date_format):

    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime(date_format)
    return dt_string