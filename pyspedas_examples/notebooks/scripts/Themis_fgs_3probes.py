# This code demonstrates how to plot data from three THEMIS probes on a single plot. When plotting with Pytplot, each tplot variable cooresponds to an individual panel. To visualize data from three probes in a single panel, it's necessary to create 
# a combined tplot variable that aggregates data from all three probes.
# Step: 1. 'split_vec': to split vectors into three compoents, x, y and z
#       2. 'store_data': store data from three probes together.

%pip install ipykernel

from pyspedas.themis import fgm
import pytplot

# load THEMIS FGM data, we use fgs gsm data here

# Load THEMIS FGM data for THD, THE, and THA
fgm(probe='d', trange=['2021-07-10/01:00', '2021-07-10/02:10'], time_clip=True)
fgm(probe='e', trange=['2021-07-10/01:00', '2021-07-10/02:10'], time_clip=True)
fgm(probe='a', trange=['2021-07-10/01:00', '2021-07-10/02:10'], time_clip=True)

# split_vec will split a vector into three component. e.g. thd_fgs_gsm will be splited into thd_fgs_gsm_x, thd_fgs_gsm_y, thd_fgs_gsm_z

# Split the 3D FGM data into individual components
pytplot.tplot_math.split_vec('thd_fgs_gsm')
pytplot.tplot_math.split_vec('the_fgs_gsm')
pytplot.tplot_math.split_vec('tha_fgs_gsm')

# Join the Bx components from the three probes into one tplot variable
pytplot.store_data("combined_bx", data=['tha_fgs_gsm_x', 'the_fgs_gsm_x', 'thd_fgs_gsm_x'])

# Modify the options
pytplot.options('combined_bx', 'Color',['b','r','k'])
pytplot.options('combined_bx', 'legend_names', ['tha','the','thd'])
pytplot.options('combined_bx', 'ytitle', 'fgs Bx')
pytplot.options('combined_bx', 'ysubtitle', '[nT]')

# Plot the tplot variable
pytplot.tplot('combined_bx')

