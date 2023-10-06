# # pySPEDAS 1.0 Tutorial
# 
# Eric Grimes
# 
# egrimes@igpp.ucla.edu
# 
# # Introduction
# 
# ### Requirements
# 
# - Python 3.5 or later
# 
# ### All of this depends on the hard work of the pyTplot developers at LASP
# To learn more about pytplot:
# 
# https://pytplot.readthedocs.io/
# 
# ### Virtual Environments
# - Best to use them to avoid dependency issues; Python 3.5 and later make creating a virtual environment as simple as:
# 
# `python -m venv pyspedas-tutorial`
# 
# Then, to run the virtual environment, on Windows:
# 
# `.\pyspedas-tutorial\Scripts\activate`
# 
# and on macOS / Linux:
# 
# `source pyspedas-tutorial/bin/activate`
# 
# To exit the current virtual environment, type `deactivate`
# 
# ### Installing pySPEDAS
# 
# In your virtual environment, type:
# 
# `pip install pyspedas`
# 
# ### Upgrade pySPEDAS
# 
# `pip install pyspedas --upgrade`
# 
# ### pySPEDAS on GitHub
# 
# https://github.com/spedas/pyspedas
# 
# ### Problems with Anaconda
# 
# Note: if you have trouble creating a virtual environment or installing pyspedas and are using Anaconda, try to update Anaconda in your terminal with the command:
# 
# `conda update --all`

# # Getting Started
# 
# ### Structure of the load routines
# The structure of the load routines follow:
# 
#     pyspedas.mission.instrument()
# 
# e.g., 
# 
#     pyspedas.mms.fgm()
# 
# Data options are set via keywords passed to the load routines; e.g., 
# 
#     pyspedas.mms.fgm(trange=['2015-12-15', '2015-12-16'])
# 
# these have defaults which should load some default data. 
# 
# These functions return the names of the tplot variables created. Note: some options change the return values, e.g., setting `notplot=True` will tell the load routine to return the variables in hash tables containing numpy arrays; `downloadonly=True` will return the names of the files downloaded.
# 
# ### Local data directory
# 
# Your data directory can be set using the `SPEDAS_DATA_DIR` environment variable. Each mission also has its own data directory, e.g., `MMS_DATA_DIR`, `THM_DATA_DIR`, etc. Note: mission data directories will override the root data directory set in `SPEDAS_DATA_DIR`.
# 
# ### Importing pySPEDAS
# To get started, import pyspedas:
# 

import pyspedas

# You can also access the load routines by importing the mission modules:

from pyspedas import mms, themis, cluster

# This allows you to load data via mms.fgm(trange=[...])
# 
# You can also import the instrument load routines, e.g.:

from pyspedas.mms import fgm, fpi
from pyspedas.themis import esa, sst

# # Projects Supported
# 
# - Advanced Composition Explorer (ACE)
# - Arase (ERG) - note: experimental!
# - Cluster
# - Colorado Student Space Weather Experiment (CSSWE)
# - Deep Space Climate Observatory (DSCOVR)
# - Equator-S
# - Fast Auroral Snapshot Explorer (FAST)
# - Geotail
# - Geostationary Operational Environmental Satellite (GOES)
# - Imager for Magnetopause-to-Aurora Global Exploration (IMAGE)
# - Mars Atmosphere and Volatile Evolution (MAVEN)
# - Magnetic Induction Coil Array (MICA)
# - Magnetospheric Multiscale (MMS)
# - OMNI
# - Polar Orbiting Environmental Satellites (POES)
# - Polar
# - Parker Solar Probe (PSP)
# - Van Allen Probes (RBSP)
# - Solar Terrestrial Relations Observatory (STEREO)
# - Time History of Events and Macroscale Interactions during Substorms (THEMIS)
# - Two Wide-Angle Imaging Neutral-Atom Spectrometers (TWINS)
# - Ulysses
# - Wind

# To find the available options in a load routine, call the help() function on the load routine

help(pyspedas.mms.fpi)

help(esa)

# # Loading Data
# ### Magnetospheric Multiscale (MMS) Mission
# To load 6 hours of MMS FGM data on Oct 16, 2015:

data = pyspedas.mms.fgm(trange=['2015-10-16/6:00', '2015-10-16/12:00'], time_clip=True)

data

# To list the tplot variables loaded, use `tplot_names` from `pytplot`

from pytplot import tplot_names

tplot_names()

# To plot a variable, import `tplot` from pytplot

from pytplot import tplot

tplot('mms1_fgm_b_gse_srvy_l2')

# `tplot` also accepts a list of variable names, e.g.,

tplot(['mms1_fgm_b_gse_srvy_l2', 'mms1_fgm_b_gsm_srvy_l2'], save_png='/path/to/filename')

# To load MMS FPI burst-mode electron energy spectra (from the moments CDFs)

pyspedas.mms.fpi(trange=['2015-10-16/13:06', '2015-10-16/13:07'], data_rate='brst', datatype='des-moms')

tplot(['mms1_des_energyspectr_omni_brst', 'mms1_des_energyspectr_perp_brst', 'mms1_des_energyspectr_par_brst'])

# ### Time History of Events and Macroscale Interactions during Substorms (THEMIS)
# 
# To load THEMIS search-coil magnetometer (SCM) data:

pyspedas.themis.scm(probe='d', trange=['2016-10-16', '2016-10-17'])

tplot(['thd_scf_gse', 'thd_scf_gsm'])

# The plot metadata can be updated with `options` fron `pytplot`

from pytplot import options

# To find the available options, run the help() function on the options function after importing it

help(options)

# Set the label names

options('thd_scf_gsm', 'legend_names', ['Bx GSM', 'By GSM', 'Bz GSM'])

