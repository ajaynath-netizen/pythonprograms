class Animal:
    def __init__ (self,color,typeof,legs):
         self.color=color
         self.type=typeof
         self.legs=legs
    def get_animal(self):
        print(self.color) 
        print(self.type)    
        print(self.legs)
    def action(self):
        print(self.color+" "+"animal is"+" "+self.type+" having"+" "+self.legs+" "+"legs")   
         
class Tiger(Animal):

    def __init__(self,color,typeof,legs,danger):
      self.dang=danger
      super().__init__(color,typeof,legs)

class Lion(Tiger):
    def __init__(self,color,typeof,legs,danger):
        super().__init__(color,typeof,legs,danger)

        
t=Tiger("red","wild",4,"yes")

l=Lion("yellow","WILD","4","TOOdanger")




def abc(a):
    for i in range(len(a)):
        a[i]="bat"
        print(a[i])
    return a     
a=[8,"dog","pig","rabbit"]       


# # y="yes" 
# while y=="yes":
#     y=input("yes or no")  
# else:
#     print("dh")       




line="From an india ro usa \n \n widhd djksjkd hdhdj hdjdj hdhjd \n hdhsjhs hdjdjd\n hdjdkslsjk."
line=line.split()
print(line)

