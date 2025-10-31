# %%
from solid import cube
import utils

# %%
w = 250
h = 100
d = 100
r = 5
# 壁の厚さ
smgn = 10
# バーの幅
bar_h1 = 20
bar_h2 = 20
# バーの間隔
bar_h_interval = 50
# 適当な大きい値
inf_size = 1000
# 適当な小さい値
small_size = 1
# ピンベースの間隔
pin_base_interval = w/3

# 外の箱
big_box = utils.create_rounded_box(w, d, h, r)

# 中をくり抜く
subt_box = utils.create_rounded_box(w - smgn * 2, d - smgn * 2, h * 2, r)
subt_box.translate([smgn, smgn, smgn])
big_box = big_box - subt_box

# バーの上をくり抜く
subt_box = utils.MyObj(cube([inf_size, inf_size, inf_size]))
subt_box.translate([0, smgn, bar_h1 + bar_h_interval + bar_h2])
big_box = big_box - subt_box

# バーの下をくり抜く
subt_box = utils.MyObj(cube([inf_size, inf_size, bar_h_interval]))
subt_box.translate([0, smgn, bar_h1])
big_box = big_box - subt_box

# ピン止め
pin_base = utils.get_pin_base()
pin_base.rotate_x(90)
pin_base.rotate_z(180)
pin_base.rotate_y(180)
pin_base.translate([-utils.pin_base.ita_w/2, 0, h/2])
pin_base.translate([w/2, 0, 0])
pin_base1 = pin_base.copy()
pin_base2 = pin_base.copy()
pin_base1.translate([-pin_base_interval, 0, 0])
pin_base2.translate([pin_base_interval, 0, 0])

# ファイル出力
dst_dir_path = "../myobject"
all_obj = big_box - pin_base1 - pin_base2
# all_obj = pin_base
all_obj.to_file(f"{dst_dir_path}/keshoudai_okiba.scad")
all_obj.save_stl(f"{dst_dir_path}/keshoudai_okiba.stl")



# %%
