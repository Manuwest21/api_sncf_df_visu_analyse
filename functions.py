from datetime import datetime, timedelta



def list_dates(start_date, end_date):
    start = datetime.strptime(start_date, '%d%m%Y')
    end = datetime.strptime(end_date, '%d%m%Y')
    delta = timedelta(days=1)
    result = []
    while start <= end:
        result.append(start.strftime('%d%m%Y'))
        start += delta
    return result