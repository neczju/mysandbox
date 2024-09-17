# inventory.py
stuff = {'lina': 1, 'pochodnia': 6,
         'złote monety': 42, 'sztylet': 1, 'strzał': 12}


def displayInventory(inventory):
    print('Inwentarz:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v

    print('Całkowita liczba przedmiotów: ' + str(item_total))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        for k in inventory:
            if item == k:
                inventory[k] += 1  # adds new item amount
        inventory.setdefault(item, 1)  # adds new item to list

    return inventory


inv = {'złote monety': 42, 'lina': 1}
dragonLoot = ['złote monety', 'sztylet',
              'złote monety', 'złote monety', 'ruby']
inv = addToInventory(inv, dragonLoot)


displayInventory(stuff)
displayInventory(inv)
