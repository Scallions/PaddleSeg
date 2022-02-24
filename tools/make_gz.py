# 生成数据列表
import os
import glob
import cv2

def check_shape(a_fp, b_fp, label_fp):
    a = cv2.imread(a_fp)
    b = cv2.imread(b_fp)
    label = cv2.imread(label_fp)
    if a.shape == b.shape and b.shape == label.shape:
        return True
    return False

def creat_data_list(dataset_path, mode='train'):
    with open(os.path.join(dataset_path, (mode + '_list.txt')), 'w') as f:
        starts = {}
        for fp in glob.iglob(os.path.join(dataset_path,"T1/*")):
            name = fp.split("/")[-1].split(".")[0]
            idx = name.split("_")[2]
            starts[idx] = fp #"/".join(fp.split("/")[2:])
        ends = {}
        for fp in glob.iglob(os.path.join(dataset_path,"T2/*")):
            name = fp.split("/")[-1].split(".")[0]
            idx = name.split("_")[2]
            ends[idx] = fp #"/".join(fp.split("/")[2:])
        for lb_fp in glob.iglob(os.path.join(dataset_path, "labels_change/*")):
            lb_name = lb_fp.split("/")[-1].split(".")[0]
            idx = lb_name.split("_")[2]
            fp = lb_fp #"/".join(lb_fp.split("/")[2:])
            # 验证三者大小是否一致
            if not check_shape(starts[idx], ends[idx], fp):
                break
            f.write(starts[idx] + ' ' + ends[idx] + ' ' + fp + '\n')  # 写入list.txt

    print(mode + '_data_list generated')

dataset_path = 'dataset/CD_Data_GZ'  # data的文件夹
# 分别创建三个list.txt
creat_data_list(dataset_path, mode='train')
# creat_data_list(dataset_path, mode='test')
# creat_data_list(dataset_path, mode='val')