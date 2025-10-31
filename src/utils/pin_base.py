# %%
from solid import cube, cylinder
# from utils import MyObj
from .myobj import MyObj

# %%
hole_segments = 64
small_hole_r = 1.2 + 0.6
small_hole_h = 9
# big_hole_r = 12/2 + 0.8
big_hole_r = 35/2
# big_hole_h = 8
big_hole_h = 1000
big_hole_trans_h = 1.8
ita_w = 12 + 0.5
ita_d = 36.5
ita_h = 3
hols_trans_d = 10


def get_pin_base():
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
    return ous


# 使い方のサンプル
if __name__ == "__main__":
    base_w = 18
    base_d = 40
    base_h = ita_h + big_hole_trans_h
    base = MyObj(cube((base_w, base_d, base_h), center=False))

    ous = get_pin_base()
    ous.translate([3, 3, 0])
    all_obj = base - ous
    dst_dir_path = "../myobject"
    all_obj.to_file(f"{dst_dir_path}/test.scad")
    all_obj.save_stl(f"{dst_dir_path}/test.stl")
