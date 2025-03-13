def display_inventory(invt):
    total_number = 0
    for k, v in invt.items():
        print("Items in the inventory: ")
        print(f"{v} {k}")
        total_number +=v
    print(f"The total number of items is: {total_number}")
    
    
def addToInventory(invt, dragonLoot):
    for item in dragonLoot:
        if item in invt:
            invt[item] +=1
        else:
            invt[item] = 1
    return invt
        
        

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
invt = addToInventory(stuff, dragonLoot)
display_inventory(invt)