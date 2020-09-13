class Player:
    """Model for player"""

    def __init__(self, name, salary, year, level):
        self.name = name
        self.salary = salary
        self.year = year
        self.level = level

    def toJSON(self):
        return {
            "name": self.name,
            "salary": self.salary,
            "year": self.year,
            "level": self.level,
        }
