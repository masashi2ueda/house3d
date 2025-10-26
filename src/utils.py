# %%
import viewscad

from solid import union, scad_render_to_file
from solid import rotate, translate, scale

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
