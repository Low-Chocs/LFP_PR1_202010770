class producto:

    def __init__(self, product, price, quantity):
        self.product=product
        self.price=price
        self.quantity=quantity
    
    def getPrice(self):
        return self.price

    def getProduct(self):
        return self.product
    
    def getQuantity(self):
        return self.quantity
