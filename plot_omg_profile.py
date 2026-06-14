
import os
import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc4
import warnings
warnings.filterwarnings('ignore')

file_name = 'OMG_Ocean_AXCTD_L2_20210906135507.nc'


# read in the data

ds = nc4.Dataset(os.path.join('data',file_name))
temperature = ds.variables['temperature'][0,:]
salinity = ds.variables['salinity'][0,:]
depth = ds.variables['depth'][0,:]
ds.close()

# make the plot

fig = plt.figure(figsize=(8,5))

plt.suptitle('OMG AXCTD Profile: '+file_name)

plt.subplot(1,2,1)
plt.plot(temperature, depth, 'r-')
plt.gca().invert_yaxis()
plt.xlabel('Temperature (°C)')
plt.ylabel('Depth (m)')

plt.subplot(1,2,2)
plt.plot(salinity, depth, 'b-')
plt.gca().invert_yaxis()
plt.xlabel('Salinity (kg/kg)')

plt.tight_layout()

plt.show()




