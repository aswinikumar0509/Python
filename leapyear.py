# Cheching the year is leap year or not
def leapyear(year):
    if( year%4==0 and ( year%100!=0)) or (year%400==0) :
        return "Leap year"
    else:
        return "Not leap year"

print(leapyear(2020))
