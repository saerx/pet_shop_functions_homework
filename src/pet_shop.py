# WRITE YOUR FUNCTIONS HERE

#1. Get Pet Shop Name
def get_pet_shop_name(shop):
    return shop["name"]

#2. Get total cash
def get_total_cash(shop):
    return shop["admin"]["total_cash"]

#3. Add or remove cash
def add_or_remove_cash(shop, payment):
    shop["admin"]["total_cash"] += payment

#4. Get pets sold
def get_pets_sold(shop):
    return shop["admin"]["pets_sold"]

#5. Increase pets sold
def increase_pets_sold(shop, pet_num):
    shop["admin"]["pets_sold"] += pet_num

#6. Get stock count
def get_stock_count(shop):
    return len(shop["pets"])

#7. Get pets by breed
def get_pets_by_breed(shop, breed):
    breed_matches = []
    for pet in shop["pets"]:
       if pet["breed"] == breed:
           breed_matches.append(pet)
    return breed_matches

#8. Find pet by name
def find_pet_by_name(shop, name):
    found_pet = None
    for pet in shop["pets"]:
        if pet["name"] == name:
            found_pet = pet
    return found_pet

#9. Remove pet by name
def remove_pet_by_name(shop, name):
    for pet in shop["pets"]:
        if pet["name"] == name:
            shop["pets"].remove(pet)

#10. Add pet to stock
def add_pet_to_stock(shop, pet):
    shop["pets"].append(pet)

#11. Get customer cash
def get_customer_cash(human):
    return human["cash"]

#12. Remove customer cash
def remove_customer_cash(human, payment):
    human["cash"] -= payment

#13. Get customer pet count
def get_customer_pet_count(human):
    return len(human["pets"])

#14. Add pet to customer
def add_pet_to_customer(human, name):
    human["pets"].append(name)

    # --- OPTIONAL ---

#15. Check customer can afford pet
def customer_can_afford_pet(human, pet):
    if get_customer_cash(human) >= pet["price"]:
        return True
    else:
        return False

 # These are 'integration' tests so we want multiple asserts.
    # If one fails the entire test should fail

#16. Sell pet to customer
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
            



    
