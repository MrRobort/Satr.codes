class Bikes():
    def __init__(self):
        self.description = ''
        self.cost = 0
        self.sale_price = 0
        self.condution = 0
        self.sold = False

    def create(self, description,cost, sale_price, condution):
        self.description = description
        self.cost= cost
        self.sale_price = sale_price
        self.condution = condution
        

    def sell(self,bike):
        self.sold = True

    def update_price(self,new_price):
        if (self.sold):
            print("Action Not allowed, the bike already sold")
        else:
            self.sale_price = new_price

    def print_values(self):
        print("Description: " , self.description , 'Cost: ' , self.cost , 'Sale price: ' , self.sale_price , "Condution: " , self.condution , "Sold: ", self.sold)

bike_obj = Bikes()

bike1 = bike_obj.create('bike', 100, 250, 0.35)
bike_obj.print_values()
bike_obj.update_price(500)
bike_obj.print_values()
