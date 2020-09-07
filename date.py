from datetime import datetime
from dateutil import relativedelta
#Code to convert difference between dates in terms of Years, Weeks and Days 


def dif_dates(day_commencement, month_commencement, year_commencement, day_expiration, month_expiration, year_expiration):
	date_0 = datetime(year_commencement, month_commencement, day_commencement)
	date_1 = datetime(year_expiration, month_expiration, day_expiration)

	diff = relativedelta.relativedelta(date_1, date_0)

	years = diff.years
	months = diff.months
	days = diff.days
	return '{} years {} months and {} days'.format(years, months, days)
