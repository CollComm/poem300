class PeachTree:
    def __init__(self):
        self.flourishing = False
        self.fruitful = False
        self.leaves = False

    def blossom(self):
        self.flourishing = True

    def bear_fruit(self):
        if self.flourishing:
            self.fruitful = True

    def grow_leaves(self):
        if self.fruitful:
            self.leaves = True


class Son:
    def __init__(self):
        self.home = Home()

    def return_home(self):
        if self.home.check_condition():
            return True
        else:
            return False


class Home:
    def __init__(self):
        self.peach_tree = PeachTree()

    def check_condition(self):
        if self.peach_tree.flourishing and self.peach_tree.fruitful and self.peach_tree.leaves:
            return True
        else:
            return False

    def welcome_son(self, son):
        if son.return_home():
            return True
        else:
            return False


# Initialize the objects
my_home = Home()
my_son = Son()

# The peach tree blooms, bears fruit, and grows leaves
my_home.peach_tree.blossom()
my_home.peach_tree.bear_fruit()
my_home.peach_tree.grow_leaves()

# The son returns home
my_home.welcome_son(my_son)
