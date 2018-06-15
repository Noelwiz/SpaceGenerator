#iimorts
import math
import random

class  Body(object):
    #name of the body
    Name = "name"
    #Mass
    Mass = 0
    #radius
    Rad = 0
    #density
    Density = 0
    #body orbted
    Orbiting = None
    #orbeted by
    OrbtedBy = None


    def __init__(self, mass, radius, orbiting, orbitedby):
        self.Mass = mass
        self.Rad = radius
        #mass / volume of a sphere, assumes perfect sphere
        self.Density = self.Mass / (4/3 * math.pi * (radius ** 3))
        self.Orbiting = orbiting
        self.OrbitedBy = orbitedby

##    def __equals__(self, other):
##        #test if both same type
##        #test if share name, check if masses are the same as well, or something
##        return True

    def __toStr__(self):
        return str(Name)

    def mass_ToStr(self):
        return str(self.Mass)+" Kg"

    def radius_ToStr(self):
        return str(self.Rad)+" Km" #meters?

    def density_ToStr(self):
        return str(self.Density) + " gm/cm^3"

    def orbiting_ToStr(self):
        return str(self.orbiting)

    def orbitedBy_ToStr(self):
        #might not work, or might want to custom make this
        return str(self.OrbitedBy)
        
    def set_Name(self, name):
        self.Name = name
        return

    def set_Mass(self, mass):
        self.Mass = mass
        return

    def set_Rad(self, radius):
        self.Rad = radius
        return

    def set_Orbiting(self, body):
        self.Orbiting = body
        return

    def set_OrbitedBy(self, body):
        if(OrbitedBy == None):
            self.OrbitedBy = body
            return
        #don't need to include else
        self.OrbitedBy.append(body)
        return


class Orbit(object):
    #Properties
    Radius = 0
    Eccentrricity = 0
