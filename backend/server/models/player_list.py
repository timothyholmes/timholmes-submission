class PlayerList:
    """Model for PlayerList"""

    def __init__(self, players):
        self.players = players

    def toJSON(self):
        return list(map(lambda player: player.toJSON(), self.players))

    def get_salaries(self):
        def price_map(price):
            numbers_only = list(filter(lambda x: x.isdigit(), list(price)))
            return int("".join(numbers_only))

        salaries = list(
            map(
                price_map,
                filter(
                    lambda salary: len(
                        list(filter(lambda x: x.isdigit(), list(salary)))
                    )
                    > 0,
                    map(lambda x: x.salary, self.players),
                ),
            ),
        )

        salaries.sort(reverse=True)

        return salaries
