# # ELFIN EPD data loading example
# This notebook demonstrates how to load elfin state data, l1 and l2 epd data. And how to generate overview plots with l2 data.

import pyspedas
from pytplot import tplot, tplot_options

# ### 1. load elfin state tplot variables:

state_var = pyspedas.elfin.state(trange=['2022-01-14/06:28', '2022-01-14/06:35'], probe='a', no_update=True)
print(state_var)

# plot position and attitude data

tplot(['ela_pos_gei', 'ela_att_gei'])

# ### 2. load epd l1 tplot variables:

# load raw data
epd_l1_raw = pyspedas.elfin.epd(
    trange=['2022-08-03/08:30:00','2022-08-03/09:00:00'], 
    probe='a', 
    level='l1', 
    type_='cps', 
    no_update=True)
print(epd_l1_raw)

# load cps data
epd_l1_cps = pyspedas.elfin.epd(
    trange=['2022-08-03/08:30:00','2022-08-03/09:00:00'], 
    probe='a', 
    level='l1', 
    type_='raw', 
    no_update=True)
print(epd_l1_cps)

# load nflux
epd_l1_nflux = pyspedas.elfin.epd(
    trange=['2022-08-03/08:30:00','2022-08-03/09:00:00'], 
    probe='a', 
    level='l1', 
    type_='nflux', 
    no_update=True)
print(epd_l1_nflux)

# load eflux
epd_l1_eflux = pyspedas.elfin.epd(
    trange=['2022-08-03/08:30:00','2022-08-03/09:00:00'], 
    probe='a', 
    level='l1', 
    type_='eflux', 
    no_update=True)
print(epd_l1_eflux)

# plot epd l1 raw, cps, nflux and eflux together

tplot_options('wsize', [1600,500])
tplot(['ela_pef_raw', 'ela_pef_cps', 'ela_pef_nflux', 'ela_pef_eflux'])

# ### 3. load epd l2 tplot variables:

# load l2 nflux
epd_l2_nflux = pyspedas.elfin.epd(
    trange=['2022-08-28/15:54','2022-08-28/16:15'], 
    probe='a', 
    level='l2', 
    type_='nflux', 
    fullspin=False,
    no_update=True)
print(epd_l2_nflux)



