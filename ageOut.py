import time

'''
I was born mach 20th 1995
Today is May 15th-ish 2014

2014 - 1995 = 19. (Assumes birthday is january 1st, sorta)

birthDayAfterJune1st = (birthMonth > 6) or (birthMonth == 6 and birthDay > 1) 
If your birthday is after june 1st, on june 1st, you'll be a year younger that
expected.
'''    

def calculateAgeOut(month, day, year):
    maxAge = 21
    bonusYear = (month >= 6)
    return (year + maxAge) + (bonusYear)

def haveIAgedOut(month, day, year):
    currentYear = int(time.strftime('%Y'))
    currentMonth = int(time.strftime('%m'))
    finalsAreOver = (currentMonth > 8) # This is not completely correct.
    return (currentYear > calculateAgeOut(month, day, year) or 
            (currentYear == calculateAgeOut(month, day, year) and 
            finalsAreOver))
