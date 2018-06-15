#stuff
import random
import math
import BaseClasses as Base


class Star(Base.Body, Base.Orbit):
    #mass, name, radius, density, body being orbited, and orbiting bodies inherited
    
    #color
    Color = "yellow"
    #star type
    Classification = '?'
    #Birth Date
    Birth = 0  #years ago
    #estimated Life
    Life = 0

    #Luminocity
    Lum = 0
   #surface temp
    SurfTemp = 0

    #inner orbital limit
    InnerLim = 0
    #outter orbit limit
    OuterLim = 0
    #frost Line
    FrostLine = 0

    ###Habitable Zone###
    #inner limit
    InnerHabit = 0
    #outter limit
    OuterHabbit = 0
    #is it habitable?
    Habitable? = False
    



    #constructer
    def __init__ (self, luminocity):
        self.lum = luminocity
        
        #CalcStuff(self)
        #end init

    def __init__(self, luminocity, mass, surftemp, radius):
        self.lum = luminocity
        self.mass = mass
        self.temp = surftemp
        self.rad = radius

        #CalcStuff(self)
        #end init

    #calc planet orbital distances for a solar system like clone
    def calcSolarOrbitDist(self):
        return

##    def MakeRandomStar(self):
##        luminocity = random.randrange(0,100)
##        #calc more stuff and rng a planet
##        return self
##
##    def CalcStuff(self):
##        #magic the planet into existance
##        return

    def calc_Lum(self):
        self.Lim = self.Mass ** 4 # * sun luminocity
        return

    #treat this like a static? 
    def calc_Lum(self, mass):
        return mass ** 4
    

    
