import numpy
import re

def extract(data):
    lat_array = numpy.array([])
    lon_array = numpy.array([])
    elevation_array = numpy.array([])
    distance_array = numpy.array([])
    velocity_array = numpy.array([])
    acceleration_array = numpy.array([])
    
    temp = data.readline()
    
    while "<trkpt " not in temp:
        temp = data.readline()
    
    while True:
        lonlat = re.findall("[-+]?\d+[\.]?\d*", temp)
        lat_array = numpy.append(lat_array,float(lonlat[0]))
        lon_array = numpy.append(lon_array,float(lonlat[1]))
        
        temp = data.readline()   #elevation
        elevation = re.findall("[-+]?\d+[\.]?\d*", temp)[0]
        elevation_array = numpy.append(elevation_array, float(elevation))
    
        temp = data.readline() #time
        temp = data.readline() #extensions
        temp = data.readline() #distance m
        distance = re.findall("[-+]?\d+[\.]?\d*", temp)[0]
        distance_array = numpy.append(distance_array, float(distance))
        
        temp = data.readline() #speed m/s
        velocity = re.findall("[-+]?\d+[\.]?\d*", temp)[0]
        velocity_array = numpy.append(velocity_array, float(velocity))
    
        temp = data.readline() #course 
        temp = data.readline() #acceleration m/s**2
        acceleration = re.findall("[-+]?\d+[\.]?\d*", temp)[0]
        acceleration_array = numpy.append(acceleration_array,float(acceleration))
        
        temp = data.readline() #/extensions
        temp = data.readline() #</trkpt>
        temp = data.readline() # lonlat or </trkseg>
        
        if "</trkseg>" in temp:
            temp=data.readline() #<trkseg> or nothing
            if "<trkseg>" not in temp:
                break
            else:
                temp = data.readline() # lonlat

    velocity_array*=3.6
    return lat_array, lon_array, elevation_array, distance_array, velocity_array,acceleration_array