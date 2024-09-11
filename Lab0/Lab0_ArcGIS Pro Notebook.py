import arcpy
folder_path = "C:/Mac/Home/Desktop/Grad School/GIS 5571/Labs/Lab0/shp/fgdb_trans_roadcenterline/trans_roadcenterline.gdb"
arcpy.env.workspace = folder_path
print("Workspace set to:", arcpy.env.workspace)

input_feature_class = "RoadCenterline"
output_buffer = "100ft_buffer_output.shp"
buffer_distance = "100 feet"
arcpy.Buffer_analysis(input_feature_class,output_buffer,buffer_distance)

import arcpy.mp as mp
aprx = mp.ArcGISProject("CURRENT")
map_obj = aprx.listMaps("Jupyter in ArcPro")[0]
data_path = r"C:/Mac/Home/Desktop/Grad School/GIS 5571/Labs/Lab0/shp/fgdb_trans_roadcenterline/trans_roadcenterline.gdb/RoadCenterline"
map_obj.addDataFromPath(data_path)
aprx.save()


