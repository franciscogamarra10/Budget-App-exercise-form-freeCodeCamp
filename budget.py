import math
class Category:
### creamos una clase que reciba el nombre de la categoria y crea una lista ledger inicialize con categoria de gasto

# food = budget.Category("Food") ## se instancia con una categoria
# food.deposit(1000, "initial deposit")## metodo para depositar se asume que lo primero que hay que hacer por el metodo es depositar pero sino depositamos tenemos metodos que no nos van a dejar sacar ni transferir $
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = budget.Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)  
### balance=0 
  ## definimos una variable inicializa a 0 el balance
  ## y la lista
  def __init__(self,nombre):
    
    self.nombre=nombre
    # self.ledger2=[]
    self.bal=0
    self.ledger=list()


      
    
# {"amount": amount, "description": description}
  def deposit(self,amount,description=""):
    self.amount=amount
    self.description=description
    self.bal+=self.amount
    # self.ledger.append( [self.amount,self.description])
    self.ledger.append( {'amount':self.amount,'description':self.description})
    
  #  def __str__(self):
  #   ##
  #    return print(f"")
  def withdraw(self,amount,description=""):
      self.amount=amount
      self.description=description
      if self.check_funds(self.amount):
        # self.bal-=-amount 
        # self.ledger.append( [-self.amount,self.description])
        self.ledger.append( {'amount':-self.amount,'description':self.description})
        # print(self.ledger)
        return True
      else:
        return False
        

  def get_balance(self):
    
    tot=0
    # for ele in range(len(self.ledger)):
    for ele in self.ledger:  
        # print(self.ledger[ele][0])
        # tot+=self.ledger[ele][0]
        tot+=ele['amount']
        
        # print(ele)
    return tot
      
  def transfer(self,amount,nombre2):
      self.amount=amount
      
      if self.check_funds(self.amount):
        self. withdraw(self.amount,"Transfer to "+nombre2.nombre)
        nombre2.deposit(self.amount, "Transfer from "+self.nombre)
        return True
      else:
        return False
      
       
    
       
  def check_funds(self,amount):

    self.amount=amount
    tot3=0
    # for ele in range(len(self.ledger)):
    for ele in self.ledger:  
        # print(self.ledger[ele][0])
        # tot3+=self.ledger[ele][0]
        tot3+=ele['amount']
    if self.amount>tot3:
       return False
    else:
       return True
       
  def __str__(self):
  #   ##
     
     # encabezado='*'*13+self.nombre+'*'*13
     encabezado=f"{self.nombre:*^30}"
    
     lista=""
     tot2=0
     # for ele in range(len(self.ledger)):
     for ele in self.ledger:  
       # lista+=f"{self.ledger[ele][1] [0:23]:23}"+f"{self.ledger[ele][0]:>7.2f}"+"\n"
       lista+=f"{ele['description'] [0:23]:23}"+f"{ele['amount']:>7.2f}"+"\n"
       # tot2+=self.ledger[ele][0] 
       tot2+=ele['amount'] 
     lista=encabezado+'\n'+lista+"Total: "+str(tot2)  
     return lista   
    
# food =Category("Food")
# print(food.deposit(100, "deposit"))
# print(food.withdraw(100.10))
# "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "  
        # good_withdraw = self.food.withdraw(100.10))
def create_spend_chart(categories):
  # linea="Percentage spent by category".ljust(20)+"\n"
  linea="Percentage spent by category\n"
  per=[]
  # categories=[]
  # for obje in categories2:
  #   categories.append(Category(obje))
    
  # print(categories[0].ledger[0])
  
  for ll in range(len(categories)):
      
      val=0
      for ele in categories[ll].ledger:
        val2=ele['amount']
        if val2 <0:
            val+=val2
      per.append(val)      
    
  # print(per) len(food.nombre)
  pert=sum(per)  
  
  ss=[]
  for i in range(len(per)):
     ss.append(len(categories[i].nombre))
  for i in range(len(per)):
     per[i]=per[i]/pert
  # print(ss)   
  maxl=max(ss)
  # print(per)
  for i in range(len(per)):
   per[i]=math.floor(round(per[i]*100)/10)*10

  # print(per)
  # print(per) 
  # encabezado=f"{self.nombre:*^30}"
  # lineam=" "+"-"*10
  # lineam=f"    {lineam}"  
  # linea=f"Percentage spent by category\n" 
  
  for i in range(100,-1,-10):
    # linea+=f"{i :>3}|\n"+" "
    linea+=f"{str(i)+'|':>4}"
    for j in range(len(per)):
        
        if i <= per[j]:
          linea+=" "+"o"
        else:
          linea=linea+"  " 
        linea=linea+" "
    linea=linea+" "+'\n'     
  linea=linea+" "*4+f'----------'+"\n"
  linea=linea+" "*4
  # linea=linea+lineam+"\n"
  # print(maxl)
  for i in range(maxl):
    # print(i)
    for j in range(len(per)):
      nombre3=categories[j].nombre
      nombre3=str(nombre3)
      # print(nombre3)
      linea=" "+linea
      if i <=len(nombre3)-1:
        #  print(nombre3[i])
         linea=linea+" "+nombre3[i]
      else:
         linea=linea+"  "  
      linea=linea+" "  
    linea=linea+" "+"\n" 
    linea=linea+" "*4







  # pass
    
  return linea.strip()+"  "

food = Category("Food")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

# print(food)
# print(clothing)

# print(create_spend_chart([food, clothing, auto]))
food = Category("Food")
business=Category("Business")
entertainment = Category("Entertainment")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)


print(create_spend_chart([business, food, entertainment]))


print("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  ")

print(len(create_spend_chart([business, food, entertainment])))
print(len("Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "))