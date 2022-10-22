import arcpy
arcpy.env.overwriteOutput = True
with arcpy.EnvManager(scratchWorkspace=r"D:\Sushant Aryal\Programming\ArcPy\arcgis Files\TestProject.gdb", workspace=r"D:\Sushant Aryal\Programming\ArcPy\arcgis Files\TestProject.gdb"):
    country=arcpy.GetParameterAsText(0)
    countries = r"D:\Sushant Aryal\Programming\ArcPy\data\countries\ne_10m_admin_0_countries.shp"
    places = r"D:\Sushant Aryal\Programming\ArcPy\data\populatedPlaces\ne_10m_populated_places.shp"
    arcpy.analysis.Select(countries, r"D:\Sushant Aryal\Programming\ArcPy\arcgis Files\TestProject.gdb\selCountry", "NAME = '{}'".format(country))
    arcpy.analysis.Buffer("selCountry", r"D:\Sushant Aryal\Programming\ArcPy\arcgis Files\TestProject.gdb\selCountry_Buffer", "200 Kilometers", "FULL", "ROUND", "NONE", None, "PLANAR")
    arcpy.analysis.Clip(places, "selCountry_Buffer", r"D:\Sushant Aryal\Programming\ArcPy\arcgis Files\TestProject.gdb\Places_Clip", None)
    places = arcpy.management.GetCount("Places_Clip")
    arcpy.AddMessage("Total places in and around {0} 200Km buffer is {1} ".format(country,places))
