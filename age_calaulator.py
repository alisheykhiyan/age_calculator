# age_counter.py
# tip = this program's time has been planed by lunar calendar.mind it while you are entering thr date.
# reciving the borning date
# mind that this program thinks that you where born at 00:00:00 .
print ("(# mind that this program thinks that you where born at 00:00:00 .)")
print ("(tip = this program's time has been planed by lunar calendar.mind it while you are entering thr date.)")
print ("Enter your borning date by the defined role or enter 'q' in next level:")
borning_year = int(input("Enter the year you've boarned in:"))
borning_month = int(input("Enter the month you've boarned in:"))
borning_day = int(input("Enter the day you've boarned in:"))
# defining the present date and time
import datetime
date_and_time = datetime.datetime.now()
year = (date_and_time.year)
month = (date_and_time.month)
day = (date_and_time.day)
hour = (date_and_time.hour)
minute = (date_and_time.minute)
second = (date_and_time.second)
# one by one calculation of date
# if (month of born =< present month)
if borning_month <= month:
    age_year = year - borning_year
    age_month = month - borning_month
else :
    age_year = (year - borning_year) - 1
    age_month = 12 + (month - borning_month)
    #if (day of born =< present day) 
if borning_day <= day:
    age_day = day - borning_day
else:
    age_day =  30 + (day - borning_day)
    age_month = age_month - 1
# one by one calculation of date
age_hour = hour 
age_minute = minute 
age_second = second
# printing the accurate age
print (age_year ,'years' ,age_month ,'months' ,age_day ,'days' ,
                age_hour ,'hours' ,age_minute ,'minutes' ,age_second ,'seconds')

