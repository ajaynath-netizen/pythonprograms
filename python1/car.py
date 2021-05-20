class Car:
    def __init__(self,color,company,tyres,capacity=None):
        self.color=color
        self.company=company
        
        self.tyres=tyres
        
    def move(self):
        print(" {}  {} moves".format(self.color,self.company))

    def describe(self):
        print("{} {} {}".format(self.color,self.company,self.tyres))


class Battery:
   
     def __init__(self,capacity):
         self.capacity=capacity


class DieselCar(Car):

      def __init__(self,color,company,tyres,capacity=None):
        super().__init__(color,company,tyres)
        
    
        if capacity==None:
          self.battery=Battery(70)
        else:
          self.battery=Battery(capacity)

class Electriccar(Car):
    def __init__(self,color,company,tyres,capacity=None):
        super().__init__(color,company,tyres)
        
        if capacity==None:
          self.battery=Battery(70)
        else:
          self.battery=Battery(capacity)
  
    
 
car=DieselCar("red","swift",4,456)      

print(car.battery.capacity)
car.describe()