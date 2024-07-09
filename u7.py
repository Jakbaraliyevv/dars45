class Mashina:
    def __init__(self,turi,narxi,yili,nomi) -> None:
        self.nomi = nomi
        self.turi = turi
        self.narxi = narxi
        self.yili = yili

    def get_info(self):
        print(f"Mashina turi {self.turi}")
        print(f"Mashina nomi {self.nomi}")
        print(f"Mashina narxi {self.narxi}")
        print(f"Mashina yili {self.yili}")
        print()
    

mashinalar =  [

    Mashina("Toyota Camry", "Yengil", 2018, 20000),
    Mashina("Ford F-150", "Yuk avtomobili", 2020, 30000),
    Mashina("Chevrolet Malibu", "Yengil", 2017, 18000),
    Mashina("Ram 1500", "Yuk avtomobili", 2021, 35000),
    Mashina("Honda Accord", "Yengil", 2019, 25000),
    Mashina("Nissan Altima", "Yengil", 2016, 15000),
    Mashina("GMC Sierra", "Yuk avtomobili", 2022, 40000),
    Mashina("Mazda 6", "Yengil", 2015, 14000),
    Mashina("Tesla Model S", "Yengil", 2023, 70000),
    Mashina("Toyota Tundra", "Yuk avtomobili", 2019, 32000)
]
        
soredlist = sorted(mashinalar,key=lambda car: car.yili)

for mashina in soredlist:
    mashina.get_info()
    #print("-" * 20)
