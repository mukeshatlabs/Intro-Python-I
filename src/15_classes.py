# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lt=0, ln=0):
        self.lat = lt
        self.lon = ln
    def get_data(self):
        print(f'Lat is {self.lat} and Long is {self.lon}')
    def __str__(self):
        return(f'Lat is {self.lat} and Long is {self.lon}')


# myLoc = LatLon(10,20)
# myLoc.get_data()

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, name = "", lt=0, ln=0):
        super().__init__(lt, ln)
        self.name = name
    def get_data(self):
        print(f'Name is {self.name},  Lat is {self.lat} ,and Long is {self.lon}')
    def __str__(self):
        return(f'Name is {self.name},  Lat is {self.lat} ,and Long is {self.lon}')
# myWayPoint = Waypoint("SF", 10, 20)
# myWayPoint.get_data()

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name = "", difficulty=0, size=0, lt=0, ln=0):
        super().__init__(name, lt, ln)
        self.difficulty = difficulty
        self.size = size
    def get_data(self):
        print(f'Name is {self.name}, Difficulty is {self.difficulty}, Size is {self.size}, Lat is {self.lat} ,and Long is {self.lon}')
    def __str__(self):
        return(f'Name is {self.name}, Difficulty is {self.difficulty}, Size is {self.size}, Lat is {self.lat} ,and Long is {self.lon}')
# myGeocache = Geocache("SF",1,2, 10, 20)
# myGeocache.get_data()

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint("Catacombs", 41.70505, -121.51521)
print(waypoint)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
# print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print(geocache)
# Print it--also make this print more nicely
# print(geocache)
