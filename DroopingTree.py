class DroopingTree:
    def __init__(self):
        self.has_vines = False

    def attach_vines(self):
        self.has_vines = True

    def is_overgrown(self):
        return self.has_vines

class Vines:
    def __init__(self):
        self.state = 'bare'

    def tangle(self, tree):
        if isinstance(tree, DroopingTree):
            tree.attach_vines()
            self.state = 'tangled'
            
    def overgrow(self, tree):
        if isinstance(tree, DroopingTree) and tree.is_overgrown():
            self.state = 'overgrown'
            
    def flourish(self, tree):
        if isinstance(tree, DroopingTree) and tree.is_overgrown():
            self.state = 'flourished'

class Gentleman:
    def __init__(self, tree, vines):
        self.tree = tree
        self.vines = vines

    def maintain(self):
        self.vines.tangle(self.tree)
        
    def manage(self):
        self.vines.overgrow(self.tree)

    def accomplish(self):
        self.vines.flourish(self.tree)

# Instantiate the elements
drooping_tree = DroopingTree()
vines = Vines()
gentleman = Gentleman(drooping_tree, vines)

# The gentleman starts to maintain the vines
gentleman.maintain()

# The gentleman manages the overgrown vines
gentleman.manage()

# The gentleman finally accomplishes the vine's flourishing
gentleman.accomplish()
