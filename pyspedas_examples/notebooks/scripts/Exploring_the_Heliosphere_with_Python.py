# # Exploring the Heliosphere with Python
# 
# This notebook demonstrates loading and plotting science data in the Heliosphere using PySPEDAS and SunPy. It includes simple examples from 17 missions, as well as data from ground magnetometers and geomagnetic indices.
# 
# **By Eric Grimes, UCLA - Earth, Planetary, and Space Sciences/Institute of Geophysics and Planetary Physics**
# 
# egrimes(at)igpp.ucla.edu
# 
# Last updated: June 20, 2023
# 
# Notes:
# - I tried to start with the Sun, and go all the way to the ground; so solar data are first and ground data are last (with a short detour to Mars)
# - For the most part, the data shown are from March 27, 2017; exceptions are Parker Solar Probe and Solar Orbiter (which had not launched yet, so more recent examples are used).
# - Only a few data products are loaded/plotted for each spacecraft in this notebook, so not all spacecraft/instruments/data products are demonstrated. For a list of the full capabilities, please see the documentation:
# 
# PySPEDAS: https://pyspedas.readthedocs.io/
# 
# SunPy: https://sunpy.org/
# 
# - The SunPy examples were taken from the SunPy examples gallery, with minor changes for our event
# - Other Python in Heliophysics Community (PyHC) projects used in this notebook:
# 
# cdflib: https://cdflib.readthedocs.io/
# 
# PyTplot: https://pytplot.readthedocs.io/
# 
# Geopack: https://github.com/tsssss/geopack
# 
# HAPI client: https://github.com/hapi-server/client-python

# >[Exploring the Heliosphere with Python](#scrollTo=7of2f7In4ju9)
# 
# >>[Solar and Heliospheric Observatory satellite (SOHO)](#scrollTo=63VP0tdm7sr5)
# 
# >>[Solar Dynamics Observatory (SDO)](#scrollTo=LBbTEsRU8iJP)
# 
# >>[Parker Solar Probe](#scrollTo=YI5IRRJTIgoh)
# 
# >>[Solar Orbiter](#scrollTo=dOmstkoqI6G0)
# 
# >>[Advanced Composition Explorer (ACE)](#scrollTo=repQs8PglYkK)
# 
# >>[Deep Space Climate Observatory (DSCOVR)](#scrollTo=uNUdKsUhkzL7)
# 
# >>[Solar Terrestrial Relations Observatory (STEREO)](#scrollTo=r-7y4swZcPan)
# 
# >>[Mars Atmosphere and Volatile Evolution (MAVEN)](#scrollTo=GsHDJoLzlzlc)
# 
# >>[OMNI](#scrollTo=P8o9_s4NlpUJ)
# 
# >>[Kyoto Dst](#scrollTo=kvwReQcYoTga)
# 
# >>[Geotail](#scrollTo=3aKOINyJbquI)
# 
# >>[Magnetospheric Multiscale (MMS)](#scrollTo=KCUfQYIElyri)
# 
# >>[Cluster](#scrollTo=EcsRGbTs3Mfd)
# 
# >>[Time History of Events and Macroscale Interactions during Substorms (THEMIS)](#scrollTo=Fz40PKL4cGQF)
# 
# >>[Van Allen Probes (formerly RBSP)](#scrollTo=DDlc_B52b5Sf)
# 
# >>[Arase](#scrollTo=5mR0VVLcmQtv)
# 
# >>[Geopack (Tsyganenko field models)](#scrollTo=hgmYsl5IzQ7N)
# 
# >>[Two Wide-Angle Imaging Neutral-Atom Spectrometers (TWINS)](#scrollTo=PAY8dDZImU1N)
# 
# >>[Polar Operational Environmental Satellites (POES)](#scrollTo=nWCmey5BmYRu)
# 
# >>[Swarm](#scrollTo=85RU5QRK4CKY)
# 
# >>[Spherical Elementary Currents (SECS)](#scrollTo=IwQmONDMn14b)
# 
# >>[Equivalent Ionospheric Currents (EICS)](#scrollTo=WyuIzxA_oEDq)
# 
# >>[All Sky Imager data](#scrollTo=cS5ZJ8DQocJQ)
# 
# >>[Ground magnetometer data](#scrollTo=YupmshpcoX-l)
# 
# >>[Magnetic Induction Coil Array (MICA)](#scrollTo=BeVmdYo4oe5U)
# 
# >>[Resources](#scrollTo=CJRw4BVBMVIP)
# 
# >>>[PyTplot Basics](#scrollTo=CJRw4BVBMVIP)
# 
# >>>[Loading Data](#scrollTo=CJRw4BVBMVIP)
# 
# >>>[Plotting Data](#scrollTo=CJRw4BVBMVIP)
# 
# >>>[Dates and Times](#scrollTo=CJRw4BVBMVIP)
# 
# >>>[Coordinate Transformations](#scrollTo=CJRw4BVBMVIP)
# 
# >>>[Analysis](#scrollTo=CJRw4BVBMVIP)
# 
# >>>[Documentation](#scrollTo=CJRw4BVBMVIP)
# 
# 

