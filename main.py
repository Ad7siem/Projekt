class Port():
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def __gt__(self, other):
        return self.nazwa > other.nazwa

    def __le__(self, other):
        return self.nazwa < other.nazwa


ports = [Port('waw'), Port('krk'), Port('gdn')]

routes = [(start, stop) for start in ports for stop in ports if start < stop]
for i in range(0, len(routes)):
    print(routes[i][0].nazwa + " " + routes[i][1].nazwa)

print("Moja głowa {}".format(14124))
