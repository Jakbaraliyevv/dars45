class Account:
    def __init__(self,id,name,balance) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def get_id(self):
        ID = self.id
        return ID
    def get_name(self):
        Name = self.name
        return Name
    def get_balance(self):
        Balance = self.balance
        return Balance
    def Credit(self,new_amount):
        self.balance = new_amount
        return self.balance 

        
        
natija = Account("0107ww11","Aziz",0)
print(natija.balance)
natija.Credit(200000)
print(natija.balance)