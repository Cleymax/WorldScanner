import os
from argparse import ArgumentParser

from nbt.world import WorldFolder

from player import Player


def main():
    usage = 'python main.py [options] arg1 arg2 arg...'

    parser = ArgumentParser(
        usage=usage,
        description='WorldScanner: The best scanner in the minecraft world',
        epilog='Here is the help for all possible arguments and options.',
        prog='WorldScanner'
    )
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0')

    parser.add_argument('--region', action='store_true', help='search in region file')
    parser.add_argument('--player', action='store_true', help='search in player data file', default=True)
    parser.add_argument('--container', action='store_true', help='search in container in world')
    parser.add_argument('--tile-entity', action='store_true', help='search in title entities in world')
    parser.add_argument('--inventory', action='store_true', help='search in player''s inventory', default=True)
    parser.add_argument('--enderchest', action='store_true', help='search in player''s enderchest', default=True)

    parser.add_argument('--containers',
                        choices=['chest', 'trapped_chest', 'dropper', 'dispenser', 'hopper', 'armorstand', 'item',
                                 'furnace_minecart', 'chest_minecart', 'hopper_minecart', 'item_frame', '*'],
                        default='*', help='type of the container to search')
    parser.add_argument("--type", choices=['item', 'block', 'entity', 'enchantments', 'count', 'player'], type=str,
                        help='the type of think to search in region, player data or somewhere else')
    parser.add_argument('--count', type=int, default=1, help='minimum amount of item to get')

    needed_group = parser.add_argument_group('needed arguments')
    needed_group.add_argument('-w', '--world', type=str, help='path of the world''s folder')
    needed_group.add_argument('-id', '--id', action='extend', type=str, nargs="+",
                              help='list of item to search in the world')

    args = parser.parse_args()

    if not args.world or not args.id:
        parser.print_help()

    if not os.path.exists(args.world):
        parser.error('World not found !')

    player = Player(args)
    player.scan()


if __name__ == '__main__':
    main()
