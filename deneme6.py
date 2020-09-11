operations=[]
selectedFoodCategory1=["Waffle = 20 tl","Chocolate cake = 10 tl", "Profiterol = 15 tl"]
selectedFoodCategory2=["Beer = 25 tl","Coffe = 15 tl", "Hot Chocolate = 15 tl"] 
selectedFoodCategory3=["Chicken = 20 tl","Hamburger = 25 tl", "Pasta = 25 tl"]
category=''
 
inputName=input("enter the username :") 

if inputName=="yunus.inan":
    print("Welcome Mr.Yunus")
    inputPassword=input("enter the password :")
    while inputPassword!="12345":
        print("pls,Re-enter Password!")
        inputPassword=input("enter the password :") 
    
else:
    print("Customer Page")  

if inputName=="yunus.inan" and inputPassword=="12345":  
    print("1 : add product :")
    print("2 : menu page")
    category=str(input("select category :")) 
    
    if category=="1":
         print("which operation :")
         
    if category=="2":
         print("")      
         
print("menus ")
print("1 : Dessert ")
print("2 : Drinks ")
print("3 : Foods ")
print("q : exit ")
          
while True:
    operations=input("choose menus: ") 
    
    if operations=='1':
        print("\ndessert menu :\n ")
        print(selectedFoodCategory1)
        if category=='1':
            word=input("enter product : ")
            selectedFoodCategory1.append(word)
            print(selectedFoodCategory1)
            continue    
 
    elif operations=='2':
        print("\ndrinks menu :\n")
        print(selectedFoodCategory2)
        if category=='1':
            word=input("enter product : ")
            selectedFoodCategory2.append(word)
            print(selectedFoodCategory2)
            continue 
     
    elif operations=='3':
        print("\nfoods menu :\n")
        print(selectedFoodCategory3)
        if category=='1':
            word=input("enter product : ")
            selectedFoodCategory3.append(word)
            print(selectedFoodCategory3)
            continue 

    elif operations=='q':
        print("exit...")
        break 
    
    else:
        print("invalid click... ")
        continue