# Install PySPEDAS and all its required dependencies:

!pip install pyspedas

# Install sunpy and some related packages needed for SOHO example:

!pip install sunpy
!pip install zeep
!pip install drms

# Install basemap package (needed for SECS and EICS examples):

!pip install basemap

# Restart the session to pick up any newly installed packages:

exit()

trange = ['2017-03-27', '2017-03-28']

# ## Solar and Heliospheric Observatory satellite (SOHO) <a class="anchor" id="soho"></a>
# 
# The joint NASA-ESA [Solar & Heliospheric Observatory](https://www.nasa.gov/mission_pages/soho/index.html) mission -- SOHO -- was designed to study the Sun inside out, from its internal structure, to the extensive outer atmosphere, to the solar wind that it blows across the solar system. 

# 
# Create a figure of LASCO C2 data

import os

import matplotlib.pyplot as plt

import astropy.time
import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.visualization import ImageNormalize, SqrtStretch

import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a

timerange = a.Time('2017/03/27 06:00', '2017/03/27 06:01')
instrument = a.Instrument.lasco
detector = a.Detector.c2
result = Fido.search(timerange, instrument, detector)
downloaded_files = Fido.fetch(result)

lascomap = sunpy.map.Map(downloaded_files[0])
fig = plt.figure()
lascomap.plot()

plt.show()

# Load the CELIAS data

import pyspedas

pyspedas.soho.celias(trange=['2017-03-27', '2017-03-28'])

# Plot the proton velocity, density and SOHO spacecaft position in GSE coordinates, as a function of time:
# 
# 

from pytplot import tplot

tplot(['V_p', 'N_p', 'GSE_POS'])

# Load the COSTEP data:

pyspedas.soho.costep(trange=['2017-03-27', '2017-03-28'], time_clip=True, datatype='ephin_l3i-1min')

# Plot the COSTEP proton intensity:

tplot('P_int')

pyspedas.soho.erne(trange=trange)

from pytplot import options

options('PH', 'spec', True)
options('PH', 'ylog', True)
options('PH', 'zlog', True)

tplot(['PH'])

# ## Solar Dynamics Observatory (SDO) <a class="anchor" id="sdo"></a>
# 
# The [Solar Dynamics Observatory (SDO)](https://sdo.gsfc.nasa.gov/mission/) is designed to help us understand the Sun's influence on Earth and Near-Earth space by studying the solar atmosphere on small scales of space and time and in many wavelengths simultaneously.

# Create an HMI magnetogram

result = Fido.search(a.Time('2017/03/27 06:00', '2017/03/27 06:01'),
                     a.Instrument.hmi, a.Physobs.los_magnetic_field)
downloaded_file = Fido.fetch(result)

hmi_map = sunpy.map.Map(downloaded_file[0])
fig = plt.figure()
hmi_map.plot()

plt.show()

# Create an image from Atmospheric Imaging Assembly (AIA)

t0 = astropy.time.Time('2017-03-27T06:00:01', scale='utc', format='isot')
q = Fido.search(
    a.Instrument.aia,
    a.Physobs.intensity,
    a.Wavelength(171*u.angstrom),
    a.Time(t0, t0 + 13*u.s),
)
m = sunpy.map.Map(Fido.fetch(q))

m_cutout = m.submap(
    SkyCoord(-700*u.arcsec, -175*u.arcsec, frame=m.coordinate_frame),
    top_right=SkyCoord(150*u.arcsec, 575*u.arcsec, frame=m.coordinate_frame),
)
m_cutout.peek()

