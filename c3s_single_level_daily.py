import cdsapi
import numpy as np

# Specify years to download data for. These correspond to the year when the forecast was initialized, not the year of the forecast itself. 
# For example, a forecast initialized in May 1981 will be valid for May 1981 through April 1982.
fc_years = np.arange(1981,2026,1)

# Initialisation month. These are always a two-digit string, e.g., "05" for May.
fc_month = "05"

# Initialisation day. These are always a two-digit string, e.g., "01" for the first day of the month.
# For SEAS5, the only valid initialisation day is "01".
fc_day = "01"

# Specify forecast "center", e.g., ECMWF.
fc_center = "ecmwf"

# Specify forecast system, e.g., SEAS5. This is given a numeric identifier in the CDS API, e.g., SEAS5 is 51.
fc_system = "51"

# Variable to download. For example, "mean_sea_level_pressure" for MSLP.
fc_variable = "mean_sea_level_pressure"

# Forecast lead time in hours. 
# For example, "0/to/3672/by/24" for daily forecasts up to 153 days (3672 hours) after the initialisation date.
# Subdaily data are available every 12h. 
fc_leadtime = "0/to/3672/by/24"

# Forecast grid resolution in degrees. For example, "1.0/1.0" for 1 degree latitude by 1 degree longitude.
fc_grid = "1.0/1.0"

# Forecast area bounding box in degrees. For example, "90/-100/20/40" for a box covering the North Atlantic region.
# This goes from 90N to 20N latitude and from 100W to 40E longitude. The format is "north/west/south/east".
fc_area = "90/-100/20/40"

print("Data request parameters:")
print("Years: ", fc_years)
print("Month: ", fc_month)
print("Day: ", fc_day)
print("Center: ", fc_center)
print("System: ", fc_system)
print("Variable: ", fc_variable)
print("Lead time: ", fc_leadtime)   
print("Grid: ", fc_grid)
print("Area: ", fc_area)


# Now loop over the years and download the data for each year. 
for y, year in enumerate(fc_years):
    print(year)
    dataset = "seasonal-original-single-levels"
    request = {
        "originating_centre": fc_center,
        "system": fc_system,
        "variable": [fc_variable],
        "year": [str(year)],
        "month": [fc_month],
        "day": [fc_day],
        "leadtime_hour": [fc_leadtime],
        "data_format": "netcdf",
        "area": [fc_area],
        "grid": [fc_grid]
    }

    target=fc_center+'_system'+fc_system+'_'+str(year)+fc_month+fc_day+fc_variable+fc_area.replace('/','_')+'.nc'   
    print(target)
    client = cdsapi.Client()
    client.retrieve(dataset, request,target)
