# Create class STORE to keep track of Products ( Product Code, Name and price).
# Display menu of all products to user. Generate bill as per

class Product:
    def __init__(self,pc,name,price):
        self.pc = pc
        self.name = name
        self.price = price
class Store:
    def __init__(self):
        self.pl = []
        self.cart = []

    def add(self,product):
        self.pl.append(product)

    def display(self):
        for product in self.pl:
            print(f'{product.pc} \t {product.name} \t {product.price}')

    def atc(self,product):
        for item in self.pl:
            if item.pc == product:
                self.cart.append(item)
                print("Product added")
                return
        print("Item not present in store")

    def rfc(self,product):
        for item in self.pl:
            if item.pc == product:
                self.cart.remove(item)
                print(f'{item.name} Product remove')
                return
        print("No product found this card")

    def gb(self):
        amount = 0
        for product in self.cart:
            amount += product.price
        print(f'Total bill is {amount}')

    def dc(self):
        for item in self.cart:
            print(f'{item.name}')

    def exit(self):
        print("You are exited.")
        exit()

if __name__ == '__main__':
    s = Store()
    s.add(Product(1,"Milk",27))
    s.add(Product(2,"Wine",200))
    s.add(Product(3,"Coffe",20))
    s.add(Product(4,"Tea",7))
    s.add(Product(5,"Green Tea",10))
    while(1):
        print("\n 1.Display product \n 2.Add product to cart \n 3.Remove product form cart \n 4.View cart \n 5.Genrate bill \n 6.Exit \n")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            s.display()
        elif ch == 2:
            code = int(input("Enter Product code: "))
            s.atc(code)
        elif ch == 3:
            code = int(input("Enter Product code: "))
            s.rfc(code)
        elif ch == 4:
            s.dc()
        elif ch == 5:
            s.gb()
        elif ch == 6:
            s.exit()
        else:
            print("Enter Valid choice")