# ## Parker Solar Probe
# 
# NASA's [Parker Solar Probe](https://www.nasa.gov/content/goddard/parker-solar-probe-humanity-s-first-visit-to-a-star) mission is revolutionizing our understanding of the Sun, where changing conditions can propagate out into the solar system, affecting Earth and other worlds. Parker Solar Probe travels through the Sun’s atmosphere, closer to the surface than any spacecraft before it, facing brutal heat and radiation conditions to provide humanity with the closest-ever observations of a star.
# 
# Load and plot PSP FIELDS data (note: this example came from the team's IDL crib sheet):

time_range = ['2019-04-03', '2019-04-03/12:00']

pyspedas.psp.fields(datatype='mag_rtn_4_sa_per_cyc',
                    trange=time_range,
                    time_clip=True)
pyspedas.psp.fields(datatype='rfs_hfr',
                    varnames='psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2',
                    trange=time_range,
                    time_clip=True)
pyspedas.psp.fields(datatype='rfs_lfr',
                    varnames='psp_fld_l2_rfs_lfr_auto_averages_ch0_V1V2',
                    trange=time_range,
                    time_clip=True)

from pytplot import tplot, options

options('psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2', 'ylog', True)
options('psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2', 'zlog', True)
options('psp_fld_l2_rfs_lfr_auto_averages_ch0_V1V2', 'ylog', True)
options('psp_fld_l2_rfs_lfr_auto_averages_ch0_V1V2', 'zlog', True)

tplot(['psp_fld_l2_mag_RTN_4_Sa_per_Cyc',
       'psp_fld_l2_rfs_hfr_auto_averages_ch0_V1V2',
       'psp_fld_l2_rfs_lfr_auto_averages_ch0_V1V2'], ysize=12)

# ## Solar Orbiter
# 
# [Solar Orbiter](https://www.nasa.gov/content/solar-orbiter-science) is a space mission of international collaboration between ESA and NASA to study the Sun, its outer atmosphere and what drives the constant outflow of solar wind that affects Earth. 

pyspedas.solo.mag(trange=['2020-07-22', '2020-07-23'])


pyspedas.solo.swa(trange=['2020-07-22', '2020-07-23'], datatype='pas-eflux')

tplot(['B_RTN', 'eflux'])

# ## Advanced Composition Explorer (ACE)
# 
# The [Advanced Composition Explorer](https://www.nasa.gov/ace), or ACE, observes and measures magnetic fields and particles in space, from a vantage point approximately 1/100 of the distance from Earth to the Sun.

mfi_vars = pyspedas.ace.mfi(trange=trange)
swe_vars = pyspedas.ace.swe(trange=trange)

tplot(['BGSEc', 'Vp', 'Tpr'])

# ## Deep Space Climate Observatory (DSCOVR)
# 
# The [Deep Space Climate Observatory](https://www.nesdis.noaa.gov/current-satellite-missions/currently-flying/dscovr-deep-space-climate-observatory), or DSCOVR, was launched in February of 2015, and maintains the nation's real-time solar wind monitoring capabilities, which are critical to the accuracy and lead time of NOAA's space weather alerts and forecasts. 

mag_vars = pyspedas.dscovr.mag(trange=trange)
orb_vars = pyspedas.dscovr.orb(trange=trange)

tplot(['dsc_h0_mag_B1GSE', 'dsc_orbit_GSE_POS'])

# ## Solar Terrestrial Relations Observatory (STEREO)
# 
# The [Solar TErrestrial RElations Observatory](https://www.nasa.gov/directorates/heo/scan/services/missions/solarsystem/STEREO.html) (STEREO) consists of two nearly identical spacecraft that seek to establish a one-to-one cause and effect relationship between coronal mass ejections as seen at the sun, the acceleration of particles in interplanetary space, and terrestrial consequences.

mag_vars = pyspedas.stereo.mag(trange=trange)
plastic_vars = pyspedas.stereo.plastic(trange=trange)

tplot(['BFIELD', 'proton_number_density', 'proton_bulk_speed', 'proton_temperature'])

# ## Mars Atmosphere and Volatile Evolution (MAVEN)
# 
# The [Mars Atmosphere and Volatile EvolutioN](https://www.nasa.gov/mission_pages/maven/overview/index.html) (MAVEN) mission is part of NASA's Mars Scout program. Launched in Nov. 2013, the mission explores the Red Planet’s upper atmosphere, ionosphere and interactions with the sun and solar wind.

