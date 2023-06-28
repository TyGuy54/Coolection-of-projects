import sys
import yaml

class Factory():
    def __init__(self, name, _type, level, _list):
        self.name = name
        self.type = _type
        self.level = level
        self.demon_list = _list

    def create_demon_obj(self) -> dict:
        demon_obj = {}

        demon_obj['name1'] = demon_obj[0].strip()
        # names_dict['name2'] = names_list[1].strip()

        # res1 = dict(list(names_dict.items())[len(names_dict)//2:])
        # res2 = dict(list(names_dict.items())[:len(names_dict)//2])

    def create(self) -> str:
        pass


def commands(command: str) -> str:
    match command.split():
        case ["demon-name", demon_name]:
            return demon_name
        case ["help" | "--help" | "--h"]:
            return "commands: demon-name [NAME]"
        case["quit" | "exit"]:
            print("Exiting Program")
            sys.exit(0)
        case _:
            print("command not found")


def fuse_names() -> None:
    names_list = []
    names_dict = {}

    while len(names_list) < 2:
        command = input("$ ")

        get_name = commands(command)
        names_list.append(get_name)

    names_dict['name1'] = names_list[0].strip()
    names_dict['name2'] = names_list[1].strip()

    res1 = dict(list(names_dict.items())[len(names_dict)//2:])
    res2 = dict(list(names_dict.items())[:len(names_dict)//2])

    print(res1)
    print(res2)
    

def main() -> None:
    fuse_names()

if __name__ == '__main__':
    main()