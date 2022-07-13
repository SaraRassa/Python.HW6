from pyfiglet import Figlet

def show_list():
    for i in range(len(PRODUCTS)):
        print(PRODUCTS[i])

def show_menu():
    print('1_ Add product')
    print('2_ Edit product')
    print('3_ Delete product')
    print('4_ Search')
    print('5- Show list')
    print('6_ Buy')
    print('7_ Exit') 

PRODUCTS=[]

def add_product():
    a={}
    a['id']=int(input("Enter product code: "))
    a['name']=input('Enter product name: ')
    a['price']=int(input("Enter product price: "))
    a['count']=int(input("Enter product count: "))
    PRODUCTS.append(a)
    show_menu()

def edit_product():
    Answer=input('Enter the product name that you want to edit: ')
    for E in PRODUCTS:
        if Answer==E['name']:
            E['id']=int(input('Enter new code: '))
            E['name']=input('Enter new product name: ')
            E['price']=int(input("Enter new product price: "))
            E['count']=int(input("Enter new product count: "))
            show_list()
            break
    else:
        print("This item is not in the list!")
        

def delet_product():
    Answer=input("Which product do you want to remove? ")
    for D in PRODUCTS:
        if Answer==D['name']:
            PRODUCTS.remove(D)
    print(Answer, 'information deleted from the list!')
    show_list()

def search_product():
    S=input("Enter the name of product: ")
    for P in PRODUCTS:
        if P['name']==S:
            print(P)
            break
    else:
        print("This product does not exist in the list!")

def buy_product():
    price=0
    show_list()
    while True:
        B=int(input('Enter product code that customer wants to buy: '))
        for K in PRODUCTS:
            if B==int(K['id']):
                number=int(input("How many product? "))
                if number <= int(K['count']):
                    price=price + int(K['price'])* number
                    a=int(K['price'])*number
                    print('Cart','\nItem:', K['name'],'\t','Qty:',number,'\t' ,'price: ',a,'\nTotal price:', price)
                    (K['count'])=int(K['count'])- number
                    break
                else:
                    print('There are only', K['count'], K['name'],' available!')
                    break
        else:
            print("This product is not available!!")
        con=input("Do you want to continue shopping? [Yes/No]")
        if con!='Yes' and con!='yes' and con!='y' and con!='Y':
            break

def load():
    print("Loading...")
    MyFile = open('database.txt','r')
    Data = MyFile.read()
    ProductList = Data.split('\n')

    for i in range(len(ProductList)):
        Product_info= ProductList[i].split(',')
        mydict={}
        mydict['id']=Product_info[0]
        mydict['name']=Product_info[1]
        mydict['price']=Product_info[2]
        mydict['count']=Product_info[3]
        PRODUCTS.append(mydict)
    print("Welcome!")

load()
f = Figlet(font='standard')
print (f.renderText('Sara Store'))
show_menu()
choice=int(input("Select and option: "))

if choice==1:
    add_product()

elif choice==2:
    show_list()
    edit_product()

elif choice==3:
    delet_product()
    
elif choice==4:
    search_product()
elif choice==5:
    show_list()

elif choice==6:
    buy_product()

elif choice==7:
    exit()