mag_vars = pyspedas.maven.mag(trange=trange, spdf=True)
swe_vars = pyspedas.maven.swea(trange=trange, spdf=True)
swi_vars = pyspedas.maven.swia(trange=trange, spdf=True)

swi_vars

options('spectra_diff_en_fluxes', 'ylog', True)
options('spectra_diff_en_fluxes', 'zlog', True)
options('diff_en_fluxes', 'ylog', True)
options('diff_en_fluxes', 'zlog', True)
options('diff_en_fluxes', 'spec', True)

tplot(['OB_B', 'diff_en_fluxes', 'spectra_diff_en_fluxes'], ysize=10)

# ## OMNI 
# 
# Solar wind [magnetic field and plasma data](https://omniweb.gsfc.nasa.gov/index.html) at Earth's Bow Shock Nose (BSN), also geomagnetic activity indices and energetic proton fluxes.

omni_vars = pyspedas.omni.data(trange=['2017-03-01', '2017-04-01'], time_clip=False)

tplot(['BX_GSE', 'BY_GSE', 'BZ_GSE', 'flow_speed', 'SYM_H'])

# ## Kyoto Dst
# 
# The hourly Dst index, from the [WDC for Geomagnetism](https://wdc.kugi.kyoto-u.ac.jp/dstdir/), Kyoto, Japan; useful indicator of geomagnetic storm intensity

dst_vars = pyspedas.kyoto.dst(trange=['2017-03-01', '2017-04-01'])

tplot(['kyoto_dst', 'SYM_H'])

# ## Geotail
# 
# The [Geotail](https://solarsystem.nasa.gov/missions/geotail/in-depth/) mission was a joint project of Japan’s Institute of Space and Astronautical Science (ISAS) and later, from 2003, the Japan Aerospace Exploration Agency (JAXA) and NASA. 
# 
# 
# Geotail’s goal was to study the structure and dynamics of the long tail region of Earth’s magnetosphere, which is created on the nightside of Earth by the solar wind. During active periods, the tail couples with the near-Earth magnetosphere, and often releases energy that is stored in the tail, activating auroras in the polar ionosphere.

mgf_vars = pyspedas.geotail.mgf(trange=trange)
cpi_vars = pyspedas.geotail.cpi(trange=trange)

tplot(['IB_vector', 'SW_P_Den', 'SW_V'])

# ## Magnetospheric Multiscale (MMS)
# 
# The [Magnetospheric Multiscale](https://mms.gsfc.nasa.gov/) (MMS) mission studies the mystery of how magnetic fields around Earth connect and disconnect, explosively releasing energy via a process known a magnetic reconnection.

mec_vars = pyspedas.mms.mec(trange=trange)
fgm_vars = pyspedas.mms.fgm(trange=trange)
feeps_vars = pyspedas.mms.feeps(trange=trange)

tplot(['mms1_epd_feeps_srvy_l2_electron_intensity_omni',
       'mms1_fgm_b_gse_srvy_l2_bvec'])

from pyspedas.mms.particles.mms_part_slice2d import mms_part_slice2d

mms_part_slice2d(trange=['2017-03-27/11:00', '2017-03-27/11:30'], instrument='hpca', species='hplus')

# ## Cluster
# 
# Studying how the solar wind affects Earth, [Cluster](https://www.esa.int/Science_Exploration/Space_Science/Cluster_overview2) spacecraft pass in and out of our planet's magnetic field to make a detailed investigation of how the Sun and Earth interact.

cl_vars = pyspedas.cluster.fgm(trange=trange, probe=['1', '2', '3', '4'])

tplot('B_xyz_gse__C?_UP_FGM', ysize=12)

# ## Time History of Events and Macroscale Interactions during Substorms (THEMIS)
# 
# The [Time History of Events and Macroscale Interactions during Substorms](https://www.nasa.gov/mission_pages/themis/mission/index.html) —THEMIS — mission studies how mass and energy move through the near-Earth environment in order to determine the physical processes initiating auroras.

sta_vars = pyspedas.themis.state(probe='d', trange=trange)
fgm_vars = pyspedas.themis.fgm(probe='d', trange=trange)
gmom_vars = pyspedas.themis.gmom(probe='d', trange=trange)