options('thd_scf_gse', 'legend_names', ['Bx GSE', 'By GSE', 'Bz GSE'])

# Set the line colors

options('thd_scf_gsm', 'Color', ['blue', 'green', 'red'])

options('thd_scf_gse', 'Color', ['blue', 'green', 'red'])

# Set the yrange

options('thd_scf_gsm', 'yrange', [-20, 20])

options('thd_scf_gse', 'yrange', [-20, 20])

# Replot the data with the updated metadata

tplot(['thd_scf_gse', 'thd_scf_gsm'])

# ### Van Allen Probes (RBSP)
# 
# To load RBSP emfisis data:

pyspedas.rbsp.emfisis(trange=['2016-10-16', '2016-10-17'])

help(pyspedas.rbsp.emfisis)

tplot(['Magnitude', 'Mag'])

# Just like with MMS instruments, you can find the available options for the load routines using help()

help(pyspedas.rbsp.mageis)

# Most load routines support the downloadonly option; this tells the load routine to download the data files, but not load them into tplot variables

files = pyspedas.rbsp.mageis(trange=['2018-11-5', '2018-11-6'], probe=['a', 'b'], downloadonly=True)

files

# ### Deep Space Climate Observatory (DSCOVR)
# 
# To load DSCOVR magnetometer data:

from pyspedas import dscovr

dscovr.mag(trange=['2016-10-16', '2016-10-17'])

# and DSCOVR faraday cup data:

dscovr.fc(trange=['2016-10-16', '2016-10-17'])

tplot(['B1GSE', 'V_GSE', 'Np'])

# ### Geotail 
# 
# To load some Geotail magnetometer data, and append a suffix to the variable names:

pyspedas.geotail.mgf(trange=['2018-11-5/6:00', '2018-11-5/12:00'], suffix='_suffix', time_clip=True)

tplot(['IB_suffix', 'IB_vector_suffix'])

# and to load data from the Low Energy Particle experiment (LEP):

lep_vars = pyspedas.geotail.lep(trange=['2018-11-5/8:00', '2018-11-5/9:00'], time_clip=True)

lep_vars

tplot(['N0', 'V0'])

# ### IMAGE MENA
# 
# To load the energetic neutral atom images from the MENA instrument onboard IMAGE

pyspedas.image.mena(trange=['2003-10-31', '2003-11-1'])

# Plot the IMAGE spacecraft position

tplot('gsm_pos')

# ### OMNI 
# 
# To load OMNI solar wind data (note: OMNI data are time-shifted to the magnetopause):

pyspedas.omni.data(trange=['2013-11-5', '2013-11-6'])

tplot(['BX_GSE', 'BY_GSE', 'BZ_GSE', 'flow_speed', 'Vx', 'Vy', 'Vz', 'SYM_H'])

# # Working with the data values
# 
# You can use get_data to extract the data values from the tplot variables:

from pytplot import get_data

bx_times, bx_values = get_data('BX_GSE')

# Just as in IDL, times are stored as unix times

bx_times

bx_values

# You can convert the unix times to strings using time_string

from pyspedas import time_string

time_string(bx_times[0:5])

# You can convert the strings back to unix times using time_double

from pyspedas import time_double

time_double(time_string(bx_times[0:5]))

# For energy spectra, the process is similar

times, data, energies = get_data('mms1_des_energyspectr_omni_brst')

# note: burst mode FPI energy spectra are time varying

energies

# Internally, pytplot variables are stored as xarray objects
# 
# If you're familiar with xarray, you can access the underlying xarray object by setting `xarray=True`

xr = get_data('mms1_des_energyspectr_omni_brst', xarray=True)

xr

# You can use store_data to create tplot variables

from pytplot import store_data

store_data('bx_values', data={'x': bx_times, 'y': bx_values})

tplot('bx_values')

# You can use join_vec to join multiple tplot variables into a single tplot variable

from pytplot import join_vec

join_vec(['BX_GSE', 'BY_GSE', 'BZ_GSE'], new_tvar='OMNI_B_GSE')

tplot('OMNI_B_GSE')

# You can use split_vec to split a vector variable into multiple tplot variables

from pytplot import split_vec

split_vec('OMNI_B_GSE')

tplot(['OMNI_B_GSE_0', 'OMNI_B_GSE_1', 'OMNI_B_GSE_2'])

# Set the labels on a tplot variable

options('OMNI_B_GSE', 'legend_names', ['Bx GSE', 'By GSE', 'Bz GSE'])

tplot('OMNI_B_GSE')

# To change the colors of the lines (note: the docs for the options are incorrect here)

options('OMNI_B_GSE', 'Color', ['b', 'g', 'r'])

tplot('OMNI_B_GSE')

# To change the title on the Y axis

options('OMNI_B_GSE', 'ytitle', 'OMNI B-field (nT)')

tplot('OMNI_B_GSE')

# You can change spectra back into line plots using the 'Spec' option

options('mms1_des_energyspectr_omni_brst', 'Spec', False)

tplot('mms1_des_energyspectr_omni_brst')

# and convert it back to a spectra

options('mms1_des_energyspectr_omni_brst', 'Spec', True)

tplot('mms1_des_energyspectr_omni_brst')

# You can also control ylog and zlog using options

options('mms1_des_energyspectr_omni_brst', 'zlog', False)

tplot('mms1_des_energyspectr_omni_brst')

# Global plot options can be set with tplot_options

from pytplot import tplot_options

help(tplot_options)

tplot_options('title', 'OMNI Bz and Flow Speed')

tplot(['BZ_GSM', 'flow_speed'])

# # How to contribute
# 
# Try it out! And please report bugs, missing documentation, or any other issues so that we can fix them (feel free to email me or submit them through GitHub issues). If there's a missing dataset or analysis tool that you would like to see included, please let us know!  





