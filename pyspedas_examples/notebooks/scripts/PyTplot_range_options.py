# # PyTplot range options
# 
# This notebook shows how to set various range (x-axis, y-xaix, z-axis) range options in PyTplot

!pip install pyspedas

import pyspedas
from pytplot import tplot, options, tlimit

pyspedas.mms.fpi(datatype='des-moms', trange=['2015-10-16', '2015-10-17'])

panels = ['mms1_des_energyspectr_omni_fast', 'mms1_des_bulkv_gse_fast', 'mms1_des_numberdensity_fast']

# Zoom into a time range

tlimit(['2015-10-16/11:00', '2015-10-16/12:00'])

tplot(panels)

# Reset to the full time range with the `full` option

tlimit(full=True)

tplot(panels)

# You can set the y-axis range with the `options` routine

options(panels[1], 'yrange', [-400, 400])

tplot(panels)

# Set the y-axis range of multiple panels

options(panels[0], 'yrange', [20, 1e4])
options(panels[1], 'yrange', [-300, 300])
options(panels[2], 'yrange', [10, 100])

tplot(panels)

# Turn logarithmic scaling on / off

options(panels[0], 'ylog', False)
options(panels[2], 'ylog', False)

tplot(panels)

# Set the spectrogram color bar ranges using the `options` routine

options(panels[0], 'zrange', [1e5, 1e9])
options(panels[0], 'zlog', False)

tplot(panels)



