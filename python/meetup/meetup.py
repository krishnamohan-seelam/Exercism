import datetime
import calendar

class MeetupDayException(Exception):
    def __init__(self, value="MeetupDay error"):
            self.value = value

    def __str__(self):
        return repr(self.value)

which_map  = {'1st':0,'2nd':1,'3rd':2,'4th':3,'5th':4,}
weekdays=['monday','tuesday','wednesday','thursday','friday','saturday','sunday',]
def meetup_day(year, month, day_of_the_week, which):
    days_in_month = calendar.monthrange(year,month)[1]
    day_index = weekdays.index(day_of_the_week.lower())
    which_val = which_map.get(which,0) 
    if which =='teenth':
        first_date = datetime.date(year,month,13)
    elif which =='last':
        first_date = datetime.date(year,month,days_in_month-6)
    else:
        first_date = datetime.date(year,month,1)
    days=(day_index-first_date.weekday()+7)%7 +(which_val*7)
    if days <= days_in_month:
        print(f'date calculated:{first_date + datetime.timedelta(days=days)}')
        return first_date + datetime.timedelta(days=days)
    else:
        raise MeetupDayException()
