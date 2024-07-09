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
    
natija = Time(11,29,49)

natija.get_info()
natija.set_hour(18)
natija.set_minut(21)
natija.set_second(32)
natija.get_info()
natija.set_time(17,59,10)
natija.get_info()
natija.toString()
natija.get_info()      
    
