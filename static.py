class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)

date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")

switch(dates)
{
    case 1: "undefined";
        print("Expiry Date")
    case 2: "Timeline_date_fetch";
        print("Current date is)
    case 3: NULL
        print(Void date)
    default:
        print("bad error")
    
#input in the program will be provided by user
#Code for the date has been added
#file has been successfully updated
