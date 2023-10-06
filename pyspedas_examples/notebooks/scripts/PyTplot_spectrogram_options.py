# # PyTplot spectrogram options
# 
# This notebook shows how to create and work with spectrograms in PyTplot
# 
# Originally created at the 2022 PyHC Spring Meeting Hackathon

!pip install pytplot-mpl-temp

import numpy as np

from pytplot import store_data, options, tplot

# Create a simple spectrogram variable

data = np.array([[0,       1,       2,       3,       4],
           [5,       6,       7,       8,       9],
          [10,      11,      12,      13,      14],
          [15,      16,      17,      18,      19],
          [20,      21,      22,      23,      24]])

# Note: spectrogram variables should have the `v` option set in the data dictionary, with the y-axis values for the spectra

store_data('data', data={'x': [1, 2, 3, 4, 5], 'y': data.transpose(), 'v': [10, 20, 30, 40, 50]})

# By default, it'll still show up as a line plot

tplot('data')

# Set the `spec` option to turn it into a spectrogram

options('data', 'spec', True)

tplot('data')

# Update the y-axis range

options('data', 'yrange', [15, 45])

tplot('data')

# Change the y-axis range back

options('data', 'yrange', [10, 50])

# Update the color bar range

options('data', 'zrange', [5, 20])

tplot('data')

# Change the color bar range back

options('data', 'zrange', [0, 24])

tplot('data')

# Change the color bar
# 
# Note: this should support all of the colormaps available in matplotlib, see:
# 
# https://matplotlib.org/3.5.0/tutorials/colors/colormaps.html
# 
# for a list

options('data', 'Colormap', 'plasma')

tplot('data')

# In addition to the matplotlib colormaps, we also support the `spedas` color bar (the same one as in IDL SPEDAS). The `spedas` colormap is the default

options('data', 'Colormap', 'spedas')

tplot('data')

# To automatically interpolate in the x-direction, use the `x_interp` option

options('data', 'x_interp', True)

tplot('data')

# To automatically interpolate in the y-direction, turn off x-interpolation and turn on y-interpolation:

options('data', 'x_interp', False)
options('data', 'y_interp', True)

tplot('data')

# Turn interpolation on in both the x and y directions

options('data', 'x_interp', True)
options('data', 'y_interp', True)

tplot('data')

# Change the number of data points in the interpolation in the x-direction

options('data', 'x_interp_points', 10)

tplot('data')

# Change the number of data points in the y-direction

options('data', 'y_interp_points', 10)

tplot('data')

# Turn the y-axis to log scale

options('data', 'ylog', True)

tplot('data')

# Set the z-axis to a log scale

options('data', 'zlog', True)

# Note: for some reason, we need to change the `zrange` to remove the 0 in the log scale

options('data', 'zrange', [0.0001, 24])
options('data', 'yrange', [10, 50])

tplot('data')

# Change the opacity using the `alpha` option

options('data', 'alpha', 0.5)

tplot('data')

# Create a simple line variable with 5 data points at 30.0

store_data('line', data={'x': [1, 2, 3, 4, 5], 'y': [30]*5})

# Create a pseudo variable combining the spectrogram and the line

store_data('combined', data='data line')

# Turn the y/z logs back to linear, and set the alpha back to 1

options('data', 'zlog', False)
options('data', 'ylog', False)
options('data', 'alpha', 1)

# Plot the combined variable

tplot('combined')

# Increase the margin size on the right-side of the panel

from pytplot import tplot_options

tplot_options('xmargin', [0.1, 0.25])

tplot('combined')

# By default, both the spectra and the lines share the y-axis. To move the line plot to the right axis, set the `right_axis` option

options('combined', 'right_axis', True)

tplot('combined')

# All of the standard options should work, e.g., to add + markers at the data locations:

options('line', 'marker', '+')

tplot('combined')

# And you can update the yrange of the line:

options('line', 'yrange', [29, 31])

tplot('combined')

# Add a legend to the line:

options('line', 'legend_names', 'Line')

tplot('combined')

# Set the title of the color bar:

options('data', 'ztitle', 'Colorbar title')

tplot('combined')

# Set the z-axis subtitle:

options('data', 'zsubtitle', '[colorbar units]')

tplot('combined')



