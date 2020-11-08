# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop):
    return shop["name"]

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

def add_or_remove_cash(shop, payment):
    shop["admin"]["total_cash"] += payment

def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

def increase_pets_sold(shop, pet_num):
    shop["admin"]["pets_sold"] += pet_num

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    breed_matches = []
    for pet in shop["pets"]:
       if pet["breed"] == breed:
           breed_matches.append(pet)
    return breed_matches

def find_pet_by_name(shop, name):
    found_pet = None
    for pet in shop["pets"]:
        if pet["name"] == name:
            found_pet = pet
    return found_pet

def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)

def get_customer_cash(human):
    return human["cash"]

def remove_customer_cash(human, payment):
    human["cash"] -= payment

def get_customer_pet_count(human):
    return len(human["pets"])

def add_pet_to_customer(human, name):
    human["pets"].append(name)

    # --- OPTIONAL ---

def customer_can_afford_pet(human, pet):
    if get_customer_cash(human) >= pet["price"]:
        return True
    else:
        return False

 # These are 'integration' tests so we want multiple asserts.
    # If one fails the entire test should fail

def sell_pet_to_customer(shop, name, human):
    if name == None:
        print("Pet does not exist")
    else:
        if customer_can_afford_pet(human, name) == False:
            print("Insufficient Funds")
        else:
            pet_cost = name["price"]
            remove_customer_cash(human, pet_cost)
            add_or_remove_cash(shop, pet_cost)
            add_pet_to_customer(human, name)
            remove_pet_by_name(shop, name)
            increase_pets_sold(shop, 1)
            



    
