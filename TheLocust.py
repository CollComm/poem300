class Locust:
    def __init__(self):
        self.feathers = "Fluttering"
    
    def action(self):
        return "Fly"


class Offspring:
    def __init__(self):
        self.state = "Stable"
    
    def activity(self):
        return "Strive"


class Prosperity:
    def __init__(self, locust, offspring):
        self.locust = locust
        self.offspring = offspring

    def achieve(self):
        locust_action = self.locust.action()
        offspring_activity = self.offspring.activity()
        if locust_action == "Fly" and offspring_activity == "Strive":
            return True
        else:
            return False

locust = Locust()
offspring = Offspring()
prosperity = Prosperity(locust, offspring)
print(prosperity.achieve())  # Should print: True
