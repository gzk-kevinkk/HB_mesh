import cadquery as cq
import TempFunction

# length, width and height of Si layer
Si_xlength = 20.0
Si_ylength = Si_xlength
Si_zlength = 5.0

# length, width and height of SiO2 layer
SiO2_xlength = Si_xlength
SiO2_ylength = Si_ylength
SiO2_zlength = 1.6

# center of interconnects
# ic_centers = [(0.0, 0.0), (3.0, 0.0), (0.0, 3.0),\
#               (-3.0, 0.0), (0.0, -3.0)]
ic_centers = []

# radius and height of interconnects
ic_radius = 1.0
ic_height = 1.0

# number of interconnects
n = len(ic_centers)

# substrate model
## SiO2 layer model
hb_substrate_top = cq.Workplane("XY").workplane(offset = 0.5*(SiO2_zlength+Si_zlength))
hb_substrate_top = hb_substrate_top.box(Si_xlength, Si_ylength, Si_zlength)

hb_substrate_bottom = cq.Workplane("XY").workplane(offset = -0.5*(SiO2_zlength+Si_zlength))
hb_substrate_bottom = hb_substrate_bottom.box(Si_xlength, Si_ylength, Si_zlength)
hb_substrate_Si = hb_substrate_bottom.union(hb_substrate_top)
hb_substrate = hb_substrate_bottom.union(hb_substrate_top)

## Si layer model
hb_substrate_middle = cq.Workplane("XY")
hb_substrate_SiO2 = hb_substrate_middle.box(SiO2_xlength, SiO2_ylength, SiO2_zlength)

hb_substrate = hb_substrate.add(hb_substrate_SiO2)

# show hybrid bonding model
# show_object(hb_interconnects, name="hb_interconnects", options={"alpha":0.0, "color": (237, 125, 49)})
# show_object(hb_substrate_Si, name="Si_layer", options={"alpha":0.8, "color": (91, 155, 213)})
# show_object(hb_substrate_SiO2, name="SiO2_layer", options={"alpha":0.8, "color": (112, 173, 71)})

output_file = "hb_model3.step"
cq.exporters.export(hb_substrate, output_file)

TempFunction.generate_geo(output_file, geo_filename="hb_model3.geo.in_v1")
# TempFunction.generate_geo(output_file, geo_filename="hb_model3.geo.in")
# TempFunction.generate_bcmap(output_file, n, dir="./")
# TempFunction.generate_rmark(output_file, n, dir="./")
