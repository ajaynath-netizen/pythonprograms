class virus(object):
    count=0
    
    def __init__(self,name,typeof,num):
      self.name=name
      self.typeof=typeof
      self.num=num  
      self.li=[]
      virus.count=virus.count+1
      

      
    
      
    # def num_instance(self):
    #    self.count=self.count+1
    #   return self.count
    def counts(self,count=None):
        if count==None:
          return virus.count

        else:
          virus.count=virus.count+count
          return virus.count
            
  
    def infects(self):
      print(self.name+" "+"virus infects")
      
    def kills(self):
      print(self.typeof+" "+"kilss")    

class corona(virus):
     count=0
     
     def __init__(self,panedemic,name,typeof,num):
       self.panedemic=panedemic
       corona.count=corona.count+1
       
       
       super().__init__(name,typeof,num)
       
    #  def __format__(self,name,arg):
    #     print("dramatic")
    #     self._name=name  
    #     for word in arg:
    #       self.word=word
    #       self.li.append(self.word)
    #       print(self.li)
    #       print("{0} {1} damegs".format(self._name,self.word))
          
    #  def num_instance(self):
          
    #       return self.count
          

class trojan(virus):
   count=0
   
   def __init__(self,anti,panedemic,name,typeof,num):
     self.anti=anti
     trojan.count=trojan.count+1
     super().__init__(name,typeof,num)
     


   def kills(self):
      print("{} damages".format(self.name))



v1=virus(5,3,1)
print(v1.counts())
print(virus.count)
c1=corona("pand","covid","bio","infinite")
t1=trojan("kaspersky","yes","togen","pc","infi")
t1.kills() 

v2=virus(5,6,9)
print(t1.counts())

v3=virus(9,5,6)
print(virus.count)

print(isinstance(c1,virus))
print(issubclass(corona,virus))











