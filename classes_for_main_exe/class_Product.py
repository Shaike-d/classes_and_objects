

class Product():
    VAT_RATE = 0.17
    created_count = 0
    
    
    def __init__(self,name,price,quantity=0):
        if price < 0:
            raise ValueError("price cont be a negativ num")
        else:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.created_count += 1


    def price_with_vat(self):
        return self.price * (1+self.VAT_RATE)





def answer_2():
    pen = Product("pen",5)
    print(pen.name, pen.price, pen.quantity)
    try:
        Product("bad", -10)
    except ValueError as error:
        print("error", error)


def answer_4():
    laptop = Product("Laptop", 1000)
    mouse = Product("Mouse", 50)
    print(Product.created_count)
    print(laptop.price_with_vat())