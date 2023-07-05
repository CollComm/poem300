class Bird:
    def __init__(self, species):
        self.species = species

    def sing(self):
        return f"The {self.species} sings beautifully on the isle in the river."


class Vegetation:
    def __init__(self, name):
        self.name = name

    def grow_and_flow(self):
        return f"The {self.name} grows unevenly, flowing to left and right."

    def be_picked(self):
        return f"The {self.name} is picked from left and right."

    def blossom(self):
        return f"The {self.name} blossoms unevenly, on both left and right."


class Lady:
    def __init__(self, qualities):
        self.qualities = qualities

    def describe(self):
        return f"A lady, graceful and virtuous."

    def seek(self):
        return f"The lady seeks in dreams and thoughts but fails to find."

    def restlessness(self):
        return f"She is restless, rolling and turning in bed."

    def enjoy_music(self, instruments):
        return f"The lady enjoys the music of {', '.join(instruments)}."


class Love:
    def __init__(self, gentleman, lady):
        self.gentleman = gentleman
        self.lady = lady

    def perfect_match(self):
        return f"{self.lady.describe()}, a perfect match for the gentleman."


bird = Bird('Turtledove')
print(bird.sing())

lady = Lady(['graceful', 'virtuous'])
print(lady.describe())

love = Love('gentleman', lady)
print(love.perfect_match())

vegetation = Vegetation('water plants')
print(vegetation.grow_and_flow())
print(lady.seek())
print(lady.restlessness())

print(vegetation.be_picked())
instruments = ['zither', 'bells', 'drum']
print(lady.enjoy_music(instruments))

print(vegetation.blossom())
