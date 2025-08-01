"""
Task 6: Electronics Store Nested Cart
Three friends, Tobi, Lami, and Chinedu, visit an electronics store together. 
They decide to share **one big smart cart** that can group items by the department they are picked from.
The cart keeps track of each department with the items selected inside it.

cart = {
    "phones": {},
    "laptops": {},
    "accessories": {}
}

Each product in the store is represented as a tuple: (product_name, price) because these details never change.

During shopping:
- Tobi picks up an iPhone for 750000 Naira in the "phones" department.
- Lami adds a Dell XPS Laptop for 1200000 Naira in the "laptops" department.
- Chinedu adds Wireless Earbuds for 50000 Naira in the "accessories" department.
- Tobi changes his mind and removes the iPhone from the cart.
- Lami then adds another accessory: a Gaming Mouse for 35000 Naira.

At checkout:
- A snapshot of the nested cart is taken as the order summary for the store record.
- The shared smart cart is then completely emptied to reset for the next customers.
"""

cart = {
            "phones": {},
                "laptops": {},
                    "accessories": {}
 }

iphone = ("iPhone", 750000)
dell_xps = ("Dell XPS", 1200000)
earbuds = ("Wireless Earbuds", 50000)
gaming_mouse = ("Gaming Mouse", 35000)

cart["phones"][iphone[0]] = iphone[1]
print("Tobi added an iphone")

cart["laptops"][dell_xps[0]] = dell_xps[1]
print("Lami added a dell xps")

cart["accessories"][earbuds[0]] = earbuds[1]
print("Chinedu added  earbuds")

cart["phones"].pop("iPhone")
print("Tobi removed the iphone")

cart["accessories"][gaming_mouse[0]] = gaming_mouse[1]
print("Lami added a gaming mouse")

order_summary = cart.copy()

cart.clear()

print(" Order Summary:", order_summary)

print("Smart Cart After Checkout:", cart)
