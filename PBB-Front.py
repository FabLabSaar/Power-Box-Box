from solid import *
from solid.utils import *

PBB_size = [100, 200, 42]
wall_thickness = 3
front_size = [PBB_size[2] - wall_thickness, PBB_size[0] - 2 * wall_thickness, 3]
pyramid_height = 20
pyramid_top_offset = 2 * wall_thickness
pyramid_bottom_offset = 2 * wall_thickness
usb_size = [13.5, 15, 3 * pyramid_height]

def pyramid():
    points = [
        [ 0,  0,  0 ],
        [ front_size[0] - pyramid_bottom_offset,  0,  0 ],
        [ front_size[0] - pyramid_bottom_offset,  front_size[1] - pyramid_bottom_offset,  0 ],
        [  0,  front_size[1] - pyramid_bottom_offset,  0 ],
        [  0 + pyramid_top_offset,  0 + pyramid_top_offset,  pyramid_height],
        [ front_size[0] - pyramid_top_offset - pyramid_bottom_offset,  0 + pyramid_top_offset,  pyramid_height],
        [ front_size[0] - pyramid_top_offset - pyramid_bottom_offset,  front_size[1] - pyramid_top_offset - pyramid_bottom_offset,  pyramid_height],
        [  0 + pyramid_top_offset, front_size[1] - pyramid_top_offset - pyramid_bottom_offset,  pyramid_height]]
    faces = [
        [0,1,2,3],
        [4,5,1,0],
        [7,6,5,4],
        [5,6,2,1],
        [6,7,3,2],
        [7,4,0,3]]
    return polyhedron(points, faces)

def usb():
    outer_size = [usb_size[0] * 1.1, usb_size[1] * 1.1, 1] 
    return (union()(
        up(pyramid_height + front_size[2])(cube(outer_size, center=True)),
        cube(usb_size, center=True)))

def usbs():
    return union()([translate([0, (usb_size[0] + ((front_size[1] / 2) / 3)) * i, 0])(usb()) for i in range(3)])

def top():
    return difference()(
        pyramid(),
        translate([front_size[0] / 2, 20, ])(usbs()))

front = difference()(
    union()(
        cube(front_size),
        translate([wall_thickness, wall_thickness,front_size[2]])(
            pyramid())),
    translate([front_size[0] / 2, front_size[1] / 4, 0])(
        usbs()))

scad_render_to_file(front, 'PBB-Front.scad')