class Sport:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return f"This is {self.name}"

    def __add__(self, other):
        raise TypeError("Not Possible")

    def __sub__(self, other):
        raise TypeError("Not Possible")


class Football(Sport):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def __str__(self):
        return f"This is {self.name} team, matched with teams: {', '.join(self.team)}"

    def __eq__(self, other):
        if isinstance(other, Football):
            return self.name == other.name and self.team == other.team
        return False

    def __sub__(self, other):
        if isinstance(other, Football):
            shared_teams = list(set(self.team) & set(other.team))
            if shared_teams:
                return Football(f"{self.name}: ", shared_teams)
            else:
                return f"No common teams between them"
        return "Not possible"


class Basketball(Sport):
    def __init__(self, name, team):
        super().__init__(name)
        self.team = team

    def __str__(self):
        return f"This is {self.name} team, matched with teams: {', '.join(self.team)}"

    def __eq__(self, other):
        if isinstance(other, Basketball):
            return self.name == other.name and self.team == other.team
        return False

    def __sub__(self, other):
        if isinstance(other, Basketball):
            shared_teams = list(set(self.team) & set(other.team))
            if shared_teams:
                return Basketball(f"{self.name}: ", shared_teams)
            else:
                return f"No common teams between them"
        return "Not possible"


basic = Sport("super basic!")
print(basic)

football1 = Football("Football", ["Giants", "Dolphins"])
football2 = Football("Football", ["Steelers", "Eagles"])

basketball1 = Basketball("Basketball", ["Kings", "Rockets"])
basketball2 = Basketball("Basketball", ["Jazz", "Kings"])

print(football1)
print(basketball1)


print(football1 == football2)

print(basketball1 - basketball2)