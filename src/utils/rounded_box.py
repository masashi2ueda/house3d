# %%
from solid import sphere, hull, translate
from .myobj import MyObj


def create_rounded_box(width, depth, height, radius, segments=32):
    """
    角の丸い直方体を作成する関数

    Args:
        width: 幅
        depth: 奥行き
        height: 高さ
        radius: 角の丸みの半径
        segments: 円の分割数（滑らかさ）

    Returns:
        MyObj: 角の丸い直方体
    """
    # 8つの角に球を配置
    spheres = []
    positions = [
        [radius, radius, radius],                          # 前左下
        [width - radius, radius, radius],                  # 前右下
        [radius, depth - radius, radius],                  # 後左下
        [width - radius, depth - radius, radius],          # 後右下
        [radius, radius, height - radius],                 # 前左上
        [width - radius, radius, height - radius],         # 前右上
        [radius, depth - radius, height - radius],         # 後左上
        [width - radius, depth - radius, height - radius]  # 後右上
    ]

    for pos in positions:
        sphere_obj = sphere(r=radius, segments=segments)
        sphere_obj = translate(pos)(sphere_obj)
        spheres.append(sphere_obj)

    # hullを使って8つの球を結合し、滑らかな角の丸い直方体を作成
    rounded_box_obj = hull()(*spheres)

    return MyObj(rounded_box_obj)


if __name__ == "__main__":
    # 使用例
    # パラメータ設定
    box_width = 50
    box_depth = 30
    box_height = 20
    # corner_radius = 5
    box_width = 10
    box_depth = 15
    box_height = 20
    corner_radius = 3

    # 方法1: hull()を使った角の丸い直方体
    rounded_box1 = create_rounded_box(box_width, box_depth, box_height, corner_radius)

    # ファイル出力
    dst_dir_path = "../myobject"
    rounded_box1.to_file(f"{dst_dir_path}/rounded_box.scad")
    rounded_box1.save_stl(f"{dst_dir_path}/rounded_box.stl")

    print("角の丸い直方体を作成しました！")
    print(f"SCAD ファイル: {dst_dir_path}/rounded_box.scad")
    print(f"STL ファイル: {dst_dir_path}/rounded_box.stl")

# %%
