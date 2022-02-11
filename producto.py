class producto:
    def __init__(self, product, price, quantity):
        self.product=product
        self.price=price
        self.quantity=quantity
    
    def getPrice(self):
        print(self.price)
