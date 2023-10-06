# # PyTplot legend options
# 
# This notebook shows how to change legend options in tplot figures. 
# 
# Originally created at the 2022 PyHC Spring Meeting Hackathon

!pip install pytplot-mpl-temp

from pytplot import store_data, options, tplot

# Create a simple tplot variable named data with all values set to 1

store_data('data', data={'x': [1, 2, 3, 4, 5, 6], 'y': [1, 1, 1, 1, 1, 1]})

# By default, no legend is created

tplot('data')

# To add a legend, set the `legend_names` option. 
# 
# If there are multiple lines in the tplot variable, you'll need to specify an array of strings for each line

options('data', 'legend_names', 'Data at 1')

tplot('data')

# By default, the legend uses matplotlib's `best` option for the location. To change this, set the `legend_location` option.
# 
# Specifying the `spedas` value in `legend_location` option places the legend on the right-hand side of the panel (like in IDL tplot)

options('data', 'legend_location', 'spedas')

tplot('data')

# See:
# 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
# 
# For other available options for the legend location. To move the legend to the lower left:

options('data', 'legend_location', 'lower left')

tplot('data')

# Change the legend location back to the `best` option

options('data', 'legend_location', 'best')

tplot('data')

# Increase the size of the text in the legend

options('data', 'legend_size', 16)

tplot('data')

# Add a title to the legend

options('data', 'legend_title', 'This is our legend')

tplot('data')

# Increase the size of the legend title

options('data', 'legend_titlesize', 20)

tplot('data')

# Change the color of the legend text

options('data', 'legend_color', 'blue')

tplot('data')

# Add a shadow to the legend

options('data', 'legend_shadow', True)

tplot('data')

# Switch the marker to the left-hand side of the legend

options('data', 'legend_markerfirst', True)

tplot('data')

# Add a hexagon marker and increase the size of the marker on the legend

options('data', 'legend_markerscale', 3)

options('data', 'marker', 'H')

tplot('data')

# Lower the size of the markers in the legend back to the default

options('data', 'legend_markerscale', 1)

tplot('data')

# Change the background color of the legend

options('data', 'legend_facecolor', 'pink')

tplot('data')

# Change the edge color of the legend

options('data', 'legend_edgecolor', 'blue')

tplot('data')

# Move the legend back to the right-side of the panel, like in IDL SPEDAS

options('data', 'legend_location', 'spedas')

tplot('data')



