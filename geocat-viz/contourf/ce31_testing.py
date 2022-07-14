###############################################################################
# Import Packages:
import numpy as np
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from cartopy.mpl.gridliner import LongitudeFormatter, LatitudeFormatter

import geocat.datafiles as gdf
import geocat.viz as gv

###############################################################################
# Read in data:

# Open a netCDF data file using xarray default engine and load the data into xarrays
ds = xr.open_dataset(gdf.get('netcdf_files/h_avg_Y0191_D000.00.nc'),
                     decode_times=False)
# Extract a slice of the data
t = ds.T.isel(time=0, z_t=0).sel(lat_t=slice(-60, 30), lon_t=slice(30, 120))
u = t.interpolate_na(dim='lat_t', method='linear', fill_value='extrapolate')
###############################################################################
# Plot:

# Use geocat.viz utility function to create a contour plot
plot_ = gv.Contour(
    t,  # data
    w=10,  # width of plot
    h=8,  # height of plot
    contour_lines=False,
    xlim=(30, 120),
    ylim=(-60, 30),
    cb_shrink=0.75,
    cb_orientation="vertical",  # orientation of colorbar
    cb_draw_edges=True,  # draw edges between colors in colorbar
    cb_tick_labels=np.arange(0, 32, 2),  # colorbar tick labels
    cb_ticks=np.arange(0, 32, 2),  # colorbar tick locations
    levels=np.linspace(0, 31, 40),
    main_title_fontsize=23,
    left_title_fontsize=23,
    right_title_fontsize=23,
    land_on=True,
    main_title="30-degree major and 10-degree minor ticks")

# Add in other customizations that are not possible with gv.Contour function
# Get current axis
ax = plt.gca()

# Customize tick length and width
ax.tick_params(axis='both', which='minor', length=8, width=1)
ax.tick_params(axis='both', which='major', length=15, width=1.1)

# Show the plot
plot_.show()
