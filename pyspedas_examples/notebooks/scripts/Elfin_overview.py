# # ELFIN EPD data loading example
# This notebook demonstrates how to load elfin state data, l1 and l2 epd data. And how to generate enegy and picth angle spectrogram with l2 data.

!git clone --branch elfin https://github.com/spedas/pyspedas.git
!pip install pyspedas/

import pyspedas
from pytplot import tplot, store_data, options

trange = ['2021-07-14/11:55', '2021-07-14/12:05']
probe='a'

# ### 1. load elfin state tplot variables:  
# Eight variables will be loaded:  
# - ela_pos_gei
# - ela_vel_gei
# - ela_att_gei
# - ela_att_solution_date
# - ela_att_flag
# - ela_att_spinper
# - ela_spin_orbnorm_angle
# - ela_spin_sun_angle

state_var = pyspedas.elfin.state(trange=trange, probe=probe)

# plot position and attitude data

tplot(['ela_pos_gei', 'ela_att_gei'])

# ### 2. load epd l1 tplot variables:  
# l1 data can be loaded as 'raw/cps/nflux/eflux'. Five variables will be loaded:  
# - ela_pef_raw/cps/nflux/eflux
# - ela_pef_sectnum
# - ela_pef_nspinsinsum 
# - ela_pef_nsectors
# - ela_pef_spinper

# load raw data
epd_l1_raw = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l1', 
    type_='cps')

# load cps data
epd_l1_cps = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l1', 
    type_='raw')

# load nflux
epd_l1_nflux = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l1', 
    type_='nflux')

# load eflux
epd_l1_eflux = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l1', 
    type_='eflux')

# plot epd l1 raw and eflux together

tplot(['ela_pef_raw', 'ela_pef_eflux'])

# ### 3. load epd l2 tplot variables:
# L2 spectrogram can be loaded in 'nflux/eflux' and 'halfspin/fullspin'  
# Energy spectrogram variable names:  
# - elx_pef_hs/fs_nflux/eflux_omni  
# - elx_pef_hs/fs_nflux/eflux_para  
# - elx_pef_hs/fs_nflux/eflux_anti  
# - elx_pef_hs/fs_nflux/eflux_perp  
# 
# Pitch angle spectrogram variable names:
# - elx_pef_hs/fs_nflux/eflux_ch0-3

# #### 3.1 plot energy and pitch angle spectrogram

# load l2 half spin nflux data
epd_l2_hs_nflux = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe,
    level='l2', 
    type_='nflux', 
    fullspin=False)

# load l2 nflux full spin data
epd_l2_fs_nflux = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l2', 
    type_='nflux', 
    fullspin=True)

# load l2 half spin eflux data
epd_l2_hs_nflux = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l2', 
    type_='eflux', 
    fullspin=False)

# load l2 full spin eflux data
epd_l2_hs_nflux = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l2', 
    type_='eflux', 
    fullspin=True)

# plot energy spectrogram
tplot(['ela_pef_hs_nflux_omni', 'ela_pef_hs_nflux_para', 'ela_pef_hs_nflux_anti','ela_pef_hs_nflux_perp']) 

# plot pitch angle spectrogram
tplot(['ela_pef_hs_nflux_ch0', 'ela_pef_hs_nflux_ch1', 'ela_pef_hs_nflux_ch2', 'ela_pef_hs_nflux_ch3'])

# #### 3.2 add loss cone line to pitch angle spectrogram plot

options('ela_pef_hs_LCdeg','thick', 3)
options('ela_pef_hs_LCdeg','line_style', 'solid_line')
options('ela_pef_hs_antiLCdeg','thick', 3)
options('ela_pef_hs_antiLCdeg','line_style', 'dash')

store_data('ela_pef_hs_nflux_ch0_LC', data=['ela_pef_hs_nflux_ch0', 'ela_pef_hs_LCdeg', 'ela_pef_hs_antiLCdeg'])
tplot('ela_pef_hs_nflux_ch0_LC')

# #### 3.3 modify tolerance angle for energy spectrogram

# There are two tolerance angles for energy spectrogram:
# - Espec_LCfatol: tolerance angle for para and anti flux. A positive value makes the loss cone/antiloss cone smaller by specified amount. Default is 22.25 deg.
# - Espec_LCfptol: tolerance angle for perp flux. A negative value means a wider angle for perp flux by specified amount. Default is -11 deg.

epd_l2_hs_nflux = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l2', 
    type_='nflux', 
    fullspin=False,
    Espec_LCfatol=15,
    Espec_LCfptol=-20, 
    )
tplot(['ela_pef_hs_nflux_omni', 'ela_pef_hs_nflux_para', 'ela_pef_hs_nflux_anti', 'ela_pef_hs_nflux_perp'])

# #### 3.4 modify energy channels for pitch angle spectrogram
# Energy channel table:
# | energy_channel  | energy_range (keV) | energy_midbin (keV)|
# |:-----|:------:|-----:|
# | 0   | 50-80     | 63.2     |
# | 1   | 80-120    | 97.9     |
# | 2   | 120-160   | 138.5    |
# | 3   | 160-210   | 183.3    |
# | 4   | 210-270   | 238.1    |
# | 5   | 270-345   | 305.2    |
# | 6   | 345-430   | 385.1    |
# | 7   | 430-630   | 520.4    |
# | 8   | 630-900   | 752.9    |
# | 9   | 900-1300  | 1081.6   |
# | 10  | 1300-1800 | 1529.7   |
# | 11  | 1800-2500 | 2121.3   |
# | 12  | 2500-3350 | 2893.9   |
# | 13  | 3350-4150 | 3728.6   |
# | 14  | 4150-5800 | 4906.1   |
# | 15  | 5800+     | 6500.0   |
# 
# There are two ways to set energy channels for pitch angel spectrogram.
# 
# Examples of specified energy bins:  
# - PAspec_energybins = [(0,2), (3,5), (6,8), (9,15)] (default)
# 
# Examples of specified energy channels: 
# - PAspec_energies = [(50.,160.), (160.,345.), (345.,900.), (900.,7000.)]
# 
# 
# If both 'PAspec_energybins' and 'PAspec_energies' are set, 'PAspec_energybins' takes precedence.

epd_l2_hs_nflux = pyspedas.elfin.epd(
    trange=trange, 
    probe=probe, 
    level='l2', 
    type_='nflux', 
    fullspin=False,
    PAspec_energybins = [(0,3), (4,8)]
    )
print(epd_l2_hs_nflux)

tplot(['ela_pef_hs_nflux_ch0', 'ela_pef_hs_nflux_ch1'])

