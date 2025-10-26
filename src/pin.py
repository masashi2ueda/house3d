# %%
import numpy as np
import viewscad
import copy

from solid import union, cube, cylinder, scad_render_to_file, import_stl, rotate, translate, scale, polyhedron, linear_extrude, polygon, difference, sphere, mirror
import sys
from solid.utils import right, up, down, left, forward, back
from solid import screw_thread

obj_dir_path = "C:/Users/uedam/Documents/roba/roba-scad/objects"
openscad_exec = "C:/Program Files/OpenSCAD/openscad.exe"


# %%
def get_render():
    return viewscad.Renderer(openscad_exec=openscad_exec)


class MyObj:
    def __init__(self, *args):
        self.objects = union()(*args)

    @property
    def r(self):
        return get_render()
        # return viewscad.Renderer()

    def translate(self, vec):
        self.objects = translate(vec)(self.objects)

    def rotate_x(self, angle):
        self.objects = rotate(angle, [1, 0, 0])(self.objects)

    def rotate_y(self, angle):
        self.objects = rotate(angle, [0, 1, 0])(self.objects)

    def rotate_z(self, angle):
        self.objects = rotate(angle, [0, 0, 1])(self.objects)

    def scale(self, all_scace: float):
        self.objects = scale(all_scace)(self.objects)

    def add(self, obj):
        if isinstance(obj, MyObj):
            self.objects = union()(self.objects, obj.objects)
        else:
            self.objects = union()(self.objects, obj)

    def minus(self, obj):
        if isinstance(obj, MyObj):
            self.objects = self.objects - obj.objects
        else:
            self.objects = self.objects - obj

    def render(self):
        self.r.render(self.objects)

    def to_file(self, path):
        scad_render_to_file(self.objects, path)

    def save_stl(self, path):
        self.r.render(self.objects, outfile=path)

    def __add__(self, other):
        if isinstance(other, MyObj):
            return MyObj(self.objects + other.objects)
        return MyObj(self.objects + other)

    def __sub__(self, other):
        if isinstance(other, MyObj):
            return MyObj(self.objects - other.objects)
        return MyObj(self.objects - other)


# %%
base_w = 18
base_d = 40
hole_segments = 64
small_hole_r = 1.2 + 0.6
small_hole_h = 9
big_hole_r = 12/2 + 0.8
big_hole_h = 8
big_hole_trans_h = 1.8
ita_w = 12 + 0.5
ita_d = 36.5
ita_h = 3
hols_trans_d = 10

base_h = ita_h + big_hole_trans_h


base = MyObj(cube((base_w, base_d, base_h), center=False))
small_hole = MyObj(cylinder(h=small_hole_h, r=small_hole_r, center=False,
                            segments=hole_segments))
big_hole = MyObj(cylinder(h=big_hole_h, r=big_hole_r, center=False,
                           segments=hole_segments))
big_hole.translate([0, 0, big_hole_trans_h])
ita = MyObj(cube((ita_w, ita_d, ita_h), center=False))
ita.translate([-ita_w/2, 0, 0])
holes = small_hole + big_hole
holes.translate([0, hols_trans_d, ita_h])
ous = holes + ita
ous.translate([ita_w/2, 0, 0])

# ous.translate([ita_w/2, 0, 0])
# ous.translate([base_w/2, base_d/2, 0])
# ous.translate([base_w/2, base_d/2, 0])

ous.translate([3, 3, 0])
all_obj = base - ous
# all_obj = ous + base
# all_obj = base
# all_obj = holes + ita
all_obj.to_file("test.scad")
all_obj.save_stl("test.stl")
# %%
# holse2 = copy.deepcopy(holes)
# holes.translate([base_w/2, base_d/2, 0])
# holse2.translate([-base_w/2, -base_d/2, 0])
