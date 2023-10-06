!pip install pyspedas

exit()

import pyspedas

from pyspedas.cluster.load_csa import load_csa

load_csa(datatypes=['CP_CIS-HIA_PAD_HS_MAG_IONS_PF'])

from pytplot import get_data, store_data, options, tplot

data = get_data('Differential_Particle_Flux__C1_CP_CIS_HIA_PAD_HS_MAG_IONS_PF')
metadata = get_data('Differential_Particle_Flux__C1_CP_CIS_HIA_PAD_HS_MAG_IONS_PF', metadata=True)

metadata['CDF']['VATT']

# So the pitch angles are:

data.v1

# And the energies are:

data.v2

data.y.shape

# Create time vs. energy by summing over the pitch angle dimension:

import numpy as np

en_flux = np.nansum(data.y, axis=1)

en_flux.shape

store_data('diff_part_flux', data={'x': data.times,
                                   'y': en_flux,
                                   'v': data.v2})

options('diff_part_flux', 'spec', True)
options('diff_part_flux', 'ylog', True)
options('diff_part_flux', 'zlog', True)
options('diff_part_flux', 'ztitle', 'cm^-2 s^-1 sr^-1 Kev^-1')

tplot('diff_part_flux')

# Create pitch angle distribution:

pa_flux = np.nansum(data.y, axis=2)

pa_flux.shape

store_data('diff_part_flux_pa', data={'x': data.times,
                                      'y': pa_flux,
                                      'v': data.v1})

options('diff_part_flux_pa', 'spec', True)
options('diff_part_flux_pa', 'zlog', True)

tplot('diff_part_flux_pa')



