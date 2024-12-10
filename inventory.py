

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'danger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print(f"Total number of items: {item_total}")


def addToInventory(inv, dragonLoot):
    for item in dragonLoot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1

    return inv




dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'gold coin']
inv = {'gold coin': 42, 'rope':1}
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)