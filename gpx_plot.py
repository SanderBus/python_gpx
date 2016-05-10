import matplotlib.pyplot as plt
import numpy
from gpx_load import extract
from scipy.ndimage.filters import gaussian_filter

data = open("Bodenwerder_20160503_153749.gpx",'r')
lat_array, lon_array, elevation_array, distance_array, velocity_array,acceleration_array = extract(data)


plt.figure()
plt.plot(lon_array,lat_array,'-')
plt.axes().set_aspect('equal')

plt.figure()
plt.plot(distance_array,velocity_array,'.')
plt.plot(distance_array,numpy.mean(velocity_array)*numpy.ones(len(distance_array)))
plt.plot(distance_array,gaussian_filter(velocity_array,3),'-')

percentage = 100*1000*(elevation_array[:-1] - elevation_array[1:])/numpy.where(distance_array[:-1] - distance_array[1:]<0.00001,10000.,distance_array[:-1] - distance_array[1:])

plt.figure()
plt.plot((distance_array[:-1] + distance_array[1:])/2,gaussian_filter(percentage,3))

plt.show()

