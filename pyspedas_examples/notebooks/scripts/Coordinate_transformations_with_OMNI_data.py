# # Coordinate transformations with OMNI data
# 
# **By Eric Grimes, UCLA - Earth, Planetary, and Space Sciences; egrimes(at)igpp.ucla.edu**
# 
# This notebook shows how to load OMNI data, combine the B-field components into a single variable, then use `cotrans` to transform the data to GSM coordinates, and finally plot the B-field in GSE and GSM coordinates

!pip install pyspedas

import pyspedas

# Load some OMNI data; we'll transform the B-field from GSE coordinates to GSM coordinates

pyspedas.omni.data(trange=['2015-10-16', '2015-10-17'])

# The B-field components are stored as separate variables; to transform them using `cotrans`, we'll need to combine them into a single variable. We'll use `join_vec` from `pytplot` to do this:

from pytplot import join_vec

join_vec(['BX_GSE', 'BY_GSE', 'BZ_GSE'], new_tvar='B_GSE')

# Now we can transform `B_GSE` to GSM coordinates using `cotrans`

from pyspedas import cotrans

cotrans(name_in='B_GSE', name_out='B_GSM', coord_in='gse', coord_out='gsm')

# Set some plot metadata on our new variables

from pytplot import options

options('B_GSE', 'ytitle', 'OMNI B-field')
options('B_GSE', 'ysubtitle', '[nT]')
options('B_GSE', 'legend_names', ['Bx GSE', 'By GSE', 'Bz GSE'])

options('B_GSM', 'ytitle', 'OMNI B-field')
options('B_GSM', 'ysubtitle', '[nT]')
options('B_GSM', 'legend_names', ['Bx GSM', 'By GSM', 'Bz GSM'])

# Now we can plot the B-field in GSE and GSM coordinates

from pytplot import tplot

tplot(['B_GSE', 'B_GSM'])



