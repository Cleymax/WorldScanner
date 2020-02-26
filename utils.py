from Item import Item


class Position:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


def item_from_nbt(item):
    return Item(item['id'].value, item['Count'].value, item['Damage'].value)


def items_from_nbt(items):
    _items = {}
    for item in items:
        _items[len(_items)] = item_from_nbt(item)
    return _items
