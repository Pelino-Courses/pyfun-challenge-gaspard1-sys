import datetime
"""
function to calculate the difference 
 between two detes in days.
"""
def date_difference(date1, date2, date_format="%Y-%m-%d"):
    try:
        date1 = datetime.datetime.strptime(date1, date_format)
        date2 = datetime.datetime.strptime(date2, date_format)
        difference_days = abs((date1-date2).days)
        return difference_days
    except Valueerror as error:
        print(error)
date1 = input("enter the first date:")
date2 = input("enter the another date:") 
all_days = date_difference(date1,date2)
print(f"difference days between this dates is: {all_days}")      

 
