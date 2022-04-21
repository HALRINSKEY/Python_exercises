class Rider():
    def __init__(self, n):
        self.name_rider = n


class Horse():
    def __init__(self, n, rider):
        self.name = n
        self.rider = rider

the_rider = Rider("Sally")
harry_the_horse = Horse("Harry", the_rider)

print("The name of Horse is {}".format(harry_the_horse.name))
print("The name of Rider is {}".format(harry_the_horse.rider.name_rider))
