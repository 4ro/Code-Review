class Ship:
    def __init__(self,draft,crew):
        self.draft=draft
        self.crew=crew

    def is_worth_it(self):
        amt = self.crew*1.5
        if (self.draft-amt)>=20:
            return True
        else:
            return False

Titanic = Ship(900,50)
print(Titanic.is_worth_it())
