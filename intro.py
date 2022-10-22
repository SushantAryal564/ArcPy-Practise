import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"D:\Sushant Aryal\Programming\ArcPy\arcgis Files\TestProject.gdb"

def print_message(message):
    arcpy.AddMessage(message)
    print(message)

fc= arcpy.GetParameterAsText(0)
if(fc==""):
    fc = r"D:\Sushant Aryal\Programming\ArcPy\data\countries\ne_10m_admin_0_countries.shp"
numFeature= arcpy.management.GetCount(fc)
#arcpy.analysis.Select(fc,"Egypt","NAME='Egypt'")
print_message("shapefile has a {} features".format(numFeature))
