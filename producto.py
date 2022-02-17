class producto:

    def __init__(self, product, price, quantity):
        self.product=product
        self.price=price
        self.quantity=quantity
        self.sales=float(price)*int(quantity)
    
    def getPrice(self):
        return self.price

    def getProduct(self):
        return self.product
    
    def getQuantity(self):
        return self.quantity

    def getSales(self):
        return self.sales
