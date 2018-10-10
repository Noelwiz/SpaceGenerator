#imports
import math
import random
import BaseClasses as Base


class Planet(Base.Body, Base.Orbit):
    #gravety on the surface, should be null for gas giants
    SurfaceGravity = 0 *U.m / (U.second **2)

    #unclear
    #Dist_To_Body = 0

    #bool, true if planet is a gas giant
    GasGiant = False

    #bool indicates if tidally locked to another body
    TidalLock = False
    #LockedBody = otherplanet

    #rotational speed
    Rotational_Speed = 0

    

####habitablity####
    Habitable = False

    Axial_Tilt = 0 * U.deg

    Surface_Temp = 0
    
    
