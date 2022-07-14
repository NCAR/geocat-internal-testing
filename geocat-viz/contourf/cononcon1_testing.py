################################################################################
# Import packages:

import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

import geocat.datafiles as gdf
import geocat.viz as gv

###############################################################################
# Read in data:

# Open a netCDF data file using xarray default engine and load the data into xarrays
ds = xr.open_dataset(gdf.get("netcdf_files/mxclim.nc"))
# Extract variables
U = ds.U[0, :, :]
V = ds.V[0, :, :]

################################################################################
# Plot:

gplot = gv.Contour(
    U,
    type="press_height",
    line_color="red",
    line_width=1,
    levels=17,
    contour_fill=False,
    main_title="Ensemble Average 1987-89",
    draw_contour_labels=True,
    contour_label_box=True,
    minor_per_major=[4, None],
    #raxis_ticks=np.arange(4, 30, 4),
    yticks=[1000, 850, 700, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10],
    ytick_labels=[
        "1000", "850", "700", "500", "400", "300", "250", "200", "150", "100",
        "70", "50", "30", "10"
    ],
)

hplot = gv.Contour(
    V,
    overlay=gplot,
    levels=np.linspace(-2.8, 3.2, 16),
    contour_labels=np.linspace(-2.8, 3.2, 16),
    line_color="blue",
    line_width=1,
    draw_contour_labels=True,
)

gplot.show()