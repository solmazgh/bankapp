'''project 6
By solmaz Gharagozloo
12/06/2018'''
#Read from the file:


fileRead=open  ("UserInformation.txt" , "r")
username=[]
balance=[]
for row in fileRead:
    cols= row.split()
    username.append(cols[0])
    balance.append(int(cols[1]))
    

#Validate      

'''def validateinput(name):
  if (name!=username[i]):
     print("Please make sure that the spell of the username you entered is correct ")
     name=input("Please re-enter the username: ")
 return name'''
 
    
Balance=0

newbalance=0

  #Adding to the balance    
def addtobalance(Balance):
    add=int(input("Please enter the amount you would like to add: "))
    newbalance=Balance+add
    return newbalance
    
    
   #withdraw money
def drawfrombalance(Balance):
    draw=int(input("Please enter the amount you would like to draw: "))
    if Balance<draw:
        print("there is not Enough Fund to draw")
        draw=input("Please reenter yout amount and it could be unedr the avaliable balance: ")
    else:
        newbalance=Balance-draw
    return newbalance  
    
    
    #get the Index
index=0  

 
def getindex():    
 for i in range(len(username)):
    if (name==username[i]):
        index=i
 return index 
 



'''def getusername():
    return username[getindex()]'''
    
    
    
 #get the balance
def getbalance():
 Balance=balance[getindex()]
 return Balance
 



def makechoice():
    
 
 print("\033[1;32myour balance is ", getbalance())
 print("\033[1;30mType D to deposit money\nType W to withdraw money\nType B to display Balance\nType C to change user, display user name\nType E to exit")
 choice=str(input("Please choose your transaction from the list: "))

 if (choice=='D' or choice=="d"):
    
    print("\033[1;32myour newbalance is", addtobalance(getbalance()))
 elif (choice=="W" or choice=="w"):
    print("\033[1;32myour newbalance is",drawfrombalance(getbalance()))
 elif (choice=="C" or choice=="c"):
    name=input("Please Enter your Username: ")
    #I am tring to call the function here to repeat the program but its holding the index of the previous username
    makechoice()
    
    
 else:
    exit(0) 
    
    


print("\033[0;34m**************   Welcome To Wells Fargo ATM   ****************\n")
name= input("\033[1;30mPlease Enter your Username: ")
makechoice()

    