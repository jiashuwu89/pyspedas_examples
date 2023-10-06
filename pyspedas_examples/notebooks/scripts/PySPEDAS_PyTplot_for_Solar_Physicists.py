# # PySPEDAS/PyTplot for Solar Physicists
# 
# **By Eric Grimes, UCLA - Earth, Planetary, and Space Sciences; egrimes@igpp.ucla.edu**
# 
# - PySPEDAS: https://pyspedas.readthedocs.io/
# - PyTplot: https://pytplot.readthedocs.io/
# 
# 
# This notebook is available online at:
# 
# https://colab.research.google.com/drive/1OOobvI53Qgb6HszUc1pFsF9BmLYQGVN7?usp=sharing
# 
# 
# A little history: 
# - `tplot` started as an IDL project in 1995, by Davin Larson, and is the core of SPEDAS (and now PySPEDAS)
# - in 2017, some developers on the MAVEN team created an initial Python version, using Qt as a back-end for creating figures
# - in late 2021, development began on a `matplotlib` version, which is what we're using in this notebook
# - it has primarily been used in Magnetospheric Physics, but I'm sure it's also going to be useful for timeseries data in other areas of Heliophysics

!pip install pyspedas

import pyspedas
from pytplot import tplot

# ### Setting your local data directory
# 
# By default, data files are saved in a subfolder of your current working directory; you can change this by setting the `SPEDAS_DATA_DIR` environment variable. Directories for individual missions can also be changed from the default with mission-specific environment variables, e.g., `PSP_DATA_DIR` or `SOLO_DATA_DIR`

# ### Load some Parker Solar Probe FIELDS data
# 
# #### Set a timespan for four days near perihelion 2
# 
# This example time range was taken from the PSP FIELDS team's IDL example

trange = ['2019-04-03', '2019-04-07']

# ### Load the MAG data in RTN coordinates
# 
# Note: the load routines in PySPEDAS all follow the form: pyspedas.mission.instrument(), and have the same core keywords for accessing data (trange, level, datatype, etc). 

variables = pyspedas.psp.fields(datatype='mag_rtn_4_sa_per_cyc', trange=trange)

# To find the supported load routines and keywords, see our documentation: https://pyspedas.readthedocs.io/
# 
# You can also see the supported options by calling `help` on the load routine you're interested in

help(pyspedas.solo.mag)

# Note: most load routines have some reasonable defaults for every keyword (including trange), so simply calling `pyspedas.mission.instrument()` should load some data, e.g., 

pyspedas.solo.mag()

# And we can now plot it:

tplot('B_RTN')

# ### PSP Radio Frequency Spectrometer (RFS) HFR and LFR data
# 
# Note: specifying the variable names with the varnames keyword isn't required, but does speed up loading these data

pyspedas.psp.fields(datatype='rfs_hfr', trange=trange, varnames='psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2')
pyspedas.psp.fields(datatype='rfs_lfr', trange=trange, varnames='psp_fld_l2_rfs_lfr_auto_averages_ch0_V1V2')

# You can use the `xsize` and `ysize` options to change the figure size

tplot(['psp_fld_l2_mag_RTN_4_Sa_per_Cyc',
       'psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2',
       'psp_fld_l2_rfs_lfr_auto_averages_ch0_V1V2'], xsize=20)

# Return the data in `numpy` arrays

from pytplot import get_data

data = get_data('psp_fld_l2_mag_RTN_4_Sa_per_Cyc')

# The time values are stored in `data.times` (as unix times)

data.times

# The data values (for a simple line plot) are stored in `data.y`

data.y

# You can then use the `numpy` `ndarray` methods to work with these data, e.g., to find the shape of the data:

data.y.shape

# You can convert from unix times to strings using `time_string`

from pyspedas import time_string

time_string(data.times[0])

# And convert back using `time_double`

from pyspedas import time_double

time_double('2019-04-03 00:00:00.075775')

# And convert to datetime objects using `time_datetime`

from pyspedas import time_datetime

time_datetime(data.times[0])

# For spectra variables, `data.y` contains the data values (z-axis), and  `data.v` contains the y-axis values at each point

rfs_data = get_data('psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2')

rfs_data.y

rfs_data.y.shape

rfs_data.v

rfs_data.v.shape

# The metadata for a variable can be obtained using the `metadata` option in `get_data`

metadata = get_data('psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2', metadata=True)

metadata

# You can create new `tplot` variables using `store_data`

from pytplot import store_data

store_data('mag_rtn', data={'x': data.times, 'y': data.y})

tplot('mag_rtn')

# To find the names of all of the loaded `tplot` variables, use `tplot_names`

from pytplot import tplot_names

variables = tplot_names()

# To change the plot options, use the `options` function in `pytplot`

from pytplot import options

help(options)

# For example:

options('mag_rtn', 'color', ['purple', 'green', 'black'])
options('mag_rtn', 'legend_names', ['R', 'T', 'N'])
options('mag_rtn', 'ytitle', 'Parker Solar Probe B-field')
options('mag_rtn', 'ysubtitle', '[nT]')
options('mag_rtn', 'char_size', 15)

tplot(['psp_fld_l2_mag_RTN_4_Sa_per_Cyc', 'mag_rtn'])

# Note: `options` changes panel-level options, figure-level options can be set with `tplot_options`, e.g., 
# 
# 
# Note: not all of these options are supported by the `matplotlib` version yet; if you find one that isn't working, please let us know and we'll prioritize it
# 

from pytplot import tplot_options

help(tplot_options)

tplot_options('title', 'Parker Solar Probe Data')

tplot(['psp_fld_l2_mag_RTN_4_Sa_per_Cyc', 'mag_rtn'])

# You can save figures using keywords to `tplot`, e.g., to save a PNG file:

tplot('psp_fld_l2_mag_RTN_4_Sa_per_Cyc', save_png='figure')

# To save the figure as a postscript file:

tplot('psp_fld_l2_mag_RTN_4_Sa_per_Cyc', save_eps='figure')

# Or save as a PDF:

tplot('psp_fld_l2_mag_RTN_4_Sa_per_Cyc', save_pdf='figure')

# Note: you can have full control over the figures and axes by returning the objects using the `return_plot_objects` keyword, e.g., 

fig, axes = tplot('psp_fld_l2_mag_RTN_4_Sa_per_Cyc', return_plot_objects=True)

axes

# For example, to add some text to a figure:

from datetime import datetime, timezone
import matplotlib

time = matplotlib.dates.date2num(datetime(2019, 4, 6, 13, 0, 0, tzinfo=timezone.utc))
axes.annotate('Your text', (time, -110), fontsize='x-large')

fig



