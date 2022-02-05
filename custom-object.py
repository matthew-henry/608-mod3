
class Purchase(object):
    def __init__(self, amount):
        #constructor initializes class with the purchase amount
        self.amount = amount
        self.tip = 0
        self.tax = 0
    
    def calculateTax(self, taxPercent):
        self.tax = self.amount * taxPercent/100
        return self.tax
    
    def calculateTip(self, tipPercent):
        self.tip = self.amount * tipPercent/100
        return self.tip

    def calculateTotal(self):
        return self.amount + self.tax + self.tip
    
def main():
    purchase = Purchase(100.0)
        
    taxPercent = 7.5
    tipPercent = 20.0
        
    tax = purchase.calculateTax(taxPercent)
    tip = purchase.calculateTip(tipPercent)

    print(f'Tax: {tax}')
    print(f'Tip: {tip}')
    print(f'Total {purchase.calculateTotal()}')

if __name__ == "__main__":
    main()