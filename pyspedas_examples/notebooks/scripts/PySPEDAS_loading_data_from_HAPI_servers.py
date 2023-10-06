# # Loading data from HAPI servers with PySPEDAS
# 
# This notebook shows how to load data from HAPI servers using PySPEDAS
# 
# Originally created at the 2022 PyHC Spring Meeting Hackathon

!pip install pyspedas

import pyspedas

# To see the available options:

help(pyspedas.hapi.hapi.hapi)

# To see the available datasets, set the `catalog` keyword:

pyspedas.hapi.hapi.hapi(trange=['2015-10-16', '2015-10-17'], 
                        server='https://cdaweb.gsfc.nasa.gov/hapi', 
                        catalog=True)

# Load some RBSP magnetometer data

opts = {'trange': ['2015-10-16', '2015-10-17'],
        'server': 'https://cdaweb.gsfc.nasa.gov/hapi'}

pyspedas.hapi.hapi.hapi(**opts, dataset='RBSP-A_MAGNETOMETER_1SEC-SM_EMFISIS-L3')

# Plot the B-field magnitude and vector:

from pytplot import tplot
tplot(['Magnitude', 'Mag'])



