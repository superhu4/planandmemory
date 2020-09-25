import pandas as pd
import datetime


def create_dates(start_date, readings):
    all_dates = []
    current_date = datetime.datetime.strptime(start_date, '%m/%d/%Y')
    for reading in readings:
        while current_date.weekday() > 4:  # while we have a weekend date
            # increment current date
            current_date += datetime.timedelta(days=1)
        all_dates.append(current_date.strftime(
            '%m/%d/%Y'))  # append the weekday
        current_date += datetime.timedelta(days=1)  # increment current date
    return all_dates


def create_dates_with_blanks(start_date, readings):
    updated_readings, all_dates = [], []
    current_date = datetime.datetime.strptime(start_date, '%m/%d/%Y')
    for reading in readings:
        while current_date.weekday() > 4:  # if we have a weekend date, then
            updated_readings.append("")  # insert blank value into our readings
            # also insert current date into our dates
            all_dates.append(current_date.strftime('%m/%d/%Y'))
            # increment date by one day
            current_date += datetime.timedelta(days=1)
        updated_readings.append(reading)
        all_dates.append(current_date.strftime(
            '%m/%d/%Y'))  # append the weekday
        current_date += datetime.timedelta(days=1)  # increment current date
    return updated_readings, all_dates


in_file = input('Name of input CSV file?\n')
out_file = input('Name of output CSV file?\n')
start_date = input('When would you like to start? Format is MM/DD/YYYY.\n')
blanks = input('Do you want blanks? (Y/N)\n')
data = pd.read_csv(in_file)


if blanks.lower() == 'y':
    updated_readings, all_dates = create_dates_with_blanks(
        start_date, data['Subject'].tolist())
    data2 = pd.DataFrame(list(zip(all_dates, updated_readings)),
                         columns=['Start Date', 'Subject'])
    data2.to_csv(out_file)
else:
    all_dates = create_dates(start_date, data['Subject'].tolist())
    data['Start Date'] = all_dates
    data.to_csv(out_file)
