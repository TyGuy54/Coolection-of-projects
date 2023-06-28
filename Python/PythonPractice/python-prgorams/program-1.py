class ListOfStuff:
    def __init__(self):
        self.list_of_stuff = []
    
    def add_to_list(self):
        while len(self.list_of_stuff) < 5:
            if len(self.list_of_stuff) >= 5:
                break
            elif len(self.list_of_stuff) <= 5:
                user_input = input("Add an item to a list: ")

                self.list_of_stuff.append(user_input)
                print(f'This is your final list: {self.list_of_stuff}')


def main():
    list_of_stuff = ListOfStuff()
    list_of_stuff.add_to_list()

if __name__ == '__main__':
    main()