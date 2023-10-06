# # PyTplot markers and symbols
# 
# This notebook shows how to use markers and symbols in tplot figures. 
# 
# Originally created at the 2022 PyHC Spring Meeting Hackathon

!pip install pytplot-mpl-temp

from pytplot import store_data, tplot, options

# Create a simple tplot variable named data with all values set to 1
# 

store_data('data', data={'x': [1, 2, 3, 4, 5, 6], 'y': [1, 1, 1, 1, 1, 1]})

# By default, no markers are set

tplot('data')

# Change the marker to `X`

options('data', 'marker', 'X')

tplot('data')

# Change the plot to use symbols to disable the line connecting the markers

options('data', 'symbols', True)

tplot('data')

# Change the `marker_size` option to increase the size of the symbols

options('data', 'marker_size', 200)

tplot('data')

# Disable `symbols` to enable to line connecting the data points

options('data', 'symbols', False)

# Lower the marker size. Note: the definition of `marker_size` seems to be different depending on if the `symbols` option is set

options('data', 'marker_size', 20)

tplot('data')

# Update the figure to only show the marker every 2 data points

options('data', 'markevery', 2)

tplot('data')

# Change the markers to hexagons.
# 
# Note: this supports all of the same markers shown at:
# 
# https://matplotlib.org/stable/api/markers_api.html

options('data', 'marker', 'H')

tplot('data')



