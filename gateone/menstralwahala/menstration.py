from datetime import datetime, timedelta


start_day = input("Enter the starting date of your menstral period (DD/MM/YYYY): ")
period_of_flow = int(input("Enter the days it takes for your period "))
menstral_cycle_days = input("Enter your menstral cycle days number ")
menstral_cycle_days = int(menstral_cycle_days)
user_date = datetime.strptime(start_day, "%d/%m/%Y")
days = timedelta(days=period_of_flow - 1)
days_of_flow = user_date + days
day = days_of_flow.day
month = days_of_flow.month
year = days_of_flow.year
OVULATION_CONST = 14
ovulation_calc = int(menstral_cycle_days) - OVULATION_CONST
ovulation_calc = int(ovulation_calc)
ovulation_day = user_date + timedelta(days= ovulation_calc -1)
ovu_day = ovulation_day.day
ovu_month = ovulation_day.month
ovu_year = ovulation_day.year
last_day_of_unsafe_period = ovulation_calc + 2
first_day_of_unsafe_period = ovulation_calc- 6
last_unsafe = user_date + timedelta(days= last_day_of_unsafe_period -1)
first_unsafe = user_date + timedelta(days= first_day_of_unsafe_period -1)
last_day = last_unsafe.day
last_month = last_unsafe.month
last_year = last_unsafe.year
first_day = first_unsafe.day
first_month = first_unsafe.month
first_year = first_unsafe.year
safe_period_before_unsafe = user_date, first_unsafe - timedelta(days=1)
next_period_date = user_date + timedelta(days=menstral_cycle_days)
safe_period_after_unsafe = (last_unsafe + timedelta(days=1)), next_period_date - timedelta(days=1)
next_period_date_day = next_period_date.day
next_period_date_month = next_period_date.month
next_period_date_year = next_period_date.year


 
print(f"your days of flow is from {start_day} to {day:02d}/{month:02d}/{year} ")
print(f"your ovulation day is {ovu_day:02d}/{ovu_month:02d}/{ovu_year} ")
print(f"your unsafe period starts from {first_day:02d}/{first_month:02d}/{first_year} and ends at {last_day:02d}/{last_month:02d}/{last_year}")
print(f"Safe days before the unsafe days, flow days: {safe_period_before_unsafe[0].strftime('%d/%m/%Y')} to {safe_period_before_unsafe[1].strftime('%d/%m/%Y')}")
print(f"Safe period after the unsafe period: {safe_period_after_unsafe[0].strftime('%d/%m/%Y')} to {safe_period_after_unsafe[1].strftime('%d/%m/%Y')}")
print(f"your next period starts from {next_period_date_day:02d}/{next_period_date_month:02d}/{next_period_date_year}")