from solid import *
from solid.utils import *

def bohrungen(wall_thickness):
    bohrung = union()(
       translate([0,0,2.2])(cylinder(h=2 * wall_thickness, d=3.5, segments=100)),
        cylinder(r2=1.75, r1=3.3, h=2.3, segments=100),)
    bohrungen = []
    for x,y in [(x,y) for x in [0,80] for y in [0, 120]]:
        bohrungen.append(translate([x,y,0])(bohrung))
    return translate([10 + wall_thickness, 61 + wall_thickness, -0.01])(union()(bohrungen))

wall_thickness = 3
y_offset = 12
inner_size = [100, 200 + y_offset, 42]
inner_cube = cube(size=inner_size)
outer_size = list(map(lambda x: x + 2 * wall_thickness, inner_size))
outer_cube = cube(size=outer_size)

frame = difference()(
    outer_cube,
    translate([wall_thickness, wall_thickness, 2 * wall_thickness + wall_thickness * 0.01])(inner_cube),
    translate([0, y_offset, 0])(bohrungen(wall_thickness))
)

scad_render_to_file(frame, 'PBB.scad')