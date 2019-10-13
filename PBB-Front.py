from solid import *


front = union()(
    cube([10,10,2])    
)

scad_render_to_file(front, 'PBB-Front.scad')