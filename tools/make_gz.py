# 生成数据列表
import os
import glob

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
            f.write(starts[idx] + ' ' + ends[idx] + ' ' + fp + '\n')  # 写入list.txt

    print(mode + '_data_list generated')

dataset_path = 'dataset/CD_Data_GZ'  # data的文件夹
# 分别创建三个list.txt
creat_data_list(dataset_path, mode='train')
# creat_data_list(dataset_path, mode='test')
# creat_data_list(dataset_path, mode='val')