# # Timeseries data with PySPEDAS + PyTplot
# 
# This notebook demonstrates how to work with time series data using PySPEDAS and PyTplot. 

!pip install pyspedas

# ## Load some data
# 
# We'll use MMS FPI ion distribution data as an example; this is a good case to show because the data are multi-dimensional

import pyspedas

pyspedas.mms.fpi(trange=['2015-10-16/13:05', '2015-10-16/13:06'],
                 data_rate='brst',
                 datatype=['dis-dist', 'dis-moms'])

# ## Store data that is a function of time

# The data are now loaded into `tplot` variables (the `t` stands for `timeseries`!); access the data:

from pytplot import get_data

data = get_data('mms1_dis_dist_brst', dt=True)

# ## Handle time scales with leapseconds
# 
# The `dt` option tells `get_data` to return the times as a `numpy` array of type `datetime64[ns]`. These are unix times (so no leap seconds) in UTC. 
# 
# Note: the original dataset contains leap seconds and we remove them when loading the data. I think having this policy technically meets the requiremnt of handling time scales with leapseconds. 

data.times

# ## Store multi-dimensional data

# The data values are in `data.y` (note the 4D dataset, simply stored as a `numpy` array):

data.y.shape

# ## Store and use physical units with the data and any non-time indices

# This is a function of time, energy, theta and phi. The phi values, which are time varying for this dataset, are in `v1`:

data.v1.shape

# The phi values for the first time stamp are:

data.v1[0, :]

# The theta values are:

data.v2.shape

data.v2

# And the energy values are (also time varying for this dataset):

data.v3.shape

# So the energy table for the first timestamp are:

data.v3[0, :]

# ## Store data in a format that can be used with scientific Python libraries
# 
# Since all of the data are available as `numpy` arrays, I think this requirement is met, but you can also access the underlying `xarray` object using `get_data`:

xrdata = get_data('mms1_dis_dist_brst', xarray=True)

xrdata

# ## Ability to convert to other common time series objects (e.g. pandas.DataFrame)
# 
# The `xarray` DataArray for the bulk velocity data:

xrbulkv = get_data('mms1_dis_bulkv_gse_brst', xarray=True)

pandas_bulkv = xrbulkv.to_pandas()

pandas_bulkv

# ## Store metadata alongside actual data

# You can also access the metadata of a tplot variable using `get_data`:

metadata = get_data('mms1_dis_dist_brst', metadata=True)

# This is just a dictionary, containing the CDF and plot metadata:

metadata.keys()

# So to get the CDF metadata for our DF variable:

metadata['CDF']['VATT']

# ## Have a way to store an observer coordinate alongside the time index (?)

# If the CDF metadata includes a coordinate system (which this one doesn't), it'll be available using `cotrans_get_coord`

from pyspedas.cotrans.cotrans_get_coord import cotrans_get_coord

cotrans_get_coord('mms1_dis_dist_brst')

# You can set it with `cotrans_set_coord`

from pyspedas.cotrans.cotrans_set_coord import cotrans_set_coord

cotrans_set_coord('mms1_dis_dist_brst', 'DBCS')

# And now it's available:

cotrans_get_coord('mms1_dis_dist_brst')

# ## Have an easy way to do common data manipulation tasks
# 
# Storing data in `tplot` variables makes implementing routines for common data manipulation tasks easy, e.g., to interpolate our FPI data to the electric field data:

pyspedas.mms.edp(trange=['2015-10-16/13:05', '2015-10-16/13:06'], data_rate='brst')

# Interpolate the electric field data to the bulk velocity:

from pyspedas import tinterpol

tinterpol('mms1_edp_dce_gse_brst_l2', 'mms1_dis_bulkv_gse_brst')

new_efield = get_data('mms1_edp_dce_gse_brst_l2-itrp')

new_efield.y.shape

# These should be at the same timestamps as the bulk velocity:

bulkv = get_data('mms1_dis_bulkv_gse_brst')
bulkv.y.shape

# ## Have a way to combine multiple timeseries objects, and keep track of metadata
# 
# You can split a tplot variable into individual components using `split_vec`, and combine them using `join_vec`, e.g., 
# 
# Note: keeping track of the metadata could be improved

from pytplot import join_vec, split_vec

split_vec('mms1_edp_dce_gse_brst_l2')

# Plot the individual components:

from pytplot import tplot

tplot(['mms1_edp_dce_gse_brst_l2_x',
       'mms1_edp_dce_gse_brst_l2_y',
       'mms1_edp_dce_gse_brst_l2_z'])

# And you can use `join_vec` to join them back together:

join_vec(['mms1_edp_dce_gse_brst_l2_x',
          'mms1_edp_dce_gse_brst_l2_y',
          'mms1_edp_dce_gse_brst_l2_z'], new_tvar='efield_from_components')

tplot('efield_from_components')



# ## Functionality for loading and saving out to common file formats
# 
# PyTplot makes this simple (already contains loaders for CDFs, netCDFs, and STS files, and it's easy to add more). 
# 
# The examples above focus on accessing the data; to create tplot variables, remove the leap seconds and call `pytplot.store_data` to save the variables, and `pytplot.options` to set plot options on the variables. Global plot options can be set with `pytplot.tplot_options`



