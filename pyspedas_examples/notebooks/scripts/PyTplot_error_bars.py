# # PyTplot error bars
# 
# This notebook shows how to add error bars to tplot variables
# 
# Originally created at the 2022 PyHC Spring Meeting Hackathon

!pip install pytplot-mpl-temp

from pytplot import store_data

# Create a simple variable without errors:

store_data('data_without_errors', data={'x': [1, 2, 3, 4, 5, 6], 'y': [1, 1, 1, 1, 1, 1]})

from pytplot import tplot

tplot('data_without_errors')

# To add error bars to a tplot variable, set the `dy` key in the data dictionary:

store_data('data_with_errors', data={'x': [1, 2, 3, 4, 5, 6], 
                                     'y': [1, 1, 1, 1, 1, 1],
                                     'dy': [0.25]*6})

tplot('data_with_errors')

# Note: the y-axis range doesn't update due to the error bars, so we'll have to update the y-axis range to see the full error bars

from pytplot import options

options('data_with_errors', 'yrange', [0, 2])

tplot('data_with_errors')

# Use the `errorevery` option to only show the error bars on every other data point

options('data_with_errors', 'errorevery', 2)

tplot('data_with_errors')

# Change the color of the error bars to blue:

options('data_with_errors', 'ecolor', 'blue')

tplot('data_with_errors')

# Change the width of the color bars:

options('data_with_errors', 'elinewidth', 5)

tplot('data_with_errors')

# Add caps to the end of the error bars:

options('data_with_errors', 'capsize', 10)

tplot('data_with_errors')



