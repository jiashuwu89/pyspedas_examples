# # Working with dates and times with PySPEDAS/PyTplot
# 
# **By Eric Grimes, UCLA - Earth, Planetary, and Space Sciences; egrimes(at)igpp.ucla.edu**
# 
# This notebook includes examples of working with date/time values in PySPEDAS and PyTplot
# 

!pip install pyspedas

# Time values in PyTplot variables are stored internally as datetime64 objects.
# However, the PyTplot time conversion routines assume that numerical timestamps
# are represented as Unix times, in units of seconds.  (The conversions to and from
# the internal datetime64 representation are performed automatically in the store_data and
# get_data routines.)
# 
# https://en.wikipedia.org/wiki/Unix_time
# 
# We have routines for working with times, including:
# 
# `time_double`: convert a string to a unix time

from pyspedas import time_double

time_double('2015-10-16/13:06')

# This also accepts a list of time values

time_double(['2015-10-16/13:06', '2015-10-16/13:07:01'])

# The input format for the string is extremely flexible, e.g., 

time_double('Oct 16, 2015 at 13:06')

# To convert a unix time back to a string, use `time_string`

from pyspedas import time_string

time_string(1445000760.0)

# This also accepts lists of times, e.g., 

time_string([1445000760.0, 1445000821.0])

# To change the format of the output string, use the `fmt` option, e.g., 

time_string([1445000760.0, 1445000821.0], fmt='%Y-%m-%d/%H:%M:%S')

# Please see the strftime cheatsheet at https://strftime.org for possible formats.
# (Supported formats may vary depending on the platform being used.)

time_string([1445000760.0, 1445000821.0], fmt='%B %d, %Y at %H:%M')

# Finally, to convert to datetime objects, use `time_datetime`

from pyspedas import time_datetime

time_datetime(1445000760.0)

# Note that this routine also accepts strings

time_datetime('October 16, 2015 at 13:06')

# as well as lists:

time_datetime(['October 16, 2015 at 13:06', 'October 16, 2015 at 13:07'])

