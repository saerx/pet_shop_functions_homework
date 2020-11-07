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
