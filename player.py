from os import listdir

from nbt.nbt import NBTFile

from Item import Item


def is_scan_item(args, _item):
    for _id in args.id:
        for idd in _id.split(','):
            if str(idd) == str(_item.material):
                return True
    return False


class Player:
    def __init__(self, args):
        self.args = args

    def scan(self):
        for file in listdir(self.args.world + '/playerdata/'):
            nbt = NBTFile(self.args.world + '/playerdata/' + file, 'rb')

            inv_items = nbt['Inventory']
            ec_items = nbt['EnderItems']

            if self.args.inventory and len(inv_items) != 0:
                for item in inv_items:
                    _item = Item(item['id'].value, item['Count'].value, item['Damage'].value)
                    if is_scan_item(self.args, _item) and _item.count >= self.args.count:
                        print('Found {0}*{1} in {2}\'s inventory !'.format(
                            _item.count,
                            _item.material,
                            file.replace('.dat', '')
                        ))

            if self.args.enderchest and len(ec_items) != 0:
                for item in ec_items:
                    _item = Item(item['id'].value, item['Count'].value, item['Damage'].value)
                    if is_scan_item(self.args, _item) and _item.count > self.args.count:
                        print('Found {0}*{1} in {2}\'s enderchest !'.format(
                            _item.count,
                            _item.material,
                            file.replace('.dat', '')
                        ))
