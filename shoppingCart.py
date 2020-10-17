# Start function
def get_order():
    print("[command] [item] (command is a to add, d to delete, q tp quit)")
    
    line = input()

    command = line[:1]
    item = line[2:]

    return command, item


# Start function
def add_to_cart(item, cart):
    if not item in cart:
        cart[item] = 0

    cart[item] +=1


# Start function
def delete_from_item(item,cart):
  
      if item in cart:
        cart[item] -=1


      if cart[item] == 0:
        cart.pop(item)



# Start function
def process_order(order, cart):
    command, item = order

    if command == "a":
        add_to_cart(item, cart)
    elif command == "d" and item in cart:
        delete_from_item(item,cart)
    elif command == "q":
        return False

    return True



    
# Start function
def go_shopping():
    cart = dict()

    while True:
        order = get_order()

        if not process_order(order, cart):
           break
        
        
    print(cart)
    print("Finished!")




go_shopping()
