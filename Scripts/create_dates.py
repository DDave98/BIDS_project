import pandas as pd
from datetime import datetime, timedelta

def generate_date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)

def create_dataframe(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    data = []
    for date in generate_date_range(start_date, end_date):
        date_info = {
            'Date': date.strftime('%Y-%m-%d'),
            'Year': date.year,
            'Month': date.month,
            'Day': date.day
        }
        data.append(date_info)

    df = pd.DataFrame(data)
    return df