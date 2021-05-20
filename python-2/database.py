class database:

   tdb=[] 
   def __init__(self,name,email,phn,salary,designation) :
  
      self.name=name
      self.email=email
      self.phn=phn
      self.salary=salary
      self.designation=designation
    
   
   def create_db(self):
        
          self.db={"name":self.name,"email":self.email,"phn":self.phn,"salary":self.salary,"designation":self.designation}
         
          return self.db
   
   def ad_db(self):
       
       database.tdb.append(self.create_db())
       return database.tdb

obj=database("ajay","ajaynath630@gmail.com",9618035625,56563,"manager")
obj2=database("vijay","vijaynath630@gmail.com",9614523625,56463,"jmanager")
print(obj.ad_db())
# print(obj2.ad_db())
       

