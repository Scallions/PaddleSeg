

import glob
import os


def gen_dir(ds_root, mode="train"):
    dir = os.path.join(ds_root, mode)
    txt_fp = os.path.join(ds_root,f"{mode}.txt")
    with open(txt_fp, "w") as f:
        for fp in glob.iglob(dir+"/image/*"):
            fname = fp.split("/")[-1]
            label_fp = dir+"/label/"+fname
            if not os.path.exists(label_fp):
                continue
            f.write(f"{mode}/image/{fname} {mode}/label/{fname}\n")
            # break

def main():
    ds_root = "dataset/aerialimage"
    modes = ["train", "val", "test"]
    for mode in modes:
        gen_dir(ds_root, mode)


if __name__ == '__main__':
    main()