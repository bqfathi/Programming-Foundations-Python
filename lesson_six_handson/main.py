#Part 1 

class Stadium:
    """This is a doc string for Stadium"""
    def __init__(self, name, city_state, capacity, sport, seats):
        self.name = name #The name of the stadium
        self.city_state = city_state #the City and State where the stadium is
        self.capacity = capacity #how many people can fit in the stadium
        self.sport = sport #the main sport played in the stadium
        self.seats = seats #the number of available seats
    
    def describe_stadium(self):
        print("The " + self.name + " stadium is in " + self.city_state + " and holds " + self.capacity + " fans.")
    
    def sport_played(self):
        print("The following sport is mainly played in this stadium: " + self.sport)
    
    def seats_available(self):
        print("There are " + self.seats + " still available for tonight's game.")

stadium1 = Stadium("Merecedes Benz Arena", "Atlana, GA", "70,000", "Football", "15,000")

stadium1.describe_stadium()
stadium1.sport_played()
stadium1.seats_available()


#Part 2