tplot(['thd_fgs_gse', 'thd_ptiff_velocity_gse', 'thd_pteff_density'], ysize=8)

# ## Van Allen Probes (formerly RBSP)
# 
# NASA's [Van Allen Probes](https://www.nasa.gov/mission_pages/rbsp/mission/index.html) mission was designed to help us understand the Sun’s influence on Earth and Near-Earth space by studying the Earth’s radiation belts on various scales of space and time.

emfisis_vars = pyspedas.rbsp.emfisis(trange=['2017-03-27/15:00', '2017-03-27/16:00'], 
                                     datatype='magnetometer', 
                                     level='l3', 
                                     time_clip=True)
efw_vars = pyspedas.rbsp.efw(trange=['2017-03-27/15:00', '2017-03-27/16:00'], 
                             level='l3',
                             time_clip=True)
rbspice_vars = pyspedas.rbsp.rbspice(trange=['2017-03-27/15:00', '2017-03-27/16:00'], 
                                     time_clip=True)

tplot(['Mag', 'rbspa_rbspice_l3_TOFxEH_proton_omni'])

# ## Arase
# 
# The [Arase](https://global.jaxa.jp/projects/sas/erg/) mission aims at elucidating how highly charged electrons have been born while they generate and vanish repeatedly along with space storms caused by the disturbance of solar wind caused by space storms, and how space storms are developed.
# 
# 

pyspedas.erg.orb(trange=trange)
pyspedas.erg.mgf(trange=trange)
pyspedas.erg.mepe(trange=trange)
pyspedas.erg.lepe(trange=trange)

tplot(['erg_mgf_l2_mag_8sec_sm', 
       'erg_mepe_l2_omniflux_FEDO'])

# ## Geopack (Tsyganenko field models)

from pyspedas.geopack import tt89

# convert the Arase position data to km (from Re)
from pyspedas import tkm2re
tkm2re('erg_orb_l2_pos_gsm', km=True)

tt89('mms1_mec_r_gsm')
tt89('thd_pos_gsm')
tt89('erg_orb_l2_pos_gsm_km')

tplot(['mms1_fgm_b_gsm_srvy_l2_bvec', # MMS measured field
       'mms1_mec_r_gsm_bt89', # T89 at the MMS1 position
       'thd_fgs_gsm', # THEMIS measured field
       'thd_pos_gsm_bt89', # T89 at the THEMIS-c position
       'erg_mgf_l2_mag_8sec_gsm', # ERG measured field
       'erg_orb_l2_pos_gsm_km_bt89'], ysize=15) # T89 at the ERG position

# ## Two Wide-Angle Imaging Neutral-Atom Spectrometers (TWINS)
# 
# The identical [TWINS-A and TWINS-B observatories](http://science.nasa.gov/missions/twins/) provide a new capability for stereoscopically imaging the magnetosphere

lad_vars = pyspedas.twins.lad(trange=trange)
eph_vars = pyspedas.twins.ephemeris(trange=trange)

tplot(['lad1_data', 'lad2_data', 'FSCGSM'], ysize=9)

# ## Polar Operational Environmental Satellites (POES)

sem_vars = pyspedas.poes.sem(trange=['2017-03-27', '2017-03-28'])

options('ted_pro_tel0_low_eflux', 'ylog', False)
options('ted_pro_tel30_low_eflux', 'ylog', False)

from pytplot import tplot
tplot('ted_pro_tel*_low_eflux', ysize=8)

# ## Swarm

swarm_vars = pyspedas.swarm.mag(trange=['2017-03-27/06:00', '2017-03-27/08:00'])

tplot('swarma_B_VFM', var_label=['swarma_Longitude', 'swarma_Latitude'], ysize=9)

# ## Spherical Elementary Currents (SECS)

from pyspedas.secs.makeplots import make_plots

# set your content directory for SECS/EICS data
from pyspedas.secs.config import CONFIG
CONFIG['plots_dir'] = '/content/'

pyspedas.secs.data(trange=trange, 
                   resolution=10,
                   dtype='SECS', 
                   no_download=False, 
                   downloadonly=False, 
                   out_type='df')

make_plots(dtype='SECS', 
           dtime='2017-03-27/06:00:00', 
           vplot_sized=True, 
           contour_den=201, 
           s_loc=False, 
           quiver_scale=30)

# ## Equivalent Ionospheric Currents (EICS)
# 

