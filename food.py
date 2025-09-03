class Menu:
    def __init__(self):
        self.items = [
            "Chicken Alfredo",
            "Spaghetti with Meatballs",
            "Baked Ziti",
            "Chicken Carbonara"
        ]

    def displayMenu(self):
        print("Today's Menu:\n")
        for item in self.items:
            print(item)


menu = Menu()
menu.displayMenu()