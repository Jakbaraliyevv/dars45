class Time:
    def __init__(self,hour,minut,second) -> None:
        self.hour = hour
        self.minut = minut
        self.second =second

    def get_hour(self):
        return self.hour
    def get_minut(self):
        return self.minut
    def get_second(self):
        return self.second
    
    def set_hour(self,new_hour):
        self.hour = new_hour

    def set_minut(self,new_minut):
        self.minut = new_minut

    def set_second(self,new_second):
        self.second = new_second
    
    def set_time(self,newH,newM,newS):
        self.hour = newH
        self.minut = newM
        self.second = newS

    def get_info(self):
        print(f"{self.get_hour()}:{self.get_minut()}:{self.get_second()}")
        print()

    def toString(self):
        change = str(f"{self.hour}:{self.minut}:{self.second}")
        return change
    def next_second(self):

        if self.second == 59:
            self.second = 0

            if self.minut == 59:
                self.minut = 0
                self.hour +=1
            else:
                self.minut += 1
        else: 
            self.second += 1
    
    def previousSecond(self):

        if self.second == 0:
            self.second = 59
            
            if self.minut == 0:
                self.minut = 59
                self.hour -=1
            else:
                self.minut -= 1
        else:
            self.second -= 1
    






natija = Time(11,29,49)

natija.get_info()   #Birinchi xolati
natija.set_hour(18)
natija.set_minut(21)
natija.set_second(32)
natija.get_info()   #Har biri alohida set bolgan holati
natija.set_time(17,59,59)
natija.get_info()   #Data set bolgan holati
natija.toString()   
natija.get_info()   #Stringa ozgargan xolati
natija.next_second()
natija.get_info()   #Secund qoshilgan holati
natija.previousSecond()
natija.get_info()   #Secund ayrilgan holati
   
    