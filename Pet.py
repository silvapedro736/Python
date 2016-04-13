class Pet:
    def __init__(self,petname,petspecies):
        self.name=petname
        self.species=petspecies

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def speak(self):
        if self.species == "dog" or "Dog":
            print "Woof"
        else:
            if self.species =="cat":
                print "Meow"

            else:
                print "No Animal"

    def intro(self):

        print


p1 = Pet("Puppy", "Dog")
#print p1.getname() + " is a " + p1.getSpecies()
#print p1
p1.speak()
