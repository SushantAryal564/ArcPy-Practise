import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Sushant Aryal\Programming\ArcPy\arcgis Files\TestProject.gdb"
fc = r"D:\Sushant Aryal\Programming\ArcPy\data\countries\ne_10m_admin_0_countries.shp"
numFeature= arcpy.management.GetCount(fc)
arcpy.analysis.Select(fc,"Egypt","NAME='Egypt'")
print ("shapefile has a",numFeature,"features")
