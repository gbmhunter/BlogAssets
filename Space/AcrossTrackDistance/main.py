# Script to calculate nadir-to-target ground distances in the across track direction
# for a satellite, using both a flat earth and spherical earth approximation

import math
import matplotlib
import matplotlib.pyplot as plt

# fig1 = plt.figure()

# SPHERICAL APPROXIMATION

thetaSat_deg = 35.0 # Roll-angle of satellite w.r.t nadir. Flat earth approximation performs poorer with larger angle.
thetaSat_rad = math.radians(thetaSat_deg)

# The higher the satellite, the poorer the performance of the flat earth approximation
satAltitude_m  = 800000.0 

earthRadius_m = 6371000.0

# Use law of sin to calculate angle at surface.
# NOTE that this is the ambiguous case! We have to subtract pi from the answer otherwise the law of sin gives
# us the wrong answer
thetaSurface_rad = math.pi - math.asin(((earthRadius_m + satAltitude_m)*math.sin(thetaSat_rad))/earthRadius_m)

print('thetaSurface (deg) = ' + str(math.degrees(thetaSurface_rad)))

thetaEarth_rad = math.pi - thetaSat_rad - thetaSurface_rad

print('thetaEarth (deg) = ' + str(math.degrees(thetaEarth_rad)))

# d = R*thetaEarth
acrossTrackDistance_m = earthRadius_m*thetaEarth_rad

print('acrossTrackDistance_m = ' + str(acrossTrackDistance_m))

# FLAT EARTH APPROXIMATION

# distance = altitude*tan(satTheta)
acrossTrackDistanceFlatEarth_m = satAltitude_m*math.tan(thetaSat_rad)

print('acrossTrackDistanceFlatEarth_m = ' + str(acrossTrackDistanceFlatEarth_m))

# COMPARE SHPERICAL WITH FLAT EARTH

error_perc = (math.fabs(acrossTrackDistanceFlatEarth_m - acrossTrackDistance_m)/acrossTrackDistance_m)*100.0

print('error_perc = ' + str(round(error_perc, 2)))