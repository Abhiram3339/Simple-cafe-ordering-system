menu={
    'Pizza':100,
    'Burgar':60,
    'Coffee':10,
    'Pasta':50,
}
print("WELCOME TO MY CAFE")
print("Pizza: Rs40\nBurgar: Rs60\nCoffee: Rs10\nPasta: Rs50")
total_order=0
order_1=input("ENTER THE ITEM YOU WANT:")
if order_1 in menu:
    total_order=+menu[order_1]
    print(f"Your item {order_1}has been added to cart")
else:
    print(f"sorry{order_1}is currently not available")
further=input("Do you want to add more?(Yes/No)")
if further=="Yes":
    order_2=input("ENTER THE IIEM YOU WANT TO ADD:")
    if order_2 in menu:
        total_order=+[order_2]
        print(f"Item{order_2}has been added to cart")
    else:
        print(f("Sorry{order_2}is currently not available"))
print(f"The total amount of items is{total_order}")   