pyspedas.secs.data(trange=trange, 
                   resolution=10,
                   dtype='EICS', 
                   no_download=False, 
                   downloadonly=False, 
                   out_type='df')

make_plots(dtype='EICS', 
           dtime='2017-03-27/06:00:00', 
           vplot_sized=True, 
           contour_den=201, 
           s_loc=False, 
           quiver_scale=30)

# ## All Sky Imager data

ask_vars = pyspedas.themis.ask(trange=trange)

tplot(['thg_ask_atha', 'thg_ask_chbg', 'thg_ask_inuv'])

# ## Ground magnetometer data

pyspedas.themis.gmag(trange=trange)

tplot(['thg_mag_atha', 'thg_mag_chbg', 'thg_mag_inuv'], ysize=8)

# Subtract the median from the ground mag data

from pyspedas import subtract_median

subtract_median(['thg_mag_atha', 'thg_mag_chbg', 'thg_mag_inuv'])

options('thg_mag_atha-m', 'yrange', [-400, 400])
options('thg_mag_chbg-m', 'yrange', [-400, 400])
options('thg_mag_inuv-m', 'yrange', [-400, 400])

tplot(['thg_mag_atha-m', 'thg_mag_chbg-m', 'thg_mag_inuv-m'], ysize=8)

# ## Magnetic Induction Coil Array (MICA)

nal_vars = pyspedas.mica.induction(site='NAL', trange=trange)


tplot('spectra_?_1Hz_NAL')

