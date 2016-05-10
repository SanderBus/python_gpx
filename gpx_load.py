import numpy
import matplotlib.pyplot as plt
import re
from scipy.ndimage.filters import gaussian_filter


def extract(data):
    lat_array = numpy.array([])
    lon_array = numpy.array([])
    elevation_array = numpy.array([])
    distance_array = numpy.array([])
    velocity_array = numpy.array([])
    acceleration_array = numpy.array([])
    
    temp = data.readline()
    
    while temp[0:7] != "<trkpt " and temp[6:13] != "<trkpt ":
        temp = data.readline()
    
    print temp
    while True:
        lonlat = re.findall("[-+]?\d+[\.]?\d*", temp)
        lat_array = numpy.append(lat_array,float(lonlat[0]))
        lon_array = numpy.append(lon_array,float(lonlat[1]))
        
        temp = data.readline()   #elevation
        elevation = re.findall("[-+]?\d+[\.]?\d*", temp)[0]
        print elevation
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
        
        if temp[0:13] == "    </trkseg>" or temp[0:9] == "</trkseg>":
            temp=data.readline() #<trkseg> or nothing
            if temp[0:12] != "    <trkseg>":
                break
            else:
                temp = data.readline() # lonlat

    velocity_array*=3.6
    return lat_array, lon_array, elevation_array, distance_array, velocity_array,acceleration_array

##A = open("lon.txt",'r')
#data_A = open("Groningen_20160307_091305.gpx",'r')
#data_B = open("Haren_20160307_195303.gpx",'r')


#lat_array_A, lon_array_A, elevation_array_A, distance_array_A, velocity_array_A,acceleration_array_A = extract(data_A)
#lat_array_B, lon_array_B, elevation_array_B, distance_array_B, velocity_array_B,acceleration_array_B = extract(data_B)

#plt.figure()
#plt.plot(lon_array_A,lat_array_A,'-')
#plt.plot(lon_array_B,lat_array_B,'-')
#plt.axes().set_aspect('equal')


#plt.figure()
#plt.plot(distance_array_A,velocity_array_A,'.')
#plt.plot(distance_array_A,gaussian_filter(velocity_array_A,3),'-')
#plt.plot(distance_array_A,gaussian_filter(velocity_array_A,10),'-.')
#plt.plot(distance_array_A,gaussian_filter(velocity_array_A,25),'--')

#plt.plot(distance_array_B,velocity_array_B,'.')
#plt.plot(distance_array_B,gaussian_filter(velocity_array_B,3),'-')
#plt.plot(distance_array_B,gaussian_filter(velocity_array_B,10),'-.')
#plt.plot(distance_array_B,gaussian_filter(velocity_array_B,25),'--')
#plt.show()
    
  