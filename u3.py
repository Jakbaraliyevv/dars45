class Data:
    def __init__(self,day,month,year) -> None:
        self.day = day
        self.month = month
        self.year = year
    
    def get_Day(self):
        kun = self.day
        return kun
    def get_month(self):
        oy = self.month
        return oy
    def get_year(self):
        yil = self.year
        return yil
    
    def set_Day(self,new_Day):
        self.day = new_Day
    def set_Month(self,new_oy):
        self.month = new_oy
    def set_Year(self,new_yil):
        self.year = new_yil
    def set_date(self,newd,newm,newy):
        self.day = newd
        self.month = newm
        self.year = newy
    def toString(self):
        day = self.day
        month = self.month
        year = self.year
        resualt = str(day).zfill(2) +'.'+ str(month).zfill(2)+'.'+ str(year).zfill(4)
        return resualt

    def get_info(self):
        return f"{self.get_Day()}/{self.get_month()}/{self.get_year()}"
    def __str__(self) -> str:
       return self.get_info()
        

natija = Data(29,11,2005)
print(natija)
natija.set_Day(1)
natija.set_Month(9)
natija.set_Year(2024)
print(natija)
natija.set_date(7,11,2021)
print(natija)
natija.toString()
print(natija)