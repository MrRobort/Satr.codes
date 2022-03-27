class Bikes:
    def __init__(self,description, cost, sale_price, condution):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condution = condution
    
    def create(self):
        return {
            'Description': self.description,
            'Cost': self.cost,
            'Sale Price': self.sale_price,
            'Condition': self.condution,
            'Sold': False
            }
    
    def sell(self,bike):
        bike['Sold'] = True
        
    def update_price(self, bike, sale_price):
        if(bike['Sold'] == True):
            print("Action Not Allowed, the bike already sold")
        else:
            bike['Sale Price'] = sale_price
            
    
bike_obj = Bikes('Univerage voge', cost=100, sale_price=350, condution=0.5)
bike1 = bike_obj.create()
print(bike1)
bike_obj.update_price(bike1, 800)
print(bike1)
bike_obj.sell(bike1)
print(bike1)
