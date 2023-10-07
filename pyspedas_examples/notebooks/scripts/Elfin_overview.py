# # ELFIN EPD data loading example
# This notebook demonstrates how to load elfin state data, l1 and l2 epd data. And how to generate enegy and picth angle spectrogram with l2 data.

import pyspedas
from pytplot import tplot, tplot_options

# ### 1. load elfin state tplot variables:

state_var = pyspedas.elfin.state(trange=['2022-01-14/06:28', '2022-01-14/06:35'], probe='a', no_update=True)
print(state_var)

# plot position and attitude data

tplot(['ela_pos_gei', 'ela_att_gei'])

# ### 2. load epd l1 tplot variables:
# l1 data can be loaded as type_='raw/cps/nflux/eflux'

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
# l2 spectrogram can be loaded in 'nflux/eflux' and 'halfspin/fullspin'  
# Example of tplot variable names:  
# - elx_pef_hs/fs_nflux/eflux_omni  
# - elx_pef_hs/fs_nflux/eflux_para  
# - elx_pef_hs/fs_nflux/eflux_anti  
# - elx_pef_hs/fs_nflux/eflux_perp  

# load l2 half spin nflux data
epd_l2_hs_nflux = pyspedas.elfin.epd(
    trange=['2022-08-28/15:54','2022-08-28/16:15'], 
    probe='a',
    level='l2', 
    type_='nflux', 
    fullspin=False,
    no_update=True)
print(epd_l2_hs_nflux)

# load l2 nflux full spin data
epd_l2_fs_nflux = pyspedas.elfin.epd(
    trange=['2022-08-28/15:54','2022-08-28/16:15'], 
    probe='a', 
    level='l2', 
    type_='nflux', 
    fullspin=True,
    no_update=True)
print(epd_l2_fs_nflux)

# load l2 half spin eflux data
epd_l2_hs_nflux = pyspedas.elfin.epd(
    trange=['2022-08-28/15:54','2022-08-28/16:15'], 
    probe='a', 
    level='l2', 
    type_='eflux', 
    fullspin=False,
    no_update=True)
print(epd_l2_hs_nflux)

# load l2 full spin eflux data
epd_l2_hs_nflux = pyspedas.elfin.epd(
    trange=['2022-08-28/15:54','2022-08-28/16:15'], 
    probe='a', 
    level='l2', 
    type_='eflux', 
    fullspin=True,
    no_update=True)
print(epd_l2_hs_nflux)

# plot energy spectrogram
tplot(['ela_pef_hs_nflux_omni', 'ela_pef_hs_eflux_para', 'ela_pef_hs_eflux_anti','ela_pef_hs_eflux_perp']) 

# plot pitch angle spectrogram
tplot(['ela_pef_hs_nflux_ch0', 'ela_pef_hs_nflux_ch1', 'ela_pef_hs_nflux_ch2', 'ela_pef_hs_nflux_ch3'])

