# # Van Allen Probes RBSPICE
# 
# This notebook is based on the IDL crib sheet in SPEDAS:
# general/missions/rbsp/rbspice/rbsp_load_rbspice_crib.pro
# 
# The prime RBSPICE scientific products are: 
# - TOFxEH proton spectra
# - TOFxEnonH helium spectra
# - TOFxEnonH oxygen spectra
# - TOFxPHHHELT proton spectra
# - TOFxPHHHELT oxygen spectra

!pip install pyspedas

import pyspedas
from pytplot import tplot

probe = 'a'
prefix = 'rbsp'+probe
trange = ['2015-10-16', '2015-10-17']
level = 'l3'

# load TOFxEH (proton) data:

pyspedas.rbsp.rbspice(probe=probe, trange=trange, datatype='TOFxEH', level = level)

# plot the H+ flux for all channels

tplot('rbspa_rbspice_l3_TOFxEH_proton_omni_spin')

from pyspedas.rbsp.rbspice_lib.rbsp_rbspice_pad import rbsp_rbspice_pad

# calculate the PAD for 48-106keV protons

rbsp_rbspice_pad(probe=probe, datatype='TOFxEH', energy=[48, 106], bin_size = 15, level = level)

# calculate the PAD for 105-250 keV protons

rbsp_rbspice_pad(probe=probe, datatype='TOFxEH', energy=[105, 250], bin_size = 15, level = level)

# plot the PAD for 48-106keV (top), 105-250 keV (bottom) protons

tplot(['rbspa_rbspice_l3_TOFxEH_proton_omni_48-106keV_pad',
       'rbspa_rbspice_l3_TOFxEH_proton_omni_105-250keV_pad'])

# load TOFxEnonH (helium and oxygen) data:

pyspedas.rbsp.rbspice(probe=probe, trange=trange, datatype='TOFxEnonH', level = level)

# plot the He++ flux for all channels

tplot('rbspa_rbspice_l3_TOFxEnonH_helium_omni_spin')

# plot the O+ flux for all channels

tplot('rbspa_rbspice_l3_TOFxEnonH_oxygen_omni_spin')

# load TOFxPHHHELT (proton and oxygen) data:

pyspedas.rbsp.rbspice(probe=probe, trange=trange, datatype='TOFxPHHHELT', level=level)

# plot the TOFxPHHHELT proton spectra

tplot('rbspa_rbspice_l3_TOFxPHHHELT_proton_omni_spin')

# plot the TOFxPHHHELT oxygen spectra

tplot('rbspa_rbspice_l3_TOFxPHHHELT_oxygen_omni_spin')

# calculate the TOFxPHHHELT PAD for protons

rbsp_rbspice_pad(probe=probe, datatype='TOFxPHHHELT', energy=[0, 30], bin_size = 15, level=level)

tplot(['rbspa_rbspice_l3_TOFxPHHHELT_proton_omni_spin',
       'rbspa_rbspice_l3_TOFxPHHHELT_proton_omni_0-30keV_pad_spin'])