# ## Resources
# 
# ### PyTplot Basics
# - [Introduction to PyTplot](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/Introduction_to_PyTplot.ipynb)
# 
# ### Loading Data
# - [MMS examples](https://github.com/spedas/mms-examples/tree/master/basic)
# - [THEMIS examples](https://github.com/spedas/themis-examples/tree/main/basic)
# - [Load data from HAPI servers](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PySPEDAS_loading_data_from_HAPI_servers.ipynb)
# 
# ### Plotting Data
# - [Annotations](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_annotations.ipynb)
# - [Range options](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_range_options.ipynb)
# - [Spectrogram options](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_spectrogram_options.ipynb)
# - [Legend options](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_legend_options.ipynb)
# - [Markers and symbols](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_markers_and_symbols.ipynb)
# - [Error bars](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_error_bars.ipynb)
# - [Pseudo variables](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_pseudo_variables.ipynb)
# - [Highlight intervals and vertical bars](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/PyTplot_highlight_intervals_and_vertical_bars.ipynb)
# 
# ### Dates and Times
# - [Working with dates and times](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/Working_with_dates_and_times_with_PySPEDAS_PyTplot.ipynb)
# 
# ### Coordinate Transformations
# - [Coordinate transformations](https://github.com/spedas/pyspedas_examples/blob/master/pyspedas_examples/notebooks/Coordinate_transformations_with_OMNI_data.ipynb)
# - [Boundary normal (LMN) coordinates](https://github.com/spedas/mms-examples/blob/master/advanced/MMS_LMN_coordinate_transformation.ipynb)
# - [Quaternion transformations with SpacePy](https://github.com/spedas/mms-examples/blob/master/basic/MMS_quaternion_coordinate_transformations.ipynb)
# 
# ### Analysis
# - [Plasma calculations with PlasmaPy](https://github.com/spedas/mms-examples/blob/master/advanced/Plasma%20calculations%20with%20PlasmaPy.ipynb)
# - [Poynting flux with MMS data](https://github.com/spedas/mms-examples/blob/master/advanced/Poynting_flux_with_MMS_data.ipynb)
# - [Plasma beta with MMS data](https://github.com/spedas/mms-examples/blob/master/basic/Plasma%20Beta%20with%20FGM%20and%20FPI%20data.ipynb) (note: the PlasmaPy notebook above shows a much easier method)
# - [Curlometer calculations](https://github.com/spedas/mms-examples/blob/master/basic/Curlometer%20Technique.ipynb)
# - [Neutral sheet models](https://github.com/spedas/mms-examples/blob/master/advanced/MMS_neutral_sheet_models.ipynb)
# - [Wave polarization calculations](https://github.com/spedas/mms-examples/blob/master/advanced/Wave_polarization_using_SCM_data.ipynb)
# - [Dynamic power spectra calculations](https://github.com/spedas/mms-examples/blob/master/basic/Search-coil%20Magnetometer%20(SCM).ipynb)
# - [2D slices of MMS distribution functions](https://github.com/spedas/mms-examples/blob/master/advanced/Generate_2D_slices_of_FPI_and_HPCA_data.ipynb)
# - [Generating spectrograms and moments from MMS distribution functions](https://github.com/spedas/mms-examples/blob/master/advanced/Generate%20spectrograms%20and%20moments%20with%20mms_part_getspec.ipynb)
# 
# 
# ### Documentation
# - [Advanced Composition Explorer (ACE)](https://pyspedas.readthedocs.io/en/latest/ace.html)
# - [Akebono](https://pyspedas.readthedocs.io/en/latest/akebono.html)
# - [Arase (ERG)](https://pyspedas.readthedocs.io/en/latest/erg.html)
# - [Cluster](https://pyspedas.readthedocs.io/en/latest/cluster.html)
# - [Colorado Student Space Weather Experiment (CSSWE)](https://pyspedas.readthedocs.io/en/latest/csswe.html)
# - [Communications/Navigation Outage Forecasting System (C/NOFS)](https://pyspedas.readthedocs.io/en/latest/cnofs.html)
# - [Deep Space Climate Observatory (DSCOVR)](https://pyspedas.readthedocs.io/en/latest/dscovr.html)
# - [Dynamics Explorer 2 (DE2)](https://pyspedas.readthedocs.io/en/latest/de2.html)
# - [Equator-S](https://pyspedas.readthedocs.io/en/latest/equator-s.html)
# - [Fast Auroral Snapshot Explorer (FAST)](https://pyspedas.readthedocs.io/en/latest/fast.html)
# - [Geotail](https://pyspedas.readthedocs.io/en/latest/geotail.html)
# - [Geostationary Operational Environmental Satellite (GOES)](https://pyspedas.readthedocs.io/en/latest/goes.html)
# - [Imager for Magnetopause-to-Aurora Global Exploration (IMAGE)](https://pyspedas.readthedocs.io/en/latest/image.html)
# - [Kyoto Dst Index](https://pyspedas.readthedocs.io/en/latest/kyoto.html)
# - [LANL](https://pyspedas.readthedocs.io/en/latest/lanl.html)
# - [Mars Atmosphere and Volatile Evolution (MAVEN)](https://pyspedas.readthedocs.io/en/latest/maven.html)
# - [Magnetic Induction Coil Array (MICA)](https://pyspedas.readthedocs.io/en/latest/mica.html)
# - [Magnetospheric Multiscale (MMS)](https://pyspedas.readthedocs.io/en/latest/mms.html)
# - [OMNI](https://pyspedas.readthedocs.io/en/latest/omni.html)
# - [Polar Orbiting Environmental Satellites (POES)](https://pyspedas.readthedocs.io/en/latest/poes.html)
# - [Polar](https://pyspedas.readthedocs.io/en/latest/polar.html)
# - [Parker Solar Probe (PSP)](https://pyspedas.readthedocs.io/en/latest/psp.html)
# - [Solar & Heliospheric Observatory (SOHO)](https://pyspedas.readthedocs.io/en/latest/soho.html)
# - [Solar Orbiter (SOLO)](https://pyspedas.readthedocs.io/en/latest/solo.html)
# - [Solar Terrestrial Relations Observatory (STEREO)](https://pyspedas.readthedocs.io/en/latest/stereo.html)
# - [Space Technology 5 (ST5)](https://pyspedas.readthedocs.io/en/latest/st5.html)
# - [Spherical Elementary Currents (SECS)](https://github.com/spedas/pyspedas/blob/master/pyspedas/secs/README.md)
# - [Swarm](https://github.com/spedas/pyspedas/blob/master/pyspedas/swarm/README.md)
# - [Time History of Events and Macroscale Interactions during Substorms (THEMIS)](https://pyspedas.readthedocs.io/en/latest/themis.html)
# - [Two Wide-Angle Imaging Neutral-Atom Spectrometers (TWINS)](https://pyspedas.readthedocs.io/en/latest/twins.html)
# - [Ulysses](https://pyspedas.readthedocs.io/en/latest/ulysses.html)
# - [Van Allen Probes (RBSP)](https://pyspedas.readthedocs.io/en/latest/rbsp.html)
# - [Wind](https://pyspedas.readthedocs.io/en/latest/wind.html)



