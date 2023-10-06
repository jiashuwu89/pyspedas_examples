# # Introduction to PyTplot
# 
# This notebook demonstrates how to work with time series data using the `matplotlib` version of PyTplot. 
# 
# We'll install PySPEDAS to get PyTplot (as well as some load routines for quickly accessing some data, and additional tools for working with `tplot` variables). If you would like to install the `matplotlib` version of PyTplot without installing PySPEDAS, you can do so with:
# 
# `pip install pytplot-mpl-temp`

!pip install pyspedas

# If you're working in Google Colab, you'll need to restart the runtime after installing PyTplot using `exit()` or using the menu at: "Runtime" -> "Restart Runtime".
# 
# This is because we require a newer version of `matplotlib` than the one that comes pre-installed with Colab (due to a spectrogram bug)

exit()

# ## Load some data
# 
# We'll use MMS FPI ion data as an example; this is a good case to show because the data includes multi-dimensional distribution function data

import pyspedas

pyspedas.mms.fpi(trange=['2015-10-16/13:05', '2015-10-16/13:06'],
                 data_rate='brst',
                 datatype=['dis-dist', 'dis-moms'])

# ## Plot some variables
# 
# The data are now loaded into `tplot` variables (the `t` stands for `timeseries`!); You can plot them with `tplot`:

from pytplot import tplot

tplot(['mms1_dis_bulkv_gse_brst', 'mms1_dis_energyspectr_omni_brst'])

# ## Access the data and time values

# You can access the data using `get_data`:

from pytplot import get_data

data = get_data('mms1_dis_dist_brst', dt=True)

# ## Time values
# 
# The `dt` option tells `get_data` to return the times as a `numpy` array of type `datetime64[ns]`. These are unix times (so no leap seconds) in UTC. 

data.times.shape

data.times

# ## Multi-dimensional data values

# The data values are in `data.y` (note the 4D dataset, simply stored as a `numpy` array):

data.y.shape

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

# ## Access to the `xarray` `DataArray` objects
# 
# You can also access the underlying `DataArray` object using `get_data`:

xrdata = get_data('mms1_dis_dist_brst', xarray=True)

xrdata

# ## Convert to other common time series objects (e.g. `pandas.DataFrame`)
# 
# If you would prefer to work with pandas objects, you can convert the `xarray` `DataArray`, e.g., to convert the DIS bulk velocity to a `pandas.DataFrame`:

xrbulkv = get_data('mms1_dis_bulkv_gse_brst', xarray=True)

pandas_bulkv = xrbulkv.to_pandas()

pandas_bulkv

# ## Access the metadata
# 
# You can also access the metadata of a tplot variable using `get_data`:

metadata = get_data('mms1_dis_dist_brst', metadata=True)

# This is just a dictionary, containing the CDF and plot metadata:

metadata.keys()

# So to get the CDF metadata for our DF variable:

metadata['CDF']['VATT']

# ## Create a `tplot` variable
# 
# Use `store_data` to create a `tplot` variable:

from pytplot import store_data
import numpy as np

# For our time values, we'll just create an array of 100 values from 0 to 100 as an example. If the input to `store_data` are floats, they should be unix times in UTC

times = np.linspace(0, 100, 100)

# For the data values, we'll use the cosine of the time values

cosine = np.cos(times)

store_data('cosine', data={'x': times,
                           'y': cosine})

from pytplot import tplot

tplot('cosine')

# In addition to `x` and `y`, `store_data` accepts the `v` tag (for spectrograms), as well as the `v1`, `v2` and `v3` tags (for multi-dimensional data).
# 
# For the time values (`x`), `store_data` accepts `datetime64` objects as well:

times = np.array([1, 2, 3, 4, 5], dtype='datetime64[s]')

times

store_data('another_variable', data={'x': times,
                                     'y': [1, 2, 3, 4, 5]})

tplot('another_variable')

# ## Combine multiple `tplot` variables
# 
# You can split a tplot variable into individual components using `split_vec`, and combine them using `join_vec`, e.g., 
# 
# Note: keeping track of the metadata needs to be improved

