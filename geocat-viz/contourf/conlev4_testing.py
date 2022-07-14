###############################################################################
# Import packages:
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from cartopy.mpl.gridliner import LongitudeFormatter, LatitudeFormatter

import cartopy.crs as ccrs
import geocat.datafiles as gdf
import geocat.viz as gv

###############################################################################
# Read in data:

# Open a netCDF data file using xarray default engine and load the data into xarrays
ds = xr.open_dataset(gdf.get("netcdf_files/b003_TS_200-299.nc"),
                     decode_times=False)
x = ds.TS

# Apply mean reduction from coordinates as performed in NCL's dim_rmvmean_n_Wrap(x,0)
# Apply this only to x.isel(time=0) because NCL plot plots only for time=0
newx = x.mean('time')
newx = x.isel(time=0) - newx

# Fix the artifact of not-shown-data around 0 and 360-degree longitudes
newx = gv.xr_add_cyclic_longitudes(newx, "lon")

###############################################################################
# Plot:

fplot = gv.Contour(
    newx,
    w=11,
    h=7,
    cb_shrink=0.8,
    contour_lines=False,
    levels=np.arange(-14, 16, 2),
    cb_tick_labels=np.arange(-12, 13, 2),
    cb_ticks=np.arange(-12, 13, 2),
    right_title='K',
    left_title="Anomalies: Surface Temperature",
)

ax = plt.gca()
# Remove degree symbol from tick labels
ax.yaxis.set_major_formatter(LatitudeFormatter(degree_symbol=''))
ax.xaxis.set_major_formatter(LongitudeFormatter(degree_symbol=''))

fplot.show()