# # PyTplot annotations
# 
# This notebook shows how to set annotations on tplot figures. 
# 
# Originally created at the 2022 PyHC Spring Meeting Hackathon

!pip install pyspedas

from pytplot import tplot, store_data, options, annotate

# Create a simple variable with 6 data points at 1.0:

store_data('data', data={'x': [1, 2, 3, 4, 5, 6], 'y': [1, 1, 1, 1, 1, 1]})

# By default, the tplot variable's name is used as the y-axis title
# 
# (ignore the Colab warnings)

tplot('data')

# You can change this by setting the `ytitle` option

options('data', 'ytitle', 'This is the data')

tplot('data')

# Set a subtitle on the y-axis:

options('data', 'ysubtitle', '[units]')

tplot('data')

# Use greek letters in annotations

options('data', 'ytitle', 'Lambda λ')

tplot('data')

# You can also use latex
# 
# Note: in this case, the string must be specific as a raw string

options('data', 'ytitle', r'Lambda $\lambda$')

tplot('data')

# Use superscripts and subscripts in annotations; exponents can be set with a simple ^

options('data', 'ysubtitle', r'cm^2')

tplot('data')

# Use latex to specify subscripts

options('data', 'ytitle', r'Lambda$_{λ}$')

tplot('data')

# Change the size of the text
# 
# Note: this also updates the z-axis title and subtitle size

options('data', 'charsize', 16)

tplot('data')

# Add a title to the figure

from pytplot import tplot_options

tplot_options('title', 'Figure Title')

tplot('data')

# Use the annotate function to add text to the figure

annotate('This is our text', [0.5, 0.5])

tplot('data')

help(annotate)

# You can set the `xycoords` keyword to change coordinates specified in the `position` keyword. For example, to add some text in data coordinates:

from datetime import datetime, timezone
import matplotlib

time = matplotlib.dates.date2num(datetime(1970, 1, 1, 0, 0, 3, tzinfo=timezone.utc))

annotate('This is the second text', [time, 0.925], xycoords='data')

tplot('data')

# You can also set the options in an `opts` dictionary, and supply them with `**opts`

opts = {'xycoords': 'data',
        'fontsize': 'xx-large',
        'color': 'blue',
        'rotation': 'vertical'}

annotate('This is the third text', [time, 0.925], **opts)

tplot('data')

# Delete the annotations by setting the `delete` keyword. This removes all of the current annotations previously set with the `annotate` function

annotate(delete=True)

tplot('data')



