

class Vehicule:
    def __init__(self):
        print ("init Vehicule")

class Camion(Vehicule):
    def __init__(self):
        print ("init Camion")

class Voiture(Vehicule):
    def __init__(self):
        print ("init Voiture")

class Transport(Voiture, Camion):
    def __init__(self):
        print ("init Transport")
