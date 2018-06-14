#imports
import Star as ST
import math
import random


class StarSystem(object):
#####Binary Star Info####
    #list of stars in the system
    Stars = []
    #number of stars
    Star_Count = 0
   #Barry Centre
    CenterOfMass = 0
    #eccentricity
    eccent = 0
    #max seperation
    MaxSep = 0
    #min seperation
    MinSep = 0

    #Forbidden Zone
    ForbidLim = 0

####System Info####
    #name
    Name = "Star System"
    #Luminocity
    Lum = 0
    #Mass
    Mass = 0
   #surface temp
    Temp = 0

    #outter orbit limit
    OuterLim = 0
    #frost Line
    FrostLine = 0

####Habitable Zone####
    #inner limit
    InnerHabit = 0
    #outter limit
    OuterHabbit = 0



    #constructor
    def __init__(self, stars):
        self.Stars = stars
        
        Star_Count = len(items)
        
        #calc System total values
        #Calc_SysTotals(stars)

    def __init__(self):
        #generate 1 or two stars
        star1 = ST.MakeRandomStar()
    
        #calc System total values
        #Calc_SysTotals(stars)

        #calulate stuff like habitable zone, and possible orbits
        #Calc_OrbitInfo()


    def Calc_SysTotals(self, stars):
        return

    def Calc_OrbitInfo(self):
        return



    
