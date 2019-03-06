# def is_leap_year(year):
#   div,rem = divmod(year,100)
#    return  div % 4 ==0 if (rem ==0) else year % 4 ==0 

def is_leap_year(year):
    return year %4 ==0 and (year %100!=0  or year% 400==0)