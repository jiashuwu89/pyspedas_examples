# # Swarm magnetometer data in PySPEDAS
# 
# This notebook shows how to load and plot Swarm magnetometer data using PySPEDAS. 
# 
# Note: we're using the HAPI load routine in PySPEDAS to access the data from the Swarm HAPI server. For more in-depth access to Swarm data products in Python, please see the official Python client: 
# 
# https://swarm.magneticearth.org/docs/welcome.html

!pip install pyspedas

# Get started by importing PySPEDAS:

import pyspedas

# Load 2-hours of magnetometer data from probe 'a' on March 27, 2017

pyspedas.swarm.mag(probe='a', 
                   trange=['2017-03-27/06:00', '2017-03-27/08:00'], 
                   datatype='hr')

# Create a figure showing the data for probe 'a'

from pytplot import tplot

tplot('swarma_B_VFM', var_label=['swarma_Latitude', 'swarma_Longitude'])



