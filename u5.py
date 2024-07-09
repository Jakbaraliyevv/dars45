class Rectangle:
    def __init__(self,height,widh) -> None:
        self.height = height
        self.widh = widh

    def get_height(self):
        return self.height
    def set_height(self,new_height):
        self.height = new_height
        return self.height
    def get_widh(self):
        return self.widh
    def set_widh(self,new_widh):
        self.widh = new_widh
        return self.widh
    def get_area(self):
        return self.height * self.widh
    def get_perimetr(self):
        return 2*(self.height + self.widh)
    def get_info(self):
        print(f"Xona boyi {self.get_height()}")
        print(f"Xona eni {self.get_widh()}")
        print(f"Xona yuzasi {self.get_area()}")
        print(f"Xona eni {self.get_perimetr()}")
        print()

natija = Rectangle(5,3)
natija.get_info()
natija.set_height(7)
natija.set_widh(4)
natija.get_info()
            

