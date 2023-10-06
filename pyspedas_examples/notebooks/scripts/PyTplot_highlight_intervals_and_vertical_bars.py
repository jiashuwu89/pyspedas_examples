# # Vertical bars at certain times, and highlight time intervals 
# 
# This notebook shows how to create vertical bars and highlight time intervals in tplot figures. 
# 
# Originally created at the 2022 PyHC Spring Meeting Hackathon

!pip install pytplot-mpl-temp

from pytplot import store_data, highlight, tplot

# Create a simple tplot variable named `data` with all values set to 1

store_data('data', data={'x': [1, 2, 3, 4, 5, 6], 'y': [1, 1, 1, 1, 1, 1]})

tplot('data')

from pytplot import timebar

# Check the documentation for avaiable options. 
# 
# Note: the `matplotlib` version of pytplot doesn't support the `dash` keyword

help(timebar)

# Call `timebar` to create a timebar at the unix time of 2.0 (2 seconds after 1 Jan 1970). If no `varname` keyword is specified, all panels on the figure will have the vertical bar

timebar(2)

tplot(['data', 'data'])

# Specify the `varname` keyword to limit the vertical bar to one specific panel

timebar(3, varname='data')

tplot('data')

# Set the color to blue using the `color` keyword

timebar(4, color='blue')

tplot('data')

# Highlight time intervals with the `highlight` function in `pytplot`

help(highlight)

# Highlight a time interval between 4.5 and 5 seconds

highlight(['data'], [4.5, 5])

tplot('data')

# Highlight another time interval between 5.1 and 6 seconds, with a blue 'o' hatch pattern

highlight(['data'], [5.1, 6], color='blue', hatch='O')

tplot('data')

# Delete all of the highlighted time intervals using the `delete` keyword

highlight('data', delete=True)

tplot('data')

# Delete vertical bars using the `delete` keyword

timebar(2, delete=True)

tplot('data')

# `timebar` also accepts keywords for controlling the aesthetics of the vertical bars

timebar(2, thick=5, color='pink')

tplot('data')



