leap_year=True
not_leap=False
def is_leap_year(year):
	if year%4==0:
		if year%100==0:
			if year%400==0:
				return(leap_year)
			else:
				return(not_leap)
		else:
			return(leap_year)
	else:
		return(not_leap)
	
def days_in_month(month,year):
	month_days=[31,28,31,30,31,30,31,31,30,31,30,31]
	for days in month_days:
		if is_leap_year(year) :
			month_days[1]=29
		days=month_days[month-1]
		return days
	
year=int(input("Enter the year: "))
month=int(input("Enter the month: "))
days=days_in_month(month,year)
print(days)