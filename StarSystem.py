#imports
import Star as ST
import math
import random

class StarSystem(ST.Star):
#####Binary Star Info####
    #type, 'P' or 'S'
    Type = None
    #list of stars in the system
    Stars = None
    #number of stars
    Star_Count = 0
    #eccentricity of the stars
    #seperate from the Base.Orbit because it should be different from the property inherited maybe
    SystemEccent = 0
    #max seperation
    MaxSep = 0
    #min seperation
    MinSep = 0

    #Forbidden Zone
    ForbidInnerLim = 0
    ForbidOutterLim = 0


    #constructor
    def __init__(self, stars):
        self.Stars = stars
        #add the berry center distince property to both stars
        
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



    
