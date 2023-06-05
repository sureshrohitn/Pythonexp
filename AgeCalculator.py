from datetime import datetime

def ageCalculator(years, months, days,year,month,date):
    import datetime
    today = datetime.date(years,months,days)
    dob = datetime.date(year, month, date)
    years= ((today-dob).total_seconds()/ (365.242*24*3600))
    yearsInt=int(years)
    months=(years-yearsInt)*12
    monthsInt=int(months)
    days=(months-monthsInt)*(365.242/12)
    daysInt=int(days)
    print('You are {0} years, {1} months, {2} days old.'.format(yearsInt,monthsInt,daysInt))

birthdate = input("Enter your birthdate :")
my_date = datetime.strptime(birthdate, "%Y-%m-%d")
b_year = my_date.year
b_month = my_date.month
b_date = my_date.day
# current date and time
now = datetime.now()

# get year from date
c_year = int(now.strftime("%Y"))

# get month from date
c_month = int(now.strftime("%m"))

# get day from date
c_date =int( now.strftime("%d"))

ageCalculator(c_year,c_month,c_date,b_year,b_month,b_date)