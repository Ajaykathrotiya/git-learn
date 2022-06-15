class Mobile:
    def __init__(self,price,brand):
        self.price=price
        self.brand=brand 

obj1=Mobile(100,'nokia')
obj2=Mobile(200,'Apple')
print(obj1.price,obj1.brand)
print(obj2.price,obj2.brand)