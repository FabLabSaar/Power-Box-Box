from solid import *
from solid.utils import *

wall_thickness = 3
y_offset = 12 - 3 * wall_thickness
inner_size = [110, 200 + y_offset - 2 * wall_thickness, 45]
inner_cube = cube(size=inner_size)
outer_size = [inner_size[0] + 2 * wall_thickness, inner_size[1] + 0.1 + 1 * wall_thickness, inner_size[2]]
outer_cube = cube(size=outer_size)

def bohrungen():
    bohrung = union()(
       translate([0,0,2.2])(cylinder(h=2 * wall_thickness, d=3.5, segments=100)),
        cylinder(r2=1.75, r1=3.3, h=2.3, segments=100),)
    bohrungen = []
    for x,y in [(x,y) for x in [0,80] for y in [0, 120]]:
        bohrungen.append(translate([x,y,0])(bohrung))
    return translate([15 + wall_thickness, 61 + wall_thickness, -0.01])(union()(bohrungen))

box = difference()(
    outer_cube,
    translate([wall_thickness, -0.1, 2 * wall_thickness + 0.1])(inner_cube),
    translate([0, -y_offset, 0])(bohrungen()))

clutch = difference()(
    cube([outer_size[0], 3 * wall_thickness, outer_size[2]]),
    translate([2 * wall_thickness, -0.1, 2 * wall_thickness])(
        cube([outer_size[0] - 4 * wall_thickness, 3 * wall_thickness + 0.2, outer_size[2]])),
    translate([wall_thickness, wall_thickness, -0.1])(
        cube([outer_size[0] - 2 * wall_thickness, wall_thickness, outer_size[2] + 0.2])))

frame = union()(
    translate([0, 3 * wall_thickness - 0.1, 0])(box),
    clutch)

scad_render_to_file(frame, 'PBB-Frame.scad')
