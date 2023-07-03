# class, attributes, inheritance


class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price 
        self.deal_price = deal_price 
        self.rating = rating 
        
    def display_product_details(self):
        print("Name : {}".format(self.name))
        print("Price : {}".format(self.price))
        print("Deal_price : {}".format(self.deal_price))
        print("Rating : {}".format(self.rating)) 

class Electronic_product(Product):
    def __init__(self, name, price, deal_price, rating, warranty_in_month):
        super().__init__(name, price, deal_price, rating)
        self.warranty_in_month = warranty_in_month
        
    def get_warranty_in_months(self):
        return self.warranty_in_month
    
    def display_product_details(self):
        super().display_product_details()
        print("Warranty_in_months : {}".format(self.warranty_in_month))
        

tv = Electronic_product("TV", 35000, 5000, 4.2, 12)
tv.display_product_details()
