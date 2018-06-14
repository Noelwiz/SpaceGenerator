#stuff
import random
import math


class Star(object):
    #name
    Name = "Star"
    #color
    Color = "yellow"
    #star type
    StarType =k
    #Birth Date
    Birth = 0  #years ago
    #estimated Life
    Life = 0

    #Luminocity
    Lum = 0
    #Mass
    Mass = 0
   #surface temp
    Temp = 0
    #radius
    Rad = 0

    #outter orbit limit
    OuterLim = 0
    #frost Line
    FrostLine = 0

    ###Habitable Zone###
    #inner limit
    InnerHabit = 0
    #outter limit
    OuterHabbit = 0
    



    #constructer
    def __init__ (self, luminocity):
        self.lum = luminocity
        
        CalcStuff(self)
        #end init

    def __init__(self, luminocity, mass, surftemp, radius):
        self.lum = luminocity
        self.mass = mass
        self.temp = surftemp
        self.rad = radius

        CalcStuff(self)
        #end init

    def MakeRandomStar(self):
        luminocity = random.randrange(0,100)
        #calc more stuff and rng a planet
        return self

    def CalcStuff(self):
        #magic the planet into existance
        return
        

    
