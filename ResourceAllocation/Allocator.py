import fiona
import math
FOOTTRAFICWEIGHT = 20.9

def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist


#open sidewalk and mbta datasets
with fiona.open("./Sidewalks_/Sidewalks_.shp", 'r') as city:
    with fiona.open("./mbta_rapid_transit/MBTA_ARC.shp") as mbta:
        for sidewalk in city:
            #find center of sidewalk
            try:
                g = sidewalk['geometry']
                cords = g['coordinates']
                x = [float(p[0]) for p in cords[0]]
                y = [float(p[1]) for p in cords[0]]
                sidewalkCentroid = (sum(x)/len(cords),sum(y)/len(cords))
                print(sidewalkCentroid)
            except:
                continue

            #find foot score for each sidewalk (proximity to frequently used area)
            footScore = 0
            closestStop = (-1,-1)
            for stop in mbta:
                try:
                    #find center of mbta stop
                    mg = stop['geometry']
                    mcords = mg['coordinates']
                    x = [float(p[0]) for p in mcords]
                    y = [float(p[1]) for p in mcords]
                    stopCentroid = (sum(x)/len(mcords),sum(y)/len(mcords))
                    if(closestStop==(-1,-1)):
                        closestStop = stopCentroid

                except:
                    1;
