#iimorts
import math
import random
from astropy import units as U

#TODO, check if these exist in astropy already
#constants
LunarMass = 734200000000000000000000 * U.kg
LunarRad = 1738.1 * 1000 * U.m
EarthGravety = 9.8 * U.m / (U.s**2)
EarthEscapeVel = 11186 * U.m / (U.s**2)
LifeTimeOfSun = 10000000000000 * U.year
SunSurfaceTemp = 5772 U.K



class Body(object):
    """A generic Body type for astrological bodies
    Functions for getting atributes as a string, and calculating/recalculating values
    uses astropy for units"""
    #name of the body
    Name = "name"
    #Mass
    Mass = 0 * U.kg
    #radius
    Rad = 0
    #density
    Density = 0 * U.kg / (U.m ** 3)
    #body orbted
    Orbiting = None
    #orbeted by
    OrbtedBy = None
    #is orbeted by anything?
    IsOrbited = False
    #Number of things orbiting this
    NumOrbiting = 0
    #escape velocity
    EscapeVelocity = 0 * U.m / U.second

    #TODO: calc escape velocity, check for units on numbers incomging
    def __init__(self, mass, radius, orbiting, orbitedby, name):
        """Initalize a body
        Mass, Radius, The body it orbits, orbiting bodies, name)
        sets the given values, then calulates the rest
        """
        self.Name = name
        self.Mass = mass
        #check if Mass has units of kg yet or not
        #code
        self.Rad = radius
        #mass / volume of a sphere, assumes perfect sphere
        self.calc_Density()
        self.Orbiting = orbiting
        self.OrbitedBy = orbitedby
        if (orbitedby == None):
            self.IsOrbited = False
        else:
            self.IsOrbited = True
            self.NumOrbiting = len(self.OrbtedBy)
        #calc escape velocity
        

    def __equals__(self, other):
        #test if both same type
        if(! (typeof(self) == typeof(other)) ):            
            #test if share name, check if masses are the same as well, or something
            return( (self.Name == other.Name) and (self.Mass == other.Mass) #hopefully this checks regardless of units
        #else
        return False

    def __toStr__(self):
        """Return the name of the body as a string
        Mostly for consistancy since it should already be a string
        also, it stops acadental name changes due to object references
        """
        return str(Name)

    def mass_ToStr(self):
        """Return the mass as a string, with units"""
        return str(self.Mass)

    def radius_ToStr(self):
        """Returns the Radius as a string, with units"""
        return str(self.Rad)+" Km" #meters?

    def density_ToStr(self):
        """Returns the Density as a string, with units"""
        return str(self.Density)

    def orbiting_ToStr(self):
        """Returns the name of the planet being orbited as a string"""
        return str(self.orbiting)

    def orbitedBy_ToStr(self):
        """Returns the list of names of bodies orbiting as a string"""
        #might not work, or might want to custom make this
        return str(self.OrbitedBy)

    def calc_Density(self):
        self.Density = self.Mass/(math.pi*(4/3)*(self.Rad**3))
        return

    def add_Satellite(self, body):
        self.NumOrbiting++
        if (self.OrbtedBy == None):
            self.OrbtedBy = [body]
        else:
            self.OrbtedBy.append(body)
            NumOrbiting = len(orbitedby)

        assert(self.OrbtedBy != None)
        return



class Orbit(object):
    #Properties
    SemiMajorAxis = 0 * U.AU
    Eccentrricity = 0
    Pitch = 0 * U.deg
    Yaw = 0 * U.deg
    Roll = 0 * U.deg
    TrueAnomoly = 0 * U.deg

    #TODO check if numbers already have appropriate units
    def __init__(semimajor, eccentricity, pitch, yaw, roll, trueAnomoly):
        SemiMajorAxis = semimajor
        Eccentrricity = eccentricity
        Pitch = pitch
        Yaw = yaw
        Roll = roll
        TrueAnomoly = trueAnomoly

    #any thing else


