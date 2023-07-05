class GeTan:
    def __init__(self):
        self.status = "In the Valley"
        self.leaf = "Flourishing"
        self.bird = "Yellow Bird"
        self.noise = "Chirping"
        self.bird_in_bushes = False
        self.cleanliness = "Dirty"
        self.family = None

    def spread(self):
        self.status = "Spread in the Valley"
        self.bird_in_bushes = False

    def fly_yellow_bird(self):
        self.bird_in_bushes = True

    def chirp(self):
        return self.noise if self.bird_in_bushes else "Silent"

    def harvest(self):
        self.leaf = "Harvested"

    def inform_teacher(self, teacher):
        teacher.receive_message_from(self)

    def return_home(self, family):
        self.family = family
        self.cleanliness = "Clean"
        family.welcome(self)


class Teacher:
    def receive_message_from(self, ge_tan):
        print("Received message from Ge Tan.")


class Family:
    def welcome(self, ge_tan):
        print("Welcome back, Ge Tan.")


ge_tan = GeTan()
teacher = Teacher()
family = Family()

# Ge Tan spreads in the valley
ge_tan.spread()
# Yellow bird flies
ge_tan.fly_yellow_bird()
# Ge Tan is harvested
ge_tan.harvest()
# Ge Tan informs the teacher
ge_tan.inform_teacher(teacher)
# Ge Tan returns home
ge_tan.return_home(family)