from pytplot import join_vec, split_vec

split_vec('mms1_dis_bulkv_gse_brst')

# Plot the individual components:

from pytplot import tplot

tplot(['mms1_dis_bulkv_gse_brst_x',
       'mms1_dis_bulkv_gse_brst_y',
       'mms1_dis_bulkv_gse_brst_z'])

# And you can use `join_vec` to join them back together:

join_vec(['mms1_dis_bulkv_gse_brst_x',
          'mms1_dis_bulkv_gse_brst_y',
          'mms1_dis_bulkv_gse_brst_z'], new_tvar='bulkv_from_components')

tplot('bulkv_from_components')

# ## More examples
# 
# Please see the following for more examples:
# ### Loading Data
# - [MMS examples](https://github.com/spedas/mms-examples/tree/master/basic)
# - [THEMIS examples](https://github.com/spedas/themis-examples/tree/main/basic)
# - [Load data from HAPI servers](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PySPEDAS_loading_data_from_HAPI_servers.ipynb)
# - [Exploring the Heliosphere with Python](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/Exploring_the_Heliosphere_with_Python.ipynb)
# 
# ### Plotting Data
# - [Annotations](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_annotations.ipynb)
# - [Range options](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_range_options.ipynb)
# - [Spectrogram options](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_spectrogram_options.ipynb)
# - [Legend options](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_legend_options.ipynb)
# - [Markers and symbols](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_markers_and_symbols.ipynb)
# - [Error bars](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_error_bars.ipynb)
# - [Pseudo variables](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_pseudo_variables.ipynb)
# - [Highlight intervals and vertical bars](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_highlight_intervals_and_vertical_bars.ipynb)
# 
# 
# ### Dates and Times
# - [Working with dates and times](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/Working_with_dates_and_times_with_PySPEDAS_PyTplot.ipynb)
# 
# ### Coordinate Transformations
# - [Coordinate transformations](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/Coordinate_transformations_with_OMNI_data.ipynb)
# - [Transforming MMS data to boundary normal (LMN) coordinates](https://github.com/spedas/mms-examples/blob/master/advanced/MMS_LMN_coordinate_transformation.ipynb)
# - [Quaternion transformations with SpacePy](https://github.com/spedas/mms-examples/blob/master/basic/MMS_quaternion_coordinate_transformations.ipynb)
# 
# ### Analysis
# - [Plasma calculations with PlasmaPy](https://github.com/spedas/mms-examples/blob/master/advanced/Plasma%20calculations%20with%20PlasmaPy.ipynb)
# - [Calculating Poynting flux with MMS data](https://github.com/spedas/mms-examples/blob/master/advanced/Poynting_flux_with_MMS_data.ipynb)
# - [Plasma beta with MMS data](https://github.com/spedas/mms-examples/blob/master/basic/Plasma%20Beta%20with%20FGM%20and%20FPI%20data.ipynb) (note: the PlasmaPy notebook above shows a much easier method)
# - [Curlometer calculations](https://github.com/spedas/mms-examples/blob/master/basic/Curlometer%20Technique.ipynb)
# - [Neutral sheet models](https://github.com/spedas/mms-examples/blob/master/advanced/MMS_neutral_sheet_models.ipynb)
# - [Wave polarization calculations](https://github.com/spedas/mms-examples/blob/master/advanced/Wave_polarization_using_SCM_data.ipynb)
# - [Dynamic power spectra calculations](https://github.com/spedas/mms-examples/blob/master/basic/Search-coil%20Magnetometer%20(SCM).ipynb)
# - [2D slices of MMS distribution functions](https://github.com/spedas/mms-examples/blob/master/advanced/Generate_2D_slices_of_FPI_and_HPCA_data.ipynb)
# - [Generating spectrograms and moments from MMS distribution functions](https://github.com/spedas/mms-examples/blob/master/advanced/Generate%20spectrograms%20and%20moments%20with%20mms_part_getspec.ipynb)
# 



